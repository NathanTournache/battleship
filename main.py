import tkinter as tk
from tkinter import messagebox
import random

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.plateau = [['' for _ in range(10)] for _ in range(10)]
        self.navires = []

    def ajouter_navire(self, taille, positions):
        navire = {'taille': taille, 'positions': positions, 'touche': 0}
        self.navires.append(navire)
        for x, y in positions:
            self.plateau[x][y] = navire

# Initialize the main window
root = tk.Tk()
root.title("Jeu de la Bataille Navale")
root.configure(bg='navy')

# Create grid for player
player_grid = [[None for _ in range(10)] for _ in range(10)]

# Create a dedicated area for ships
ship_area = tk.Frame(root, bg='navy')
ship_area.grid(row=0, column=12, rowspan=10)

# Create grid with buttons
def create_grid(grid, start_row, start_col, command):
    for i in range(10):
        for j in range(10):
            grid[i][j] = tk.Button(root, width=2, height=1, bg='lightblue', command=lambda i=i, j=j: command(i, j))
            grid[i][j].grid(row=start_row + i, column=start_col + j, padx=1, pady=1)

create_grid(player_grid, 0, 0, lambda i, j: on_player_click(i, j))

# Variables to store the current ship being dragged and its orientation
current_ship = None
current_orientation = 'H'
selected_ship_length = None

# Function to handle ship selection
def select_ship(event):
    global current_ship, selected_ship_length
    widget = event.widget
    selected_ship_length = int(widget.cget('text'))
    current_ship = widget

    # Add visual effect to the selected ship
    widget.config(bg='yellow')

# Function to change the orientation of the ship
def change_orientation():
    global current_orientation
    current_orientation = 'V' if current_orientation == 'H' else 'H'
    orientation_button.config(text=f"Orientation: {current_orientation}")

# Function to place the selected ship on the grid
def on_player_click(row, col):
    global current_ship, selected_ship_length

    if current_ship is None:
        messagebox.showerror("Erreur", "Veuillez sélectionner un navire.")
        return

    # Check if the ship can be placed legally on the grid
    positions = [(row + i, col) if current_orientation == 'V' else (row, col + i) for i in range(selected_ship_length)]
    
    if all(0 <= x < 10 and 0 <= y < 10 and player.plateau[x][y] == '' for x, y in positions):
        player.ajouter_navire(selected_ship_length, positions)
        for x, y in positions:
            player_grid[x][y].config(bg='black')
        current_ship.pack_forget()  # Remove the ship from the interface
        current_ship = None
        selected_ship_length = None

        # Update validate button state
        if len(player.navires) == 6:
            validate_button.config(state=tk.NORMAL)
    else:
        messagebox.showerror("Erreur", "Position invalide ou chevauchement de navires. Réessayez.")

# Function to place player ships in the dedicated area for selection
def place_player_ships():
    ships = [('Porte-avions', 5), ('Croiseur', 4), ('Destroyer', 3), ('Destroyer', 3), ('Sous-marin', 2), ('Sous-marin', 2)]
    for ship_name, ship_length in ships:
        label = tk.Label(ship_area, text=str(ship_length), bg='black', fg='white', width=ship_length*2)
        label.pack(pady=5)
        label.bind("<Button-1>", select_ship)

# Function to start a new game
def new_game():
    global player
    player = Joueur("Joueur 1")
    place_player_ships()
    turn_label.config(text="Placez vos navires")
    validate_button.config(state=tk.DISABLED)

# Function to validate the placement of ships and start the game
def validate_placement():
    if len(player.navires) == 6:
        messagebox.showinfo("Placement validé", "Tous les navires sont placés. La partie peut commencer.")
        turn_label.config(text="Tour du joueur")
        # Disable further placement of ships
        for widget in ship_area.winfo_children():
            widget.unbind("<Button-1>")
    else:
        messagebox.showerror("Erreur", "Tous les navires ne sont pas encore placés.")

# Add a button to change the orientation of the ships
orientation_button = tk.Button(root, text=f"Orientation: {current_orientation}", command=change_orientation)
orientation_button.grid(row=12, column=12)

# Add a button to start a new game and validate placement of ships
new_game_button = tk.Button(root, text="Nouvelle Partie", command=new_game)
new_game_button.grid(row=12, column=0, columnspan=5)

validate_button = tk.Button(root, text="Valider Placement", command=validate_placement)
validate_button.grid(row=12, column=5, columnspan=5)
validate_button.config(state=tk.DISABLED)

# Add a label to indicate the current turn or instructions
turn_label = tk.Label(root, text="Placez vos navires", bg='navy', fg='white')
turn_label.grid(row=11, column=0, columnspan=10)

# Start the main loop of Tkinter
root.mainloop()