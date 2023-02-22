#takes the formula as a string from the user
user_formula = input("Enter your chemical equation: ")


#imports and stuff
import ele
prefixes = []
proccessed_formula = []
element_names = []
outbound = ""


#prints a blank string to improve formating
print("")


#processes the string into a list of the chemical´s compnents
sliced_formula = list(user_formula)
for item in sliced_formula:
    if item.isupper():
        proccessed_formula.append(item)
    else:
        lpf = len(proccessed_formula) - 1
        proccessed_formula[lpf] = proccessed_formula[lpf] + item


#finds the prefixes for each of the items in the proccessed_formula list
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

for item in proccessed_formula:
    lol = item
    lol = ''.join([i for i in lol if not i.isdigit()])
    for i in range(1,119):
        current_element = ele.periodic[i]
        if current_element[1] == lol:
            element_names.append(current_element[0])


print("")
print(prefixes)
print(element_names)

for item in element_names:
    outbound = outbound + " "  + prefixes[element_names.index(item)] + item   
    
print(outbound)