def gen_ion_com(proccessed_formula, atomic_nums, prefixes, metalic):
    import ele
    outbound = ''
    subscripts = []
    
    for item in proccessed_formula:
        if "2" in item:
            subscripts.append(2)
        elif "3" in item:
            subscripts.append(3)
        elif "4" in item:
            subscripts.append(4)
        elif "5" in item:
            subscripts.append(5)
        elif "6" in item:
            subscripts.append(6)
        elif "7" in item:
            subscripts.append(7)
        elif "8" in item:
            subscripts.append(8)
        elif "9" in item:
            subscripts.append(9)
        elif "10" in item:
            subscripts.append(10)
        else:
            subscripts.append(1)

    
    #Converts numbers to roman numerals
    num_map = [(10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    def num2roman(num):
        roman = ''
        while num > 0:
            for i, r in num_map:
                while num >= i:
                    roman += r
                    num -= i
        return roman
    
    
    if metalic == False:
        if len(proccessed_formula) == 2:
            outbound = 'amonium'
        elif len(proccessed_formula) == 3:
            atomic_nums.remove(1)
            atomic_nums.remove(7)
            outbound = 'amonium ' + ele.periodic[atomic_nums[0]][3] + 'ide'
        else:
            outbound = 'polyatomic amonium based ionic'
    else:
        typei = [3,4,11,12,19,20,37,38,55,56,87,88,74] #Group 1 metals, Group 2 metals and Tungsten
        typeii = [13, 21, 22, 23, 24, 25 ,26, 27, 28, 29, 30, 31, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116]
        if any(item in typei for item in atomic_nums):
            if len(proccessed_formula) == 2:
                metal = list(set(atomic_nums).intersection(typei))
                atomic_nums.remove(metal[0])
                outbound = ele.periodic[metal[0]][0] + ' ' + ele.periodic[atomic_nums[0]][3] + 'ide'
            else:
                outbound = 'polyatomic type i metal based ionic'
        else:
            if len(proccessed_formula) == 2:
                metal = list(set(atomic_nums).intersection(typeii))
                atomic_nums.remove(metal[0])
                charge = abs(ele.periodic[atomic_nums[0]][4]) * subscripts[1] / subscripts[0]
                numeral = '(' + num2roman(charge) + ')'
                outbound = ele.periodic[metal[0]][0] + ' ' + numeral + ' ' + ele.periodic[atomic_nums[0]][3] + 'ide'
            else:
                outbound = 'polyatomic type ii metal based ionic'
    
    
    print('')
    print(outbound.title())
