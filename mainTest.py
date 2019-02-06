import os
import mysql.connector
from mysql.connector import Error
from dataProcessor import dataProcessor

def main():

    # Throw this script in the directory you want or use the below os.chdir to specify the directory you want to look
    # in (just make sure to comment line 148 out if you move the script to your working directory
    os.chdir('./Testing/')
    currentWD = os.getcwd()

    # pull in needed classes to pass into the process
    dataP = dataProcessor()

    # Pass the current working directory to function to get a list of files to process and assign it to a variable
    filesToProcess = getFiles(currentWD)

    # Useful to see if you are looking at the right directory
    print "\n[****] Here are the files I found for processing [****]\n\n", filesToProcess

    for workingFile in filesToProcess:

        # Get the file folder and file name for each file processed - assign to a variable to pass to on to the
        # processing function
        str_split = workingFile.split('/')
        file_folder = str_split[len(str_split) - 2]
        file_name = str_split[len(str_split) - 1]

        # Pass the working file to the dataProcessor class
        print "\n[****] Processing file: ", workingFile
        dataP.processFile(workingFile, file_folder, file_name)


def getFiles(currentWD):
    filesToRead = []
    for dirname, dirnames, filenames in os.walk(currentWD):
        for filename in filenames:

            # ignore some files we don't care about
            excludeList = ['.DS_Store', '._']

            if any(item in filename for item in excludeList):
                pass
            else:
                filePath = os.path.join(dirname, filename)
                filesToRead.append(filePath)
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

    return connection

main()