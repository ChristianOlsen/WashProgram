from washit import Washit
from datetime import datetime as dt

from washit import Washit
from washit import User


# these tests should be own unittests in tests dir
def test_washit():
    w = Washit(12)
    u1 = User('Chris')
    
    for _ in range(12):
        w.book(u1, 'kokvask', dt.now()) # u1 books all 12 washers now
    assert len(u1.getBookings()) == 12  # u1 should have 12 bookings on profile
    assert w.book(u1, 'kokvask', dt.now()) == False # u1 should not be allowed to have more than one booking per washer
    
    print(f'{u1} BOOKGINS')
    for b in u1.getBookings():
        print(b)
    
    assert w.cancelBook(u1, 5) == True
    assert len(u1.getBookings()) == 11
    assert w.cancelBook(u1, 999) == False
    
    
test_washit()
