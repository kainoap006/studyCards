from tkinter import Toplevel, Text, Frame, Button, Label, filedialog, BOTH, END
import json
import os

def open_editor(root, fileName=None):
    # Create a new window
    editor_window = Toplevel(root)
    editor_window.title("Edit JSON File")
    editor_window.geometry("500x410")
    
    # Text widget for editing JSON
    text_editor = Text(editor_window, wrap="word")
    text_editor.pack(fill=BOTH, expand=True, padx=10, pady=10)

    def load_file(file_path):
        """Helper function to load a JSON file into the editor."""
        try:
            with open(file_path, "r") as file:
                content = json.load(file)
                text_editor.delete(1.0, END)  # Clear existing content
                text_editor.insert(END, json.dumps(content, indent=4))  # Pretty-print JSON
        except (json.JSONDecodeError, FileNotFoundError) as e:
            # Handle errors (invalid JSON or file not found)
            error_label.config(text=f"Error: {str(e)}", fg="red")

    # Automatically load the file if fileName is provided and exists
    if fileName:
        target_folder = os.path.join(os.getcwd(), "json_files")
        file_path = os.path.join(target_folder, fileName)
        if os.path.exists(file_path):
            load_file(file_path)
        else:
            error_label.config(text=f"Error: File '{fileName}' does not exist!", fg="red")

    
    def open_file():
        # Define the target folder within the project directory
        target_folder = os.path.join(os.getcwd(), "json_files")        
        
        # Ensure the folder exists (optional, in case you want to restrict access)
        os.makedirs(target_folder, exist_ok=True)
        
        # Ask for a file from the target folder
        file_path = filedialog.askopenfilename(
            initialdir=target_folder,
            title="Open JSON File",
            filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")],
        )
        
        if file_path:
            try:
                # Open and load the JSON content
                with open(file_path, "r") as file:
                    content = json.load(file)
                    text_editor.delete(1.0, END)  # Clear existing content
                    text_editor.insert(END, json.dumps(content, indent=4))  # Pretty-print JSON
            except (json.JSONDecodeError, FileNotFoundError) as e:
                # Handle errors (invalid JSON or file not found)
                error_label.config(text=f"Error: {str(e)}", fg="red")
        

    def save_file():
        # Define the target folder within the project directory
        target_folder = os.path.join(os.getcwd(), "json_files")
        
        # Ensure the folder exists
        os.makedirs(target_folder, exist_ok=True)

        if (fileName is not None):
            # Parse the text content to ensure it's valid JSON
            content = json.loads(text_editor.get(1.0, END))
            # Save the file
            with open(target_folder + "/" + fileName, "w") as file:
                json.dump(content, file, indent=4)
                return None
        
        # Ask for the file name without path
        file_name = filedialog.asksaveasfilename(
            initialdir=target_folder,
            title="Save JSON File",
            defaultextension=".json",
            filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")],
        )
        
        # Ensure the file is saved in the target folder
        if file_name:
            try:
                # Parse the text content to ensure it's valid JSON
                content = json.loads(text_editor.get(1.0, END))
                # Save the file
                with open(file_name, "w") as file:
                    json.dump(content, file, indent=4)
            except json.JSONDecodeError:
                # Handle invalid JSON
                error_label.config(text="Error: Invalid JSON format!", fg="red")


    # Buttons for file operations
    button_frame = Frame(editor_window)
    button_frame.pack(pady=10)
    
    open_button = Button(button_frame, text="Open JSON File", command=open_file)
    open_button.pack(side="left", padx=5)
    
    save_button = Button(button_frame, text="Save JSON File", command=save_file)
    save_button.pack(side="left", padx=5)
    
    # Error label for displaying JSON errors
    error_label = Label(editor_window, text="", fg="red")
    error_label.pack(pady=5)

