def make_set(lst):
    new_set = []
    # only appends if item isn't already in lst, avoiding duplicates
    for i in lst:
        # note "not in" rather than in
        if i not in new_set:
            new_set.append(i)
    return new_set

def inter(lst1, lst2):
    new_lst = []
    # only appends if item is found in lst2 (meaning both lists have them)
    for i in lst1:
        if i in lst2:
            new_lst.append(i)
    # removes duplicates (creates set)
    new_set = make_set(new_lst)
    return new_set

def union(lst1, lst2):
    # merges both lists together, including duplicates
    new_lst = lst1 + lst2
    # removes duplicates (creates set)
    new_set = make_set(new_lst)
    return new_set

def sym_dif(lst1, lst2):
    new_lst = []
    # only appends if item is exclusive to lst1
    for i in lst1:
        # note "not in" rather than in
        if i not in lst2: 
            new_lst.append(i)
    # only appends if item is exclusive to lst2
    for i in lst2:
        # note "not in" rather than in
        if i not in lst1: 
            new_lst.append(i)
    # removes duplicates (creates set)
    new_set = make_set(new_lst)
    return new_set