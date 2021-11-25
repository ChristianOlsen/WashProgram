import itertools
import bisect

class User:
    newid = itertools.count().__next__
    def __init__(self, name):
        self.id = User.newid()
        self.name = name
        self.bookings = []
        
    def addBooking(self, booking):
        bisect.insort(self.bookings, booking)
        
    def getBookings(self):
        return self.bookings
    
    def __str__(self):
        return f'{self.name} #{self.id}'
