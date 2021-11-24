from datetime import datetime, timedelta

class Program:
            
    def __init__(self, start, name, temperature, duration):
        """
        Settings of a washing program
        
        Args:
            name (string): name of program type
            temperature (int): in degrees Celcius
            length (int): duration in minutes
        """
        self.name = name
        self.temperature = temperature
        self.duration = duration
        self.start = start
        
    def getStart(self, roundTo = None):
        if roundTo is not None:
            return (self.start + timedelta(minutes=self.duration)).isoformat(" ", roundTo)
        return self.start
    
    def getEnd(self, roundTo = None):
        if roundTo is not None:
            return (self.start + timedelta(minutes=self.duration)).isoformat(" ", roundTo)
        return self.start + timedelta(minutes=self.duration)
    
    def __str__(self):
        return 

