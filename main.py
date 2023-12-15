import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
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
        self.vul_list = list()
        self.vul_list2 = list()
        self.listboxUsers = Listbox()
        self.var = IntVar()
        self.concepts_list = list()
        self.new_concepts_list = list()
        self.vulnerability_items = list()
        self.concepts_items = list()
        self.concept_vulnerabilities_list = list()
        self.max_value = 24

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
        self.RRemoveTxt = Entry(RRemoveGroupBox, state="disabled",
                                textvariable=self.name_vulnerability)
        self.RRemoveTxt.place(x=120, y=10, width=270)

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
        self.listFindVulnerabilities = Listbox(concepts_tab)
        self.listFindVulnerabilities.place(x=280, y=80, height=150, width=180)

        # find super classes
        btnFindSuperClasses = ttk.Button(
            concepts_tab, text="Find super classes", command=self.find_superclass_from_concepts)
        btnFindSuperClasses.pack()
        btnFindSuperClasses.place(x=470, y=20, width=160)
        self.listFindSuperClasses = Listbox(concepts_tab)
        self.listFindSuperClasses.place(x=470, y=50, height=180, width=160)

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
        # User tab
        UserTabBar = ttk.Notebook(user_tab)
        Users = ttk.Frame(user_tab)
        Ability = ttk.Frame(UserTabBar)
        job = ttk.Frame(UserTabBar)

        # make tab bar in concepts++
        UserTabBar.add(Users, text='Users')
        UserTabBar.add(Ability, text="Ability")
        UserTabBar.add(job, text="Job")
        UserTabBar.pack()
        UserTabBar.place(x=0, y=20, width=800, height=600)
        # User tab
        UserTabBar = ttk.Notebook(user_tab)
        Users = ttk.Frame(user_tab)
        Ability = ttk.Frame(UserTabBar)
        job = ttk.Frame(UserTabBar)

        # make tab bar in concepts++
        UserTabBar.add(Users, text='Users')
        UserTabBar.add(Ability, text="Ability")
        UserTabBar.add(job, text="Job")
        UserTabBar.pack()
        UserTabBar.place(x=0, y=20, width=800, height=600)

        # make group box for add Users in User
        AddUsersGroupBox = LabelFrame(Users, text="Add new User")
        AddUsersGroupBox.place(x=10, y=10, width=470, height=230)

        # make group box for delete Users in User
        DelUsersGroupBox = LabelFrame(Users, text="Delete User")
        DelUsersGroupBox.place(x=10, y=250, width=470, height=180)

        # text Delete user
        Lbl1DelUser = ttk.Label(
            DelUsersGroupBox, text="Delete User: ", anchor="e")
        Lbl1DelUser.place(x=10, y=50)

        # entry Delete user
        TxtDelUser = Entry(DelUsersGroupBox, textvariable=self.txtDelUser)
        TxtDelUser.place(x=80, y=50, width=270)

        # btn for add name from listbox to delete entry
        btnGetNameFromLbox = ttk.Button(
            DelUsersGroupBox, text="<<<", command=self.get_name_listbox)
        btnGetNameFromLbox.pack()
        btnGetNameFromLbox.place(x=370, y=50, width=50)

        # btn Delete user
        btnDelUsers = ttk.Button(
            DelUsersGroupBox, text="Delete", command=self.delete_user)
        btnDelUsers.pack()
        btnDelUsers.place(x=350, y=120)

        # text add user
        Lbl1AddUser = ttk.Label(
            AddUsersGroupBox, text="Add User: ", anchor="e")
        Lbl1AddUser.place(x=10, y=50)

        # entry add user
        TxtAddUser = Entry(AddUsersGroupBox, textvariable=self.txtUser)
        TxtAddUser.place(x=70, y=50, width=270)

        # btn add user
        btnAddUsers = ttk.Button(
            AddUsersGroupBox, text="Add", command=self.add_user)
        btnAddUsers.pack()
        btnAddUsers.place(x=350, y=160)

        # make group box for tab Ability in User
        AbilityGroupBox = LabelFrame(Ability, text="Add new Ability")
        AbilityGroupBox.place(x=10, y=10, width=470, height=230)

        # txt in ability
        Lbl1AddAbility = ttk.Label(AbilityGroupBox, text="Add : ", anchor="e")
        Lbl1AddAbility.place(x=10, y=50)

        Lbl2AddAbility = ttk.Label(
            AbilityGroupBox, text="to be Ability of", anchor="e")
        Lbl2AddAbility.place(x=330, y=50)

        # entry to add ability
        TxtAddAbility = Entry(AbilityGroupBox, textvariable=self.txtAbility)
        TxtAddAbility.place(x=50, y=50, width=270)

        # btn to add ability in ability tab
        btnAddAbility = ttk.Button(
            AbilityGroupBox, text="Add", command=self.add_ability)
        btnAddAbility.pack()
        btnAddAbility.place(x=350, y=160)

        # ability delete group box
        AbilityDelGroupBox = LabelFrame(Ability, text='Delete Ability')
        AbilityDelGroupBox.place(x=10, y=260, width=470, height=232)

        # txt for delete ability Gbox
        Lbl1DelAbility = ttk.Label(
            AbilityDelGroupBox, text="Delete Ability Of : ", anchor="e")
        Lbl1DelAbility.place(x=5, y=50)

        Lbl4DelAbility = ttk.Label(AbilityDelGroupBox, text="Select the Ability "
                                   "from the right side list", anchor="e")
        Lbl4DelAbility.place(x=0, y=110)

        # Entry to delete ability
        TxtDelAbility = Entry(AbilityDelGroupBox, textvariable=self.txtAbility)
        TxtDelAbility.place(x=105, y=50, width=215)

        # btn del ability
        btnDelAbility = ttk.Button(
            AbilityDelGroupBox, text="Delete", command=self.delete_ability)
        btnDelAbility.pack()
        btnDelAbility.place(x=350, y=150)

        # btn for show user ability
        btnShowUserAbl = ttk.Button(
            Ability, text='Show Selected User Ability', command=self.show_user_ability)
        btnShowUserAbl.pack()
        btnShowUserAbl.place(x=520, y=260, height=30, width=250)

        # list box2 for Ability
        listboxAbility = Listbox(Ability)
        listboxAbility.place(x=520, y=312, height=180, width=250)
        listboxAbility.bind("<<ListboxSelect>>", self.update_entry)

        # label for list box user ability
        lbl_user_ability = Label(Ability, text='User Ability :')
        lbl_user_ability.place(x=520, y=290)

        # job Tab vulnerabilities group box
        jobVulGroupBox = LabelFrame(job, text='Select vulnerabilities')
        jobVulGroupBox.place(x=10, y=20, width=470, height=300)

        # btn to add vulnerabilities to text box
        btnAddVulTextBox = ttk.Button(
            jobVulGroupBox, text="Add", command=self.add_vul_to_txtbox, state=DISABLED)
        btnAddVulTextBox.place(x=230, y=160, width=225)

        # txt in job Vulnerabilities group box
        lbl1AddJob = ttk.Label(
            jobVulGroupBox, text="Vulnerabilities:", anchor="e")
        lbl1AddJob.place(x=230, y=10)

        lbl2AddJob = ttk.Label(jobVulGroupBox, text="concepts:", anchor="e")
        lbl2AddJob.place(x=10, y=70)

        # list box for Vulnerabilities in job tab
        listboxvuljob = Listbox(jobVulGroupBox)
        listboxvuljob.place(x=230, y=30, height=120, width=225)

        # btn to show user ability job tab
        btnShowUserAblJob = ttk.Button(
            job, text='Show Selected User Ability', command=self.show_user_ability)
        btnShowUserAblJob.pack()
        btnShowUserAblJob.place(x=520, y=260, height=30, width=250)

        # list box for user ability in job tab
        listboxAbilityJob = Listbox(job)
        listboxAbilityJob.place(x=520, y=312, height=180, width=250)

        # label for list box user ability in job tab
        lbl_user_ability = Label(job, text='User Ability :')
        lbl_user_ability.place(x=520, y=290)

        # text box to add vulnerabilities job
        textboxVul = Text(jobVulGroupBox, state=DISABLED)
        textboxVul.place(x=230, y=195, height=80, width=225)

        # radio buttons in job tab
        job_radio = tk.IntVar()
        class_radio = Radiobutton(jobVulGroupBox, text="Base on class",
                                  value=0, variable=job_radio, command=self.by_class)
        class_radio.place(x=10, y=10)

        vul_radio2 = Radiobutton(jobVulGroupBox, text="Base on vulnerabilities",
                                 value=1, variable=job_radio, command=self.by_vul)
        vul_radio2.place(x=10, y=30)

        # vulnerabilities combo box in job tab
        self.jobVulCombo = ttk.Combobox(jobVulGroupBox, state='readonly')
        self.jobVulCombo.place(x=10, y=90, width=180)
        self.jobVulCombo.bind("<<ComboboxSelected>>", self.update_listbox)

        # make group box for tab Job in User
        jobTimeGroupBox = LabelFrame(job, text="Add new")
        jobTimeGroupBox.place(x=10, y=330, width=470, height=200)

        # txt in time group box in job tab
        lbl1Time = ttk.Label(
            jobTimeGroupBox, text="From       Time", anchor="e")
        lbl1Time.place(x=10, y=20)

        lbl2AddJob = ttk.Label(jobTimeGroupBox, text="Date:", anchor="e")
        lbl2AddJob.place(x=180, y=20)

        lbl2Time = ttk.Label(
            jobTimeGroupBox, text="To             Time", anchor="e")
        lbl2Time.place(x=10, y=80)

        lbl2AddJob = ttk.Label(jobTimeGroupBox, text="Date:", anchor="e")
        lbl2AddJob.place(x=180, y=80)

        # spin boxes in job tab

        TxtFromTime = Spinbox(jobTimeGroupBox, from_=1, to=self.max_value, validate="key",
                              validatecommand=(self.master.register(self.validate_spinbox_input), '%P'))
        TxtToTime = Spinbox(jobTimeGroupBox, from_=1, to=self.max_value, validate="key",
                            validatecommand=(self.master.register(self.validate_spinbox_input), '%P'))

        from_date_entry = DateEntry(jobTimeGroupBox, width=12, background='darkblue',
                                    foreground='white', borderwidth=2, date_pattern='dd/MM/y', state='readonly')
        from_date_entry.place(x=220, y=20)

        to_date_entry = DateEntry(jobTimeGroupBox, width=12, background='darkblue',
                                  foreground='white', borderwidth=2, date_pattern='dd/MM/y', state='readonly')
        to_date_entry.place(x=220, y=80)

        btn_save_job = ttk.Button(
            jobTimeGroupBox, text="Save", command=self.add_job)
        btn_save_job.place(x=350, y=140)

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
        for i in vulnerability_list:
            self.vulnerability_items.append(i[1])

        self.vulnerability_items.extend(new_vul)
        for i in self.vulnerability_items:
            self.listboxVul.insert(END, i)

    # finding concepts
    def split_concepts(self):
        onto = get_ontology(self.myOntoPath[0]).load()
        concepts_lists = list(onto.classes())
        for i in concepts_lists:
            self.concepts_list.append(str(i).split("."))
        return self.concepts_list

    # adding concepts to box
    def set_concepts_combobox(self):

        concepts_list = self.split_concepts()
        for i in concepts_list:
            self.new_concepts_list.append(i[1])
        self.conceptsCombo['values'] = self.new_concepts_list

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

    # update an entry in the GUI based on the selected item from a listbox
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
        search_string = self.search_str.get().lower()
        self.listboxConcepts.delete(0, tk.END)

        if search_string == "":
            self.show_concepts()
        else:
            filtered_data = list()
            for item in concepts_list:
                if item[1].lower().find(search_string) != -1:
                    filtered_data.append(item[1])

            for data in filtered_data:
                self.listboxConcepts.insert(tk.END, data)

    def find_vulnerabilities_from_concept(self):
        self.vul_list = self.show_vulnerabilities_from_concepts()
        self.listboxVul.delete(0, tk.END)
        c = 1
        if self.vul_list:
            for item in self.vul_list:
                self.listFindVulnerabilities.insert(c, item)
                c += 1

    # show_superclass_from_concepts method
    def find_superclass_from_concepts(self):
        onto = get_ontology(self.myOntoPath[0]).load()
        concepts_lists = list(onto.classes())
        concept_name = self.listboxConcepts.get(tk.ACTIVE)
        c_name = concept_name[0] if isinstance(
            concept_name, tuple) else concept_name
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

    def show_remove_concepts(self):
        onto = get_ontology(self.myOntoPath[0]).load()
        vulnerabilities_items = list(onto.hasVulnerability.get_relations())
        concepts_lists = list(onto.classes())
        vulnerability_name = self.RRemoveTxt.get()

        for concept in concepts_lists:
            for vulnerability in vulnerabilities_items:
                if concept == vulnerability[0] and vulnerability[1] == vulnerability_name:
                    sp_concepts = str(concept).split(".")
                    self.conceptsCombo['values'] = sp_concepts[1]

    def get_subclass_of(self):
        onto = get_ontology(self.myOntoPath[0]).load()
        txt_subclass = str(self.txtSubClass.get())
        concept = self.listboxConceptPlus.get(ACTIVE)
        concepts_lists = list(onto.classes())
        c = ''

        for item in concepts_lists:
            sp_concept = str(item).split(".")
            if sp_concept[1] == concept:
                c = item

        with onto:
            new_class = types.new_class(txt_subclass, (c,))

        onto.save(file=self.myOntoPath[0])

    def get_first_concept_obj(self):
        first_concept = ""
        if self.checkVar1.get() == 1:
            first_concept = self.listboxConceptPlus.get(ACTIVE)
            self.txtPartOf1.set(first_concept)
            self.btn1PartOf.config(state="normal")
        else:
            self.txtPartOf1.set("")
            self.btn1PartOf.config(state="disabled")

        return self.txtPartOf1.get()

    def get_second_concept_obj(self):
        second_concept = ""

        if self.checkVar2.get() == 1:
            second_concept = self.listboxConceptPlus.get(ACTIVE)
            self.txtPartOf2.set(second_concept)
            self.btn2PartOf.config(state="normal")
        else:
            self.txtPartOf2.set("")
            self.btn2PartOf.config(state="disabled")

        return second_concept

    def show_concept_have_vul(self):
        onto = get_ontology(self.myOntoPath[0]).load()
        concepts_list = list(onto.hasVulnerability.get_relations())

        for i in concepts_list:
            concepts_items.append(i[0])

        new_concepts_items = []
        for i in concepts_items:
            sp_item = str(i).split(".")
            new_concepts_items.append(sp_item[1])

        del concepts_list
        concepts_items = []
        for i in new_concepts_items:
            if i not in concepts_items:
                concepts_items.append(i)

        del new_concepts_items
        for i in concepts_items:
            self.listBoxHaveVul.insert(END, i)

    def show_concept_not_vul(self):
        onto = get_ontology(self.myOntoPath[0]).load()
        self.vul_list = list(onto.hasVulnerability.get_relations())
        vul_items = [str(i[0]).split(".")[1] for i in self.vul_list]

        con_list = list(onto.classes())
        con_item = [str(i).split(".")[1] for i in con_list]

        all_list = vul_items + con_item
        concepts_items = [i for i in all_list if i not in vul_items]

        for i in concepts_items:
            self.listBoxNotVul.insert(END, i)

    def add_job(self):
        fill_data = False
        selected = self.job_radio.get()

        if selected == 0:
            if self.jobVulCombo.current() != -1:
                selected_concept = self.jobVulCombo.get()
                fill_data = True
            else:
                messagebox.showwarning(
                    'Warning', 'You should select a concept from the combo box')

        if selected == 1:
            text = self.textboxVul.get("1.0", "end-1c").split('\n')[:-1]
            self.vul_list = [i[1] for i in self.vul_list2]

            if not set(text).issubset(self.vul_list):
                messagebox.showwarning(
                    'Warning', 'The selected vulnerability is not in the list')
            elif not text:
                messagebox.showwarning(
                    'Warning', 'You should add at least one vulnerability from the list')
            else:
                selected_concept = text
                fill_data = True

        if fill_data:
            if self.listboxUsers.curselection():
                user = self.listboxUsers.get(ACTIVE)
                start_time = self.TxtFromTime.get()
                end_time = self.TxtToTime.get()
                start_day = self.from_date_entry.get()
                end_day = self.to_date_entry.get()
                current_file_dir = dirname(abspath(__file__))
                new_file_path = join(current_file_dir, "job.txt")

                try:
                    with open('job.txt', 'a', encoding='utf-8') as f:
                        f.write(
                            f"*{user}* should start From : *{start_day}* at *{start_time}* and end in *{end_day}* at *{end_time}* for vulnerabilities : *{selected_concept}* \n\n")
                    messagebox.showinfo('Successful', f'Job added for {user}')
                except Exception as e:
                    messagebox.showwarning(
                        'Unsuccessful', 'Job was not added for the user')
            else:
                messagebox.showwarning(
                    'Warning', 'You should select a user to add a job from the user list box')

    def by_vul(self):
        self.btnAddVulTextBox.config(state=NORMAL)
        self.textboxVul.config(state=NORMAL)

    def by_class(self):
        self.btnAddVulTextBox.config(state=DISABLED)
        self.textboxVul.delete('1.0', END)
        self.textboxVul.config(state=DISABLED)

    def get_vulnerabilities(self):

        onto = get_ontology(self.myOntoPath[0]).load()
        self.vul_list = list(onto.hasVulnerability.get_relations())
        self.vul_list2 = [(i[0].name, i[1]) for i in self.vul_list]
        concepts_items = []
        for i in self.vul_list:
            if i[0].name not in concepts_items:
                concepts_items.append(i[0].name)
        self.jobVulCombo['values'] = concepts_items

    def update_listbox(self, event):
        selected_option = self.jobVulCombo.get()
        self.listboxvuljob.delete(0, tk.END)
        for i in self.vul_list2:
            if i[0] == selected_option:
                self.listboxvuljob.insert(tk.END, i[1])

    def validate_spinbox_input(self, input_value):
        if input_value.isdigit() and int(input_value) <= self.max_value:
            return True
        elif input_value == '':
            return True
        else:
            return False

    def show_advance_data(self):
        onto = get_ontology(self.myOntoPath[0]).load()
        self.show_concept_not_vul()
        self.show_concept_have_vul()
        x = list(default_world.sparql("""
                PREFIX my: <http://www.semanticweb.org/imana/ontologies/2022/10/Network#>
                SELECT ?x
                        WHERE { ?x owl:onProperty my:hasVulnerability.
                        }
                """))
        has_vulnerabilities_length = list(
            onto.hasVulnerability.get_relations()) + x
        self.strResult.set(str(len(has_vulnerabilities_length)))

    def add_user(self):
        onto = get_ontology(self.myOntoPath[0]).load()
        user_name = self.TxtAddUser.get()
        try:
            with onto:
                new_class = types.new_class(user_name, (onto.Users,))
            onto.save(file=self.myOntoPath[0])
            messagebox.showinfo("successful!", "User Added!")
            self.show_user()
        except:
            messagebox.showinfo("Unsuccessful!", "User was not Added!")

    def delete_user(self):
        name = self.TxtDelUser.get()
        onto = get_ontology(self.myOntoPath[0]).load()
        try:
            name_for_delete = onto[name]
            destroy_entity(name_for_delete)
            onto.save(file=self.myOntoPath[0], format="rdfxml")
            self.TxtDelUser.delete(0, END)
            messagebox.showinfo("successful!", "User Deleted!")
        except:
            messagebox.showinfo("Unsuccessful!", "User was not Deleted!")

        self.show_user()

    def get_name_listbox(self):
        name = self.listboxUsers.get(ACTIVE)
        self.TxtDelUser.delete(0, END)
        self.TxtDelUser.insert(0, name)

    def show_user_ability(self):
        onto = get_ontology(self.myOntoPath[0]).load()
        self.listboxAbility.delete(0, END)
        self.listboxAbilityJob.delete(0, END)
        self.TxtDelAbility.delete(0, END)
        selected_item = self.listboxUsers.get(self.listboxUsers.curselection())
        class_name = onto[selected_item]
        user_ability = list(class_name.subclasses())
        for i in user_ability:
            user_name = str(i).split('.')[1]
            self.listboxAbility.insert(0, user_name)
            self.listboxAbilityJob.insert(0, user_name)

    def add_ability(self):
        ability = self.TxtAddAbility.get()
        onto = get_ontology(self.myOntoPath[0]).load()
        user_to_add_ability = self.listboxUsers.get(ACTIVE)
        parent_user_class = onto[user_to_add_ability]
        try:
            with onto:
                new_class = types.new_class(ability, (parent_user_class,))
                messagebox.showinfo(
                    "successful!", f"Ability Added for {user_to_add_ability}!")
                self.TxtAddAbility.delete(0, END)
        except:
            messagebox.showinfo(
                "Unsuccessful!", f"Ability was not Added for {user_to_add_ability}!")
        onto.save(self.myOntoPath[0])
        self.show_user_ability()

    def delete_ability(self):
        ability_name = self.TxtDelAbility.get()
        onto = get_ontology(self.myOntoPath[0]).load()
        try:
            name_for_delete = onto[ability_name]
            destroy_entity(name_for_delete)
            self.TxtDelAbility.delete(0, END)
            onto.save(file=self.myOntoPath[0], format="rdfxml")
            messagebox.showinfo("successful!", "Ability Deleted!")
        except:
            messagebox.showinfo("Unsuccessful!", "Ability was not Deleted!")

        self.show_user_ability()

    def add_vul_to_txtbox(self):
        vul = self.listboxvuljob.get(ACTIVE)
        textbox_text = self.textboxVul.get("1.0", "end-1c").split('\n')
        text = f'{vul}\n'
        if vul not in textbox_text:
            self.textboxVul.insert('end', text)

    def show_user(self):
        self.listboxUsers.delete(0, END)
        onto = get_ontology(self.myOntoPath[0]).load()
        class_name = onto.Users
        users_name = list(class_name.subclasses())
        for i in users_name:
            self.listboxUsers.insert(0, i.name)

    # show vulnerabilities based on concepts
    def show_vulnerabilities_from_concepts(self):
        onto = get_ontology(self.myOntoPath[0]).load()
        self.listFindVulnerabilities.delete(0, END)
        self.vulnerabilities_items = list(
            onto.hasVulnerability.get_relations())
        concepts_lists = list(onto.classes())
        concept_name = self.listboxConcepts.get(ACTIVE)
        c_name = concept_name[0] if isinstance(
            concept_name, tuple) else concept_name
        for concept in concepts_lists:
            for vulnerability in self.vulnerabilities_items:
                sp_vulnerability = str(vulnerability[0]).split(".")
                if vulnerability[0] == concept and sp_vulnerability[1] == c_name:
                    self.concept_vulnerabilities_list.append(vulnerability[1])

        for vul in self.concept_vulnerabilities_list:
            self.listFindVulnerabilities.insert(END, vul)


# main loop
def main():
    root = tk.Tk()
    app = NetworkSecurityOntologyApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
