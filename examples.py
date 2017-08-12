l = lambda x: x != 5

def alter(values, check):
    return [val for val in values if check(val)]

my_list = [1, 2, 3, 4, 5]


another_list = alter(my_list,l)

print("list is {}".format(another_list))


another_list = alter(my_list, lambda x: x != 2)

print("list is {}".format(another_list))

def alter2(values, check):
    return list(filter(check,values))

my_list = [ "a", "2", "c"]

def remove_numbers(value):
    return alter(value, lambda x: x not in [str(n) for n in range(10)])

print("now remove number{}".format(remove_numbers(my_list)))

