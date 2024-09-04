import logging
from google.generativeai import GenerativeModel, configure


def model_operations(config, prompt):
    logging.info("Model Operations started")
    model = setup_model(config)
    response = generate_content(model, prompt)
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
        msg = f"Model Setup failed : {e}"
        logging.error(msg)
        raise Exception(msg)


def generate_content(model, prompt):
    try:
        response = model.generate_content(prompt)
        logging.info("Content generated successfully.")

        if response.text.strip().lower() == 'output token limit exceeded':
            msg = "Output token limit exceeded. Please try again later."
            logging.error(msg)
            raise Exception(msg)

        return response
    except Exception as e:
        msg = f"API Call failed : {e}"
        logging.error(msg)
        raise Exception(msg)
