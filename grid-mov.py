import numpy as np

print("Welcome to Robot Movement Manipulator, this works in a 3D plane.\n")
print("Define movement needed as...\n")

# Movement history stored globally
movement_history = []

# Function to print available shortcuts
def print_shortcuts():
    print("""Shortcuts for Movement:
          
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

# Function to print the current position
def current_pos(position):
    print("Current position is \n", position)
    return position

# Define movement bounds (-10 to 10 in all axes)
bounds = {
    "min": np.array([-10, -10, -10]),
    "max": np.array([10, 10, 10])
}

# Function to handle user movement
def user_input(position):
    print_shortcuts()

    # Dictionary for movement vectors
    moves = {
        "forward": np.array([0, 1, 0]),
        "backward": np.array([0, -1, 0]),
        "left": np.array([-1, 0, 0]),
        "right": np.array([1, 0, 0]),

        # Diagonal 2D movements
        "forward-right": np.array([1, 1, 0]),
        "forward-left": np.array([-1, 1, 0]),
        "backward-right": np.array([1, -1, 0]),
        "backward-left": np.array([-1, -1, 0]),

        # Up & Down
        "up": np.array([0, 0, 1]),
        "down": np.array([0, 0, -1]),

        # Diagonal 3D movements
        "up-forward": np.array([0, 1, 1]),  
        "up-backward": np.array([0, -1, 1]),  
        "up-left": np.array([-1, 0, 1]),  
        "up-right": np.array([1, 0, 1]),  
        "up-forward-right": np.array([1, 1, 1]),  
        "up-forward-left": np.array([-1, 1, 1]),  
        "up-backward-right": np.array([1, -1, 1]),  
        "up-backward-left": np.array([-1, -1, 1]),  

        "down-forward": np.array([0, 1, -1]),  
        "down-backward": np.array([0, -1, -1]),  
        "down-left": np.array([-1, 0, -1]),  
        "down-right": np.array([1, 0, -1]),  
        "down-forward-right": np.array([1, 1, -1]),  
        "down-forward-left": np.array([-1, 1, -1]),  
        "down-backward-right": np.array([1, -1, -1]),  
        "down-backward-left": np.array([-1, -1, -1])
    }

    # Dictionary for movement shortcuts
    shortcuts = {
        "f": "forward", "b": "backward", "l": "left", "r": "right",
        "fr": "forward-right", "fl": "forward-left", "br": "backward-right", "bl": "backward-left",
        "u": "up", "d": "down",
        "uf": "up-forward", "ub": "up-backward", "ul": "up-left", "ur": "up-right",
        "ufr": "up-forward-right", "ufl": "up-forward-left",
        "ubr": "up-backward-right", "ubl": "up-backward-left",
        "df": "down-forward", "db": "down-backward", "dl": "down-left", "dr": "down-right",
        "dfr": "down-forward-right", "dfl": "down-forward-left",
        "dbr": "down-backward-right", "dbl": "down-backward-left"
    }

    while True:
        direction = input("Define the direction or type 'exit' to stop: ").lower().strip()

        if direction == "exit":
            print("Exiting program... Final position:\n", position)
            print("Movement history:\n", movement_history)
            break 

        if direction in shortcuts:
            direction = shortcuts[direction]

        if direction in moves:
            new_position = position + moves[direction]
            
            # ✅ Check if movement is within bounds before updating position
            if np.all(new_position >= bounds["min"]) and np.all(new_position <= bounds["max"]):
                position = new_position
                movement_history.append(position.copy())
                current_pos(position)
            else:
                print("Out of bounds! Cannot move in that direction.")
        else:
            print("Invalid direction! Use a valid movement command.")

# Start movement
initial_position = np.array([0, 0, 0])
user_input(initial_position)
