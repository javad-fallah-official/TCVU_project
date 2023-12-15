from funcs import *
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from owlready2 import *
from os.path import dirname, abspath, join
from tkcalendar import DateEntry


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
