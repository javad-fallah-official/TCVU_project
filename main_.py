from funcs import *
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from owlready2 import *
from os.path import dirname, abspath, join
from tkcalendar import DateEntry


# concept++
conceptsPlusTabBar = ttk.Notebook(conceptsPlusTab)
subClass = ttk.Frame(conceptsPlusTabBar)
partOf = ttk.Frame(conceptsPlusTabBar)
# make tab bar in concepts++
conceptsPlusTabBar.add(subClass, text="Sub class")
conceptsPlusTabBar.add(partOf, text="Part of")
conceptsPlusTabBar.pack()
conceptsPlusTabBar.place(x=0, y=70, width=500, height=450)
# list box for concepts++
listboxConceptPlus = Listbox(conceptsPlusTab)
listboxConceptPlus.place(x=520, y=10, height=560, width=265)
# make group box for tab subClass in concepts++
SubClassGroupBox = LabelFrame(
    subClass, text="Add new concepts to be sub class of existing concepts")
SubClassGroupBox.place(x=10, y=40, width=470, height=230)
Lbl1AddSubClass = ttk.Label(SubClassGroupBox, text="Add : ", anchor="e")
Lbl1AddSubClass.place(x=10, y=50)
TxtAddSubClass = Entry(SubClassGroupBox, textvariable=txtSubClass)
TxtAddSubClass.place(x=50, y=50, width=270)
Lbl2AddSubClass = ttk.Label(
    SubClassGroupBox, text="to be sub class of", anchor="e")
Lbl2AddSubClass.place(x=330, y=50)
Lbl3AddSubClass = ttk.Label(SubClassGroupBox, text='Write a proper name for the new concept.just user alphaNumeric '
                                                   'Character and "-" "_"', anchor="e")
Lbl3AddSubClass.place(x=0, y=100)
Lbl4AddSubClass = ttk.Label(SubClassGroupBox, text="Select the SuperClass for your new Concept"
                                                   "from the right side list", anchor="e")
Lbl4AddSubClass.place(x=0, y=140)
# btn add for subclass
SubClassAddGroupBox = LabelFrame(subClass)
SubClassAddGroupBox.place(x=10, y=290, width=470, height=100)
btnSubClass = ttk.Button(
    SubClassAddGroupBox, text="Add", command=set_subclass_of)
btnSubClass.pack()
btnSubClass.place(x=350, y=40)
# make group box for tab partOf in concepts++
partOfGroupBox = LabelFrame(partOf, text="Add new")
partOfGroupBox.place(x=10, y=40, width=470, height=230)
# first add partOf

Txt1AddPartOf = Entry(partOfGroupBox, textvariable=txtPartOf1)
Txt1AddPartOf.place(x=10, y=50, width=270)
btn1PartOf = ttk.Button(partOfGroupBox, text="<<<",
                        state="disabled", command=set_first_concept_obj)
btn1PartOf.pack()
btn1PartOf.place(x=285, y=47, width=50)
checkVar1 = tk.IntVar()
checkVar2 = tk.IntVar()
checkBox1PartOf = Checkbutton(partOfGroupBox, variable=checkVar1,
                              onvalue=1, offvalue=0, command=get_first_concept_obj)
checkBox1PartOf.pack()
checkBox1PartOf.place(x=335, y=47)
lbl1PartOf = ttk.Label(partOfGroupBox, text="Get from concept", anchor="e")
lbl1PartOf.place(x=355, y=50)
# second add partOf

Txt2AddPartOf = Entry(partOfGroupBox, textvariable=txtPartOf2)
Txt2AddPartOf.place(x=10, y=120, width=270)
btn2PartOf = ttk.Button(partOfGroupBox, text="<<<",
                        state="disabled", command=set_second_concept_obj)
btn2PartOf.pack()
btn2PartOf.place(x=285, y=117, width=50)
checkBox2PartOf = Checkbutton(partOfGroupBox, variable=checkVar2,
                              onvalue=1, offvalue=0, command=get_second_concept_obj)
