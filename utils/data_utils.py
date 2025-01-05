import pandas as pd
import gdown
import zipfile
from typing import Tuple

data_output_path = "../data/"

def construct_url(file_id: str) -> str:
    return f"https://docs.google.com/uc?export=download&id={file_id}"

def download_file(download_url: str, output_path=f"{data_output_path}rossmann_data.zip"):
    gdown.download(download_url, output_path, quiet=False)
    with zipfile.ZipFile(output_path, 'r') as zip_ref:
        zip_ref.extractall(f"{data_output_path}rossmann_data")


def load_file() -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    csv_file_path = f"{data_output_path}rossmann_data/"
    store_data = pd.read_csv(f"{csv_file_path}store.csv")
    train_data = pd.read_csv(f"{csv_file_path}train.csv")
    test_data = pd.read_csv(f"{csv_file_path}test.csv")
    sample_submission = pd.read_csv(f"{csv_file_path}sample_submission.csv")
    return store_data, train_data, test_data, sample_submission