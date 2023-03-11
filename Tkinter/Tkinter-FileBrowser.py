import os
import platform
import subprocess
import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog

class FileBrowser:
    def __init__(self, root):
        self.root = root
        self.current_path = os.getcwd()
        self.tree = None
        self.create_widgets()
        self.update_tree()

    def create_widgets(self):
        # create frame for buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(fill=tk.X, padx=5, pady=5)

        # create buttons
        tk.Button(button_frame, text="New Folder", command=self.new_folder).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="New File", command=self.new_file).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Delete", command=self.delete_item).pack(side=tk.LEFT, padx=5)

        # create treeview widget
        self.tree = tk.ttk.Treeview(self.root)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # add columns to treeview
        self.tree["columns"] = ("type", "size")
        self.tree.column("#0", width=300)
        self.tree.column("type", width=100)
        self.tree.column("size", width=100)

        # add column headings
        self.tree.heading("#0", text="Name")
        self.tree.heading("type", text="Type")
        self.tree.heading("size", text="Size")

        # bind double-click to open file/folder
        self.tree.bind("<Double-1>", self.open_item)

        # create status bar
        self.status_bar = tk.Label(self.root, text=self.current_path, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def update_tree(self):
        # clear tree
        self.tree.delete(*self.tree.get_children())

        # add parent directory to tree
        parent_dir = os.path.abspath(os.path.join(self.current_path, os.pardir))
        self.tree.insert("", "end", text="..", values=("Directory", ""), iid=parent_dir)

        # add files and directories to tree
        for item in os.listdir(self.current_path):
            item_path = os.path.join(self.current_path, item)
            if not item.startswith(".") and os.path.exists(item_path):
                if os.path.isdir(item_path):
                    self.tree.insert("", "end", text=item, values=("Directory", ""), iid=item_path)
                else:
                    size = os.path.getsize(item_path)
                    self.tree.insert("", "end", text=item, values=("File", f"{size} bytes"), iid=item_path)

        # update status bar
        self.status_bar.config(text=self.current_path)

        # update status bar
        self.status_bar.config(text=self.current_path)

    def new_folder(self):
        # get name for new folder from user input
        folder_name = simpledialog.askstring("New Folder", "Enter folder name:")

        if folder_name:
            # create new folder and update tree
            folder_path = os.path.join(self.current_path, folder_name)
            os.mkdir(folder_path)
            self.update_tree()

    def new_file(self):
        # prompt user for file name
        file_name = filedialog.asksaveasfilename(initialdir=self.current_path)
        if file_name:
            # create empty file and update tree
            open(file_name, "a").close()
            self.update_tree()

    def delete_item(self):
        # get selected item(s) from tree
        selected_items = self.tree.selection()

        if selected_items:
            # confirm deletion
            confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete the selected item(s)?")
        if confirm:
            # delete item(s) and update tree
            for item in selected_items:
                item_path = self.tree.item(item, "text")
                if os.path.isdir(item_path):
                    os.rmdir(item_path)
                else:
                    os.remove(item_path)
            self.update_tree()

    def open_item(self, event):
        # get selected item from tree
        item = self.tree.selection()[0]
        item_name = self.tree.item(item, "text")

        # get full path of selected item
        item_path = os.path.join(self.current_path, item_name)

        if os.path.isdir(item_path):
            # change to selected directory and update tree
            self.current_path = item_path
            self.update_tree()
            # update status bar with new path
            self.status_bar.config(text=os.path.abspath(self.current_path))
        else:
            # open file with system default program
            if platform.system() == 'Windows':
                subprocess.run(['start', item_path], shell=True)
            else:
                subprocess.run(['xdg-open', item_path])
            
# create Tkinter window
root = tk.Tk()
root.title("File Browser")
root.geometry("800x600")

# create file browser object
file_browser = FileBrowser(root)

# run window
root.mainloop()