checkBox2PartOf.pack()
checkBox2PartOf.place(x=335, y=120)
lbl2PartOf = ttk.Label(partOfGroupBox, text="Get from concept", anchor="e")
lbl2PartOf.place(x=355, y=120)
# btn add for PartOf
jobVulGroupBox = LabelFrame(partOf)
jobVulGroupBox.place(x=10, y=290, width=470, height=100)
btnPartOf = ttk.Button(jobVulGroupBox, text="Add", command=is_part_of)
btnPartOf.pack()
btnPartOf.place(x=350, y=40)


# User tab
UserTabBar = ttk.Notebook(UserTab)
Users = ttk.Frame(UserTab)
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
Lbl1DelUser = ttk.Label(DelUsersGroupBox, text="Delete User: ", anchor="e")
Lbl1DelUser.place(x=10, y=50)
# entry Delete user

TxtDelUser = Entry(DelUsersGroupBox, textvariable=txtDelUser)
TxtDelUser.place(x=80, y=50, width=270)
# btn for add name from listbox to delete entery
btnGetNameFromLbox = ttk.Button(
    DelUsersGroupBox, text="<<<", command=get_name_listbox)
btnGetNameFromLbox.pack()
btnGetNameFromLbox.place(x=370, y=50, width=50)
# btn Delete user
btnDelUsers = ttk.Button(DelUsersGroupBox, text="Delete", command=delete_user)
btnDelUsers.pack()
btnDelUsers.place(x=350, y=120)
# text add user
Lbl1AddUser = ttk.Label(AddUsersGroupBox, text="Add User: ", anchor="e")
Lbl1AddUser.place(x=10, y=50)
# entry add user

TxtAddUser = Entry(AddUsersGroupBox, textvariable=txtUser)
TxtAddUser.place(x=70, y=50, width=270)
# btn add user
btnAddUsers = ttk.Button(AddUsersGroupBox, text="Add", command=add_user)
btnAddUsers.pack()
btnAddUsers.place(x=350, y=160)
# make group box for tab Ability in User
AbilityGroupBox = LabelFrame(Ability, text="Add new Ability")
AbilityGroupBox.place(x=10, y=10, width=470, height=230)
# list box for User
listboxUsers = Listbox(UserTab)
listboxUsers.place(x=520, y=60, height=230, width=250)
# label for user list box
usr_lb_label = Label(UserTab, text='User list :')
usr_lb_label.place(x=520, y=46, height=10)
# txt in ability
Lbl1AddAbility = ttk.Label(AbilityGroupBox, text="Add : ", anchor="e")
Lbl1AddAbility.place(x=10, y=50)
Lbl2AddAbility = ttk.Label(
    AbilityGroupBox, text="to be Ability of", anchor="e")
Lbl2AddAbility.place(x=330, y=50)
# entery to add ability

TxtAddAbility = Entry(AbilityGroupBox, textvariable=txtAbility)
TxtAddAbility.place(x=50, y=50, width=270)
# bt to add ability in ability tab
btnAddAbility = ttk.Button(AbilityGroupBox, text="Add", command=add_ability)
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
# Entery to delete ability

TxtDelAbility = Entry(AbilityDelGroupBox, textvariable=txtAbility)
TxtDelAbility.place(x=105, y=50, width=215)
# btn del ability
btnDelAbility = ttk.Button(
    AbilityDelGroupBox, text="Delete", command=delete_ability)
btnDelAbility.pack()
btnDelAbility.place(x=350, y=150)
# btn for show user ability
btnShowUserAbl = ttk.Button(
    Ability, text='Show Selected User Ability', command=show_user_ability)
