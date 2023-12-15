import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import filedialog
import types
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from owlready2 import *
from os.path import dirname, abspath, join
from tkcalendar import DateEntry


class NetworkSecurityOntologyApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Network Security Ontology")
        self.master.geometry("800x600")

        # Variables
        self.initialize_variables()

        # Create tabs
        self.create_tabs()

    # variables initialized
    def initialize_variables(self):
        self.my_concept_var = StringVar(value="0")
        self.my_subclasses_var = StringVar(value="0")
        self.my_Vulnerabilities_var = StringVar(value="0")
        self.my_is_part_of_var = StringVar(value="0")
        self.my_has_vulnerability_var = StringVar(value="0")
        self.relationships = StringVar(value="0")
        self.name_vulnerability = StringVar()
        self.conceptsCombo_value = StringVar()
        self.txtSubClass = StringVar()
        self.txtPartOf1 = StringVar()
        self.txtPartOf2 = StringVar()
        self.search_str = StringVar()
        self.strResult = StringVar()
        self.txtDelUser = StringVar()
        self.txtAbility = StringVar()
        self.txtAbility = StringVar()
        self.R1AddTxt = StringVar()
        self.R2AddTxt = StringVar()
        self.txtUser = StringVar()
        self.listboxVul = Listbox()
        self.myOntoPath = list()
        self.var = IntVar()

    # all tabs initialized
    def create_tabs(self):
        tab_control = ttk.Notebook(self.master)
        self.create_main_tab(tab_control)
        self.create_vulnerabilities_tab(tab_control)
        self.create_concepts_tab(tab_control)
        self.create_concepts_plus_tab(tab_control)
        self.create_advanced_check_tab(tab_control)
        self.create_user_tab(tab_control)
        tab_control.pack(expand=1, fill="both")

    # main tab initialized
    def create_main_tab(self, tab_control):
        main_tab = ttk.Frame(tab_control)
        tab_control.add(main_tab, text="Main")

        # Labels for showing data in main tab menu
        lblConcepts = ttk.Label(
            main_tab, text="Number of concepts we currently support: ", anchor="e")
        lblConcepts.place(x=10, y=440)
        lblConceptsValue = ttk.Label(
            main_tab, textvariable=self.my_concept_var)
        lblConceptsValue.place(x=240, y=440)
        lblVulnerabilities = ttk.Label(
            main_tab, text="Number of concepts we Vulnerabilities support: ", anchor="e")
        lblVulnerabilities.place(x=10, y=460)
        lblVul = ttk.Label(main_tab, textvariable=self.my_Vulnerabilities_var)
        lblVul.place(x=260, y=460)
        lblSubClassOf = ttk.Label(
            main_tab, text="Number of SubClassOf: ", anchor="e")
        lblSubClassOf.place(x=10, y=480)
        lblSubClass = ttk.Label(main_tab, textvariable=self.my_subclasses_var)
        lblSubClass.place(x=140, y=480)
        lblIsPartOf = ttk.Label(
            main_tab, text="Number of IsPartOf relationship: ", anchor="e")
        lblIsPartOf.place(x=10, y=500)
        lblIsPart = ttk.Label(main_tab, textvariable=self.my_is_part_of_var)
        lblIsPart.place(x=190, y=500)
        lblHasVulnerability = ttk.Label(
            main_tab, text="Number of hasVulnerability relationship: ", anchor="e")
        lblHasVulnerability.place(x=10, y=520)
        lblHasVulnerabilityValue = ttk.Label(
            main_tab, textvariable=self.my_has_vulnerability_var)
        lblHasVulnerabilityValue.place(x=230, y=520)
        lblRelationships = ttk.Label(
            main_tab, text="Relationships: ", anchor="e")
        lblRelationships.place(x=10, y=540)
        lblRelationShips = ttk.Label(main_tab, textvariable=self.relationships)
        lblRelationShips.place(x=90, y=540)

        # open file button
        lblBrowse = ttk.Label(main_tab, text="select file : ", anchor="e")
        lblBrowse.place(x=10, y=20)
        btnBrowse = ttk.Button(main_tab, text="file", command=self.open_file)
        btnBrowse.pack()
        btnBrowse.place(x=70, y=20)
        self.current_file_dir = dirname(abspath(__file__))

    # vulnerabilities tab initialized
    def create_vulnerabilities_tab(self, tab_control):
        vulnerabilities_tab = ttk.Frame(tab_control)
        tab_control.add(vulnerabilities_tab, text="Vulnerabilities")

        # vulnerabilities listbox
        lblVulnerabilitiesTitle = ttk.Label(
            vulnerabilities_tab, text="A list of security vulnerabilities:", anchor="e")
        lblVulnerabilitiesTitle.place(x=10, y=10)
        self.name_entry = Entry(vulnerabilities_tab,
                                textvariable=self.name_vulnerability)
        self.name_entry.place(x=450, y=10, width=320)
        self.listboxVul = Listbox(vulnerabilities_tab)
        self.listboxVul.bind('<<ListboxSelect>>',
                             self.show_vulnerabilities_textbox)
        self.listboxVul.place(x=10, y=40, height=500, width=280)

        # showing Vulnerability name
        lblVulnerabilitiesName = ttk.Label(
            vulnerabilities_tab, text="Vulnerability name:", anchor="e")
        lblVulnerabilitiesName.place(x=340, y=10)

        # showing ?
        vulnerabilitiesGroupBox = LabelFrame(
            vulnerabilities_tab, text="This is a LabelFrame")
        vulnerabilitiesGroupBox.place(x=340, y=40, width=435, height=500)

        # First radio button design
        R1Add = Radiobutton(vulnerabilitiesGroupBox, text="Add an existing vulnerability to concepts", value=1, variable=self.var,
                            command=self.show_vulnerabilities_option)
        R1Add.place(x=10, y=10)
        R1AddGroupBox = LabelFrame(vulnerabilitiesGroupBox)
        R1AddGroupBox.place(x=10, y=40, width=410, height=50)
        R1AddLbl = ttk.Label(
            R1AddGroupBox, text="Select vulnerability:", anchor="e")
        R1AddLbl.place(x=10, y=10)
        self.R1AddTxt = Entry(R1AddGroupBox, state="disabled",
                              textvariable=self.name_vulnerability)
        self.R1AddTxt.place(x=120, y=10, width=270)

        # Second radio button design
        R2Add = Radiobutton(vulnerabilitiesGroupBox, text="Add a new vulnerability to concepts", value=2, variable=self.var,
                            command=self.show_vulnerabilities_option)
        R2Add.place(x=10, y=120)
        R2AddGroupBox = LabelFrame(vulnerabilitiesGroupBox)
        R2AddGroupBox.place(x=10, y=150, width=410, height=50)
        R2AddLbl = ttk.Label(
            R2AddGroupBox, text="New vulnerability:", anchor="e")
        R2AddLbl.place(x=10, y=10)
        self.R2AddTxt = Entry(R2AddGroupBox, state="disabled")
        self.R2AddTxt.place(x=120, y=10, width=270)

        # Third radio button design
        RRemove = Radiobutton(vulnerabilitiesGroupBox, text="Remove a vulnerability to concepts", value=3, variable=self.var,
                              command=self.show_vulnerabilities_option)
        RRemove.place(x=10, y=230)
        RRemoveGroupBox = LabelFrame(vulnerabilitiesGroupBox)
        RRemoveGroupBox.place(x=10, y=260, width=410, height=50)
        RRemoveLbl = ttk.Label(
            RRemoveGroupBox, text="Select vulnerability:", anchor="e")
        RRemoveLbl.place(x=10, y=10)
        RRemoveTxt = Entry(RRemoveGroupBox, state="disabled",
                           textvariable=self.name_vulnerability)
        RRemoveTxt.place(x=120, y=10, width=270)

        # Select concepts
        LblVulnerabilityConcepts = ttk.Label(
            vulnerabilitiesGroupBox, text="Select Concepts:", anchor="e")
        LblVulnerabilityConcepts.place(x=60, y=330)
        self.conceptsCombo = ttk.Combobox(
            vulnerabilitiesGroupBox, textvariable=self.conceptsCombo_value, state="readonly")
        self.conceptsCombo.place(x=160, y=330, width=200)

        # Button for applying changes in vulnerabilities tab
        btnVulnerabilityApply = ttk.Button(
            vulnerabilitiesGroupBox, text="Apply", command=self.apply_vulnerability)
        btnVulnerabilityApply.pack()
        btnVulnerabilityApply.place(x=185, y=440)

    # concepts tab initialized
    def create_concepts_tab(self, tab_control):
        concepts_tab = ttk.Frame(tab_control)
        tab_control.add(concepts_tab, text="Concepts")

        # concepts tab bar design
        # search
        lblSearchInConcepts = ttk.Label(
            concepts_tab, text="Search", anchor="e")
        lblSearchInConcepts.place(x=10, y=20)
        TxtSearchInConcepts = Entry(concepts_tab, textvariable=self.search_str)
        TxtSearchInConcepts.bind('<Return>', self.search_concepts)
        TxtSearchInConcepts.place(x=55, y=20, width=200)

        # list box for concepts
        self.listboxConcepts = Listbox(concepts_tab)
        self.listboxConcepts.place(x=10, y=50, height=500, width=245)

        # find Vulnerabilities
        btnFindVulnerabilities = ttk.Button(
            concepts_tab, text="Find Vulnerabilities", command=self.find_vulnerabilities_from_concept)
        btnFindVulnerabilities.pack()
        btnFindVulnerabilities.place(x=280, y=50, width=180)
        listFindVulnerabilities = Listbox(concepts_tab)
        listFindVulnerabilities.place(x=280, y=80, height=150, width=180)

        # find super classes
        btnFindSuperClasses = ttk.Button(
            concepts_tab, text="Find super classes", command=self.find_superclass_from_concepts)
        btnFindSuperClasses.pack()
        btnFindSuperClasses.place(x=470, y=20, width=160)
        listFindSuperClasses = Listbox(concepts_tab)
        listFindSuperClasses.place(x=470, y=50, height=180, width=160)

        # find Parts
        btnFindParts = ttk.Button(concepts_tab, text="Find parts")
        btnFindParts.pack()
        btnFindParts.place(x=640, y=20, width=140)
        listFindParts = Listbox(concepts_tab)
        listFindParts.place(x=640, y=50, height=180, width=140)

        # radio buttons for concepts
        RSuperClasses = Radiobutton(
            concepts_tab, text="base on SuperClasses", value=0)
        RSuperClasses.place(x=280, y=230)
        RSuperClasses = Radiobutton(
            concepts_tab, text="base on Concepts parts", value=1)
        RSuperClasses.place(x=280, y=250)
        RSuperClasses = Radiobutton(
            concepts_tab, text="base on SuperClass and concept`s parts", value=2)
        RSuperClasses.place(x=280, y=270)

        # inference button
        btnInference = ttk.Button(concepts_tab, text="inference")
        btnInference.pack()
        btnInference.place(x=280, y=320, width=120, height=50)
        listInference = Listbox(concepts_tab)
        listInference.place(x=440, y=320, height=230, width=340)

    # concepts++ tab initialized

    def create_concepts_plus_tab(self, tab_control):
        concepts_plus_tab = ttk.Frame(tab_control)
        tab_control.add(concepts_plus_tab, text="Concepts++")

        # concepts++ added code
        conceptsPlusTabBar = ttk.Notebook(concepts_plus_tab)
        subClass = ttk.Frame(conceptsPlusTabBar)
        partOf = ttk.Frame(conceptsPlusTabBar)
        conceptsPlusTabBar.add(subClass, text="Sub class")
        conceptsPlusTabBar.add(partOf, text="Part of")
        conceptsPlusTabBar.pack()
        conceptsPlusTabBar.place(x=0, y=70, width=500, height=450)

        # list box for concepts++
        self.listboxConceptPlus = Listbox(concepts_plus_tab)
        self.listboxConceptPlus.place(x=520, y=10, height=560, width=265)

        # SubClassGroupBox
        SubClassGroupBox = LabelFrame(
            subClass, text="Add new concepts to be sub class of existing concepts")
        SubClassGroupBox.place(x=10, y=40, width=470, height=230)

        # btn add for subclass
        SubClassAddGroupBox = LabelFrame(subClass)
        SubClassAddGroupBox.place(x=10, y=290, width=470, height=100)
        btnSubClass = ttk.Button(
            SubClassAddGroupBox, text="Add", command=self.set_subclass_of)
        btnSubClass.pack()
        btnSubClass.place(x=350, y=40)

        # partOfGroupBox
        partOfGroupBox = LabelFrame(partOf, text="Add new")
        partOfGroupBox.place(x=10, y=40, width=470, height=230)

        # btn add for PartOf
        jobVulGroupBox = LabelFrame(partOf)
        jobVulGroupBox.place(x=10, y=290, width=470, height=100)
        btnPartOf = ttk.Button(jobVulGroupBox, text="Add",
                               command=self.is_part_of)
        btnPartOf.pack()
        btnPartOf.place(x=350, y=40)

    # advanced check tab initialized
    def create_advanced_check_tab(self, tab_control):
        advanced_check_tab = ttk.Frame(tab_control)
        tab_control.add(advanced_check_tab, text="Advanced Check")

    # user tab initialized
    def create_user_tab(self, tab_control):
        user_tab = ttk.Frame(tab_control)
        tab_control.add(user_tab, text="User")

    # loading file and datas
    def open_file(self):
        path = self.file_open_box()
        self.myOntoPath.append(path)

        try:
            self.show_data_main()
            self.set_vulnerabilities_item()
            self.set_concepts_combobox()
            self.show_concepts()
            self.show_user()
            self.get_vulnerabilities()
        except TypeError:
            messagebox.showinfo("Warning!", "File not found!")

    # file select window
    def file_open_box(self):
        root = tk.Tk()
        root.withdraw()  # Hide the main window

        file_path = filedialog.askopenfilename(
            filetypes=[("OWL Files", "*.owl")], title="Select an OWL File"
        )
        return file_path

    # showing datas in main tab labels
    def show_data_main(self):
        onto = get_ontology(self.myOntoPath[0]).load()
        concepts_length = "1012"
        vul_length = "78"
        subclass_length = list(default_world.sparql("""
            SELECT ?x ?y
            WHERE { ?x rdfs:subClassOf ?y.
            ?x rdf:type owl:Class.
            }
        """))
        y = list(default_world.sparql("""
            PREFIX my: <http://www.semanticweb.org/imana/ontologies/2022/10/Network#>
            SELECT ?x
            WHERE {?x owl:onProperty my:isPartOf.
            }
        """))
        x = list(default_world.sparql("""
            PREFIX my: <http://www.semanticweb.org/imana/ontologies/2022/10/Network#>
            SELECT ?x
            WHERE { ?x owl:onProperty my:hasVulnerability.
            }
        """))
        has_vulnerabilities_length = list(
            onto.hasVulnerability.get_relations()) + x
        is_part_of_length = list(onto.isPartOf.get_relations()) + y
        self.my_concept_var.set(str(concepts_length))
        self.my_Vulnerabilities_var.set(str(vul_length))
        self.my_subclasses_var.set(str(len(subclass_length)))
        self.my_is_part_of_var.set(str(len(is_part_of_length)))
        self.my_has_vulnerability_var.set(str(len(has_vulnerabilities_length)))
        self.relationships.set("3")

    # setting vulnerabilities items
    def set_vulnerabilities_item(self):
        onto = get_ontology(self.myOntoPath[0]).load()
        x = list(default_world.sparql("""
                PREFIX my: <http://www.semanticweb.org/imana/ontologies/2022/10/Network#>
                SELECT ?x
                        WHERE { ?x owl:onProperty my:hasVulnerability.
                        }
                """))
        new_vul = []
        for i in x:
            sp_x = str(i).split("'")
            new_vul.append(sp_x[1])

        vulnerability_list = list(onto.hasVulnerability.get_relations())
        vulnerability_items = list()
        for i in vulnerability_list:
            vulnerability_items.append(i[1])

        vulnerability_items.extend(new_vul)
        for i in vulnerability_items:
            self.listboxVul.insert(END, i)

    # finding concepts
    def split_concepts(self):
        onto = get_ontology(self.myOntoPath[0]).load()
        concepts_list = list()
        concepts_lists = list(onto.classes())
        for i in concepts_lists:
            concepts_list.append(str(i).split("."))
        return concepts_list

    # adding concepts to box
    def set_concepts_combobox(self):
        new_concepts_list = list()
        concepts_list = self.split_concepts()
        for i in concepts_list:
            new_concepts_list.append(i[1])
        self.conceptsCombo['values'] = new_concepts_list

    # checking wich radio button and disable other ones
    def show_vulnerabilities_option(self):
        selection = self.var.get()
        match selection:
            case 1:
                selection1 = str((self.listboxVul.get(ACTIVE)))
                self.name_vulnerability.set(selection1)
                self.R2AddTxt.config(state="disabled")
                self.set_concepts_combobox()
            case 2:
                self.R2AddTxt.config(state="normal")
                self.set_concepts_combobox()
            case 3:
                selection2 = str((self.listboxVul.get(ACTIVE)))
                self.name_vulnerability.set(selection2)
                self.R2AddTxt.config(state="disabled")
                self.show_remove_concepts()

    # adding vulnerability to
    def add_vulnerability(self, vulnerability_name):
        onto = get_ontology(self.myOntoPath[0]).load()
        try:
            concepts = self.conceptsCombo_value.get()
            concepts_lists = list(onto.classes())
            for i in concepts_lists:
                if str(i).find(concepts) != -1:
                    i.hasVulnerability = [vulnerability_name]
            messagebox.showinfo("successful!", "Added vulnerability!")
        except TypeError:
            messagebox.showinfo(
                "Unsuccessful!", "The vulnerability was not added!")
        onto.save(file=self.myOntoPath[0])

    # checking wich radio button to appply
    def apply_vulnerability(self):
        selection = self.var.get()
        match selection:
            case 1:
                self.add_existing_vulnerability()
            case 2:
                self.add_new_vulnerability()
            case 3:
                self.remove_vulnerability_from_concept()

    # add an existing vulnerability to a concept
    def add_existing_vulnerability(self):
        vulnerability_name = self.R1AddTxt.get()
        self.add_vulnerability(vulnerability_name)

    # add a new vulnerability
    def add_new_vulnerability(self):
        vulnerability_name = self.R2AddTxt.get()
        self.add_vulnerability(vulnerability_name)
        self.listboxVul.insert(END, vulnerability_name)

    # remove a vulnerability from a concept
    def remove_vulnerability_from_concept(self):
        onto = get_ontology(self.myOntoPath[0]).load()
        try:
            concepts = self.conceptsCombo_value.get()
            concepts_lists = list(onto.classes())
            for i in concepts_lists:
                if str(i).find(concepts) != -1:
                    i.hasVulnerability = ""

            messagebox.showinfo("successful!", "Removed vulnerability!")
        except TypeError:
            messagebox.showinfo(
                "Unsuccessful!", "The vulnerability was not added!")

        # onto.save(file="filename")
        onto.save(file=self.myOntoPath[0])

    # add selected vulnerabilitie to textbox
    def show_vulnerabilities_textbox(self, evt):
        self.name_entry.config(state="disabled")
        selection = str((self.listboxVul.get(tk.ACTIVE)))
        self.name_vulnerability.set(selection)

    def update_entry(self, event):
        try:
            selected_item = self.listboxAbility.get(
                self.listboxAbility.curselection())
            self.TxtDelAbility.delete(0, tk.END)
            self.TxtDelAbility.insert(0, selected_item)
        except:
            pass

    def search_concepts(self, event):
        concepts_list = self.split_concepts()
        search_string = self.search_str.get()
        self.listboxConcepts.delete(0, tk.END)
        if search_string == "":
            self.show_concepts()
        else:
            filtered_data = list()
            for item in concepts_list:
                if item[1].find(search_string) != -1:
                    filtered_data.append(item[1])
            for data in filtered_data:
                self.listboxConcepts.insert(tk.END, data)

    def find_vulnerabilities_from_concept(self):
        vul_list = self.show_vulnerabilities_from_concepts()
        self.listboxVul.delete(0, tk.END)
        c = 1

        for item in vul_list:
            self.listFindVulnerabilities.insert(c, item)
            c += 1

    # show_superclass_from_concepts method
    def find_superclass_from_concepts(self):
        onto = get_ontology(self.myOntoPath[0]).load()
        concepts_lists = list(onto.classes())
        concept_name = self.listboxConcepts.get(tk.ACTIVE)
        c_name = ''

        if isinstance(concept_name, tuple):
            c_name = concept_name[0]
        else:
            c_name = concept_name

        for concept in concepts_lists:
            sp_concept = str(concept).split(".")
            if sp_concept[1] == c_name:
                c = str(concept.is_a).split(".")
                self.listFindSuperClasses.insert(1, c[1][:-1])

    # show_concepts method

    def show_concepts(self):
        concepts_list = self.split_concepts()
        c = 1
        for i in concepts_list:
            self.listboxConcepts.insert(c, i[1])
            self.listboxConceptPlus.insert(c, i[1])
            c += 1

    # set_subclass_of method

    def set_subclass_of(self):
        try:
            self.get_subclass_of()
            self.listboxConceptPlus.insert(0, self.txtSubClass.get())
            messagebox.showinfo("Successful!", "Added subclass!")
        except TypeError:
            messagebox.showinfo("Unsuccessful!", "The subclass was not added!")

    # is_part_of method

    def is_part_of(self):
        f = self.txtPartOf1.get()
        s = self.txtPartOf2.get()
        onto = self.get_ontology(self.myOntoPath[0]).load()
        concepts_lists = list(onto.classes())
        first_concept = ''
        second_concept = ''
        try:
            for i in concepts_lists:
                if str(i).find(f) != -1:
                    sp_i = str(i).split(".")
                    if sp_i[1] == f:
                        first_concept = i

            for j in concepts_lists:
                if str(j).find(s) != -1:
                    sp_j = str(j).split(".")
                    if sp_j[1] == s:
                        second_concept = j

            first_concept.isPartOf = [second_concept]
            onto.save(file=self.myOntoPath[0])
            messagebox.showinfo("Successful!", f"The {f} is_part_of {s}!")
        except TypeError:
            messagebox.showinfo(
                "Unsuccessful!", f"The {f} was not made is_part_of the {s}!")


# main loop
def main():
    root = tk.Tk()
    app = NetworkSecurityOntologyApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
