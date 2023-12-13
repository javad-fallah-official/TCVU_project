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


def show_vulnerabilities_option():
    selection = var.get()
    if selection == 1:
        selection1 = str((listboxVul.get(ACTIVE)))
        name_vulnerability.set(selection1)
        R2AddTxt.config(state="disabled")
        set_concepts_combobox()
    elif selection == 2:
        R2AddTxt.config(state="normal")
        set_concepts_combobox()
    elif selection == 3:
        selection2 = str((listboxVul.get(ACTIVE)))
        name_vulnerability.set(selection2)
        R2AddTxt.config(state="disabled")
        show_remove_concepts()


def add_vulnerability(vulnerability_name):
    onto = get_ontology(myOntoPath[0]).load()
    try:
        concepts = conceptsCombo_value.get()
        concepts_lists = list(onto.classes())
        for i in concepts_lists:
            if str(i).find(concepts) != -1:
                i.hasVulnerability = [vulnerability_name]

        messagebox.showinfo("successful!", "Added vulnerability!")
    except TypeError:
        messagebox.showinfo(
            "Unsuccessful!", "The vulnerability was not added!")

    onto.save(file=myOntoPath[0])


def add_existing_vulnerability():
    vulnerability_name = R1AddTxt.get()
    add_vulnerability(vulnerability_name)


def add_new_vulnerability():
    vulnerability_name = R2AddTxt.get()
    add_vulnerability(vulnerability_name)
    listboxVul.insert(END, vulnerability_name)


def show_remove_concepts():
    onto = get_ontology(myOntoPath[0]).load()
    vulnerabilities_items = list(onto.hasVulnerability.get_relations())
    concepts_lists = list(onto.classes())
    vulnerability_name = RRemoveTxt.get()

    for concept in concepts_lists:
        for vulnerability in vulnerabilities_items:
            if concept == vulnerability[0] and vulnerability[1] == vulnerability_name:
                sp_concepts = str(concept).split(".")
                conceptsCombo['values'] = sp_concepts[1]


def remove_vulnerability_to_concepts():
    onto = get_ontology(myOntoPath[0]).load()
    try:
        concepts = conceptsCombo_value.get()
        concepts_lists = list(onto.classes())
        for i in concepts_lists:
            if str(i).find(concepts) != -1:
                i.hasVulnerability = ""

        messagebox.showinfo("successful!", "Removed vulnerability!")
    except TypeError:
        messagebox.showinfo(
            "Unsuccessful!", "The vulnerability was not added!")

    # onto.save(file="filename")
    onto.save(file=myOntoPath[0])


def apply_vulnerability():
    selection = var.get()
    if selection == 1:
        add_existing_vulnerability()
    elif selection == 2:
        add_new_vulnerability()
    elif selection == 3:
        remove_vulnerability_to_concepts()


def show_concepts():
    concepts_list = split_concepts()
    c = 1

    for i in concepts_list:
        listboxConcepts.insert(c, i[1])
        listboxConceptPlus.insert(c, i[1])
        c += 1


def search_concepts(event):
    concepts_list = split_concepts()
    search_string = search_str.get()
    listboxConcepts.delete(0, END)
    if search_string == "":
        show_concepts()
    else:
        filtered_data = list()
        for item in concepts_list:
            if item[1].find(search_string) != -1:
                filtered_data.append(item[1])
        for data in filtered_data:
            listboxConcepts.insert(1, data)


def show_vulnerabilities_from_concepts():
    onto = get_ontology(myOntoPath[0]).load()
    listFindVulnerabilities.delete(0, END)
    vulnerabilities_items = list(onto.hasVulnerability.get_relations())
    concepts_lists = list(onto.classes())
    concept_name = listboxConcepts.get(ACTIVE)
    c_name = ''
    concept_vulnerabilities_list = list()

    if isinstance(concept_name, tuple):
        c_name = concept_name[0]
    else:
        c_name = concept_name

    for concept in concepts_lists:
        for vulnerability in vulnerabilities_items:
            sp_vulnerability = str(vulnerability[0]).split(".")
            if vulnerability[0] == concept and sp_vulnerability[1] == c_name:
                concept_vulnerabilities_list.append(vulnerability[1])

    return concept_vulnerabilities_list


