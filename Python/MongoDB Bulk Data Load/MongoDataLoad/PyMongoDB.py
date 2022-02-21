#!/usr/bin/env python
# coding: utf-8

import pymongo
import pandas as pd
import logging
logging.basicConfig(filename="App.log", level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


class PyMongoDatabase:
    def __init__(self, CLIENT_URL, DB_NAME, COLL_NAME):
        self.client_url = CLIENT_URL
        self.dbname = DB_NAME
        self.coll_name = COLL_NAME

        self.client = pymongo.MongoClient(CLIENT_URL, tls=True, tlsAllowInvalidCertificates=True)
        self.db_conn = self.client[DB_NAME]
        self.coll = self.db_conn[COLL_NAME]
        logging.info("... class PyMongoDatabase was initiated ...")

    def connectivity_check(self):
        """
        To check the connectivity of Mongo DB connection
        :return: None
        """
        try:
            self.client.list_database_names()
            logging.info(f"Data Base Connection Established........ \n"
                         f"DB Name: {self.dbname} \nCollection: {self.coll_name}")
        except Exception as err:
            logging.exception(f"Data Base Connection failed. Error: {err}")


class PyMongoDbFindFilter(PyMongoDatabase):
    def __init__(self, CLIENT_URL, DB_NAME, COLL_NAME):
        super().__init__(CLIENT_URL, DB_NAME, COLL_NAME)
        logging.info("... class PyMongoDbFindFilter was initiated ...")

    def find_doc(self, column=None, operator=None, value=0):
        """
        This function will retrieve the document from DB collection based on the condition
        and convert it to Pandas Dataframe.

        :param column: Column Name
        :param operator: Operation (such as EQ, GT, GTE, LT, LTE, etc..,
        :param value: Value to be filtered
        :return: Pandas Dataframe
        """
        result_df = []
        try:
            result_df = pd.DataFrame.from_dict(self.coll.find({column: {operator: value}}))
            logging.info(f"Find doc initiated for {column: {operator: value}} for the collection {self.coll}")
        except Exception as err:
            logging.exception(f"Exception occurred in find_doc: {err}")

        return result_df

    def find_all(self):
        """
        This function retrieve all the document from DB collection
        and convert it to Pandas Dataframe.

        :return: Pandas Dataframe
        """
        result_df = []
        try:
            result_df = pd.DataFrame.from_dict(self.coll.find())
            logging.info(f"Find all doc initiated for the collection {self.coll}")
        except Exception as err:
            logging.exception(f"Exception occurred in find_all: {err}")

        return result_df

    def get_doc_count(self, query=None):
        """
        This function will get the count of all documents retrieved from DB based on the query
        and convert them into Pandas Dataframe

        :param query: Query to be filtered, enclosed in {}
        :return: Pandas Dataframe
        """
        count = 0
        try:
            count = self.coll.count_documents(query)
            logging.info(f"Get count initiated for {query} in the collection {self.coll}")
        except Exception as err:
            logging.exception(f"Exception occurred in get_doc_count: {err}")

        return count

    def get_doc_limit(self, limit_n):
        """
        This function will retrieve top 'n' documents from DB
        and convert them into Pandas Dataframe

        :param limit_n: Any integer value
        :return: Pandas Dataframe
        """
        result_df = []
        try:
            result_df = pd.DataFrame.from_dict(self.coll.find().limit(limit_n))
            logging.info(f"Get doc limit initiated for the collection {self.coll}")
        except Exception as err:
            logging.exception(f"Exception occurred in get_doc_count: {err}")

        return result_df

    def filter_with_and(self, query1, query2):
        """
        This function uses logical AND operator to filter the documents and
        convert them into Pandas Dataframe. Both conditions to be satisfied.

        :param query1: Query to be filtered, enclosed in {}
        :param query2: Query to be filtered, enclosed in {}
        :return: Pandas Dataframe
        """
        result_df = []
        try:
            result_df = pd.DataFrame.from_dict(self.coll.find({"$and": [query1, query2]}))
            logging.info(f"Filter AND initiated for {query1} and {query2} in the collection {self.coll}")
        except Exception as err:
            logging.exception(f"Exception occurred in filter_with_and: {err}")

        return result_df

    def filter_with_or(self, query1, query2):
        """
        This function uses logical OR operator to filter the documents and
        convert them into Pandas Dataframe. Either one of the query to be satisfied.

        :param query1: Query to be filtered, enclosed in {}
        :param query2: Query to be filtered, enclosed in {}
        :return: Pandas Dataframe
        """
        result_df = []
        try:
            result_df = pd.DataFrame.from_dict(self.coll.find({"$or": [query1, query2]}))
            logging.info(f"Filter OR initiated for {query1} and {query2} in the collection {self.coll}")
        except Exception as err:
            logging.exception(f"Exception occurred in filter_with_or: {err}")

        return result_df


class PyMongoDbOperations(PyMongoDbFindFilter):
    def __init__(self, CLIENT_URL, DB_NAME, COLL_NAME):
        super().__init__(CLIENT_URL, DB_NAME, COLL_NAME)
        logging.info("... class PyMongoDbOperations was initiated ...")

    def insert_many(self, data):
        """
        This function will load all the documents to the DB.

        :param data: Dictionary documents enclosed in list
        :return: None
        """
        try:
            self.coll.insert_many(data)
            logging.info(f"All the documents loaded successfully in collection {self.coll}")
        except Exception as err:
            logging.exception(f"Exception occurred in insert_many: {err}")

    def insert_one_doc(self, data):
        """
        This function will load only one document to the DB Collection.

        :param data: Dictionary document
        :return: None
        """
        try:
            self.coll.insert_one(data)
            logging.info(f"Document loaded successfully in collection {self.coll}")
        except Exception as err:
            logging.exception(f"Exception occurred in insert_one_doc: {err}")

    def update_many(self, query, column, new_val):
        """
        This function will update all the documents which are retrieved from DB Collection

        :param query: Query to be filtered. Should be enclosed in {}
        :param column: Column name to be updated.
        :param new_val: New value to be updated
        :return: None
        """
        try:
            self.coll.update_many(query, {"$set": {column: new_val}})
            logging.info(f"Documents were updated for {query} in the collection {self.coll}")
        except Exception as err:
            logging.exception(f"Exception occurred in update_many: {err}")

    def update_one(self, query, column, new_val):
        """
        This function will update only one document which is retrieved from DB Collection.

        :param query: Query to be filtered. Should be enclosed in {}
        :param column: Column to be updated
        :param new_val: New value to be updated
        :return: None
        """
        try:
            self.coll.update_one(query, {"$set": {column: new_val}})
            logging.info(f"Document was updated for {query} in the collection {self.coll}")
        except Exception as err:
            logging.exception(f"Exception occurred in update_one: {err}")

    def find_one_and_update(self, query, column, new_val):
        """
        This function will update only one document which is retrieved from DB Collection using the query.

        :param query: Query to be filtered. Should be enclosed in {}
        :param column: Column to be updated
        :param new_val: New value to be updated
        :return: None
        """
        try:
            self.coll.find_one_and_update(query, {"$set": {column: new_val}})
            logging.info(f"Document was updated for {query} in the collection {self.coll}")
        except Exception as err:
            logging.exception(f"Exception occurred in find_one_and_update: {err}")

    def delete_many(self, query):
        """
        This function will delete all the documents which are retrieved from DB using the query filter.

        :param query: Query to be filtered. Should be enclosed in {}
        :return: None
        """
        try:
            self.coll.delete_many(query)
            logging.info(f"Documents were deleted for {query} in the collection {self.coll}")
        except Exception as err:
            logging.exception(f"Exception occurred in delete_many: {err}")

    def delete_one(self, query):
        """
        This function will delete only one document which is retrieved from DB using query filter.

        :param query: Query to be filtered. Should be enclosed in {}
        :return: None
        """
        try:
            self.coll.delete_one(query)
            logging.info(f"Document was deleted for {query} in the collection {self.coll}")
        except Exception as err:
            logging.exception(f"Exception occurred in delete_one: {err}")


class PyMongoDbDropColl(PyMongoDatabase):
    def __init__(self, CLIENT_URL, DB_NAME, COLL_NAME):
        super().__init__(CLIENT_URL, DB_NAME, COLL_NAME)
        logging.info("... class PyMongoDbDropColl was initiated ...")

    def drop_collection(self):
        """
        This function will drop the collection passed in the object creation.

        :return:None
        """
        try:
            self.coll.drop()
            logging.info(f"The collection {self.coll} was dropped")
        except Exception as err:
            logging.exception(f"Exception occurred in drop_collection: {err}")