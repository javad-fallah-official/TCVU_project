from tkinter import StringVar, Listbox
from tkinter import filedialog, messagebox, ttk, Button, Label, LabelFrame, Spinbox, Entry
from tkcalendar import DateEntry
import tkinter as tk
import owlready2
import types


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
        self.txtDelUser = StringVar()
        self.txtAbility = StringVar()
        self.txtAbility = StringVar()
        self.onto_path = StringVar()
        self.txtUser = StringVar()
        self.prefix = StringVar()
        self.onto = StringVar()
        self.myOntoPath = list()
        self.vul_list2 = list()
        self.vul_list = list()
        self.max_value = 24

    # all tabs initialized
    def create_tabs(self):
        tab_control = ttk.Notebook(self.master)
        self.create_view_tab(tab_control)
        self.create_user_tab(tab_control)
        tab_control.pack(expand=1, fill="both")

    def create_view_tab(self, tab_control):
        view_tab = ttk.Frame(tab_control)
        tab_control.add(view_tab, text="Standards")

        # Create a frame to hold the Listboxes, labels, and buttons in one row
        listboxes_frame = ttk.Frame(view_tab, padding=(5, 5, 5, 5))
        listboxes_frame.pack()

        # Create labels for each Listbox
        label1 = Label(listboxes_frame, text="Standards")
        label2 = Label(listboxes_frame, text="Controllers Group")
        label3 = Label(listboxes_frame, text="Controllers")
        label4 = Label(listboxes_frame, text="Sub Controls")
        label5 = Label(listboxes_frame, text="Controllers Group Examples")
        label6 = Label(listboxes_frame, text="Controllers examples")

        # Create six Listboxes in one row
        self.standards_Lbox = Listbox(listboxes_frame, height=15, width=20)
        self.controllers_group_Lbox = Listbox(
            listboxes_frame, height=15, width=20)
        self.controllers_Lbox = Listbox(listboxes_frame, height=15, width=20)
        self.subclass_Lbox = Listbox(listboxes_frame, height=15, width=20)
        listbox5 = Listbox(listboxes_frame, height=15, width=20)
        listbox6 = Listbox(listboxes_frame, height=15, width=20)

        # Place labels and Listboxes in the grid
        label1.grid(row=0, column=0, padx=10, pady=3)
        label2.grid(row=0, column=1, padx=10, pady=3)
        label3.grid(row=0, column=2, padx=10, pady=3)
        label4.grid(row=0, column=3, padx=10, pady=3)
        label5.grid(row=2, column=2, padx=10, pady=3)
        label6.grid(row=2, column=3, padx=10, pady=3)

        self.standards_Lbox.grid(row=1, column=0, padx=10, pady=5)
        self.controllers_group_Lbox.grid(row=1, column=1, padx=10, pady=5)
        self.controllers_Lbox.grid(row=1, column=2, padx=10, pady=5)
        self.subclass_Lbox.grid(row=1, column=3, padx=10, pady=5)
        listbox5.grid(row=3, column=2, padx=10, pady=5)
        listbox6.grid(row=3, column=3, padx=10, pady=5)

        # Create buttons and associate them with callback functions
        button1 = Button(listboxes_frame, text="show controllers Group",
                         command=lambda: self.show_controllers_group())
        button2 = Button(listboxes_frame, text="show controllers",
                         command=lambda: self.show_controllers())
        button3 = Button(listboxes_frame, text="show subclass",
                         command=lambda: self.show_subclass())
        button4 = Button(listboxes_frame, text="Get Selected",
                         command=lambda: self.show_subclass())
        button5 = Button(listboxes_frame, text="Get Selected",
                         command=lambda: self.show_subclass())
        button6 = Button(listboxes_frame, text="Get Selected",
                         command=lambda: self.show_subclass())

        # Place buttons in the grid
        button1.grid(row=2, column=0, padx=10, pady=5)
        button2.grid(row=2, column=1, padx=10, pady=5)
        button3.grid(row=2, column=2, padx=10, pady=5)
        button4.grid(row=2, column=3, padx=10, pady=5)
        button5.grid(row=4, column=2, padx=10, pady=5)
        button6.grid(row=4, column=3, padx=10, pady=5)

        # open file button
        lblBrowse = Label(view_tab, text="select file : ", anchor="e")
        lblBrowse.place(x=10, y=50)
        btnBrowse = Button(view_tab, text="file", command=self.load_file)
        btnBrowse.pack()
        btnBrowse.place(x=70, y=50)

        # Prefix input
        lblBrowse2 = Label(view_tab, text="Prefix : ", anchor="e")
        lblBrowse2.place(x=10, y=20)
        self.prefixBox = Entry(view_tab, textvariable=self.prefix, width=90)
        # default value
        self.prefixBox.insert(0, "http://www.semantic.org/hamidzadeh/SOSM")
        self.prefixBox.place(x=70, y=20)

    def show_controllers_group(self):
        selected_item = self.standards_Lbox.get(
            self.standards_Lbox.curselection())
        contollresgroup = self.extract_Subclasses(selected_item)
        self.controllers_group_Lbox.delete(0, 'end')
        for item in contollresgroup:
            self.controllers_group_Lbox.insert("end", item.name)

    def show_controllers(self):
        selected_item = self.controllers_group_Lbox.get(
            self.controllers_group_Lbox.curselection())
        contollres = self.extract_Subclasses(selected_item)
        self.controllers_Lbox.delete(0, 'end')
        for item in contollres:
            self.controllers_Lbox.insert("end", item.name)

    def show_subclass(self):
        selected_item = self.controllers_Lbox.get(
            self.controllers_Lbox.curselection())
        contollres = self.extract_Subclasses(selected_item)
        self.subclass_Lbox.delete(0, 'end')
        for item in contollres:
            self.subclass_Lbox.insert("end", item.name)

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
        AddUsersGroupBox = LabelFrame(Users, text="Add new User")
        AddUsersGroupBox.place(x=10, y=10, width=470, height=230)

        # make group box for delete Users in User
        DelUsersGroupBox = LabelFrame(Users, text="Delete User")
        DelUsersGroupBox.place(x=10, y=250, width=470, height=180)

        # label for user list box
        usr_lb_label = Label(user_tab, text='User list :')
        usr_lb_label.place(x=520, y=46, height=10)

        # list box for User
        self.listboxUsers = Listbox(user_tab)
        self.listboxUsers.place(x=520, y=60, height=230, width=250)

        # text Delete user
        Lbl1DelUser = Label(
            DelUsersGroupBox, text="Delete User: ", anchor="e")
        Lbl1DelUser.place(x=10, y=50)

        # entry Delete user
        self.TxtDelUser = Entry(
            DelUsersGroupBox, textvariable=self.txtDelUser)
        self.TxtDelUser.place(x=80, y=50, width=270)

        # btn for add name from listbox to delete entry
        btnGetNameFromLbox = Button(
            DelUsersGroupBox, text="<<<", command=self.get_name_listbox)
        btnGetNameFromLbox.pack()
        btnGetNameFromLbox.place(x=370, y=50, width=50)

        # btn Delete user
        btnDelUsers = Button(
            DelUsersGroupBox, text="Delete", command=self.delete_user)
        btnDelUsers.pack()
        btnDelUsers.place(x=350, y=120)

        # text add user
        Lbl1AddUser = Label(
            AddUsersGroupBox, text="Add User: ", anchor="e")
        Lbl1AddUser.place(x=10, y=50)

        # entry add user
        self.TxtAddUser = Entry(AddUsersGroupBox, textvariable=self.txtUser)
        self.TxtAddUser.place(x=70, y=50, width=270)

        # btn add user
        btnAddUsers = Button(
            AddUsersGroupBox, text="Add", command=self.add_user)
        btnAddUsers.pack()
        btnAddUsers.place(x=350, y=160)

        # make group box for tab Ability in User
        AbilityGroupBox = LabelFrame(Ability, text="Add new Ability")
        AbilityGroupBox.place(x=10, y=10, width=470, height=230)

        # txt in ability
        Lbl1AddAbility = Label(AbilityGroupBox, text="Add : ", anchor="e")
        Lbl1AddAbility.place(x=10, y=50)

        Lbl2AddAbility = Label(
            AbilityGroupBox, text="to be Ability of", anchor="e")
        Lbl2AddAbility.place(x=330, y=50)

        # entry to add ability
        self.TxtAddAbility = Entry(
            AbilityGroupBox, textvariable=self.txtAbility)
        self.TxtAddAbility.place(x=50, y=50, width=270)

        # btn to add ability in ability tab
        btnAddAbility = Button(
            AbilityGroupBox, text="Add", command=self.add_ability)
        btnAddAbility.pack()
        btnAddAbility.place(x=350, y=160)

        # ability delete group box
        AbilityDelGroupBox = LabelFrame(Ability, text='Delete Ability')
        AbilityDelGroupBox.place(x=10, y=260, width=470, height=232)

        # txt for delete ability Gbox
        Lbl1DelAbility = Label(
            AbilityDelGroupBox, text="Delete Ability Of : ", anchor="e")
        Lbl1DelAbility.place(x=5, y=50)

        Lbl4DelAbility = Label(AbilityDelGroupBox, text="Select the Ability "
                               "from the right side list", anchor="e")
        Lbl4DelAbility.place(x=0, y=110)

        # Entry to delete ability
        self.TxtDelAbility = Entry(
            AbilityDelGroupBox, textvariable=self.txtAbility)
        self.TxtDelAbility.place(x=105, y=50, width=215)

        # btn del ability
        btnDelAbility = Button(
            AbilityDelGroupBox, text="Delete", command=self.delete_ability)
        btnDelAbility.pack()
        btnDelAbility.place(x=350, y=150)

        # btn for show user ability
        btnShowUserAbl = Button(
            Ability, text='Show Selected User Ability', command=self.show_user_ability)
        btnShowUserAbl.pack()
        btnShowUserAbl.place(x=520, y=260, height=30, width=250)

        # list box2 for Ability
        self.listboxAbility = Listbox(Ability)
        self.listboxAbility.place(x=520, y=312, height=180, width=250)
        self.listboxAbility.bind("<<ListboxSelect>>", self.update_entry)

        # label for list box user ability
        lbl_user_ability = Label(Ability, text='User Ability :')
        lbl_user_ability.place(x=520, y=290)

        # job Tab vulnerabilities group box
        jobVulGroupBox = LabelFrame(job, text='Select vulnerabilities')
        jobVulGroupBox.place(x=10, y=20, width=470, height=300)

        # btn to add vulnerabilities to text box
        self.btnAddVulTextBox = Button(
            jobVulGroupBox, text="Add", command=self.add_vul_to_txtbox, state=tk.DISABLED)
        self.btnAddVulTextBox.place(x=230, y=160, width=225)

        # txt in job Vulnerabilities group box
        lbl1AddJob = Label(
            jobVulGroupBox, text="Vulnerabilities:", anchor="e")
        lbl1AddJob.place(x=230, y=10)

        lbl2AddJob = Label(jobVulGroupBox, text="concepts:", anchor="e")
        lbl2AddJob.place(x=10, y=70)

        # list box for Vulnerabilities in job tab
        self.listboxvuljob = Listbox(jobVulGroupBox)
        self.listboxvuljob.place(x=230, y=30, height=120, width=225)

        # btn to show user ability job tab
        btnShowUserAblJob = Button(
            job, text='Show Selected User Ability', command=self.show_user_ability)
        btnShowUserAblJob.pack()
        btnShowUserAblJob.place(x=520, y=260, height=30, width=250)

        # list box for user ability in job tab
        self.listboxAbilityJob = Listbox(job)
        self.listboxAbilityJob.place(x=520, y=312, height=180, width=250)

        # label for list box user ability in job tab
        lbl_user_ability = Label(job, text='User Ability :')
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
        jobTimeGroupBox = LabelFrame(job, text="Add new")
        jobTimeGroupBox.place(x=10, y=330, width=470, height=200)

        # txt in time group box in job tab
        lbl1Time = Label(
            jobTimeGroupBox, text="From       Time", anchor="e")
        lbl1Time.place(x=10, y=20)

        lbl2AddJob = Label(jobTimeGroupBox, text="Date:", anchor="e")
        lbl2AddJob.place(x=180, y=20)

        lbl2Time = Label(
            jobTimeGroupBox, text="To             Time", anchor="e")
        lbl2Time.place(x=10, y=80)

        lbl2AddJob = Label(jobTimeGroupBox, text="Date:", anchor="e")
        lbl2AddJob.place(x=180, y=80)

        # spin boxes in job tab

        self.TxtFromTime = Spinbox(jobTimeGroupBox, from_=1, to=self.max_value, validate="key",
                                   validatecommand=(self.master.register(self.validate_spinbox_input), '%P'))
        self.TxtToTime = Spinbox(jobTimeGroupBox, from_=1, to=self.max_value, validate="key",
                                 validatecommand=(self.master.register(self.validate_spinbox_input), '%P'))

        self.from_date_entry = DateEntry(jobTimeGroupBox, width=12, background='darkblue',
                                         foreground='white', borderwidth=2, date_pattern='dd/MM/y', state='readonly')
        self.from_date_entry.place(x=220, y=20)

        self.to_date_entry = DateEntry(jobTimeGroupBox, width=12, background='darkblue',
                                       foreground='white', borderwidth=2, date_pattern='dd/MM/y', state='readonly')
        self.to_date_entry.place(x=220, y=80)

        btn_save_job = Button(
            jobTimeGroupBox, text="Save", command=self.add_job)
        btn_save_job.place(x=350, y=140)

    # loading file and datas
    def load_file(self):
        # choosing file
        self.onto_path = self.file_open_box()
        # loading owl
        self.onto = owlready2.get_ontology(self.onto_path).load()
        # set prefix
        self.prefix = self.prefix.get()

        self.extract_standards()
        # self.show_data_main()
        # self.set_vulnerabilities_item()
        # self.set_concepts_combobox()
        # self.show_concepts()

    # file select window
    def file_open_box(self):
        root = tk.Tk()
        root.withdraw()  # Hide the main window

        file_path = filedialog.askopenfilename(
            filetypes=[("OWL Files", "*.owl")], title="Select an OWL File"
        )
        return file_path

    # update an entry in the GUI based on the selected item from a listbox
    def update_entry(self):
        try:
            selected_item = self.listboxAbility.get(
                self.listboxAbility.curselection())
            self.TxtDelAbility.delete(0, tk.END)
            self.TxtDelAbility.insert(0, selected_item)
        except:
            pass

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

    def extract_standards(self):
       # Get the namespace from the base IRI
        namespace = self.onto.get_namespace(
            self.prefix)

        # Get the class from the namespace
        class_name = getattr(
            namespace, 'Ontology_of_standards', None)
        if class_name is not None:
            subclasses = list(class_name.subclasses())
            for subclass in subclasses:
                self.standards_Lbox.insert("end", subclass.name)

    def extract_Subclasses(self, parent):
       # Get the namespace from the base IRI
        namespace = self.onto.get_namespace(
            self.prefix)
        # Get the class from the namespace
        class_name = getattr(namespace, parent, None)

        subclasses = list(class_name.subclasses())
        return subclasses


def main():
    root = tk.Tk()
    NetworkSecurityOntologyApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
