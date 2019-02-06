import re
from dataAnalyzer import dataAnalyzer

class lineReader:

    def __init__(self):

        self.dataAnalyze = dataAnalyzer()

        # Known Data Structures

        # self.ds1 | Checks for: Username | Name | Email
        self.ds1 = """\|[A-Za-z0-9]+\|[A-Za-z0-9]+\|(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21\\x23-\\x5b\\x5d-\\x7f]|\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21-\\x5a\\x53-\\x7f]|\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])+)\])\|"""

        # self.ds2 | Checks for: Email (:|;\|) Password
        # TODO: This REGEX matches IP Address in the "Password" section - Need to fix
        self.ds2 = """(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21\\x23-\\x5b\\x5d-\\x7f]|\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21-\\x5a\\x53-\\x7f]|\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])+)\])+[:|;|\|]+[A-Za-z0-9!@#$%^&*()]+"""

        # Compile known data structure regex's
        self.checkds1 = re.compile(self.ds1)
        self.checkds2 = re.compile(self.ds2)

    def checkDataStructureOne(self, data):
        lowerdData = data.lower()
        if self.checkds1.search(lowerdData):
            return True
        else:
            return False

    def checkDataStructureTwo(self, data):
        lowerData = data.lower()
        if self.dataAnalyze.checkForIP(lowerData):
            return False
        elif self.checkds2.search(lowerData):
            return True
        else:
            return False