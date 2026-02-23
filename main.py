import sys
from Tracker.exceptions import *
from Tracker.logger import *
from Tracker.transaction import *
from Tracker.reporting import *

logger = Logger().setup_logs()

class FinancialTracker:
    def __init__(self):
        self.logger = logger
        self.choice_menu() #call the choice_menu() method of this object
    def choice_menu(self):
        try:
            with open("user_instruction.txt","r") as file:
                user_instruction = file.read()
            user_instruction = user_instruction.split("\n;\n")[0]
        except Exception as e:
            Error(e) 
        else: 
            try:
                user_input = input(user_instruction)
                if user_input == "1":
                    instruction = user_instruction.split("\n")[1].strip()
                    self.logger.info(f"User has Selected: {instruction}")
                    Transaction().transactionDetails()
                elif user_input == "2":
                    instruction = user_instruction.split("\n")[2].strip()
                    self.logger.info(f"User has Selected: {instruction}")
                    Reporting().report()
                else:
                    instruction = user_instruction.split("\n")[3].strip()
                    self.logger.info(f"User has Selected: {instruction}: {user_input}")
                    self.logger.info("Closing the Program")
                    sys.exit(0)
            except Exception as e:
                Error(e) 


#Run this code only if this file is being run directly not when it’s imported somewhere else
if __name__ == "__main__":
    FinancialTracker()