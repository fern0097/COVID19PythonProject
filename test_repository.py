import pytest 
import repo
from model import CovidRecord

# Author Wilker Fernandes de Sousa
# Date: March 26, 2021

# https://docs.pytest.org/en/stable/getting-started.html


def test_storeRecord(): # Wilker Fernandes de Sousa 

    # get all records
    records = repo.getRecords("prname")
    oldRecordsCount = len(records)

    # Add new record
    repo.storeRecord(
        pruid='321',
        prname='Ontario',
        prnameFR='Ontario',
        date='2021-02-02',
        numconf=64,
        numprob=4,
        numdeaths=2,
        numtotal=14,
        numtoday=33,
        ratetotal=123,
    )

    # Making sure the total records count is greater than 1 before
    records = repo.getRecords("prname")
    newRecordsCount = len(records)
    assert newRecordsCount == (oldRecordsCount + 1)

def test_getRecords(): 

    print("asdasd")

    # Clear all the records
    repo.deleteAllRecords()

    # Adding dummy record
    repo.storeRecord(
        pruid='1',
        prname='Vancouver',
        prnameFR='Vancouver',
        date='2021-02-02',
        numconf=2,
        numprob=1,
        numdeaths=1,
        numtotal=9,
        numtoday=6,
        ratetotal=21,
    )

    # Adding dummy record
    repo.storeRecord(
        pruid='2',
        prname='Ontario',
        prnameFR='Ontario',
        date='2021-02-03',
        numconf=64,
        numprob=4,
        numdeaths=2,
        numtotal=14,
        numtoday=33,
        ratetotal=123,
    )                           

    # Adding dummy record
    repo.storeRecord(
        pruid='3',
        prname='Quebec',
        prnameFR='Quebec',
        date='2021-02-01',
        numconf=64,
        numprob=4,
        numdeaths=2,
        numtotal=14,
        numtoday=33,
        ratetotal=123,
    )

    # Sorting records using name        
    records = repo.getRecords("prname")
    
    ontarioKey = '22021-02-03'
    vancouverKey = '12021-02-02'
    quebecKey = '32021-02-01'

    assert records[0][0] == ontarioKey
    assert records[1][0] == quebecKey
    assert records[2][0] == vancouverKey

    # Sorting records using date
    records = repo.getRecords("date")
    
    ontarioDate = '2021-02-03'
    vancouverDate = '2021-02-02'
    quebecDate = '2021-02-01'

    assert records[0][1]["date"] == quebecDate
    assert records[1][1]["date"] == vancouverDate
    assert records[2][1]["date"] == ontarioDate