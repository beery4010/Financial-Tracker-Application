from Tracker.logger import *

logger = Logger().setup_logs()

class Error(Exception):
    def __init__(self, exception):
        self.exception = exception
        if str(type(self.exception)) == "<class 'FileNotFoundError'>":
            file_name = str(self.exception).split(":")[1].strip()
            self.message = f"Please Add {file_name} file"
            logger.error(f"{file_name} File Not Fouund.")
        else:
            self.message = self.exception
            logger.error(self.exception)
        print(self.message)