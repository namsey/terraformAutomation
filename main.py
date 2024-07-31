import os
from core.core import Core

config_path = os.path.abspath('config/config.yaml')


def main():
    try:
        core = Core(config_path)
        print(core.run_automation())
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()
