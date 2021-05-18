from model import CovidRecord
import csv

# Author Wilker Fernandes de Sousa
# Date: March 26, 2021

records = {} # Wilker Fernandes de Sousa
# records = {
#   "352020-01-31": {
#       "pruid": row[0],
#       "prname": row[1],
#       "prnameFR": row[2],
#       "date": row[3],
#       "numconf": row[5],
#       "numprob": row[6],
#       "numdeaths": row[7],
#       "numtotal": row[8],
#       "numtoday": row[13],
#       "ratetotal": row[15],
#   }, "592020-01-31": {
#       "pruid": row[0],
#       "prname": row[1],
#       "prnameFR": row[2],
#       "date": row[3],
#       "numconf": row[5],
#       "numprob": row[6],
#       "numdeaths": row[7],
#       "numtotal": row[8],
#       "numtoday": row[13],
#       "ratetotal": row[15],
#   }
# }


def getCSVData(fileName: str, recordsCount: int):
    """
    This function getCSVData open and read CSV file from the app_controller.py getCSVData function and store the data into a dictionary variable called "records"

    Paramenter

    fileName: the fileName are record csv file which pass  
    Reference to update dictionary: https://www.programiz.com/python-programming/methods/dictionary/update
    recordsCount: the number of records
    """
    # global records was created in order to access from inside and outside of a function
    global records

    error = ''  
    try:
        with open(fileName) as csv_file:

            
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            count = 0

            records = {}
            for row in csv_reader:
                if count == recordsCount:
                    break
                if line_count == 0:
                    line_count += 1
                else:
                    line_count += 1
                    r = { 
                        str(row[0]) + str(row[3]) : { 
                            "pruid": row[0],
                            "prname": row[1],
                            "prnameFR": row[2],
                            "date": row[3],
                            "numconf": row[5],
                            "numprob": row[6],
                            "numdeaths": row[7],
                            "numtotal": row[8],
                            "numtoday": row[13],
                            "ratetotal": row[15],
                        }
                    }
                    records.update(r)
                    count += 1

    # Exception Handling check if the file exist/ file not found (VALIDATION)
    except FileNotFoundError:

        error = f'File is not available: {fileName}' 
    except Exception as e:
        error = 'Something went wrong!' + str(e)

    return error


def getRecords(sort):
    """ This function getRecords is get the records from the global variable called "records" and return the "records"
    items sorting the the records into a dictionary"""
    global records 
    return sorted(records.items(), key = lambda x: x[1][sort])


def saveRecords():
    """ This function is openning and writting into the "saved_records.csv" 
    https://www.programiz.com/python-programming/writing-csv-files
    """

    # open the file "saved_records.csv" where in the write mode
    with open('saved_records.csv', 'w', newline='') as f:
        global records

        # create the csv writer
        writer = csv.writer(f) 

        # write a row to the csv file 
        for key in records:
            writer.writerow(records[key].values())
        

def storeRecord(pruid, prname, prnameFR, date, numconf, numprob, numdeaths, numtotal, numtoday, ratetotal):
    """
    This function storeRecord into the global variable called "records"

    Parameters:

    pruid - pruid is the id number  
    prname - the name 
    prnameFR - name in France 
    date -  date is the date of the record
    numconf - number of confirmed
    numprob -  number of prob
    numdeaths -  number of death 
    numtotal -  total number
    numtoday - number days
    ratetotal - rate total

    The records.append(r) the append method is used to add at the end of every row in the list (array)
    which is stored into the global variable called "records"

    """
    r = {
        str(pruid) + str(date): {
            "pruid": pruid,
            "prname": prname,
            "prnameFR": prnameFR,
            "date": date,
            "numconf": numconf,
            "numprob": numprob,
            "numdeaths": numdeaths,
            "numtotal": numtotal,
            "numtoday": numtoday,
            "ratetotal": ratetotal,
        }
    }
    global records
    records.update(r)


def getRecord(pruid, date):
    """ The function getRecord from record global variable (which hold the data from "saved_records.csv" 
    looping throught the record from (class CovidRecord in the model.py file) for "record.pruid" id and "record.date" date 
    and returning the record """

    global records
    return records[str(pruid)+str(date)]


def updateRecord(pruid, prname, prnameFR, date, numconf, numprob, numdeaths, numtotal, numtoday, ratetotal):
    """ This function updateRecords updates the records using global variable called "records" (which hold the data) than loop throught the record
    looking for (record.pruid) == str(pruid) and str(record.date) == str(date) if the data match return records if not return false.

    Parameters:

    pruid - pruid is the id number  
    prname - the name 
    prnameFR - name in France 
    date -  date is the date of the record 
    numconf - number of confirmed
    numprob -  number of prob
    numdeaths -  number of death 
    numtotal -  total number
    numtoday - number days
    ratetotal - rate total
    """
    storeRecord(pruid, prname, prnameFR, date, numconf, numprob, numdeaths, numtotal, numtoday, ratetotal)


def deleteRecord(pruid, date):
    """ This function is deleteRecord delete's a record using global variable called records (which hold the data) than loop throught 
    the record for (record.pruid) == str(pruid) and str(record.date) == str(date) if the id and date matches it will delete a record return true  
    if not return false
    return true (record is deleted) if not return false. 

    Parameters:

    pruid: pruid is the id number

    date: date is the date of the record 

    """
    global records
    records.pop(str(pruid)+str(date))


def deleteAllRecords():
    global records
    records = {}