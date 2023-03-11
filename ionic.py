def gen_ion_com(proccessed_formula, atomic_nums, prefixes, metalic):
    import ele
    outbound = ''
    
    
    if metalic == False:
        if len(proccessed_formula) == 2:
            outbound = 'ammonium'
        elif len(proccessed_formula) == 3:
            atomic_nums.remove(1)
            atomic_nums.remove(7)
            outbound = 'ammonium ' + ele.periodic[atomic_nums[0]][3] + 'ide'
        else:
            outbound = 'polyatomic ammonium based ionic'
    else:
        typei = (3,4,11,12,19,20,37,38,55,56,87,88,74) #Group 1 metals, Group 2 metals and Tungsten
        if any(item in typei for item in atomic_nums):
            outbound = 'type i ionic compound'
        else:
            outbound = 'type ii ionic compound'
    
    
    print('')
    print(outbound.title())
