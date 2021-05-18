import repo

# Author Wilker Fernandes de Sousa
# Date: March 26, 2021


def reloadFromCSV(): 
    """ The function reloadFromCSV reloads the file "covid19-download.csv" using the function "getCSVData()" from "repo.py" file 
    reading and loop through the file returning 100 records from the covid19-download.csv" """

    return repo.getCSVData('covid19-download.csv', 100)


def getRecords(sort):
    """ This function getRecords get the records using the parameter "sort" to sort the records and return "getRecords()" from 
    the repo.py file which get the records the from "saved_records.csv" which hold the data """

    return repo.getRecords(sort)


def saveRecords():
    """ This function saveRecords return "saveRecords()" from repo.py file which wirte the record into
        "saved_records.csv" file """

    return repo.saveRecords()


def storeRecord(req): 
    """ This function storeRecord return "storeRecord()" from repo.py file which stores the data into
        global variable called "records" returning store record """

    return repo.storeRecord(
        req['pruid'],
        req['prname'],
        req['prnameFR'],
        req['date'],
        req['numconf'],
        req['numprob'],
        req['numdeaths'],
        req['numtotal'],
        req['numtoday'],
        req['ratetotal'],
    )


def getRecord(pruid, date): 
    """ This function getRecord return the "getRecord()" from repo.py single record matching the id and date

    Paramenter:

    pruid: id number

    date: date is the date of the record

    """

    return repo.getRecord(pruid, date)


def updateRecord(req):
    """ This function updateRecord return the "updateRecord()" from the repo.py file which is been ImmutableMultiDict  

    Parameter:

    req:is using ImmutableMultiDict 

    """

    return repo.updateRecord( 
        req['pruid'],
        req['prname'],
        req['prnameFR'],
        req['date'],
        req['numconf'],
        req['numprob'],
        req['numdeaths'],
        req['numtotal'],
        req['numtoday'],
        req['ratetotal'],
    )


def deleteRecord(pruid, date):
    """ This function deleteRecord return the "deleteRecord()" from the repo.py file which deletes the record from
        "saved_records.csv" file

    Parameter:

    pruid: id number

    date: date is the date of the record

    """

    return repo.deleteRecord(pruid, date)
