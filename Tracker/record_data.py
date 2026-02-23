import os
import csv
from Tracker.exceptions import *
from Tracker.utils import *
from Tracker.logger import *

logger = Logger().setup_logs()

class GetDataFile:
    def __init__(self):
        self.data_dir = "./Data"
        if not os.path.exists(self.data_dir):
            logger.info("Record Data Folder Does not Exists")
            os.mkdir(self.data_dir)
            logger.info("Record Data Folder Created")
            try:
                with open(os.path.join(os.getcwd(), "Data", "recordData.csv"), mode="a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(["Amount Type", "Category", "Amount"])
                    logger.info(f"recordData CSV File Created.")
            except Exception as e:
                Error(e)

class RecordData(GetDataFile):
    def __init__(self):
        super().__init__()
        logger.info("Record Data Folder Exists Accessing Record Data CSV file")
        self.filepath = os.path.join(os.getcwd(), self.data_dir, "recordData.csv")
    
    def record_transaction(self, amount_type: str, category: str, amount:float):
        try:
            with open(self.filepath, mode="a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([amount_type.capitalize(), category.capitalize(), Utils.currency_format(amount)])
                logger.info(f"Added [{amount_type.capitalize()}, {category.capitalize()}, {Utils.currency_format(amount)}] to CSV File.")
        except Exception as e:
            Error(e)
        else:
            print(f"Amount Type: {amount_type} for Category: {category} for Amount: {Utils.currency_format(amount)} is Recorded")
    
    def record_income(self, amount_type: str, category: str, amount:float):
        self.record_transaction(amount_type, category, amount)
    
    def record_expense(self, amount_type: str, category: str, amount:float):
        self.record_transaction(amount_type, category, amount)

