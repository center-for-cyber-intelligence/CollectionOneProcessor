import re

class dataAnalyzer:

    def __init__(self):
        self.emailREGEX = """(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21\\x23-\\x5b\\x5d-\\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21-\\x5a\\x53-\\x7f]|\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])+)\])"""
        self.ipREGEX = """(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}"""
        self.anyWordREGEX = "([A-Za-z0-9\!\@\#\$\%\^\&\*\(\)])+"
        self.md5_hash_REGEX = "\\b[a-fA-F\d]{32}\\b"
        self.SHA256_hash_REGEX = "\\b[A-Fa-f0-9]{64}\\b"
        self.delimREGEX = ":|;|\|"
        self.ComplexPasswordREGEX = "(?=(.*[0-9]))(?=.*[!@#$%^&*()\\[\]{}\-_+=~`|:;\"\'<>,./?])(?=.*[a-z])(?=(.*[A-Z]))(?=(.*)).{12,}"

        self.emailSearch = re.compile(self.emailREGEX)
        self.ipSearch = re.compile(self.ipREGEX)
        self.anyWordSearch = re.compile(self.anyWordREGEX)
        self.md5Search = re.compile(self.md5_hash_REGEX)
        self.sha256Search = re.compile(self.SHA256_hash_REGEX)
        self.delimSearch = re.compile(self.delimREGEX)
        self.ComplexPassword = re.compile(self.ComplexPasswordREGEX)


    def delimCheck(self, line):
        if self.delimSearch.search(line):
            return True
        else:
            return False

    def checkForUnknown(self, data):
        if self.anyWordSearch.search(data):
            return True
        else:
            return False

    def checkForIP(self, data):
        if self.ipSearch.search(data):
            return True
        else:
            return False

    def checkForComplexPassword(self, data):
        if self.ComplexPassword.search(data):
            return True
        else:
            return False

    def checkForMD5(self, data):
        if self.md5Search.search(data):
            return True
        else:
            return False

    def checkForEmail(self, data):
        # We need to force lower the entire line in order to increase the accuracy of the REGEX
        # In order to maintain the unique properties of possible passwords, this variable is only used for searching
        # lines for emails
        lookingForEmail = data.lower()
        if self.emailSearch.search(lookingForEmail):
            return True
        else:
            return False

    def checkForSHA256(self, data):
        if self.sha256Search.search(data):
            return True
        else:
            return False
