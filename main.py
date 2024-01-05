from tkinter import StringVar, Listbox
from tkinter import filedialog, ttk, Button, Label, LabelFrame, Entry
import tkinter as tk
import owlready2


class NetworkSecurityOntologyApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Network Security Ontology")
        self.master.geometry("1920x1080")

        # Variables
        self.initialize_variables()

        # Create tabs
        self.create_tabs()

    # variables initialized
    def initialize_variables(self):
        self.prefix = StringVar()
        self.onto_path = StringVar()
        self.myOntoPath = list()
        self.onto = StringVar()
        self.Listbox = []

    # all tabs initialized
    def create_tabs(self):
        tab_control = ttk.Notebook(self.master)
        self.create_view_tab(tab_control)
        tab_control.pack(expand=1, fill="both")

    def create_view_tab(self, tab_control):
        view_tab = ttk.Frame(tab_control)
        tab_control.add(view_tab, text="Standards")
        # Load File UI
        # load file GroupBox
        loadfileGroupBox = LabelFrame(view_tab, text="Load owl file")
        loadfileGroupBox.place(x=6, y=6, width=650, height=100)
        # open file button
        lblBrowse = Label(view_tab, text="select file : ", anchor="e")
        lblBrowse.place(x=12, y=60)
        btnBrowse = Button(view_tab, text="file", command=self.load_file)
        btnBrowse.place(x=90, y=60, width=90)
        tiplbl = Label(
            view_tab, text="Please make sure to enter Prefix correctly!!!")
        tiplbl.place(x=210, y=60)
        # Prefix input
        lblBrowse2 = Label(view_tab, text="Prefix : ", anchor="e")
        lblBrowse2.place(x=12, y=27)
        self.prefixBox = Entry(view_tab, textvariable=self.prefix, width=90)
        # default value
        self.prefixBox.insert(0, "http://www.semantic.org/hamidzadeh/SOSM")
        self.prefixBox.place(x=72, y=27)

        # ListBox and view UI
        # View GroupBox
        viewGroupBox = LabelFrame(view_tab, text="View")
        viewGroupBox.place(x=6, y=120, width=1890, height=810)

        label_list = []
        label_list.insert(0, Label(view_tab, text="Classes:"))
        label_list.insert(1, Label(view_tab, text="Subclass:"))
        label_list.insert(2, Label(view_tab, text="Controllers"))
        label_list.insert(3, Label(view_tab, text="Sub Controls"))

        start_x = 54
        start_y = 210
        list_width = 54
        for listnum in range(0, 5):
            self.Listbox.insert(listnum, Listbox(
                view_tab, height=30, width=list_width))
            start_x += list_width + 300 if listnum != 0 else 0
            self.Listbox[listnum].place(
                x=start_x, y=start_y)

    # loading file and datas
    def load_file(self):
        # choosing file
        self.onto_path = self.file_open_box()
        # loading owl
        self.onto = owlready2.get_ontology(self.onto_path).load()
        # set prefix
        self.prefix = self.prefixBox.get()
        self.extract_classes()

    # file select window
    def file_open_box(self):
        root = tk.Tk()
        root.withdraw()  # Hide the main window

        file_path = filedialog.askopenfilename(
            filetypes=[("OWL Files", "*.owl")], title="Select an OWL File"
        )
        return file_path

    def extract_classes(self):
        for subclass in self.extract_Subclasses('Thing'):
            self.Listbox[0].insert("end", subclass.name)

    def extract_Subclasses(self, parent):
       # Get the namespace from the base IRI
        namespace = self.onto.get_namespace(
            self.prefix)
        # Get the class from the namespace
        class_name = getattr(namespace,  parent, None)
        subclasses = list(class_name.subclasses())
        return subclasses


def main():
    root = tk.Tk()
    NetworkSecurityOntologyApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
