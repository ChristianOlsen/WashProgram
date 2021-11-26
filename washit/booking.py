from datetime import datetime, timedelta
from program import Program
import itertools

class Booking:
    newid = itertools.count().__next__
    
    def __init__(self, user, programType, washerId, start): #start, name, temperature, duration):
        """
        Settings of a washing program
        
        Args:
            name (string): name of program type
            temperature (int): in degrees Celcius
            length (int): duration in minutes
        """
        # TODO: fix ids not iterating by 1
        self.id = Booking.newid()
        self.user = user
        self.program = Program(programType)
        self.washerId = washerId
        self.start = start

    def getStart(self, roundTo=None):
        if roundTo is not None:
            return (self.start + timedelta(minutes=self.program.duration)).isoformat(" ", roundTo)
        return self.start

    def getEnd(self, roundTo=None):
        if roundTo is not None:
            return (self.start + timedelta(minutes=self.program.duration)).isoformat(" ", roundTo)
        return self.start + timedelta(minutes=self.program.duration)

    def __str__(self):
        return str(f'Booking #{self.id}: {self.user} - {self.program.description} on washer #{self.washerId}: {self.getStart("seconds")} --> {self.getEnd("seconds")}')

    def __lt__(self, other): 
        return self.getStart() < other.getStart()
