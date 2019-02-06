import re
from dataAnalyzer import dataAnalyzer
from lineReader import lineReader

class dataProcessor:

    def __init__(self):

        self.dataAnalyze = dataAnalyzer()
        self.lineRead = lineReader()
        self.delimREGEX = ":|;|\|"

    def lineSplit(self, line):
        splitLine = re.split(self.delimREGEX, line)
        return splitLine

    def processFile(self, workingFile, file_folder, file_name):

        # Open each file
        with open(workingFile) as workingFile:
            readFile = workingFile.readlines()

        for line in readFile:

            line = line.strip()
            if line is '':
                pass
            else:
                # The next two IF statements are designed for the error files that have been generated while processing dump
                if '[PROCESSED AS EMAIL] - ' in line:
                    line = re.sub("\[PROCESSED AS EMAIL\] - ", '', line)
                elif '[PROCESSED AS U/N] - ' in line:
                    line = re.sub("\[PROCESSED AS U\/N\] - ", '', line)

                if self.dataAnalyze.delimCheck(line):
                    try:
                        # Checks for: Username * Name * Email
                        dataOne = self.lineRead.checkDataStructureOne(line)
                        # Checks for: Email * Password
                        dataTwo = self.lineRead.checkDataStructureTwo(line)

                        if dataOne is True:
                            dataToInsert1 = self.processDataStructureOne(line)
                            print dataToInsert1

                        elif dataTwo is True:
                            dataToInsert2 = self.processDataStructureTwo(line)
                            print dataToInsert2

                        else:
                            splitline = self.lineSplit(line)
                            dataToWrite = ['UNKNOWN RECORD TYPE -->']

                            for dataPoint in splitline:
                                if self.dataAnalyze.checkForMD5(dataPoint):
                                    dataToWrite.append('MD5: %s' % dataPoint)
                                elif self.dataAnalyze.checkForSHA256(dataPoint):
                                    dataToWrite.append('SHA256: %s' % dataPoint)
                                elif self.dataAnalyze.checkForEmail(dataPoint):
                                    dataToWrite.append('EMAIL: %s' % dataPoint)
                                elif self.dataAnalyze.checkForIP(dataPoint):
                                    dataToWrite.append('IP: %s' % dataPoint)
                                elif self.dataAnalyze.checkForComplexPassword(dataPoint):
                                    dataToWrite.append('ComplexPassword: %s' % dataPoint)
                                else:
                                    dataToWrite.append('UNK: %s' % dataPoint)
                            print dataToWrite

                    except Exception as e:
                        print "[!] ERROR: Can not process record in dataProcessor.py | No logic set to process this " \
                              "record | Start debug at line 33 - {%s}" % e
                        # TODO: Send errors to text file for further analysis

    def processDataStructureOne(self, line):
        splitline = self.lineSplit(line)
        username = splitline[1]
        password = splitline[2]
        email = splitline[3]
        dataToInsert = [username, password, email]
        return dataToInsert

    def processDataStructureTwo(self, line):
        splitline = self.lineSplit(line)
        email = splitline[0]
        password = splitline[1]
        dataToInsert = [email, password]
        return dataToInsert

    #TODO: Create a function that pushes data to the MySQL database





