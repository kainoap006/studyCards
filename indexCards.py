from tkinter import *
from json_editor import open_editor  # type: ignore 
from quiz import display_json_content # type: ignore 
import os

def makeList():
    # Define the target folder
    target_folder = os.path.join(os.getcwd(), "json_files")
    matching_files = []

    # Ensure the folder exists
    if not os.path.exists(target_folder):
        print("Target folder does not exist.")
        return matching_files

    # Loop through each file in the folder
    for file_name in os.listdir(target_folder):
        # Check if the file is a JSON file
        if file_name.endswith(".json"):
            matching_files.append(file_name)

    return matching_files

def refresh_listbox():
    # Clear the existing content in the Listbox
    mylist.delete(0, END)

    # Re-populate the Listbox with updated JSON files
    updated_list = makeList()
    for file_name in updated_list:
        mylist.insert(END, file_name)

def selected_item():
    # Traverse the tuple returned by curselection method
    # and return corresponding value(s) in the listbox
    for i in mylist.curselection():
        return mylist.get(i)
    return 

root = Tk()
root.title("Index Cards")

# Create three buttons
buttonQuizMe = Button(root, text="Quiz me (Select one)", command=lambda: display_json_content(root, selected_item()))
buttonNewStudyCards = Button(root, text="Create/Edit new study cards", command=lambda: [open_editor(root, selected_item()), refresh_listbox()])
buttonRefresh = Button(root, text="Refresh List", command=refresh_listbox)

# Pack the buttons vertically
buttonQuizMe.pack(pady=5)
buttonNewStudyCards.pack(pady=5)
buttonRefresh.pack(pady=5)

# Create a frame to hold the Listbox and Scrollbar
frame = Frame(root)
frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

# Create the Scrollbar and Listbox inside the frame
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

mylist = Listbox(frame, yscrollcommand=scrollbar.set)
mylist.pack(side=LEFT, fill=BOTH, expand=True)

# Configure the Scrollbar to work with the Listbox
scrollbar.config(command=mylist.yview)

# Initial population of the Listbox
refresh_listbox()

mainloop()
