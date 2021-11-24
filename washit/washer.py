from program import Program
from datetime import datetime, timedelta
import itertools

class Washer:
    newid = itertools.count().__next__
    programTypes = {
        'kokvask': {
            'name': 'Kokvask',
            'temperature': 60,
            'duration': 90,
        },
        'tøyvask': {
            'name': 'Kokvask',
            'temperature': 40,
            'duration': 60,
        },
        'håndvask': {
            'name': 'håndvask',
            'temperature': 30,
            'duration': 20,
        },
    }

    def __init__(self):
        self.id = Washer.newid()
        self.bookings = []
        self.waiting_list = []
    
    def book(self, start, programType):
        if programType not in Washer.programTypes:
            raise ValueError(f'{programType} is not a program.')
        
        p = Program(start, **Washer.programTypes[programType])
        if self.isAvailable(p.getStart(), p.getEnd()):
            self.bookings.append(p)
            print(f'Booked {p.name} on washer #{self.id} from {p.getStart("seconds")} to {p.getEnd("seconds")}.')
        else:
            print(f'Washer #{self.id} unavailable at {start}')
        
        
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
            
            for p in self.bookings:
                s += f'{p.getStart("seconds")} --> {p.getEnd("seconds")} ({p.name})\n'
        return s
            
