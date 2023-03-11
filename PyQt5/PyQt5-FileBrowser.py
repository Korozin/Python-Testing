import os
import platform
import subprocess
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class FileBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_path = os.getcwd()
        self.tree = None
        self.create_widgets()
        self.update_tree()
        
        self.setGeometry(0, 0, 600, 400)

    def create_widgets(self):
        # create file system model and tree view
        self.model = QFileSystemModel()
        self.model.setRootPath(self.current_path)
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(self.current_path))
        self.tree.setSortingEnabled(True)
        self.tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tree.setUniformRowHeights(True)
        self.tree.customContextMenuRequested.connect(self.context_menu)

        # create main window layout
        self.setCentralWidget(self.tree)
        
        # connect doubleClicked signal to open_item function
        self.tree.doubleClicked.connect(lambda index: self.open_item(index))

        # create status bar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage(self.current_path)

        # create actions for context menu
        self.open_item_action = QAction("Open Item", self.tree)
        self.open_item_action.triggered.connect(lambda: self.open_item(self.tree.currentIndex()))
        self.new_folder_action = QAction("New Folder", self.tree)
        self.new_folder_action.triggered.connect(self.new_folder)
        self.new_file_action = QAction("New File", self.tree)
        self.new_file_action.triggered.connect(self.new_file)
        self.delete_action = QAction("Delete", self.tree)
        self.delete_action.triggered.connect(self.delete_item)

    def update_tree(self):
        # update model with new path
        self.model.setRootPath(self.current_path)
        self.tree.setRootIndex(self.model.index(self.current_path))

        # update status bar
        self.status_bar.showMessage(self.current_path)

    def new_folder(self):
        # get name for new folder from user input
        folder_name, ok = QInputDialog.getText(self.tree, "New Folder", "Enter folder name:")
        if ok and folder_name:
            # create new folder and update tree
            folder_path = os.path.join(self.current_path, folder_name)
            os.mkdir(folder_path)
            self.update_tree()

    def new_file(self):
        # prompt user for file name
        file_name, _ = QFileDialog.getSaveFileName(self.tree, "New File", self.current_path)
        if file_name:
            # create empty file and update tree
            open(file_name, "a").close()
            self.update_tree()

    def delete_item(self):
        # get selected item(s) from tree
        selected_items = self.tree.selectedIndexes()

        if selected_items:
            # confirm deletion
            confirm = QMessageBox.question(self.tree, "Confirm Deletion", "Are you sure you want to delete the selected item(s)?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if confirm == QMessageBox.Yes:
                # delete item(s) and update tree
                for item in selected_items:
                    item_path = self.model.filePath(item)
                    if os.path.isdir(item_path):
                        os.rmdir(item_path)
                    else:
                        os.remove(item_path)
                self.update_tree()

    def open_item(self, index):
        # get selected item from tree
        item_path = self.model.filePath(index)

        if os.path.isdir(item_path):
            # change to selected directory and update tree
            self.current_path = item_path
            self.update_tree()
        else:
            # open file with system default program
            if platform.system() == 'Windows':
                os.startfile(item_path)
            else:
                subprocess.run(['xdg-open', item_path])
                
    def context_menu(self, pos):
        # get selected item(s) from tree
        selected_items = self.tree.selectedIndexes()

        if selected_items:
            # create context menu
            menu = QMenu(self)

            # add actions to context menu
            menu.addAction(self.open_item_action)
            menu.addAction(self.new_folder_action)
            menu.addAction(self.new_file_action)
            menu.addAction(self.delete_action)

            # show context menu
            menu.exec_(self.tree.viewport().mapToGlobal(pos))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileBrowser()
    ex.show()
    sys.exit(app.exec_())