from dataclasses import dataclass

# Author Wilker Fernandes de Sousa
# Date: March 26, 2021


@dataclass
class CovidRecord: 
    """ Data class to hold one record from the CSV file """
    pruid: int
    prname: str
    prnameFR: str
    date: str
    numconf: int
    numprob: int
    numdeaths: int
    numtotal: int
    numtoday: int
    ratetotal: float

    def toCSVData(self):
        """
        The function toCSVData is a inner class which is using the objects from class CovidRecords 
        and returns arrylist of the objects of itself. https://pythonspot.com/inner-classes/
        """
        return [
            self.pruid,
            self.prname,
            self.prnameFR,
            self.date,
            self.numconf,
            self.numprob,
            self.numdeaths,
            self.numtotal,
            self.numtoday,
            self.ratetotal,
        ]
