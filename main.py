from funcs import *
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from owlready2 import *
from os.path import dirname, abspath, join
from tkcalendar import DateEntry


# make form
root = tk.Tk()
root.title("Network Security Ontology")
root.geometry("800x600")

# make tab bar Menu
tabControl = ttk.Notebook(root)

mainTab = ttk.Frame(tabControl)
vulnerabilitiesTab = ttk.Frame(tabControl)
conceptsTab = ttk.Frame(tabControl)
conceptsPlusTab = ttk.Frame(tabControl)
advancedCheckTab = ttk.Frame(tabControl)
UserTab = ttk.Frame(tabControl)

tabControl.add(mainTab, text="Main")
tabControl.add(vulnerabilitiesTab, text="Vulnerabilities")
tabControl.add(conceptsTab, text="Concepts")
tabControl.add(conceptsPlusTab, text="Concepts++")
tabControl.add(advancedCheckTab, text="Advanced Check")
tabControl.add(UserTab, text="User")
tabControl.pack(expand=1, fill="both")

# main tab layout design
lblBrowse = ttk.Label(mainTab, text="select file : ", anchor="e")
lblBrowse.place(x=10, y=20)
btnBrowse = ttk.Button(mainTab, text="file", command=open_file)
btnBrowse.pack()
btnBrowse.place(x=70, y=20)


current_file_dir = dirname(abspath(__file__))

# # imagebox in main tab menu
# imagePath = r'{}\pictures\mainPic.PNG'.format(join(current_file_dir))
# img = ImageTk.PhotoImage(Image.open(imagePath).resize(
#     (350, 500), Image.Resampling.LANCZOS))
# imageBox = ttk.Label(mainTab, image=img, anchor="e")
# imageBox.place(x=420, y=40)

# # Collage Icon
# imagePathCollage = r'pictures\ss.PNG'
# imgCollage = ImageTk.PhotoImage(Image.open(
#     imagePathCollage).resize((200, 200), Image.Resampling.LANCZOS))
# imageBox = ttk.Label(mainTab, image=imgCollage, anchor="e")
# imageBox.place(x=10, y=70)

# labels for show data in main tab menu
my_concept_var = StringVar()
my_concept_var.set("0")
lblConcepts = ttk.Label(
    mainTab, text="number of concept we currently support : ", anchor="e")
lblConcepts.place(x=10, y=440)
lblConcepts = ttk.Label(mainTab, textvariable=my_concept_var)
lblConcepts.place(x=240, y=440)

my_Vulnerabilities_var = StringVar()
my_Vulnerabilities_var.set("0")
lblVulnerabilities = ttk.Label(
    mainTab, text="number of concept we Vulnerabilities support : ", anchor="e")
lblVulnerabilities.place(x=10, y=460)
lblVul = ttk.Label(mainTab, textvariable=my_Vulnerabilities_var)
lblVul.place(x=260, y=460)

my_subclasses_var = StringVar()
my_subclasses_var.set("0")
lblSubClassOf = ttk.Label(mainTab, text="number of SubClassOf : ", anchor="e")
lblSubClassOf.place(x=10, y=480)
lblSubClass = ttk.Label(mainTab, textvariable=my_subclasses_var)
lblSubClass.place(x=140, y=480)

my_is_part_of_var = StringVar()
my_is_part_of_var.set("0")
lblIsPartOf = ttk.Label(
    mainTab, text="number of IsPartOf relationship : ", anchor="e")
lblIsPartOf.place(x=10, y=500)
lblIsPart = ttk.Label(mainTab, textvariable=my_is_part_of_var)
lblIsPart.place(x=190, y=500)

my_has_vulnerability_var = StringVar()
my_has_vulnerability_var.set("0")
lblHasVulnerability = ttk.Label(
    mainTab, text="number of hasVulnerability relationship : ", anchor="e")
lblHasVulnerability.place(x=10, y=520)
lblHasVulnerability = ttk.Label(mainTab, textvariable=my_has_vulnerability_var)
lblHasVulnerability.place(x=230, y=520)

relationships = StringVar()
relationships.set("0")
lblRelationships = ttk.Label(mainTab, text="Relationships : ", anchor="e")
lblRelationships.place(x=10, y=540)
lblRelationShips = ttk.Label(mainTab, textvariable=relationships)
lblRelationShips.place(x=90, y=540)

# Vulnerability tab layout design
lblVulnerabilitiesTitle = ttk.Label(
    vulnerabilitiesTab, text="a list of security vulnerabilities : ", anchor="e")
lblVulnerabilitiesTitle.place(x=10, y=10)

