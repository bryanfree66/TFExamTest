import tensorflow as tf
import os
import urllib.request
from zipfile import ZipFile
import pandas as pd
import numpy as np


def retrieve_url(url, filename):
    if not os.path.exists(filename) and not os.path.isfile(filename):
        urllib.request.urlretrieve(url, filename)
        print(f'Downloaded {filename}. Unzipping')
        with ZipFile(filename, 'r') as zip_ref:
            zip_ref.extractall(f'C:\\Users\\bryan\\local_code\\TFExamTest\\data')
            print(f'Unzipped {filename}. Renaming.')
            os.rename('C:\\Users\\bryan\\local_code\\TFExamTest\\data\\slump_test.data',
                      'C:\\Users\\bryan\\local_code\\TFExamTest\\data\\concrete.csv')
            print('File renamed.')

    else:
        print(f'{filename} already exists!')


def main():
    # Check GPU
    print(f"Tensorflow ver. {tf.__version__}")
    physical_devices = tf.config.list_physical_devices('GPU')
    print("Available GPUs:", len(physical_devices))

    # Get CSV Data
    url = 'http://archive.ics.uci.edu/static/public/182/concrete+slump+test.zip'
    data_path = 'data'
    filename = f'{data_path}/concrete.zip'
    retrieve_url(url, filename)
    filename = f'{data_path}/concrete.csv'
    print(f'{filename} is ready!')
    concrete_df = pd.read_csv(filename)
    print(concrete_df.head())

    # Create tensor
    concrete_df_np = concrete_df.to_numpy()
    print(concrete_df_np[:5])


if __name__ == "__main__":
    main()
