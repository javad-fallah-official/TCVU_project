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


def show_concept_not_vul():
    onto = get_ontology(myOntoPath[0]).load()
    vul_list = list(onto.hasVulnerability.get_relations())
    vul_items = list()
    con_list = list(onto.classes())
    con_item = list()
    for i in vul_list:
        sp_vul = str(i[0]).split(".")
        vul_items.append(sp_vul[1])

    for i in con_list:
        sp_con = str(i).split(".")
        con_item.append(sp_con[1])

    all_list = vul_items + con_item
    concepts_items = []

    for i in all_list:
        if i not in concepts_items and i not in vul_items:
            concepts_items.append(i)

    for i in concepts_items:
        listBoxNotVul.insert(END, i)


def show_advance_data():
    onto = get_ontology(myOntoPath[0]).load()
    show_concept_not_vul()
    show_concept_have_vul()
    x = list(default_world.sparql("""
            PREFIX my: <http://www.semanticweb.org/imana/ontologies/2022/10/Network#>
            SELECT ?x
                    WHERE { ?x owl:onProperty my:hasVulnerability.
                    }
            """))
    has_vulnerabilities_length = list(
        onto.hasVulnerability.get_relations()) + x
    strResult.set(str(len(has_vulnerabilities_length)))


def add_user():
    onto = get_ontology(myOntoPath[0]).load()
    user_name = TxtAddUser.get()
    try:
        with onto:
            new_class = types.new_class(user_name, (onto.Users,))
        onto.save(file=myOntoPath[0])
        messagebox.showinfo("successful!", "User Added!")
        show_user()
    except:
        messagebox.showinfo("Unsuccessful!", "User was not Added!")


def delete_user():
    name = TxtDelUser.get()
    onto = get_ontology(myOntoPath[0]).load()
    try:
        name_for_delete = onto[name]
        destroy_entity(name_for_delete)
        onto.save(file=myOntoPath[0], format="rdfxml")
        TxtDelUser.delete(0, END)
        messagebox.showinfo("successful!", "User Deleted!")
    except:
        messagebox.showinfo("Unsuccessful!", "User was not Deleted!")

    show_user()


def get_name_listbox():
    name = listboxUsers.get(ACTIVE)
    TxtDelUser.delete(0, END)
    TxtDelUser.insert(0, name)


def show_user_ability():
    onto = get_ontology(myOntoPath[0]).load()
    listboxAbility.delete(0, END)
    listboxAbilityJob.delete(0, END)
    TxtDelAbility.delete(0, END)
    selected_item = listboxUsers.get(listboxUsers.curselection())
    class_name = onto[selected_item]
    user_ability = list(class_name.subclasses())
    for i in user_ability:
        user_name = str(i).split('.')[1]
        listboxAbility.insert(0, user_name)
        listboxAbilityJob.insert(0, user_name)


def add_ability():
    ability = TxtAddAbility.get()
    onto = get_ontology(myOntoPath[0]).load()
    user_to_add_ability = listboxUsers.get(ACTIVE)
    parent_user_class = onto[user_to_add_ability]
    try:
        with onto:
            new_class = types.new_class(ability, (parent_user_class,))
            messagebox.showinfo(
                "successful!", f"Ability Added for {user_to_add_ability}!")
            TxtAddAbility.delete(0, END)
    except:
        messagebox.showinfo(
            "Unsuccessful!", f"Ability was not Added for {user_to_add_ability}!")
    onto.save(myOntoPath[0])
    show_user_ability()


def delete_ability():
    ability_name = TxtDelAbility.get()
    onto = get_ontology(myOntoPath[0]).load()
    try:
        name_for_delete = onto[ability_name]
        destroy_entity(name_for_delete)
        TxtDelAbility.delete(0, END)
        onto.save(file=myOntoPath[0], format="rdfxml")
        messagebox.showinfo("successful!", "Ability Deleted!")
    except:
        messagebox.showinfo("Unsuccessful!", "Ability was not Deleted!")

    show_user_ability()


def add_vul_to_txtbox():
    vul = listboxvuljob.get(ACTIVE)
    textbox_text = textboxVul.get("1.0", "end-1c").split('\n')
    text = f'{vul}\n'
    if vul not in textbox_text:
        textboxVul.insert('end', text)


def by_vul():
    btnAddVulTextBox.config(state=NORMAL)
    textboxVul.config(state=NORMAL)


def by_class():
    btnAddVulTextBox.config(state=DISABLED)
    textboxVul.delete('1.0', END)
    textboxVul.config(state=DISABLED)


def get_vulnerabilities():
    global vul_list2
    onto = get_ontology(myOntoPath[0]).load()
    vul_list = list(onto.hasVulnerability.get_relations())
    vul_list2 = [(i[0].name, i[1]) for i in vul_list]
    concepts_items = []
    for i in vul_list:
        if i[0].name not in concepts_items:
            concepts_items.append(i[0].name)
    jobVulCombo['values'] = concepts_items


def update_listbox(event):
    selected_option = jobVulCombo.get()
    listboxvuljob.delete(0, tk.END)
    for i in vul_list2:
        if i[0] == selected_option:
            listboxvuljob.insert(tk.END, i[1])


def add_job():
    fill_data = False
    selected = job_radio.get()
    if selected == 0:
        if jobVulCombo.current() != -1:
            selected_concept = jobVulCombo.get()
            fill_data = True
        else:
            messagebox.showwarning(
                'Warning', 'You should select a concept from combo box')

    if selected == 1:
        text = textboxVul.get("1.0", "end-1c").split('\n')[:-1]
        vul_list = [i[1] for i in vul_list2]
        # for vul in text:
        if not set(text).issubset(vul_list):
            messagebox.showwarning(
                'Warning', 'the slected vulnerability is not in the list')
        elif text == []:
            messagebox.showwarning(
                'Warning', 'You should add at least one vulnerability from list')
        else:
            selected_concept = text
            fill_data = True

    if fill_data:
        if listboxUsers.curselection():
            user = listboxUsers.get(ACTIVE)
            start_time = TxtFromTime.get()
            end_time = TxtToTime.get()
            start_day = from_date_entry.get()
            end_day = to_date_entry.get()
            current_file_dir = dirname(abspath(__file__))
            new_file_path = join(current_file_dir, "job.txt")

            try:
                with open('job.txt', 'a', encoding='utf-8') as f:
                    f.write(
                        f"*{user}* should start From : *{start_day}* at *{start_time}* and end in *{end_day}* at *{end_time}* for vulnerabilities : *{selected_concept}* \n\n")
                messagebox.showinfo('Successful', f'job added for {user}')
            except Exception as e:
                messagebox.showwarning(
                    'Unsuccessful', 'job was not added for user')

        else:
            messagebox.showwarning(
                'Warning', 'You should select user to add job from user list box')


def validate_spinbox_input(input_value):
    if input_value.isdigit() and int(input_value) <= max_value:
        return True
    elif input_value == '':
        return True
    else:
        return False
