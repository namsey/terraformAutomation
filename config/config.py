import yaml


# Reads YAML config file from given path and returns full config details or specific section
def read_config(file_path, target_section=None):
    try:
        with open(file_path, 'r') as file:
            content = yaml.safe_load(file)
            if content is None:
                raise ValueError("YAML File is empty")
            if target_section:
                if target_section in content:
                    return content[target_section]
                else:
                    raise KeyError(f"Section '{target_section}' not found in the YAML file")
            else:
                return content
    except FileNotFoundError:
        raise Exception(f"Error: The File '{file_path}' was not found.")
    except yaml.YAMLError as e:
        raise Exception(f"Error parsing YAML file: {e}")
    return None
