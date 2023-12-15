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
