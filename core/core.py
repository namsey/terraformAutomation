import logging
import os

from config.config import read_config
from utils.logger import setup_logging
from utils.text_utils import to_markdown
from prompt.generate_prompt import get_combined_prompt
from model.model_operations import model_operations


class Core:
    def __init__(self, config_path):
        self.__config_path = config_path
        setup_logging(config_path)

    def run_automation(self):
        try:
            logging.debug("Automation process started")

            model_config = read_config(self.__config_path, 'model')
            output_config = read_config(self.__config_path, 'output')
            prompt = get_combined_prompt()
            response = model_operations(model_config, prompt)

            generated_text = to_markdown(response.text)

            print(f"Prompt: {prompt}")
            print(f"Generated Text:\n{generated_text}")
            print(f"Prompt Feedback: {response.prompt_feedback}")

            # Save the generated text to a file
            output_file_path = output_config.get('file_path')
            if output_file_path:
                os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
                with open(output_file_path, 'w') as f:
                    f.write(generated_text)
                logging.info(f"Generated text saved to {output_file_path}")
            else:
                logging.warning("Output file path not specified in config")

            logging.debug("Automation process ended")

            return "Process successfully completed"
        except Exception as e:
            msg = f"Automation process failed : {e}"
            logging.error(msg)
            raise Exception(msg)