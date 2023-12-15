from funcs import *
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from owlready2 import *
from os.path import dirname, abspath, join
from tkcalendar import DateEntry


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