def find_vulnerabilities_from_concept():
    vul_list = show_vulnerabilities_from_concepts()
    listboxVul.delete(0, END)
    c = 1

    for item in vul_list:
        listFindVulnerabilities.insert(c, item)
        c += 1


def show_supperclass_from_concepts():
    onto = get_ontology(myOntoPath[0]).load()
    concepts_lists = list(onto.classes())
    concept_name = listboxConcepts.get(ACTIVE)
    c_name = ''

    if isinstance(concept_name, tuple):
        c_name = concept_name[0]
    else:
        c_name = concept_name

    for concept in concepts_lists:
        sp_concept = str(concept).split(".")
        if sp_concept[1] == c_name:
            c = str(concept.is_a).split(".")
            listFindSuperClasses.insert(1, c[1][:-1])


def find_superclass_from_concepts():
    show_supperclass_from_concepts()


def get_subclass_of():
    onto = get_ontology(myOntoPath[0]).load()
    txt_subclass = str(txtSubClass.get())
    concept = listboxConceptPlus.get(ACTIVE)
    concepts_lists = list(onto.classes())
    c = ''

    for item in concepts_lists:
        sp_concept = str(item).split(".")
        if sp_concept[1] == concept:
            c = item

    with onto:
        new_class = types.new_class(txt_subclass, (c,))

    # onto.save(file="filename")
    onto.save(file=myOntoPath[0])


def set_subclass_of():
    try:
        get_subclass_of()
        listboxConceptPlus.insert(0, txtSubClass.get())
        messagebox.showinfo("successful!", "Added subclass!")
    except TypeError:
        messagebox.showinfo("Unsuccessful!", "The subclass was not added!")


def get_first_concept_obj():
    first_concept = ""
    if checkVar1.get() == 1:
        first_concept = listboxConceptPlus.get(ACTIVE)
        txtPartOf1.set(first_concept)
        btn1PartOf.config(state="normal")
    else:
        txtPartOf1.set("")
        btn1PartOf.config(state="disabled")

    return txtPartOf1.get()


def set_first_concept_obj():
    onto = get_ontology(myOntoPath[0]).load()
    concepts_lists = list(onto.classes())
    new_concept = txtPartOf1.get()
    first_concept = get_first_concept_obj()
    concept = first_concept

    for i in concepts_lists:
        if str(i).find(concept) != -1:
            sp_item = str(i).split(".")
            if sp_item[1] == concept:
                new_concept = concept

    return new_concept


def get_second_concept_obj():
    second_concept = ""

    if checkVar2.get() == 1:
        second_concept = listboxConceptPlus.get(ACTIVE)
        txtPartOf2.set(second_concept)
        btn2PartOf.config(state="normal")
    else:
        txtPartOf2.set("")
        btn2PartOf.config(state="disabled")

    return second_concept


def set_second_concept_obj():
    onto = get_ontology(myOntoPath[0]).load()
    concepts_lists = list(onto.classes())
    new_concept = txtPartOf2.get()
    second_concept = get_second_concept_obj()
    concept = second_concept

    for i in concepts_lists:
        if str(i).find(concept) != -1:
            sp_item = str(i).split(".")
            if sp_item[1] == concept:
                new_concept = concept

    return new_concept


def is_part_of():
    f = txtPartOf1.get()
    s = txtPartOf2.get()
    onto = get_ontology(myOntoPath[0]).load()
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
        # onto.save(file="filename")
        onto.save(file=myOntoPath[0])
        messagebox.showinfo("successful!", f"The {f} is_part_of {s}!")
    except TypeError:
        messagebox.showinfo(
            "Unsuccessful!", f"The {f} was not made is_part_of the {s}!")


def show_concept_have_vul():
    onto = get_ontology(myOntoPath[0]).load()
    concepts_list = list(onto.hasVulnerability.get_relations())
    concepts_items = list()
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
        listBoxHaveVul.insert(END, i)


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


def show_user():
    listboxUsers.delete(0, END)
    onto = get_ontology(myOntoPath[0]).load()
    class_name = onto.Users
    users_name = list(class_name.subclasses())
    for i in users_name:
        listboxUsers.insert(0, i.name)


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


def update_entry(event):
    try:
        selected_item = listboxAbility.get(listboxAbility.curselection())
        TxtDelAbility.delete(0, tk.END)
        TxtDelAbility.insert(0, selected_item)
    except:
        pass


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
