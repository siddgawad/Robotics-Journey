import numpy as np

print("Welcome to Robot Movement manipulator, this works in 3d plane\n")
print("Define movemenet needed as...\n")



def print_shorcuts():
    print("""Shorcuts for Movement:
          
2D Movements:
f  -> forward
b  -> backward
l  -> left
r  -> right
fr -> forward-right
fl -> forward-left
br -> backward-right
bl -> backward-left

3D Movements:
u  -> up
d  -> down

Upward Diagonal:
uf  -> up-forward
ub  -> up-backward
ul  -> up-left
ur  -> up-right
ufr -> up-forward-right
ufl -> up-forward-left
ubr -> up-backward-right
ubl -> up-backward-left

Downward Diagonal:
df  -> down-forward
db  -> down-backward
dl  -> down-left
dr  -> down-right
dfr -> down-forward-right
dfl -> down-forward-left
dbr -> down-backward-right
dbl -> down-backward-left
          
          """)

     

def current_pos(position): #this is taking a parameter as position 
    print("Current position is \n", position)
    return position


def user_input(position):
    print_shorcuts()


    moves={
         "forward": np.array([0, 1, 0]),
    "reverse": np.array([0, -1, 0]),
    "left": np.array([-1, 0, 0]),
    "right": np.array([1, 0, 0]),
    
    # Diagonal 2D movements
    "forward-right": np.array([1, 1, 0]),
    "forward-left": np.array([-1, 1, 0]),
    "reverse-right": np.array([1, -1, 0]),
    "reverse-left": np.array([-1, -1, 0]),

    # Up & Down
    "up": np.array([0, 0, 1]),
    "down": np.array([0, 0, -1]),

    # Diagonal 3D movements
    "up-forward": np.array([0, 1, 1]),  
    "up-reverse": np.array([0, -1, 1]),  
    "up-left": np.array([-1, 0, 1]),  
    "up-right": np.array([1, 0, 1]),  
    "up-forward-right": np.array([1, 1, 1]),  
    "up-forward-left": np.array([-1, 1, 1]),  
    "up-reverse-right": np.array([1, -1, 1]),  
    "up-reverse-left": np.array([-1, -1, 1]),  

    "down-forward": np.array([0, 1, -1]),  
    "down-reverse": np.array([0, -1, -1]),  
    "down-left": np.array([-1, 0, -1]),  
    "down-right": np.array([1, 0, -1]),  
    "down-forward-right": np.array([1, 1, -1]),  
    "down-forward-left": np.array([-1, 1, -1]),  
    "down-reverse-right": np.array([1, -1, -1]),  
    "down-reverse-left": np.array([-1, -1, -1])

    }

    movement_history=[]
  

    shortcuts ={
          # 2D Movements
    "f": "forward",
    "b": "backward",
    "l": "left",
    "r": "right",
    "fr": "forward-right",
    "fl": "forward-left",
    "br": "backward-right",
    "bl": "backward-left",

    # 3D Up/Down Movements
    "u": "up",
    "d": "down",

    # 3D Up Movements
    "uf": "up-forward",
    "ub": "up-backward",
    "ul": "up-left",
    "ur": "up-right",
    "ufr": "up-forward-right",
    "ufl": "up-forward-left",
    "ubr": "up-backward-right",
    "ubl": "up-backward-left",

    # 3D Down Movements
    "df": "down-forward",
    "db": "down-backward",
    "dl": "down-left",
    "dr": "down-right",
    "dfr": "down-forward-right",
    "dfl": "down-forward-left",
    "dbr": "down-backward-right",
    "dbl": "down-backward-left"

        
                }
 
    while True:
        
        direction = input("Define the direction or type exit to stop ").lower()

        if direction=="exit":
            print("Exiting porgram...final positon: \n", position)
            print("Movement history:\n",movement_history)
            break 

        if direction in shortcuts:
            direction=shortcuts[direction]

        if direction in moves:
            position+=moves[direction]
            movement_history.append(position.copy())
            current_pos(position)

        else:
            print("Invalid direction! Use forward, reverse, right, left, foward-right, forward-left...")



initial_position=np.array([0,0,0])
current_pos(initial_position)
user_input(initial_position)


