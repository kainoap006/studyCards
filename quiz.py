from tkinter import Toplevel, Label, Button, messagebox
import os
import json

def display_json_content(root, file_name):
    def load_json_file(file_path):
        """Loads the JSON file and returns the content."""
        try:
            with open(file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", f"File '{file_name}' not found!")
            return None
        except json.JSONDecodeError:
            messagebox.showerror("Error", f"File '{file_name}' contains invalid JSON!")
            return None

    def update_display():
        """Updates the display with the current key-value pair."""
        nonlocal current_index
        value_label.config(bg='black')
        if current_index < len(keys):
            key = keys[current_index]
            value = json_data[key]
            key_label.config(text=f"Key: {key}")
            value_label.config(text=f"Value: {value}")
            current_index += 1
        else:
            messagebox.showinfo("End", "No more key-value pairs to display.")

    def change_bgWhite(event):
        """Change the background color of the value label when clicked."""
        value_label.config(bg='white')  # Change background to white

    # Target folder and file path
    target_folder = os.path.join(os.getcwd(), "json_files")
    file_path = os.path.join(target_folder, file_name)

    # Load the JSON content
    json_data = load_json_file(file_path)
    if json_data is None:
        return  # Exit if the file could not be loaded

    if not isinstance(json_data, dict):
        messagebox.showerror("Error", "JSON content must be a dictionary!")
        return

    # Extract keys and prepare for iteration
    keys = list(json_data.keys())
    current_index = 0

    # Create a new window
    display_window = Toplevel(root)
    display_window.title(f"Displaying: {file_name}")
    display_window.geometry("400x200")

    # Display key and value
    key_label = Label(display_window, text="Key:", font=("Arial", 14))
    key_label.pack(pady=10)

    value_label = Label(display_window, text="Value:", font=("Arial", 14), bg='black')
    value_label.pack(pady=10)
    value_label.bind("<Button-1>", change_bgWhite)

    # Button to move to the next key-value pair
    next_button = Button(display_window, text="Next", command=update_display)
    next_button.pack(pady=10)

    # Start displaying the first key-value pair
    update_display()
