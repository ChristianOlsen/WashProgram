#!/usr/bin/python3

"""
TODO:
- docstrings for all functions
- unit tests
- identify user
- updateWaitlist() should be called regularily for check if users in waitlist can be notified of free washer
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

washers = []
users = []
waitlist = [] # list of users


def addUser(name):
    users.append(User(name))

def addWasher():
    washers.append(Washer())
    
def addProgramType(programType, description, temperature, duration):
    Program.addProgramType(programType, description, temperature, duration)
    
def getPrograms():
    return Program.getPrograms()

def book(user, programType, start):
    for washer in washers:
        if washer.book(user, programType, start):
            #print(f'Booked {washer.program.description} on washer #{self.id} from {b.getStart("seconds")} to {b.getEnd("seconds")}.')
            return True
        
    print(f'All washers unavailable at {start}')
    return False

def cancelBook(user, bookId):
    for b in user.bookings:
        if bookId == b.id:
            user.bookings.remove(b)
            washers[b.washerId].bookings.remove(b)
            print(f'Removed {b}')
            return True
    print(f'Booking #{bookId} on {user} not found.')
    return False


def addWaitlist(user, programType):
    waitlist.append((user, programType))
    
# TODO: should update every n seconds on async thread
def updateWaitlist(update_interval):
    removed = []
    for index, (user, programType) in enumerate(waitlist):
        if book(user, programType):
            removed.append(index)
    for i in removed:
        waitlist.pop(i)

def setup():
    number_of_washers = 12
    update_interval = 60 # seconds
    
    for _ in range(number_of_washers):
        addWasher()
    addProgramType('kokvask', 'Kokvask', 60, 90)
    addProgramType('tøyvask', 'Tøyvask', 40, 60)
    addProgramType('håndvask', 'Håndvask', 30, 20)
    addUser('Ole')
    addUser('Hans')
    addUser('Liv')
    updateWaitlist(update_interval)

def main():
    setup()
    print('2')

    u1 = User('Ole')  
    w1 = washers[0]
    
    for _ in range(15):
        book(u1, 'kokvask', dt.now())
    for b in u1.bookings:
        print(b)
    cancelBook(u1, 54)

if __name__ == "__main__":
    main()
