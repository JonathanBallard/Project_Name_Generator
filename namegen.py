

#~ Project Name Generator
#~ Jonathan Ballard

# ToDo
#[done] Select number of words for project name
#[done] Pack the correct number of option menus based on choice
#[done] On 'generate' button click, choose element randomly for each category, assign to list 'output'
# Modal pops up with name
# Change colors and fonts
# Adjust window size
# Lock certain choices in
# Fix column for category 1 (num categories label too big)



import tkinter as tk
from tkinter import messagebox
import random
import category_list    # metals, roman_gear, roman_legions, roman_ranks, famous_romans, arthurian_knights, colors, 
                        # medieval_melee_weapons, birds_of_prey, norse_mythology, norse_creatures, large_cats, german_rivers, cute_animals, adjectives, adverbs
                        # fantasy_creatures, magical_elements, castle_parts, gemstones, trees, norse_names, heraldic_animals, ancient_battles, medieval_battles
                        # random sets a random category


config = {
    # Size
    'window_w': 90,
    'window_h': 35,
    
    'btn_w': 25,
    'btn_h': 2,
    
    'label_w': 25,
    'label_h': 2,
    
    'output_w': 45,
    'output_h': 5,
    
    'option_w': 25,
    'option_h': 1,
    
    'sm_option_w': 8,
    'sm_option_h': 1,
    
    # Colors
    'window_bg': '#272727',
    'window_fg': '#02A102',
    
    'btn_bg': "#4D4D4D",
    'btn_fg': '#02A102',
    
    'label_bg': '#272727',
    'label_fg': '#02A102',
    
    'output_bg': '#272727',
    'output_fg': "#DCB002",
    
    'option_bg': '#272727',
    'option_fg': "#DCB002",
    
    # Fonts
    'btn_font': ('Viner Hand ITC', 16, "bold"),
    'label_font': ('Century', 14),
    'output_font': ('Arial', 18),
    'option_font': ('Arial', 18),
    
    # Padding
    'option_padx': 5,
    'option_pady': 10, # Unused
    
    'label_padx': 0, # Unused
    'label_pady': 15, # Unused

    'btn_padx': 0, # Unused
    'btn_pady': 30, # Unused
    
    'output_padx': 10, # Unused
    'output_pady': 5, # Unused
}

def select_random_category():
    
    # Create a list of all the keys in the dictionary of categories - except for the random category, which defaults to "Metals"
    categories = [x if x != 'Select Category...' else 'Metals' for x in dict_of_categories.keys()]
    
    
    return random.choice(categories)




# Shows the number of categories you ask for, callback is bound to observable variable 'num_cat_var'
def choose_categories(varname, index, mode):
    global num_cat_var
    global option_menu_1
    global option_menu_2
    global option_menu_3
    global option_menu_4
    global option_menu_5
    global option_menu_6
    global curr_categories
    global menus
    
    desired_categories = int(num_cat_var.get())
    
    # if we don't want more categories, return
    if(desired_categories == curr_categories):
        return
    
    
    
    if(curr_categories > desired_categories):
        for menu in menus[desired_categories:]:
            menu.grid_remove()
    
    for i in range(desired_categories):
        menus[i].grid(column=i, row=2, padx=10)
    
    curr_categories = desired_categories
    
    output_label.grid_remove()
    output_label.grid(columnspan=curr_categories, rowspan=6, row=8, padx=config['output_padx'], pady=config['output_pady'])


# Retrieves a random element from the selected lists
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
    
    num_randoms = 0
    
    
    try:
        total_categories = int(num_cat_var.get())
    except (TypeError, ValueError):
        print('Invalid Number of Categories')
        total_categories = 6
    
    
    for i in range(total_categories): # Don't need to traverse the whole option_menu_vars list if we only want 2 categories
        category_choice = option_menu_vars[i].get() # Gets the name of the category chosen
        if category_choice == "Select Category...": # If 'random' choice is made
            num_randoms += 1
            chosen_cat = select_random_category() # Get Random name
        else:
            chosen_cat = category_choice
        
        cats_to_get_from.append(chosen_cat)
    
    # get a result for each category that we need
    for i in cats_to_get_from:
        output.append(get_result(i))
    
    print(output)
    formatted_output = ''
    
    for word in output:
        formatted_output += word + ' '
        
    output_text.set(formatted_output)


dict_of_categories = {
    # 'Select Category...': category_list.random_category, #This selects a random category for that slot
    'Select Category...': [], #This selects a random category for that slot
    
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
    'Heraldic Animals': category_list.heraldic_animals,
    
    'Ancient Battles': category_list.ancient_battles,
    'Medieval Battles': category_list.medieval_battles,
    'Planets': category_list.planets,
}

category_choices = [k for k in dict_of_categories.keys()]

output = []
curr_categories = 2 # default value


root = tk.Tk()
root.title('Project Name Generator')

frame = tk.Frame(root, bg=config['window_bg'], height=config['window_h'], width=config['window_w'])

num_category_label = tk.Label(frame, text='Number of Categories: ')
num_category_label.config(width=config['label_w'], height=config['label_h'], font=config['label_font'], bg=config['label_bg'], fg=config['label_fg'])

num_cat_var = tk.IntVar()
num_cat_options = [2, 3, 4, 5, 6]
num_cat_var.set(2) # Set default number of categories to display

num_cat_var.trace_add('write', choose_categories) # Bind callback to 'write' on num_cat_var - adjusts number of categories displayed

num_categories = tk.OptionMenu(frame, num_cat_var, *num_cat_options)

num_categories.config(width=config['sm_option_w'], height=config['sm_option_h'])

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

menus = [option_menu_1, option_menu_2, option_menu_3, option_menu_4, option_menu_5, option_menu_6]

for menu in menus:
    menu.config(width=config['option_w'], height=config['option_h'])


generate_button = tk.Button(frame, text='Generate Project Name', font=config['btn_font'],bg=config['btn_bg'], fg=config['btn_fg'], height=config['btn_h'], width=config['btn_w'], command=generate_button_handler)

output_text = tk.StringVar()
output_text.set('')
output_label = tk.Label(frame, font=config['output_font'], textvariable=output_text, bg=config['output_bg'], fg=config['output_fg'], height=config['output_h'], width=config['output_w'],)

#^ Pack the parent frame
frame.pack()

#^ Grid Initial Widgets
#~ Number of Categories
num_category_label.grid(column=0, row=1)
num_categories.grid(column=1, row=1)

#~ Starting Option Menus
option_menu_1.grid(column=0, row=2)
option_menu_2.grid(column=1, row=2, padx=config['option_padx'], pady=config['option_pady'])

output_label.grid(columnspan=6, rowspan=6, row=8, padx=config['output_padx'], pady=config['output_pady'])

#~ Generate Button
generate_button.grid(column=0, columnspan=7, row=6, padx=config['btn_padx'], pady=config['btn_pady'])

root.mainloop()



