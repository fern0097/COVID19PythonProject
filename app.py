import view
import app_controller as controller
from model import CovidRecord

from flask import Flask, request, redirect
app = Flask(__name__)
# Author Wilker Fernandes de Sousa
# Date: March 26, 2021


@app.route('/records', methods=["GET"])
def printRecords(): 
    """ Initialize flask telling what URL should trigger the fucntion "/records"
    which return a list of view records ("listRecords") from the view.py file calling the function getRecords() 
    from app_controller.py file which the function getRecords() returns records global variable called "records" 
    from the repo.py which is holding the data. The sort = "prname" is used to sort when the request have been received"""
    sort = "prname"
    if(request.args.get("sort")):
        sort = request.args.get("sort")
    return view.listRecords(controller.getRecords(sort))


@app.route('/reloadFromCSV')
def reloadFromCSV(): 
    """ Initialize flask telling what URL should trigger the fucntion 'reloadFromCSV' 
    which return  reloadFromCSV view from view.py file calling the function reloadFromCSV() from the app_controller
    which return the function getCSVData() 'covid19-download.csv' file with 100 records from the repo.py. """

    return view.reloadFromCSV(controller.reloadFromCSV())


@app.route('/')
def displayDashboard(): 
    """ Initialize flask telling what URL should trigger the fucntion 'displayDashboard' and return the view
    displayDashboard() from view.py"""

    return view.displayDashboard()


@app.route('/saveRecords')
def saveRecords(): 
    """ Initialize flask telling what URL should trigger the fucntion 'saveRecords' calls the controller which is in app_controller.py file
    calling the function saveRecord() in the repo.py file where it 'saved_records.csv' will be saved then returns the 'saved_records.csv' as a view """

    controller.saveRecords()
    return view.saveRecords()


@app.route("/createRecord")
def createRecord():
    """ Initialize flask telling what URL should trigger the fucntion '/createRecord' return a view of createRecords() function in view.py file """

    return view.createRecord()


@app.route("/saveRecord", methods=["POST"])
def saveRecord():
    """ Initialize flask telling what URL should trigger the fucntion '/saveRecord' calls the controller which is in app_controller.py file  
    calling the function storeRecord() in the repo.py file and return printRecords() printing the records data """
    
    controller.storeRecord(request.form)
    return printRecords()


@app.route("/updateRecord", methods=["GET"])
def updateRecord(): 
    """ Initialize flask telling what URL should trigger the fucntion '/updateRecord' requesting the args "id" and "date" and uses the getRecord() 
    passing the arguments returning updateRecord() as view """

    pruid = request.args.get("id")
    date = request.args.get("date")
    record = controller.getRecord(pruid, date)
    return view.updateRecord(record)


@app.route("/updateRecord", methods=["POST"]) 
def udpateRecordFromFormData():
    """ Initialize flask telling what URL should trigger the fucntion '/updateRecordFromFormData' which get the data
    from controller updateRecord() to update a data and return a printRecords() printing the records data. """

    controller.updateRecord(request.form)
    return printRecords()


@app.route("/deleteRecord", methods=["GET"])
def deleteRecord():
    """ Initialize Flask telling what URL should trigger the fucntion 'deleteRecord' using the GET method sending to the data look for 
    "id" and "date" in the record and than delete """

    pruid = request.args.get("id")
    date = request.args.get("date")
    controller.deleteRecord(pruid, date)
    return view.deleteRecord()


# Main function
if __name__ == "__main__":
    app.run()
