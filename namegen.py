

#~ Project Name Generator

# ToDo
# Select number of words for project name
# Pack the correct number of option menus based on choice
# On 'generate' button click, choose element randomly for each category, assign to list 'output'
# Modal pops up with name
# 

import tkinter as tk
from tkinter import messagebox
import random
import category_list    # metals, roman_gear, roman_legions, roman_ranks, famous_romans, arthurian_knights, colors, 
                        # medieval_melee_weapons, birds_of_prey, norse_mythology, norse_creatures, large_cats, german_rivers, cute_animals, adjectives, adverbs
                        # fantasy_creatures, magical_elements, castle_parts, gemstones, trees, norse_names, random


def choose_categories(varname, index, mode):
    global num_cat_var
    global option_menu_1
    global option_menu_2
    global option_menu_3
    global option_menu_4
    global option_menu_5
    global option_menu_6
    global curr_categories
    
    desired_categories = int(num_cat_var.get())
    
    # if we don't want more categories, return
    if(desired_categories == curr_categories):
        return
    
    
    menus = [option_menu_1, option_menu_2, option_menu_3, option_menu_4, option_menu_5, option_menu_6]
    
    if(curr_categories > desired_categories):
        for menu in menus[desired_categories:]:
            menu.grid_remove()
    
    for i in range(desired_categories):
        menus[i].grid(column=i, row=2)
    
    curr_categories = desired_categories


def get_result(category_name):
    try:
        if(category_name in dict_of_categories):
            selected_category = dict_of_categories[str(category_name)]
            res = random.choice(selected_category)
        else:
            raise LookupError
    except (IndexError, KeyError, LookupError):
        print('Invalid List Passed')
        res = 'INVALID'
    return res


def generate_button_handler():
    global num_cat_var
    global option_menu_vars
    global output
    
    output = []
    
    total_categories = num_cat_var.get()
    cats_to_get_from = []
    
    try:
        total_categories = int(num_cat_var.get())
    except (TypeError, ValueError):
        print('Invalid Number of Categories')
        total_categories = 6
    
    # Don't need to traverse the whole option_menu_vars list if we only want 2 categories
    for i in range(total_categories):
        cats_to_get_from.append(option_menu_vars[i].get())
    
    # get a result for each category that we need
    for i in cats_to_get_from:
        output.append(get_result(i))
    
    print(output)


dict_of_categories = {
    'Select Category...': category_list.random,
    
    'Metals': category_list.metals,
    'Roman Gear': category_list.roman_gear,
    'Roman Legions': category_list.roman_legions,
    'Roman Ranks': category_list.roman_ranks,
    'Famous Romans': category_list.famous_romans,
    'Arthurian Knights': category_list.arthurian_knights,
    'Colors': category_list.colors,
    
    'Medieval Weapons': category_list.medieval_melee_weapons,
    'Birds of Prey': category_list.birds_of_prey,
    'Norse Mythology': category_list.norse_mythology,
    'Norse Creatures': category_list.norse_creatures,
    'Large Cats': category_list.large_cats,
    'German Rivers': category_list.german_rivers,
    'Cute Animals': category_list.cute_animals,
    'Adjectives': category_list.adjectives,
    'Adverbs': category_list.adverbs,
    
    'Fantasy Creatures': category_list.fantasy_creatures,
    'Magical Elements': category_list.magical_elements,
    'Castle Parts': category_list.castle_parts,
    'Gemstones': category_list.gemstones,
    'Trees': category_list.trees,
    'Norse Names': category_list.norse_names,
}

category_choices = [k for k in dict_of_categories.keys()]
output = []


root = tk.Tk()
root.title('Project Name Generator')

frame = tk.Frame(root, bg='#0A0A0A', height=200, width=400)
frame.pack()


num_category_label = tk.Label(frame, text='Number of Categories: ')

num_cat_var = tk.IntVar() #between 2 and 6
num_cat_options = [2, 3, 4, 5, 6]
num_cat_var.set(2)

num_cat_var.trace_add('write', choose_categories)

num_categories = tk.OptionMenu(frame, num_cat_var, *num_cat_options)
curr_categories = 2




om_1_var = tk.StringVar()
om_1_var.set('Select Category...')
om_2_var = tk.StringVar()
om_2_var.set('Select Category...')
om_3_var = tk.StringVar()
om_3_var.set('Select Category...')
om_4_var = tk.StringVar()
om_4_var.set('Select Category...')
om_5_var = tk.StringVar()
om_5_var.set('Select Category...')
om_6_var = tk.StringVar()
om_6_var.set('Select Category...')

option_menu_vars = [om_1_var, om_2_var, om_3_var, om_4_var, om_5_var, om_6_var]

option_menu_1 = tk.OptionMenu(frame, om_1_var, *category_choices)
option_menu_2 = tk.OptionMenu(frame, om_2_var, *category_choices)
option_menu_3 = tk.OptionMenu(frame, om_3_var, *category_choices)
option_menu_4 = tk.OptionMenu(frame, om_4_var, *category_choices)
option_menu_5 = tk.OptionMenu(frame, om_5_var, *category_choices)
option_menu_6 = tk.OptionMenu(frame, om_6_var, *category_choices)


generate_button = tk.Button(frame, text='Generate Project Name', bg="#2B2B2B", fg="#02a102", command=generate_button_handler)



#^ Grid Initial Widgets
#~ Number of Categories
num_category_label.grid(column=0, row=1)
num_categories.grid(column=1, row=1)

#~ Starting Option Menus
option_menu_1.grid(column=0, row=2)
option_menu_2.grid(column=1, row=2)


#~ Generate Button
generate_button.grid(column=0, columnspan=7, row=6)

root.mainloop()



