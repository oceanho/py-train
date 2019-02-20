#!/usr/bin/env python3
#
#
# reference: https://eastlakeside.gitbooks.io/interpy-zh/content/Comprehensions/list-comprehensions.html
#

def list_comprehensions():
    odd_nums = [num for num in range(0,100) if num%2 != 0]
    print("1 - 100 odd number list is, type(odd_nums)={}".format(type(odd_nums)), odd_nums)
    odd_num_indexs = [ "index:" + str(i) + "  value:" + str(v) for i, v in enumerate(odd_nums) ]
    print(odd_num_indexs)

def dict_comprehensions():
    old_dict = { "id":1000, "name":"ocean" }
    new_dict = { str(v): k for k, v in old_dict.items()}
    print(new_dict)

def set_comprehensions():
    old_set = { 1000, 2000, 3000 }
    new_set = { item for item in old_set}
    print(new_set)

def set_comprehensions_for_enumerate():
    old_set = { 1000, 2000, 3000 }
    new_dict_index_value = { index:v for index, v in enumerate(old_set) }
    print(new_dict_index_value)

list_comprehensions()
dict_comprehensions()
set_comprehensions()
set_comprehensions_for_enumerate()