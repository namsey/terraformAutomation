import logging
from google.generativeai import GenerativeModel, configure


class TokenExhaustionError(Exception):
    """Custom exception raised when output token limit is exceeded."""
    pass


def setup_model(config):
    try:
        configure(api_key=config['api_key'])
        logging.info("API key configured successfully.")
        model = GenerativeModel(config['model_name'])
        logging.info(f"Generative model '{config['model_name']}' initialized successfully.")
        return model
    except KeyError as e:
        logging.error(f"KeyError: {e}")
        raise


def generate_content(model, prompt):
    try:
        response = model.generate_content(prompt)
        logging.info("Content generated successfully.")

        if response.text.strip().lower() == 'output token limit exceeded':
            raise TokenExhaustionError("Output token limit exceeded. Please try again later.")

        # Log the number of tokens used
        tokens_used = response.metadata.get('tokens_used', 'N/A')
        logging.info(f"Number of tokens used: {tokens_used}")

        return response
    except TokenExhaustionError as e:
        logging.error(f"TokenExhaustionError: {e}")
        raise
    except Exception as e:
        logging.error(f"Error: {e}")
        raise
