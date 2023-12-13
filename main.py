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
        self.txtUser = StringVar()
        self.txtAbility = StringVar()
        self.txtAbility = StringVar()
        self.myOntoPath = list()

    def create_tabs(self):
        tab_control = ttk.Notebook(self.master)
        self.create_main_tab(tab_control)
        self.create_vulnerabilities_tab(tab_control)
        self.create_concepts_tab(tab_control)
        self.create_concepts_plus_tab(tab_control)
        self.create_advanced_check_tab(tab_control)
        self.create_user_tab(tab_control)
        tab_control.pack(expand=1, fill="both")

    def create_main_tab(self, tab_control):
        main_tab = ttk.Frame(tab_control)
        tab_control.add(main_tab, text="Main")

        # Labels for show data in main tab menu
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

        # main tab layout design
        lblBrowse = ttk.Label(main_tab, text="select file : ", anchor="e")
        lblBrowse.place(x=10, y=20)
        btnBrowse = ttk.Button(main_tab, text="file", command=self.open_file)
        btnBrowse.pack()
        btnBrowse.place(x=70, y=20)
        current_file_dir = dirname(abspath(__file__))

    def create_vulnerabilities_tab(self, tab_control):
        vulnerabilities_tab = ttk.Frame(tab_control)
        tab_control.add(vulnerabilities_tab, text="Vulnerabilities")

        # Additional code for vulnerabilities tab
        lblVulnerabilitiesTitle = ttk.Label(
            vulnerabilities_tab, text="A list of security vulnerabilities:", anchor="e")
        lblVulnerabilitiesTitle.place(x=10, y=10)

        name_entry = Entry(vulnerabilities_tab,
                           textvariable=self.name_vulnerability)
        name_entry.place(x=450, y=10, width=320)

        self.listboxVul = Listbox(vulnerabilities_tab)
        self.listboxVul.bind('<<ListboxSelect>>', lambda evt: self.show_vulnerabilities_textbox(
            evt, name_entry, self.name_vulnerability))
        self.listboxVul.place(x=10, y=40, height=500, width=280)

        lblVulnerabilitiesName = ttk.Label(
            vulnerabilities_tab, text="Vulnerability name:", anchor="e")
        lblVulnerabilitiesName.place(x=340, y=10)

        vulnerabilitiesGroupBox = LabelFrame(
            vulnerabilities_tab, text="This is a LabelFrame")
        vulnerabilitiesGroupBox.place(x=340, y=40, width=435, height=500)

        var = IntVar()

    def create_concepts_tab(self, tab_control):
        concepts_tab = ttk.Frame(tab_control)
        tab_control.add(concepts_tab, text="Concepts")

        # Rest of the concepts tab code here...

    def create_concepts_plus_tab(self, tab_control):
        concepts_plus_tab = ttk.Frame(tab_control)
        tab_control.add(concepts_plus_tab, text="Concepts++")

        # Rest of the concepts++ tab code here...

    def create_advanced_check_tab(self, tab_control):
        advanced_check_tab = ttk.Frame(tab_control)
        tab_control.add(advanced_check_tab, text="Advanced Check")

        # Rest of the advanced check tab code here...

    def create_user_tab(self, tab_control):
        user_tab = ttk.Frame(tab_control)
        tab_control.add(user_tab, text="User")

        # Rest of the user tab code here...

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

    def file_open_box(self):
        root = tk.Tk()
        root.withdraw()  # Hide the main window

        path = filedialog.askopenfilename()
        return path

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


def main():
    root = tk.Tk()
    app = NetworkSecurityOntologyApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
