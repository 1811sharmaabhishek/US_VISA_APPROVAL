import os
import sys

import pandas as pd
from sklearn.model_selection import train_test_split

from us_visa.logger import logging
from us_visa.exception import USVisaException
from us_visa.data_access.usvisa_data import USVisaData
from us_visa.entity.artifact_entity import DataIngestionArtifact
from us_visa.entity.config_entity import DataIngestionConfig

class DataIngestion:

    def __init__(self, data_ingestion_config:DataIngestionConfig=DataIngestionConfig()):
        """
        :param data_ingestion_config: configuration for data ingestion
        """
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise USVisaException(e,sys)

    def export_data_into_feature_store(self) -> pd.DataFrame:
        """
        Method Name: export_data_into_feature_store
        Description: This method exports data from MongoDb to CSV file

        Output: data return as artifact of data ingestion of the components
        On Faliure: Write the exception log and raise the exception
        """
        try:
            logging.info("Exporting Data from mongoDb")
            usvisadata = USVisaData()
            dataframe = usvisadata.export_collection_as_dataframe(collection_name=DataIngestionConfig.collection_name)
            logging.info(f"Dataframe Created successfully with Shape: {dataframe.shape}")
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            dir_parth = self.data_ingestion_config.data_ingestion_dir
            os.makedirs(dir_parth,exist_ok=True)
            logging.info(f"Saving exported data into feature store file path : {feature_store_file_path}")
            dataframe.to_csv(feature_store_file_path,index=False,header=True)
            return dataframe
        except Exception as e:
            USVisaException(e,sys)
