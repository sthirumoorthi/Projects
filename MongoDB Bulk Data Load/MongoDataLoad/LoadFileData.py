#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import logging
logging.basicConfig(filename="App.log", level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class PyMongoBulkLoad:
    def __init__(self, FILE_PATH):
        self.file_path = FILE_PATH
        logging.info("... class PyMongoBulkLoad was initiated ...")

    def load_pandas_df(self):
        """
        This function will read the CSV file and convert it to dictionary for loading into MongoDB
        :return: Dictionary within the list
        """

        try:
            df = pd.read_csv(self.file_path, sep=';')
            # convert the object type columns to float and replace (,) with (.)
            for column in df.columns:
                if df[column].dtype == 'object':
                    df[column] = [float(string.replace(',', '.')) for string in df[column]]

            # convert the pandas dataframe to dictionary
            file_dict = df.to_dict('records')
            logging.info(f"CSV File Read was success.. Data has been converted to Dictionary format")

        except Exception as err:
            logging.exception(f"Exception occurred while loading data in Dataframe. Error: {err}")

        return file_dict
    