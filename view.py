from tabulate import tabulate 

# Author Wilker Fernandes de Sousa
# Date: March 26, 2021

# html and Bootstrap framework for design
html = """
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap initilization -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">

    <title>Wilker Fernandes de Sousa - Programming Language Research Project Assignment 2</title>

  </head>
  <body>
    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>

    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js" integrity="sha384-q2kxQ16AaE6UbzuKqyBE9/u/KzioAlnx2maXQHiDX9d4/zp8Ok3f+M7DPm+Ib6IU" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.min.js" integrity="sha384-pQQkAEnwaBkjpqZ8RU1fF1AKtTcHJwFl3pblpTlHXybJjHpMYo79HY3hIi4NKxyj" crossorigin="anonymous"></script>
    -->

    <!-- Naviagtion toolbar  -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
        <a class="navbar-brand" href="/">My Python Project</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Options
          </a>
          <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
            <li><a class="dropdown-item" href="/reloadFromCSV">Reload the data from the dataset, replacing the in-memory data</a></li>
            <li><a class="dropdown-item" href="/saveRecords">Backup records</a></li>
            <li><a class="dropdown-item" href="/records">Display in-memory records</a></li>
            <li><a class="dropdown-item" href="/createRecord"> Create a new record</a></li>
          </ul>
        </li>
        </ul>
        </div>
    </div>
    </nav>

    <div class="container mt-5">
    {0}
    </div>

  </body>
</html>

"""


def displayDashboard():
    """ This function displayDashboard display web Main Content which will display 'displayDashboard' returning 
    a global variable html """

    # global html variable can be access inside or outside of a funtion
    global html 
    return html.format("""
<div class="jumbotron">
  <h1 class="display-4">Welcome to my Python Project</h1>
  <p class="lead">
  Assignment 3 project made by Wilker Fernandes de Sousa.
  </p>
</div>

    """)


def reloadFromCSV(error):
    """ This function reloadFromCSV when the record are load will diplay a message returning html with a message 
    "All records loaded into memory successfully!, but there is an error it will pass and error "something went wrong!" 
    
    Parameter: 

    error: will pass a message error 

    " """

    if(error != ''): 
        return html.format(f"""
<div class="alert alert-danger" role="alert">
  {error}
</div>
        """)
    return html.format("""
<div class="alert alert-primary" role="alert">
  All records loaded into memory successfully!
</div>
    """)


def listRecords(result):
    """
    This fucntion listRecords print the "records" into a table with a counter of every 10 records 
    printing "Wilker Fernandes de Sousa". The table_rows variable get the data which passes to html_table.  
    """

    table_rows = ''
    counter = 1
    for key, dict in result:
        if(counter % 11 == 0): #topfall
            table_rows += f"""
               <tr><td colspan="11"><b>Wilker Fernande de Sousa</b></td></tr>
            """
        else:
            table_rows += f"""
            <tr>
                <td>{dict["pruid"]}</td>
                <td>{dict["prname"]}</td>
                <td>{dict["prnameFR"]}</td>
                <td>{dict["date"]}</td>
                <td>{dict["numconf"]}</td>
                <td>{dict["numprob"]}</td>
                <td>{dict["numdeaths"]}</td>
                <td>{dict["numtotal"]}</td>
                <td>{dict["numtoday"]}</td>
                <td>{dict["ratetotal"]}</td>
                <td>
                    <a class="btn btn-primary" href=\'\\updateRecord?id={dict["pruid"]}&date={dict["date"]}\'>UPDATE</a>
                    <a class="btn btn-danger" href=\'\\deleteRecord?id={dict["pruid"]}&date={dict["date"]}\'>DELETE</a>
                </td>
            </tr>
            """
        counter += 1

    html_table = f"""
    <table class="table table-striped">
    <thead>
        <tr>
            <th scope="col"><a href=\'\\records?sort=pruid\'>PrUID</a></th>
            <th scope="col"><a href=\'\\records?sort=prname\'>Name</a> </th>
            <th scope="col"><a href=\'\\records?sort=prnameFR\'>Name [FR]</a></th>
            <th scope="col"><a href=\'\\records?sort=date\'>Date</a> </th>
            <th scope="col"><a href=\'\\records?sort=numconf\'>Confirmed</a></th>
            <th scope="col"><a href=\'\\records?sort=numprob\'>Prob</a></th>
            <th scope="col"><a href=\'\\records?sort=numdeaths\'>Deaths</a></th>
            <th scope="col"><a href=\'\\records?sort=numtotal\'>Total</a></th>
            <th scope="col"><a href=\'\\records?sort=numtoday\'>Today</a></th>
            <th scope="col"><a href=\'\\records?sort=ratetotal\'>RateTotal</a></th>
            <th scope="col">Action</th>
        </tr>
    </thead>
    <tbody>
        {table_rows}
    </tbody>
</table>
    """

    return html.format(html_table)


