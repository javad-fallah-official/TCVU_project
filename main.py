from tkinter import StringVar, Listbox, IntVar
from tkinter import filedialog, messagebox, ttk
from tkcalendar import DateEntry
import tkinter as tk
import owlready2
import types


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
        self.txtDelUser = StringVar()
        self.txtAbility = StringVar()
        self.txtAbility = StringVar()
        self.txtUser = StringVar()
        self.listboxVul = Listbox()
        self.myOntoPath = list()
        self.vul_list = list()
        self.vul_list2 = list()
        self.listboxUsers = Listbox()
        self.concepts_list = list()
        self.new_concepts_list = list()
        self.vulnerability_items = list()
        self.concepts_items = list()
        self.max_value = 24

    # all tabs initialized
    def create_tabs(self):
        tab_control = ttk.Notebook(self.master)
        self.create_main_tab(tab_control)
        self.create_standards_tab(tab_control)
        self.create_user_tab(tab_control)
        tab_control.pack(expand=1, fill="both")

    # main tab initialized
    def create_main_tab(self, tab_control):
        main_tab = ttk.Frame(tab_control)
        tab_control.add(main_tab, text="Main")

        # tk.Labels for showing data in main tab menu
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

    def create_standards_tab(self, tab_control):
        standards_tab = ttk.Frame(tab_control)
        tab_control.add(standards_tab, text="Standards")

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

        # make group box for add Users in User
        AddUsersGroupBox = tk.LabelFrame(Users, text="Add new User")
        AddUsersGroupBox.place(x=10, y=10, width=470, height=230)

        # make group box for delete Users in User
        DelUsersGroupBox = tk.LabelFrame(Users, text="Delete User")
        DelUsersGroupBox.place(x=10, y=250, width=470, height=180)

        # label for user list box
        usr_lb_label = tk.Label(user_tab, text='User list :')
        usr_lb_label.place(x=520, y=46, height=10)

        # list box for User
        self.listboxUsers = Listbox(user_tab)
        self.listboxUsers.place(x=520, y=60, height=230, width=250)

        # text Delete user
        Lbl1DelUser = ttk.Label(
            DelUsersGroupBox, text="Delete User: ", anchor="e")
        Lbl1DelUser.place(x=10, y=50)

        # entry Delete user
        self.TxtDelUser = tk.Entry(
            DelUsersGroupBox, textvariable=self.txtDelUser)
        self.TxtDelUser.place(x=80, y=50, width=270)

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
        self.TxtAddUser = tk.Entry(AddUsersGroupBox, textvariable=self.txtUser)
        self.TxtAddUser.place(x=70, y=50, width=270)

        # btn add user
        btnAddUsers = ttk.Button(
            AddUsersGroupBox, text="Add", command=self.add_user)
        btnAddUsers.pack()
        btnAddUsers.place(x=350, y=160)

        # make group box for tab Ability in User
        AbilityGroupBox = tk.LabelFrame(Ability, text="Add new Ability")
        AbilityGroupBox.place(x=10, y=10, width=470, height=230)

        # txt in ability
        Lbl1AddAbility = ttk.Label(AbilityGroupBox, text="Add : ", anchor="e")
        Lbl1AddAbility.place(x=10, y=50)

        Lbl2AddAbility = ttk.Label(
            AbilityGroupBox, text="to be Ability of", anchor="e")
        Lbl2AddAbility.place(x=330, y=50)

        # entry to add ability
        self.TxtAddAbility = tk.Entry(
            AbilityGroupBox, textvariable=self.txtAbility)
        self.TxtAddAbility.place(x=50, y=50, width=270)

        # btn to add ability in ability tab
        btnAddAbility = ttk.Button(
            AbilityGroupBox, text="Add", command=self.add_ability)
        btnAddAbility.pack()
        btnAddAbility.place(x=350, y=160)

        # ability delete group box
        AbilityDelGroupBox = tk.LabelFrame(Ability, text='Delete Ability')
        AbilityDelGroupBox.place(x=10, y=260, width=470, height=232)

        # txt for delete ability Gbox
        Lbl1DelAbility = ttk.Label(
            AbilityDelGroupBox, text="Delete Ability Of : ", anchor="e")
        Lbl1DelAbility.place(x=5, y=50)

        Lbl4DelAbility = ttk.Label(AbilityDelGroupBox, text="Select the Ability "
                                   "from the right side list", anchor="e")
        Lbl4DelAbility.place(x=0, y=110)

        # tk.Entry to delete ability
        self.TxtDelAbility = tk.Entry(
            AbilityDelGroupBox, textvariable=self.txtAbility)
        self.TxtDelAbility.place(x=105, y=50, width=215)

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
        self.listboxAbility = Listbox(Ability)
        self.listboxAbility.place(x=520, y=312, height=180, width=250)
        self.listboxAbility.bind("<<ListboxSelect>>", self.update_entry)

        # label for list box user ability
        lbl_user_ability = tk.Label(Ability, text='User Ability :')
        lbl_user_ability.place(x=520, y=290)

        # job Tab vulnerabilities group box
        jobVulGroupBox = tk.LabelFrame(job, text='Select vulnerabilities')
        jobVulGroupBox.place(x=10, y=20, width=470, height=300)

        # btn to add vulnerabilities to text box
        self.btnAddVulTextBox = ttk.Button(
            jobVulGroupBox, text="Add", command=self.add_vul_to_txtbox, state=tk.DISABLED)
        self.btnAddVulTextBox.place(x=230, y=160, width=225)

        # txt in job Vulnerabilities group box
        lbl1AddJob = ttk.Label(
            jobVulGroupBox, text="Vulnerabilities:", anchor="e")
        lbl1AddJob.place(x=230, y=10)

        lbl2AddJob = ttk.Label(jobVulGroupBox, text="concepts:", anchor="e")
        lbl2AddJob.place(x=10, y=70)

        # list box for Vulnerabilities in job tab
        self.listboxvuljob = Listbox(jobVulGroupBox)
        self.listboxvuljob.place(x=230, y=30, height=120, width=225)

        # btn to show user ability job tab
        btnShowUserAblJob = ttk.Button(
            job, text='Show Selected User Ability', command=self.show_user_ability)
        btnShowUserAblJob.pack()
        btnShowUserAblJob.place(x=520, y=260, height=30, width=250)

        # list box for user ability in job tab
        self.listboxAbilityJob = Listbox(job)
        self.listboxAbilityJob.place(x=520, y=312, height=180, width=250)

        # label for list box user ability in job tab
        lbl_user_ability = tk.Label(job, text='User Ability :')
        lbl_user_ability.place(x=520, y=290)

        # text box to add vulnerabilities job
        self.textboxVul = tk.Text(jobVulGroupBox, state=tk.DISABLED)
        self.textboxVul.place(x=230, y=195, height=80, width=225)

        # radio buttons in job tab
        self.job_radio = tk.IntVar()
        class_radio = tk.Radiobutton(jobVulGroupBox, text="Base on class",
                                     value=0, variable=self.job_radio, command=self.by_class)
        class_radio.place(x=10, y=10)

        vul_radio2 = tk.Radiobutton(jobVulGroupBox, text="Base on vulnerabilities",
                                    value=1, variable=self.job_radio, command=self.by_vul)
        vul_radio2.place(x=10, y=30)

        # vulnerabilities combo box in job tab
        self.jobVulCombo = ttk.Combobox(jobVulGroupBox, state='readonly')
        self.jobVulCombo.place(x=10, y=90, width=180)
        self.jobVulCombo.bind("<<ComboboxSelected>>", self.update_listbox)

        # make group box for tab Job in User
        jobTimeGroupBox = tk.LabelFrame(job, text="Add new")
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

        self.TxtFromTime = tk.Spinbox(jobTimeGroupBox, from_=1, to=self.max_value, validate="key",
                                      validatecommand=(self.master.register(self.validate_spinbox_input), '%P'))
        self.TxtToTime = tk.Spinbox(jobTimeGroupBox, from_=1, to=self.max_value, validate="key",
                                    validatecommand=(self.master.register(self.validate_spinbox_input), '%P'))

        self.from_date_entry = DateEntry(jobTimeGroupBox, width=12, background='darkblue',
                                         foreground='white', borderwidth=2, date_pattern='dd/MM/y', state='readonly')
        self.from_date_entry.place(x=220, y=20)

        self.to_date_entry = DateEntry(jobTimeGroupBox, width=12, background='darkblue',
                                       foreground='white', borderwidth=2, date_pattern='dd/MM/y', state='readonly')
        self.to_date_entry.place(x=220, y=80)

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
        onto = owlready2.owlready2.get_ontology(self.myOntoPath[0]).load()
        subclass_length = list(owlready2.owlready2.default_world.sparql("""
            SELECT ?x ?y
            WHERE { ?x rdfs:subClassOf ?y.
            ?x rdf:type owl:Class.
            }
        """))
        y = list(owlready2.default_world.sparql("""
            PREFIX my: <http://www.semanticweb.org/imana/ontologies/2022/10/Network#>
            SELECT ?x
            WHERE {?x owl:onProperty my:isPartOf.
            }
        """))
        x = list(owlready2.default_world.sparql("""
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
        onto = owlready2.owlready2.get_ontology(self.myOntoPath[0]).load()
        x = list(owlready2.owlready2.default_world.sparql("""
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
            self.listboxVul.insert(tk.END, i)

    # finding concepts
    def split_concepts(self):
        onto = owlready2.owlready2.get_ontology(self.myOntoPath[0]).load()
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

    # update an entry in the GUI based on the selected item from a listbox
    def update_entry(self):
        try:
            selected_item = self.listboxAbility.get(
                self.listboxAbility.curselection())
            self.TxtDelAbility.delete(0, tk.END)
            self.TxtDelAbility.insert(0, selected_item)
        except:
            pass

    # show_concepts method
    def show_concepts(self):
        concepts_list = self.split_concepts()
        c = 1
        for i in concepts_list:
            self.listboxConcepts.insert(c, i[1])
            self.listboxConceptPlus.insert(c, i[1])
            c += 1

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
                user = self.listboxUsers.get(tk.ACTIVE)
                start_time = self.TxtFromTime.get()
                end_time = self.TxtToTime.get()
                start_day = self.from_date_entry.get()
                end_day = self.to_date_entry.get()

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
        self.btnAddVulTextBox.config(state=tk.NORMAL)
        self.textboxVul.config(state=tk.NORMAL)

    def by_class(self):
        self.btnAddVultk.TextBox.config(state=tk.DISABLED)
        self.textboxVul.delete('1.0', tk.END)
        self.textboxVul.config(state=tk.DISABLED)

    def get_vulnerabilities(self):

        onto = owlready2.get_ontology(self.myOntoPath[0]).load()
        self.vul_list = list(onto.hasVulnerability.get_relations())
        self.vul_list2 = [(i[0].name, i[1]) for i in self.vul_list]
        concepts_items = []
        for i in self.vul_list:
            if i[0].name not in concepts_items:
                concepts_items.append(i[0].name)
        self.jobVulCombo['values'] = concepts_items

    def update_listbox(self):
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

    def add_user(self):
        onto = owlready2.get_ontology(self.myOntoPath[0]).load()
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
        onto = owlready2.get_ontology(self.myOntoPath[0]).load()
        try:
            name_for_delete = onto[name]
            owlready2.destroy_entity(name_for_delete)
            onto.save(file=self.myOntoPath[0], format="rdfxml")
            self.TxtDelUser.delete(0, tk.END)
            messagebox.showinfo("successful!", "User Deleted!")
        except:
            messagebox.showinfo("Unsuccessful!", "User was not Deleted!")

        self.show_user()

    def get_name_listbox(self):
        name = self.listboxUsers.get(tk.ACTIVE)
        self.TxtDelUser.delete(0, tk.END)
        self.TxtDelUser.insert(0, name)

    def show_user_ability(self):
        onto = owlready2.get_ontology(self.myOntoPath[0]).load()
        self.listboxAbility.delete(0, tk.END)
        self.listboxAbilityJob.delete(0, tk.END)
        self.TxtDelAbility.delete(0, tk.END)
        selected_item = self.listboxUsers.get(self.listboxUsers.curselection())
        class_name = onto[selected_item]
        user_ability = list(class_name.subclasses())
        for i in user_ability:
            user_name = str(i).split('.')[1]
            self.listboxAbility.insert(0, user_name)
            self.listboxAbilityJob.insert(0, user_name)

    def add_ability(self):
        ability = self.TxtAddAbility.get()
        onto = owlready2.get_ontology(self.myOntoPath[0]).load()
        user_to_add_ability = self.listboxUsers.get(tk.ACTIVE)
        parent_user_class = onto[user_to_add_ability]
        try:
            with onto:
                new_class = types.new_class(ability, (parent_user_class,))
                messagebox.showinfo(
                    "successful!", f"Ability Added for {user_to_add_ability}!")
                self.TxtAddAbility.delete(0, tk.END)
        except:
            messagebox.showinfo(
                "Unsuccessful!", f"Ability was not Added for {user_to_add_ability}!")
        onto.save(self.myOntoPath[0])
        self.show_user_ability()

    def delete_ability(self):
        ability_name = self.TxtDelAbility.get()
        onto = owlready2.get_ontology(self.myOntoPath[0]).load()
        try:
            name_for_delete = onto[ability_name]
            owlready2.destroy_entity(name_for_delete)
            self.TxtDelAbility.delete(0, tk.END)
            onto.save(file=self.myOntoPath[0], format="rdfxml")
            messagebox.showinfo("successful!", "Ability Deleted!")
        except:
            messagebox.showinfo("Unsuccessful!", "Ability was not Deleted!")

        self.show_user_ability()

    def add_vul_to_txtbox(self):
        vul = self.listboxvuljob.get(tk.ACTIVE)
        textbox_text = self.textboxVul.get("1.0", "end-1c").split('\n')
        text = f'{vul}\n'
        if vul not in textbox_text:
            self.textboxVul.insert('end', text)

    def show_user(self):
        self.listboxUsers.delete(0, tk.END)
        onto = owlready2.get_ontology(self.myOntoPath[0]).load()
        class_name = onto.Users
        users_name = list(class_name.subclasses())
        for i in users_name:
            self.listboxUsers.insert(0, i.name)


def main():
    root = tk.Tk()
    NetworkSecurityOntologyApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
