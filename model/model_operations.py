import logging
from google.generativeai import GenerativeModel, configure


class TokenExhaustionError(Exception):
    """Custom exception raised when output token limit is exceeded."""
    pass

def model_operations(config, prompt):
    logging.info("Model Operations started")
    model = setup_model(config)
    response = generate_content(model,prompt)
    logging.info("Model Operations ended")
    return response

def setup_model(config):
    try:
        configure(api_key=config['key'])
        logging.debug("API key configured successfully.")
        model = GenerativeModel(config['name'])
        logging.debug(f"Generative model '{config['name']}' initialized successfully.")
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

        return response
    except TokenExhaustionError as e:
        logging.error(f"TokenExhaustionError: {e}")
        raise
    except Exception as e:
        logging.error(f"Error: {e}")
        raise
