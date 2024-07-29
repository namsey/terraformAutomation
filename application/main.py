import sys
import os

# Add the project root to the sys.path to ensure correct imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.config_reader import read_config
from logging_setup.logging_config import setup_logging
from model.model_operations import setup_model, generate_content
from utils.text_utils import to_markdown
from prompt.prompt_input import get_combined_prompt


def main():
    setup_logging()
    config = read_config()
    model = setup_model(config)
    prompt = get_combined_prompt()
    response = generate_content(model, prompt)

    print(f"Prompt: {prompt}")
    print(f"Generated Text:\n{to_markdown(response.text)}")
    print(f"Prompt Feedback: {response.prompt_feedback}")


if __name__ == "__main__":
    main()
