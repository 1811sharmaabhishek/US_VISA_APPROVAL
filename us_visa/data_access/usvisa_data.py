from us_visa.constants import DATABASE_NAME
from us_visa.exception import USVisaException
from us_visa.logger import logging
from us_visa.configuration.mongo_db_connection import MongoDBClient

import pandas as pd
import sys
from typing import Optional
import numpy as np

class USVisaData:
    """
    This Class help to export entire mongo db record to pandas Dataframe
    """

    def __init__(self):

        try:
            self.mongo_client = MongoDBClient.client(database_name = DATABASE_NAME)
        except Exception as e:
            raise USVisaException(e, sys)
        
    def export_collection_as_dataframe(self,collection_name:str, database_name:Optional[str]=None) -> pd.DataFrame:
        try:
            """
            export entire collection as dataframe:
            return pd.DataFrame of collection
            """
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]
            
            df = pd.DataFrame(list(collection.find_all()))

            if '_id' in df.columns:
                df.drop(columns=["_id"],axis=1, inplace=True)
            df.replace({"na",np.nan},inplace=True)
            logging.info('Records are converted to DataFrame')
            return df
        except Exception as e:
            raise USVisaException(e,sys)
