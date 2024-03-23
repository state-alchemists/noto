import os
from datetime import datetime

CURRENT_DIR = os.path.dirname(__file__)
PROJECT_DIR = os.path.dirname(os.path.dirname(CURRENT_DIR))
SRC_DIR = os.path.join(PROJECT_DIR, "src")
TODO_FILE_NAME = os.path.join(SRC_DIR, "todo.txt")

CURRENT_TIME = datetime.now()
CURRENT_YEAR = CURRENT_TIME.year
CURRENT_MONTH = CURRENT_TIME.strftime("%m")
CURRENT_DAY = CURRENT_TIME.strftime("%d")