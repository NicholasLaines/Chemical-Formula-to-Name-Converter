#takes the formula as a string from the user
user_formula = input("Enter your chemical equation: ")


#imports and blank variables
import ele
prefixes = []
proccessed_formula = []
element_names = []
outbound = ""


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


#Converts the element symbol to its name using the dictionary in ele.py
for item in proccessed_formula:
    no_num = item
    no_num = ''.join([i for i in no_num if not i.isdigit()])
    for i in range(1,119):
        current_element = ele.periodic[i]
        if current_element[1] == no_num:
            element_names.append(current_element[0])


#Combines atributes for output
for item in element_names:
    if outbound == "":
        outbound = outbound + prefixes[element_names.index(item)] + item + " "
    else:
        root = item[:2]
        ___ide = [string for string in ele.___ides if root in string]
        ___ide = ___ide[0]
        outbound = outbound + prefixes[element_names.index(item)] + ___ide + " "

#Prints output + a blank line for readablity
print("")
print(outbound.title())
