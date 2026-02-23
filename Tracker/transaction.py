from Tracker.logger import *
from Tracker.exceptions import *
from Tracker.record_data import *

logger = Logger().setup_logs()

class Transaction:
    def __init__(self):
        try:
            with open("user_instruction.txt","r") as file:
                user_instruction = file.read()
        except Exception as e:
            Error(e)
        else:
            self.amount_type_instruction = user_instruction.splitlines()[6]
            self.category_income_instruction = user_instruction.splitlines()[8]
            self.category_expense_instruction = user_instruction.splitlines()[10]
            self.amount_instruction = user_instruction.splitlines()[12]
            self.agin_instruction = user_instruction.splitlines()[14]

    def transactionDetails(self):
        count = 0
        while count < 10:
            count += 1
            amount_type = input(self.amount_type_instruction).lower().strip()
            if amount_type not in ["income", "expenditure"]:
                print("Please enter income or expenditure")
                logger.info("User Did not Correct Input for amount_type")
                continue
            else:
                if amount_type == "income":                    
                    category = input(self.category_income_instruction)
                else:
                    category = input(self.category_expense_instruction)
                try:
                    amount = float(input(self.amount_instruction).strip())
                    if amount <= 0:
                        print("Invalid amount.")
                        logger.info("Entered Invalid amount")
                        continue
                except Exception as e:
                    Error(e)
                if amount_type == "income":
                    RecordData().record_income(amount_type, category, amount)
                else:
                    RecordData().record_expense(amount_type, category, amount)
                again = input(self.agin_instruction)
                if again != "yes":
                    print("Closing the Program")
                    logger.info("Closing the Program")
                    break
        else:
            print("Transaction limit reached. You can only enter a maximum of 10 transactions.")
            logging.info("Transaction limit reached.")


