import tkinter as tk
import random
import time

class FloatingWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.config(bg="black")
        
        self.label = tk.Label(self.root, text="I see you", fg="green", bg="black", font=("Helvetica", 24))
        self.label.pack(expand=True)
        
        # Start moving the window
        self.move_window()
        
    def move_window(self):
        # Randomize position
        x = random.randint(0, self.root.winfo_screenwidth() - 500)
        y = random.randint(0, self.root.winfo_screenheight() - 500)
        self.root.geometry(f"+{x}+{y}")
        
        # Schedule next move
        self.root.after(1000, self.move_window)  # Move every second

    def run(self):
        self.root.mainloop()

def spawn_windows(num_windows):
    windows = []
    for _ in range(num_windows):
        window = FloatingWindow()
        windows.append(window)
        window.root.after(0, window.run)  # Start the window immediately

if __name__ == "__main__":
    num_windows_to_spawn = 10  # Adjust the number of windows as desired
    spawn_windows(num_windows_to_spawn)
