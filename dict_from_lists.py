'''1. Implement a function with two arguments, both are lists of possibly different length. The function must return dictionary 
(dict for Python or object for JS) with keys from the first list and corresponding values from the second. If a key lacks value,
resulting dictionary must contain None for that key (or null for JavaScript). Redundant values must be ignored. Keys are guaranteed to be unique.'''

def dict_from_lists(keys, values):
    my_dict = {}
    for i in range(len(keys)):
        if (i + 1) <= len(values):
            my_dict[keys[i]] = values[i]
        else:
            my_dict[keys[i]] = None
    return my_dict

'''
list1 = [1]
list2 = ['a', 'b', 'c']

list3 = [1, 2, 3]
list4 = ['a', 'b', 'c']

list5 = [1, 2, 3]
list6 = ['a']

dict_from_lists(list1, list2)
'''