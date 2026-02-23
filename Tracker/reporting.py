import os
import csv
from Tracker.exceptions import *
from Tracker.logger import *
from Tracker.utils import *

logger = Logger().setup_logs()

class Reporting:
    def __init__(self):
        self.filepath = os.path.join(os.getcwd(), "Data", "recordData.csv")
        if not os.path.exists(self.filepath):
            print("Add Data to Generate Report!!!")
            logger.info("Data Does Not Exists in Record Data CSV File.")
    def report(self):
        totalIncome = 0
        totalExpense = 0
        try:
            with open(self.filepath,"r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        amount = Utils.reverse_currency_format(row['Amount'])
                        if row["Amount Type"].lower() == "income":
                            totalIncome += amount
                        else:
                            totalExpense += amount
                    except Exception as e:
                        Error(e)
                totalSaving = totalIncome - totalExpense
                print("Financial Report!!")
                print(f"Total Income: {Utils.currency_format(totalIncome)}")
                print(f"Total Expenditure: {Utils.currency_format(totalExpense)}")
                print(f"Total Saving: {Utils.currency_format(totalSaving)}")
                logger.info(f"Total Income: {Utils.currency_format(totalIncome)}, Total Expenditure: {Utils.currency_format(totalExpense)} and Total Saving: {Utils.currency_format(totalSaving)}")
                logger.info("Closing the Program")

        except Exception as e:
            Error(e)
