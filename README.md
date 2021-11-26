# WashIt

### Prerequisites

* Installed python 3.0+
* Installed pip3

Install the package:
Clone this repository locally to your machine.
* Go to washit directory
```bash
$ pip3 install .
```
Now you can acess washit in command line from any directory.

### Functionality

* Users book washers by specifying the type of programme and time
* Users are able to cancel their booking
* Max 1 booking per washer per user. That means a user can have up to 12 bookings if the are 12 washers in the system
* Admin can easily add more programtypes to the system

Types for washing programmes:
* Kokvask: 60 grader, 90 minutter
* Tøyvask: 40 grader, 60 minutter
* Håndvask: 30 grader, 20 minutter

### Missing Functionality

* Command line interface
* GUI interface
* Waitlist
* Identification of user
* Checkin for user, with cancellation after 15 min overtime
* Booking of dryers

### Usage

Per now this is a python programming interface.

#### Basic example

Setup washit system and add a booking for 'Kokvask' for a user 'Chris' at date now.

```
from datetime import datetime as dt

washit = Washit(12)
u1 = User('Chris')
washit.book(u1, 'kokvask', dt.now())
```