name_vulnerability = StringVar()
name_entry = Entry(vulnerabilitiesTab, textvariable=name_vulnerability)
name_entry.place(x=450, y=10, width=320)

listboxVul = Listbox(vulnerabilitiesTab)
listboxVul.bind('<<ListboxSelect>>', show_vulnerabilities_textbox)
listboxVul.place(x=10, y=40, height=500, width=280)

lblVulnerabilitiesName = ttk.Label(
    vulnerabilitiesTab, text="vulnerability name : ", anchor="e")
lblVulnerabilitiesName.place(x=340, y=10)

vulnerabilitiesGroupBox = LabelFrame(
    vulnerabilitiesTab, text="This is a LabelFrame")
vulnerabilitiesGroupBox.place(x=340, y=40, width=435, height=500)

var = IntVar()
# first radio button design
R1Add = Radiobutton(vulnerabilitiesGroupBox, text="Add an existing vulnerabilities to concepts", value=1, variable=var,
                    command=show_vulnerabilities_option)
R1Add.place(x=10, y=10)
R1AddGroupBox = LabelFrame(vulnerabilitiesGroupBox)
R1AddGroupBox.place(x=10, y=40, width=410, height=50)
R1AddLbl = ttk.Label(R1AddGroupBox, text="select vulnerability : ", anchor="e")
R1AddLbl.place(x=10, y=10)
R1AddTxt = Entry(R1AddGroupBox, state="disabled",
                 textvariable=name_vulnerability)
R1AddTxt.place(x=120, y=10, width=270)

# second radio button design
R2Add = Radiobutton(vulnerabilitiesGroupBox, text="Add a new vulnerability to concepts", value=2, variable=var,
                    command=show_vulnerabilities_option)
R2Add.place(x=10, y=120)
R2AddGroupBox = LabelFrame(vulnerabilitiesGroupBox)
R2AddGroupBox.place(x=10, y=150, width=410, height=50)
R2AddLbl = ttk.Label(R2AddGroupBox, text="New vulnerability : ", anchor="e")
R2AddLbl.place(x=10, y=10)
R2AddTxt = Entry(R2AddGroupBox, state="disabled")
R2AddTxt.place(x=120, y=10, width=270)

# Third radio button design
RRemove = Radiobutton(vulnerabilitiesGroupBox, text="Remove a vulnerability to concepts", value=3, variable=var,
                      command=show_vulnerabilities_option)
RRemove.place(x=10, y=230)
RRemoveGroupBox = LabelFrame(vulnerabilitiesGroupBox)
RRemoveGroupBox.place(x=10, y=260, width=410, height=50)
RRemoveLbl = ttk.Label(
    RRemoveGroupBox, text="Select vulnerability : ", anchor="e")
RRemoveLbl.place(x=10, y=10)
RRemoveTxt = Entry(RRemoveGroupBox, state="disabled",
                   textvariable=name_vulnerability)
RRemoveTxt.place(x=120, y=10, width=270)

# select concepts
LblVulnerabilityConcepts = ttk.Label(
    vulnerabilitiesGroupBox, text="Select Concepts: ", anchor="e")
LblVulnerabilityConcepts.place(x=60, y=330)
conceptsCombo_value = StringVar()
conceptsCombo = ttk.Combobox(
    vulnerabilitiesGroupBox, textvariable=conceptsCombo_value, state="readonly")
conceptsCombo.place(x=160, y=330, width=200)

# button for apply changes in vulnerabilities tab
btnVulnerabilityApply = ttk.Button(
    vulnerabilitiesGroupBox, text="Apply", command=apply_vulnerability)
btnVulnerabilityApply.pack()
btnVulnerabilityApply.place(x=185, y=440)

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

txtSubClass = StringVar()
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
txtPartOf1 = StringVar()
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
txtPartOf2 = StringVar()
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

# concepts tab bar design
# search
lblSearchInConcepts = ttk.Label(conceptsTab, text="Search", anchor="e")
lblSearchInConcepts.place(x=10, y=20)
search_str = StringVar()
TxtSearchInConcepts = Entry(conceptsTab, textvariable=search_str)
TxtSearchInConcepts.bind('<Return>', search_concepts)
TxtSearchInConcepts.place(x=55, y=20, width=200)

# list box for concepts
listboxConcepts = Listbox(conceptsTab)
listboxConcepts.place(x=10, y=50, height=500, width=245)

# find Vulnerabilities
btnFindVulnerabilities = ttk.Button(
    conceptsTab, text="Find Vulnerabilities", command=find_vulnerabilities_from_concept)
btnFindVulnerabilities.pack()
btnFindVulnerabilities.place(x=280, y=50, width=180)

