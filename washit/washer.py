from program import Program
from booking import Booking
from datetime import datetime, timedelta
import itertools
import bisect

class Washer:
    newid = itertools.count().__next__
    
    def __init__(self):
        self.id = Washer.newid()
        self.bookings = [] # list of booking
        self.waitlist = [] # list of user
    
    def book(self, user, programType, start=datetime.now()):
        b = Booking(user, programType, self.id, start)
        if self.isAvailable(b.getStart(), b.getEnd()):
            users = [b.user for b in self.bookings]
            if user in users:
                print('User only allowed to have one reservation per washer')
                return
            bisect.insort(self.bookings, b)
            user.addBooking(b)
            #print(f'Booked {b.program.description} on washer #{self.id} from {b.getStart("seconds")} to {b.getEnd("seconds")}.')
            return True
        else:
            #print(f'Washer #{self.id} unavailable at {start}')
            return False
        
    def isAvailable(self, start: datetime, end: datetime):
        for booking in self.bookings:
            b_start = booking.getStart()
            b_end = booking.getEnd()
            
            # checking the requested booking overlaps existing booking
            if b_start <= start <= b_end or b_start <= end <= b_end:
                return False
        return True
    
    def __str__(self):
        s = f'=== Washer #{self.id} bookings ===\n'
        if not self.bookings:
            s += 'No bookings.'
        else:
            for b in self.bookings:
                s += f'{b}\n'
        return s
            
