#Creates inital variables (user inputs, blank variables and imports)
user_formula = input('Enter your chemical equation: ')
import ele
proccessed_formula = []
atomic_nums = []
prefixes = []
is_ionic = False


#Processes the string into a list of the compound's compnents
s_for = list(user_formula)
for item in s_for:
    if item.isupper():
        proccessed_formula.append(item)
    else:
        lpf = len(proccessed_formula) - 1
        proccessed_formula[lpf] = proccessed_formula[lpf] + item


#Calculates the prefixes for each component of the compound
for item in proccessed_formula:
    if "2" in item:
        prefixes.append("Di")
    elif "3" in item:
        prefixes.append("Tri")
    elif "4" in item:
        prefixes.append("Tetra")
    elif "5" in item:
        prefixes.append("Penta")
    elif "6" in item:
        prefixes.append("Hexa")
    elif "7" in item:
        prefixes.append("Hepta")
    elif "8" in item:
        prefixes.append("Octa")
    elif "9" in item:
        prefixes.append("Nona")
    elif "10" in item:
        prefixes.append("Deca")
    else:
        prefixes.append("Mon")
if prefixes[0] == "Mon":
    prefixes[0] = ""


#Converts the element symbol to its atomic number
for item in proccessed_formula:
    no_num = ''.join([i for i in item if not i.isdigit()])
    for i in range(1,118):
        current_element = ele.periodic[i]
        if current_element[1] == no_num:
            atomic_nums.append(i)


#Checks if the compound is ionic by checking for metals or NH4 if it is it generates the formula
if 'N' in proccessed_formula and 'H4' in proccessed_formula:
    is_ionic = True
    from ionic import gen_ion_com
    gen_ion_com(proccessed_formula, atomic_nums, prefixes, False)
for item in proccessed_formula:
    no_num = item
    no_num = ''.join([i for i in no_num if not i.isdigit()])
    for i in range(1,119):
        current_element = ele.periodic[i]
        if current_element[1] == no_num:
            if current_element[2] == 'M':
                is_ionic = True
                from ionic import gen_ion_com
                gen_ion_com(proccessed_formula, atomic_nums, prefixes, True)


#Checks if the compound is covalent by checking the is_ionic variable's status if it is it generates the formula
if is_ionic == False:
    from covalent import gen_cov_com
    gen_cov_com(proccessed_formula, atomic_nums, prefixes)
