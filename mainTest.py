import os
import mysql.connector
from datetime import datetime
from mysql.connector import Error
from dataProcessor import dataProcessor

def main():

    script_start_time = datetime.now()
    # Throw this script in the directory you want or use the below os.chdir to specify the directory you want to look
    # in (just make sure to comment line 148 out if you move the script to your working directory
    os.chdir('./Testing/')
    currentWD = os.getcwd()

    # pull in needed classes to pass into the process
    dataP = dataProcessor()

    # Pass the current working directory to function to get a list of files to process and assign it to a variable
    filesToProcess = getFiles(currentWD)

    fileCount = 0
    for file in filesToProcess:
        fileCount += 1
    num_lines = 0

    # Useful to see if you are looking at the right directory
    print "\n[*] Here are the files I found for processing...\n\n", filesToProcess

    for workingFile in filesToProcess:
        fileProcessingStart = datetime.now()
        filelines = 0
        with open(workingFile, 'r') as f:
            for line in f:
                num_lines += 1
                filelines += 1
            f.close()

        # Get the file folder and file name for each file processed - assign to a variable to pass to on to the
        # processing function
        str_split = workingFile.split('/')
        file_folder = str_split[len(str_split) - 2]
        file_name = str_split[len(str_split) - 1]

        # Pass the working file to the dataProcessor class
        print "\n[*] Processing %s lines in file %s" % (filelines, workingFile)
        dataP.processFile(workingFile, file_folder, file_name)
        fileProcessingEnd = datetime.now()
        fileProcessingElapsed = fileProcessingEnd - fileProcessingStart
        print "[*] Finished Processing File - Elapsed Time: ", fileProcessingElapsed
        dataP.processFile(workingFile, file_folder, file_name)

    script_end_time = datetime.now()
    script_elapsed_time = script_end_time - script_start_time
    print "[*] Analyzed %s files and %s total lines!" % (fileCount, num_lines)
    print "[*] Total Elapsed Time: ", script_elapsed_time


def getFiles(currentWD):
    fileCount = 0
    filesToRead = []
    for dirname, dirnames, filenames in os.walk(currentWD):
        for filename in filenames:
            # ignore some files we don't care about
            excludeList = ['.DS_Store', '._', 'dataProcessor.py', 'dataProcessor.pyc', 'FoundData.txt', 'mainTest.py']
            if any(item in filename for item in excludeList):
                pass
            else:
                filePath = os.path.join(dirname, filename)
                filesToRead.append(filePath)
                fileCount = fileCount + 1
    print "\n[!] Preparing to analyze %s files...\n" % fileCount
    return filesToRead

def dbConnection():
    # Connect to a MySQL instance
    try:
        print "[*] Establishing Connection to your MySQL Server...\n"

        connection = mysql.connector.connect(host='localhost',
                                             database='CollectionOne',
                                             user='root',
                                             password='4ZaCtr1wfY0M4zo')

        if connection.is_connected():
            dbInfo = connection.get_server_info()
            print "[*] You are connected to your MySQL Server. This server is running MySQL version: ", dbInfo
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print "[*] You are connected to database: ", record

    except Error as e:
        print "[!] Error while connecting to MySQL - ", e
        exit()

    return connection

main()