listFindVulnerabilities = Listbox(conceptsTab)
listFindVulnerabilities.place(x=280, y=80, height=150, width=180)

# find super classes
btnFindSuperClasses = ttk.Button(
    conceptsTab, text="Find super classes", command=find_superclass_from_concepts)
btnFindSuperClasses.pack()
btnFindSuperClasses.place(x=470, y=20, width=160)

listFindSuperClasses = Listbox(conceptsTab)
listFindSuperClasses.place(x=470, y=50, height=180, width=160)

# find Parts
btnFindParts = ttk.Button(conceptsTab, text="Find parts")
btnFindParts.pack()
btnFindParts.place(x=640, y=20, width=140)

listFindParts = Listbox(conceptsTab)
listFindParts.place(x=640, y=50, height=180, width=140)

# radio buttons for concepts
RSuperClasses = Radiobutton(conceptsTab, text="base on SuperClasses", value=0)
RSuperClasses.place(x=280, y=230)
RSuperClasses = Radiobutton(
    conceptsTab, text="base on Concepts parts", value=1)
RSuperClasses.place(x=280, y=250)
RSuperClasses = Radiobutton(
    conceptsTab, text="base on SuperClass and concept`s parts", value=2)
RSuperClasses.place(x=280, y=270)

# inference button
btnInference = ttk.Button(conceptsTab, text="inference")
btnInference.pack()
btnInference.place(x=280, y=320, width=120, height=50)

listInference = Listbox(conceptsTab)
listInference.place(x=440, y=320, height=230, width=340)

# Advance Checked Design
TxtHelpInAdvance = Text(advancedCheckTab, wrap=WORD, width=40, height=4)
TxtHelpInAdvance.insert(INSERT, "Advanced check will create a complete log of all relationships and information. "
                                "Note: Advance Check will take some time to complete.")
TxtHelpInAdvance.config(state="disabled")
TxtHelpInAdvance.place(x=10, y=10)

# Group box for result
resultGroupBox = LabelFrame(advancedCheckTab, text="Result")
resultGroupBox.place(x=350, y=0, width=290, height=80)

lblResult = ttk.Label(
    resultGroupBox, text="Number of new infered vulnerabilities: ", anchor="e")
lblResult.place(x=10, y=15)
strResult = StringVar()
strResult.set("0")
lblShowResult = ttk.Label(resultGroupBox, textvariable=strResult, anchor="e")
lblShowResult.place(x=245, y=15)

# btn Advance check
btnAdvanceCheck = ttk.Button(
    advancedCheckTab, text="Advance Check", command=show_advance_data)
btnAdvanceCheck.pack()
btnAdvanceCheck.place(x=660, y=8, width=120, height=70)

# label for not vulnerabilities
lblNotVul = ttk.Label(
    advancedCheckTab, text="Concepts that are not vulnerabilities: ", anchor="e")
lblNotVul.place(x=10, y=90)

# list box for not vulnerabilities
listBoxNotVul = Listbox(advancedCheckTab)
listBoxNotVul.place(x=10, y=110, height=460, width=230)

# label for vulnerabilities
lblVul = ttk.Label(
    advancedCheckTab, text="Concepts that have some vulnerabilities at first: ", anchor="e")
lblVul.place(x=260, y=90)

# list box for vulnerabilities
listBoxHaveVul = Listbox(advancedCheckTab)
listBoxHaveVul.place(x=260, y=110, height=460, width=230)

# imagebox in advance tab menu
# imagePath2 = r'pictures\advancePic.PNG'
# img2 = ImageTk.PhotoImage(Image.open(imagePath2).resize(
#     (250, 360), Image.Resampling.LANCZOS))
# imageBoxAdvance = ttk.Label(advancedCheckTab, image=img2, anchor="e")
# imageBoxAdvance.place(x=520, y=135)

# label for vulnerabilities
lblVulRel = ttk.Label(
    advancedCheckTab, text="V-R = Vulnerabilities Relationships", anchor="e")
lblVulRel.place(x=555, y=500)


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
txtDelUser = StringVar()
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
txtUser = StringVar()
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
txtAbility = StringVar()
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
txtAbility = StringVar()
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


# day combo boxes in job tab
# fromDayCombo = ttk.Combobox(jobTimeGroupBox, values=[
#                             "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], state="readonly")
# fromDayCombo.place(x=220, y=20, width=150)
# fromDayCombo.set('Saturday')

# ToDayCombo = ttk.Combobox(jobTimeGroupBox, values=[
#                           "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], state="readonly")
# ToDayCombo.place(x=220, y=80, width=150)
# ToDayCombo.set('Saturday')

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
