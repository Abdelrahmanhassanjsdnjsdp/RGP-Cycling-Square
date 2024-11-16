import tkinter as tk

running = False


def start_cycle():
    global running
    running = True
    cycle_colors()


def stop_cycle():
    global running
    running = False

def cycle_colors():
    global running
    if not running:
        return
    colors = ["red", "green", "blue"]  
    current_color = box.cget("bg")  
    next_color = colors[(colors.index(current_color) + 1) % len(colors)]  
    box.config(bg=next_color)  
    root.after(100, cycle_colors)  

root = tk.Tk()
root.title("Fast RGB Box")


box = tk.Label(root, width=20, height=10, bg="red")  
box.pack(pady=20)


start_button = tk.Button(root, text="Start RGB", command=start_cycle)
start_button.pack(side="left", padx=10)

stop_button = tk.Button(root, text="Stop RGB", command=stop_cycle)
stop_button.pack(side="right", padx=10)

root.mainloop()
