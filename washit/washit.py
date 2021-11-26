"""
TODO:
- docstrings for all functions
- unit tests
- complete getters for classes
- identify user
- updateWaitlist() should be called regularily for check if users in waitlist can be notified of free washer
- type checks in functions E.G. istinstance(x, type) and raise Value/TypeErrors
- connect users, washers, booking and programs to database, make SQL queries
- implement web framework to deploy app to web. E.G. FastAPI
- GUI framework?
- End-2-end tests, with E.G. Cypress
"""

from datetime import datetime as dt

from program import Program
from user import User
from washer import Washer
from booking import Booking

class Washit:
    
    def __init__(self, number_of_washers=0):
        self.washers = []
        self.users = []
        self.waitlist = []  # list of users
        self._setup(number_of_washers)


    def addUser(self, name):
        self.users.append(User(name))
    
    def getUsers(self):
        return self.users

    def addWasher(self):
        self.washers.append(Washer())

    def addProgramType(self, programType, description, temperature, duration):
        Program.addProgramType(programType, description, temperature, duration)

    def getPrograms(self):
        return Program.getPrograms()

    def book(self, user, programType, start):
        for washer in self.washers:
            if washer.book(user, programType, start):
                #print(f'Booked {washer.program.description} on washer #{self.id} from {b.getStart("seconds")} to {b.getEnd("seconds")}.')
                return True

        print(f'All washers unavailable at {start}')
        return False

    def cancelBook(self, user, bookId):
        for b in user.bookings:
            if bookId == b.id:
                user.bookings.remove(b)
                self.washers[b.washerId].bookings.remove(b)
                print(f'Removed {b}')
                return True
        print(f'Booking #{bookId} on {user} not found.')
        return False
    
    def getAllBookings(self):
        bookings = []
        for washer in self.washers:
            for booking in washer.bookings:
                bookings.append(booking)
        return bookings

    def addWaitlist(self, user, programType):
        self.waitlist.append((user, programType))

    # TODO: should update every n seconds on async thread
    def updateWaitlist(self, update_interval):
        removed = []
        for index, (user, programType) in enumerate(self.waitlist):
            if self.book(user, programType):
                removed.append(index)
        for i in removed:
            self.waitlist.pop(i)

    def _setup(self, number_of_washers):
        update_interval = 60  # seconds

        for _ in range(number_of_washers):
            self.addWasher()
        
        self.addProgramType('kokvask', 'Kokvask', 60, 90)
        self.addProgramType('tøyvask', 'Tøyvask', 40, 60)
        self.addProgramType('håndvask', 'Håndvask', 30, 20)
        self.addUser('Ole')
        self.addUser('Hans')
        self.addUser('Liv')
        self.updateWaitlist(update_interval)


w = Washit(6)
w.book(w.getUsers()[0], 'kokvask', dt.now())
print(w.getAllBookings()[0])
