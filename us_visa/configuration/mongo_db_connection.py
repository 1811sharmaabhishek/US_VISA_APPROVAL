import sys
import os

from us_visa.exception import USVisaException
from us_visa.logger import logging

from us_visa.constants import DATABASE_NAME,MONGODB_URL_KEY
import pymongo
import certifi

ca = certifi.where()

class MongoDBClient:
    """
    Class Name: exports_data_into_feature_stores
    Description: This method exports data from mongoDB and store it as Dataframe

    Output: connection to mongoDb
    on Faliure: raise an exception
    """

    client = None

    def __init__(self, database_name = DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(f"Eniornment Key: {MONGODB_URL_KEY} is not set.")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url,tlsCAfile = ca)
                self.client = MongoDBClient.client
                self.database = self.client[database_name]
                self.database_name = database_name
                logging.info('MongoDB Connection Succesfull')

        except Exception as e:
            raise USVisaException(e, sys)