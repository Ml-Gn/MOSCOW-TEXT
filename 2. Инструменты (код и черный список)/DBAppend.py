import csv
from pymongo import MongoClient


class DBWorker:
    def init(self, db_name):
        self.client = MongoClient()
        self.db = self.client[db_name]

    def save_data(self, file_name, collection_name, header):
        csvfile = open(file_name, 'r', encoding='utf-8')
        reader = csv.DictReader(csvfile)
        for line in reader:
            row = {}
            for field in header:
                row[field] = line[field]

            self.db[collection_name].insert_one(row)


worker = DBWorker('my_db')
worker.save_data('clean_results.csv', 'toponymics',
                 ["natasha", "start", "spacy"])
