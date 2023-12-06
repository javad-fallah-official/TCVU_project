from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
from owlready2 import *
import easygui
import types
from os.path import dirname,abspath,join
from tkcalendar import DateEntry


myOntoPath = list()
paths = ''


# open owl file reader
def file_open_box():
    path = easygui.fileopenbox()
    return path


def open_file():
    path = file_open_box()
    myOntoPath.append(path)

    try:
        show_data_main()
        set_vulnerabilities_item()
        set_concepts_combobox()
        show_concepts()
        show_user()
        get_vulnerabilities()
    except TypeError:
        messagebox.showinfo("warning!", "file not found!")


def show_data_main():
    onto = get_ontology(myOntoPath[0]).load()
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
    my_concept_var.set(str(concepts_length))
    my_Vulnerabilities_var.set(str(vul_length))
    my_subclasses_var.set(str(len(subclass_length)))
    my_is_part_of_var.set(str(len(is_part_of_length)))
    my_has_vulnerability_var.set(str(len(has_vulnerabilities_length)))
    relationships.set("3")


def set_vulnerabilities_item():
    onto = get_ontology(myOntoPath[0]).load()
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
        listboxVul.insert(END, i)


def split_concepts():
    onto = get_ontology(myOntoPath[0]).load()
    concepts_list = list()
    concepts_lists = list(onto.classes())
    for i in concepts_lists:
        concepts_list.append(str(i).split("."))

    return concepts_list


def set_concepts_combobox():
    new_concepts_list = list()
    concepts_list = split_concepts()

    for i in concepts_list:
        new_concepts_list.append(i[1])

    conceptsCombo['values'] = new_concepts_list


def show_vulnerabilities_textbox(evt):
    name_entry.config(state="disabled")
    selection = str((listboxVul.get(ACTIVE)))
    name_vulnerability.set(selection)


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


vul_list2 = []


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
    fill_data=False
    selected = job_radio.get()
    if selected == 0:
        if jobVulCombo.current() != -1:
            selected_concept = jobVulCombo.get()
            fill_data=True
        else:
            messagebox.showwarning(
                'Warning', 'You should select a concept from combo box')

    if selected == 1:
        text=textboxVul.get("1.0", "end-1c").split('\n')[:-1]
        vul_list=[i[1] for i in vul_list2]
        # for vul in text:
        if not set(text).issubset(vul_list):
            messagebox.showwarning(
                'Warning', 'the slected vulnerability is not in the list')
        elif text==[]:
            messagebox.showwarning(
                'Warning', 'You should add at least one vulnerability from list')
        else:
            selected_concept = text
            fill_data=True

    if fill_data:
        if listboxUsers.curselection():
            user=listboxUsers.get(ACTIVE)
            start_time = TxtFromTime.get()
            end_time = TxtToTime.get()
            start_day = from_date_entry.get()
            end_day = to_date_entry.get()
            current_file_dir = dirname(abspath(__file__))
            new_file_path = join(current_file_dir, "job.txt")

            try:
                with open('job.txt','a',encoding='utf-8') as f:
                    f.write(f"*{user}* should start From : *{start_day}* at *{start_time}* and end in *{end_day}* at *{end_time}* for vulnerabilities : *{selected_concept}* \n\n")
                messagebox.showinfo('Successful',f'job added for {user}')
            except Exception as e:
                messagebox.showwarning('Unsuccessful','job was not added for user')

        else:
            messagebox.showwarning('Warning','You should select user to add job from user list box')



def validate_spinbox_input(input_value):
    if input_value.isdigit() and int(input_value) <= max_value:
        return True
    elif input_value == '':
        return True
    else:
        return False


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
usr_lb_label=Label(UserTab,text='User list :')
usr_lb_label.place(x=520,y=46,height=10)

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
Lbl1DelAbility = ttk.Label(AbilityDelGroupBox, text="Delete Ability Of : ", anchor="e")
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
lbl_user_ability=Label(Ability,text='User Ability :')
lbl_user_ability.place(x=520,y=290)

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
lbl_user_ability=Label(job,text='User Ability :')
lbl_user_ability.place(x=520,y=290)


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
                      foreground='white', borderwidth=2,date_pattern='dd/MM/y',state='readonly')
from_date_entry.place(x=220,y=20)


to_date_entry = DateEntry(jobTimeGroupBox, width=12, background='darkblue',
                      foreground='white', borderwidth=2,date_pattern='dd/MM/y',state='readonly')
to_date_entry.place(x=220,y=80)
# date_entry.pack(padx=10, pady=10)



btn_save_job = ttk.Button(jobTimeGroupBox, text="Save", command=add_job)
btn_save_job.place(x=350, y=140)

root.mainloop()