def saveRecords():
    """ This function "saveRecords" display a message "All records saved successfully!" """

    return html.format("""
<div class="alert alert-primary" role="alert">
  All records saved successfully!
</div>
    """)


def createRecord():
    """ This function createRecord in html form which will be saved into "/saveRecords" 
    using the POST method sending the data which will be stores into the "saved_records.csv" """

    return html.format("""
    <form action="/saveRecord" method="POST">
    
        <label for="pruid">UID:</label><br>
        <input class="form-control" type="text" name="pruid"><br>

        <label for="prname">Name:</label><br>
        <input class="form-control" type="text" name="prname"><br>
        
        <label for="prnameFR">Name [FR]:</label><br>
        <input class="form-control" type="text" name="prnameFR"><br>
        
        <label for="date">Date:</label><br>
        <input class="form-control" type="date" name="date"><br>
        
        <label for="numconf">Confirmed:</label><br>
        <input class="form-control" type="number" name="numconf"><br>
        
        <label for="numprob">Prob:</label><br>
        <input class="form-control" type="number" name="numprob"><br>
        
        <label for="numdeaths">Deaths:</label><br>
        <input class="form-control" type="number" name="numdeaths"><br>
        
        <label for="numtotal">Total:</label><br>
        <input class="form-control" type="number" name="numtotal"><br>
        
        <label for="numtoday">Today:</label><br>
        <input class="form-control" type="number" name="numtoday"><br>
        
        <label for="ratetotal">RateTotal:</label><br>
        <input class="form-control" type="number" name="ratetotal"><r><br>
        
        <input class="btn btn-primary btn-block" type="submit" value="Submit">
    </form> 
    """)


def updateRecord(record): 
    """ The function updateRecords check if the "record" from "CovidRecord" class in model.py file is holding the data. 
    If not it will display an alert with a message "Record not found". Than returns all the values from record 
    into "/updateRecord" page and sending the new data once "submitted" """

    if(not record):
        return html.format("""
<div class="alert alert-primary" role="alert">
  Record not found
</div>
        """)
    return html.format(f""" # Wilker Fernandes de Sousa
    <form action="/updateRecord" method="POST">

        <input class="form-control" type="hidden" name="pruid" value="{record["pruid"]}">
    
        <label for="prname">Name:</label><br>
        <input class="form-control" type="text" name="prname" value="{record["prname"]}"><br>
        
        <label for="prnameFR">Name [FR]:</label><br>
        <input class="form-control" type="text" name="prnameFR" value="{record["prnameFR"]}"><br>
        
        <label for="date">Date:</label><br>
        <input class="form-control" type="date" name="date" value="{record["date"]}"><br>
        
        <label for="numconf">Confirmed:</label><br>
        <input class="form-control" type="number" name="numconf" value="{record["numconf"]}"><br>
        
        <label for="numprob">Prob:</label><br>
        <input class="form-control" type="number" name="numprob" value="{record["numprob"]}"><br>
        
        <label for="numdeaths">Deaths:</label><br>
        <input class="form-control" type="number" name="numdeaths" value="{record["numdeaths"]}"><br>
        
        <label for="numtotal">Total:</label><br>
        <input class="form-control" type="number" name="numtotal" value="{record["numtotal"]}"><br>
        
        <label for="numtoday">Today:</label><br>
        <input class="form-control" type="number" name="numtoday" value="{record["numtoday"]}"><br>
        
        <label for="ratetotal">RateTotal:</label><br>
        <input class="form-control" type="number" name="ratetotal" value="{record["ratetotal"]}"><br>
        <br>
        
        <input class="btn btn-primary btn-block" type="submit" value="Submit">
    </form> 
    """)


def deleteRecord():
    """ This function "deleteRecord" deletes a record from "saved_records.cvs" file   """
    return html.format("""
<div class="alert alert-primary" role="alert">
  Record deleted
</div>
    """)
