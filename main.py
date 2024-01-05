from tkinter import StringVar, Listbox
from tkinter import filedialog, ttk, Button, Label, LabelFrame, Entry
import tkinter as tk
from owlready2 import *


class NetworkSecurityOntologyApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Network Security Ontology")
        self.master.geometry("1920x1080")

        # Variables
        self.prefix = StringVar()
        self.onto_path = StringVar()
        self.myOntoPath = list()
        self.onto = StringVar()
        self.Listbox = []

        # Create tabs
        self.create_tabs()

    # Initialize variables
    def initialize_variables(self):
        self.prefix = StringVar()
        self.onto_path = StringVar()
        self.myOntoPath = list()
        self.onto = StringVar()
        self.Listbox = []

    # Create tabs
    def create_tabs(self):
        tab_control = ttk.Notebook(self.master)
        self.create_view_tab(tab_control)
        tab_control.pack(expand=1, fill="both")

    # Create view tab
    def create_view_tab(self, tab_control):
        view_tab = ttk.Frame(tab_control)
        tab_control.add(view_tab, text="Standards")

        # Load File UI
        loadfileGroupBox = LabelFrame(view_tab, text="Load owl file")
        loadfileGroupBox.place(x=6, y=6, width=650, height=100)

        # Open file button
        lblBrowse = Label(view_tab, text="Select file : ", anchor="e")
        lblBrowse.place(x=12, y=60)

        btnBrowse = Button(view_tab, text="File", command=self.load_file)
        btnBrowse.place(x=90, y=60, width=90)

        tiplbl = Label(
            view_tab, text="Please make sure to enter Prefix correctly!!!")
        tiplbl.place(x=210, y=60)

        # Prefix input
        lblBrowse2 = Label(view_tab, text="Prefix : ", anchor="e")
        lblBrowse2.place(x=12, y=27)
        self.prefixBox = Entry(view_tab, textvariable=self.prefix, width=90)
        self.prefixBox.insert(0, "http://www.semantic.org/hamidzadeh/SOSM")
        self.prefixBox.place(x=72, y=27)

        # ListBox and view UI
        viewGroupBox = LabelFrame(view_tab, text="View")
        viewGroupBox.place(x=6, y=120, width=1890, height=810)

        label1 = Label(view_tab, text="Classes:")
        label1.place(x=54, y=180)
        start_x = 54
        start_y = 210
        list_width = 54

        for listnum in range(0, 5):
            self.Listbox.append(Listbox(view_tab, height=30, width=list_width))
            self.Listbox[listnum].bind(
                '<<ListboxSelect>>', self.show_subclasses)
            start_x += list_width + 300 if listnum != 0 else 0
            self.Listbox[listnum].place(x=start_x, y=start_y)

    # Load file and datas
    def load_file(self):
        # Choosing file
        self.onto_path.set(self.file_open_box())
        # Loading owl
        self.onto = owlready2.get_ontology(self.onto_path.get()).load()
        # Set prefix
        self.prefix.set(self.prefixBox.get())
        self.extract_classes()

    # File select window
    def file_open_box(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("OWL Files", "*.owl")], title="Select an OWL File")
        return file_path

    # Extract classes from ontology
    def extract_classes(self):
        namespace = self.onto.get_namespace("http://www.w3.org/2002/07/owl")
        class_name = getattr(namespace, 'Thing', None)
        subclasses = list(class_name.subclasses())
        for subclass in subclasses:
            self.Listbox[0].insert("end", str(subclass.name).replace('_', ' '))

    # Extract subclasses based on the parent
    def extract_Subclasses(self, parent):
        namespace = self.onto.get_namespace(self.prefix.get())
        class_name = getattr(namespace, parent, None)
        subclasses = list(class_name.subclasses())
        return subclasses

    # Show subclasses when a Listbox item is selected
    def show_subclasses(self, event):
        num = -1  # Initialize num to an invalid value
        for i, listbox in enumerate(self.Listbox):
            if listbox.curselection() != ():
                num = i

        if num != 4:
            for list in range(num+1, 5):
                self.Listbox[list].delete(0, tk.END)
            selected_index = self.Listbox[num].curselection()
            if selected_index:
                selected_item = self.Listbox[num].get(selected_index[0])
                selected_item = str(selected_item).replace(' ', '_')
                subclasses = self.extract_Subclasses(selected_item)
                for subclass in subclasses:
                    self.Listbox[num + 1].insert("end",
                                                 str(subclass.name).replace('_', ' '))


def main():
    root = tk.Tk()
    NetworkSecurityOntologyApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
