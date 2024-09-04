import sys
import pandas as pd

sys.path.append("..")


def load_data(file_path):
    return pd.read_csv(file_path)


if __name__ == "__main__":
    choc_df = load_data("data/raw/chocolate.csv")
    print(choc_df.head())
