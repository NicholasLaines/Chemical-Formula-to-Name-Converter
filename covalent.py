def gen_cov_com(proccessed_formula, atomic_nums, prefixes):
    import ele
    outbound = ''
    hallogen = (9,17,35,53,85,117)
    
    if 'H' in proccessed_formula:
        atomic_nums.remove(1)
        if any(item in hallogen for item in atomic_nums):
            hallogen = ele.periodic[atomic_nums[0]]
            atom_name = hallogen[3]
            outbound = 'Hydro' + atom_name + 'ic Acid'
        else:
            outbound = 'polyatomic ion acid'
    else:
        for item in atomic_nums:
            sub_tup = ele.periodic[item]
            if outbound == "":
                outbound = outbound + prefixes[atomic_nums.index(item)] + sub_tup[0] + " "
            else:
                outbound = outbound + prefixes[atomic_nums.index(item)] + sub_tup[3] + 'ide '
    
    
    print('')
    print(outbound.title())