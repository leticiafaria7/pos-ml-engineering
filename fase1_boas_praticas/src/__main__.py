import pandas as pd
from yaml import safe_load, loader # no terminal: uv add PyYaml
from pathlib import Path

def read_configs():
    with open(Path(Path(__file__).parent, 'config/config.yaml'), 'r') as file:
        config = safe_load(file.read())

    return config

def main():
    configs = read_configs()
    print(configs['learning_rate'])

def dummy_function():
    dataframe: pd.DataFrame = pd.DataFrame({"A":[1, 2], "B":[3, 4]})
    print(dataframe)

if __name__ == "__main__":
    main()
