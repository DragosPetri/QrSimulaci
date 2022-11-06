import time
from statemachine import StateMachine, State

path_to_image = "path.txt"

class door(StateMachine):

    closed = State('Closed', initial=True)
    open = State('Open')

    opendoor = closed.to(open)
    closedoor = open.to(closed)
    
    def on_opendoor(self) :
        f = open(path_to_image,"w")
        f.write("check.png")
        f.close()
        print("Door is open")

    def on_closedoor(self) :
        
        f = open(path_to_image,"w")
        f.write("qr.png")
        f.close
        print("Door closed")
    

def simulate_door():
    my_door = door()
    if (my_door.is_closed) :
        my_door.opendoor()
        time.sleep(3)
        my_door.closedoor()
        