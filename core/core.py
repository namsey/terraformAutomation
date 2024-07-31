import logging

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

            config = read_config(self.__config_path, 'model')
            prompt = get_combined_prompt()
            response = model_operations(config, prompt)

            print(f"Prompt: {prompt}")
            print(f"Generated Text:\n{to_markdown(response.text)}")
            print(f"Prompt Feedback: {response.prompt_feedback}")

            logging.debug("Automation process ended")

            return "Process successfully completed"
        except Exception as e:
            msg = f"Automation process failed : {e}"
            logging.error(msg)
            raise Exception(msg)