btnShowUserAbl.pack()
btnShowUserAbl.place(x=520, y=260, height=30, width=250)
# list box2 for Ability
listboxAbility = Listbox(Ability)
listboxAbility.place(x=520, y=312, height=180, width=250)
listboxAbility.bind("<<ListboxSelect>>", update_entry)
# label for list box user ability
lbl_user_ability = Label(Ability, text='User Ability :')
lbl_user_ability.place(x=520, y=290)
# job Tab vulnerabilities group box
jobVulGroupBox = LabelFrame(job, text='Select vulnerabilities')
jobVulGroupBox.place(x=10, y=20, width=470, height=300)
# btn to add vulnerabilities to text box
btnAddVulTextBox = ttk.Button(
    jobVulGroupBox, text="Add", command=add_vul_to_txtbox, state=DISABLED)
btnAddVulTextBox.place(x=230, y=160, width=225)
# txt in job Vulnerabilities group box
lbl1AddJob = ttk.Label(jobVulGroupBox, text="Vulnerabilities:", anchor="e")
lbl1AddJob.place(x=230, y=10)
lbl2AddJob = ttk.Label(jobVulGroupBox, text="concepts:", anchor="e")
lbl2AddJob.place(x=10, y=70)
# list box for Vulnerabilities in job tab
listboxvuljob = Listbox(jobVulGroupBox)
listboxvuljob.place(x=230, y=30, height=120, width=225)
# btn to show user ability job tab
btnShowUserAblJob = ttk.Button(
    job, text='Show Selected User Ability', command=show_user_ability)
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
                          value=0, variable=job_radio, command=by_class)
class_radio.place(x=10, y=10)
vul_radio2 = Radiobutton(jobVulGroupBox, text="Base on vulnerabilities",
                         value=1, variable=job_radio, command=by_vul)
vul_radio2.place(x=10, y=30)
# vulnerabilities combo box in job tab
jobVulCombo = ttk.Combobox(jobVulGroupBox, state='readonly')
jobVulCombo.place(x=10, y=90, width=180)
jobVulCombo.bind("<<ComboboxSelected>>", update_listbox)
# make group box for tab Job in User
jobTimeGroupBox = LabelFrame(job, text="Add new")
jobTimeGroupBox.place(x=10, y=330, width=470, height=200)
# txt in time group box in job tab
lbl1Time = ttk.Label(jobTimeGroupBox, text="From       Time", anchor="e")
lbl1Time.place(x=10, y=20)
lbl2AddJob = ttk.Label(jobTimeGroupBox, text="Date:", anchor="e")
lbl2AddJob.place(x=180, y=20)
lbl2Time = ttk.Label(jobTimeGroupBox, text="To             Time", anchor="e")
lbl2Time.place(x=10, y=80)
lbl2AddJob = ttk.Label(jobTimeGroupBox, text="Date:", anchor="e")
lbl2AddJob.place(x=180, y=80)
# max value for time spinbox in job tab
max_value = 24
# spin boxes in job tab
TxtFromTime = Spinbox(jobTimeGroupBox, from_=1, to=max_value, validate="key",
                      validatecommand=(root.register(validate_spinbox_input), '%P'))
TxtFromTime.place(x=100, y=20, width=40)
TxtToTime = Spinbox(jobTimeGroupBox, from_=1, to=max_value, validate="key",
                    validatecommand=(root.register(validate_spinbox_input), '%P'))
TxtToTime.place(x=100, y=80, width=40)
from_date_entry = DateEntry(jobTimeGroupBox, width=12, background='darkblue',
                            foreground='white', borderwidth=2, date_pattern='dd/MM/y', state='readonly')
from_date_entry.place(x=220, y=20)
to_date_entry = DateEntry(jobTimeGroupBox, width=12, background='darkblue',
                          foreground='white', borderwidth=2, date_pattern='dd/MM/y', state='readonly')
to_date_entry.place(x=220, y=80)
# date_entry.pack(padx=10, pady=10)
btn_save_job = ttk.Button(jobTimeGroupBox, text="Save", command=add_job)
btn_save_job.place(x=350, y=140)

root.mainloop()
