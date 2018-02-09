
def exchange_first_last(seq):
    if type(seq) is str:
        y = seq[-1] + seq[1:-1] + seq[0]
        new_string = y
        return new_string

    elif type(seq) is tuple:
        x = list(seq)
        last_item = [x[-1]]
        middle_items = x[1:-1]
        first_item = [x[0]]
        new_list = last_item + middle_items + first_item
        new_tuple = tuple(new_list)
        return new_tuple

    else:
        last_item2 = [seq[-1]]
        middle_items2 = seq[1:-1]
        first_item2 = [seq[0]]
        new_list2 = last_item2 + middle_items2 + first_item2
        return new_list2


def remove_every_other(seq):
    if type(seq) is str:
        y = seq[0::2]
        new_string = y
        return new_string

    elif type(seq) is tuple:
        x = list(seq)
        new_list = x[0::2]
        new_tuple = tuple(new_list)
        return new_tuple

    else:
        new_list2 = seq[0::2]
        return new_list2


def first_last_four_every_other_remove(seq):
    if type(seq) is str:
        y = seq[4:-4:2]
        new_string = y
        return new_string

    elif type(seq) is tuple:
        x = list(seq)
        new_list = x[4:-4:2]
        new_tuple = tuple(new_list)
        return new_tuple

    else:
        new_list2 = seq[4:-4:2]
        return new_list2


def reverse(seq):
    if type(seq) is str:
        y = seq[::-1]
        new_string = y
        return new_string

    elif type(seq) is tuple:
        x = list(seq)
        new_list = x[::-1]
        new_tuple = tuple(new_list)
        return new_tuple

    else:
        new_list2 = seq[::-1]
        return new_list2


def middle_last_first(seq):
    third = len(seq) // 3
    if type(seq) is str:
        third = len(seq)//3
        y = seq[third:-third] + seq[-third:] + seq[0:third]
        new_string = y
        return new_string

    elif type(seq) is tuple:
        x = list(seq)
        last_third = x[-third:]
        middle_third = x[third:-third]
        first_third = x[0:third]
        new_list = middle_third + last_third + first_third
        new_tuple = tuple(new_list)
        return new_tuple

    else:
        last_third2 = seq[-third:]
        middle_third2 = seq[third:-third]
        first_third2 = seq[0:third]
        new_list2 = middle_third2 + last_third2 + first_third2
        return new_list2


# Assertion Tests
string_test = "hello world"
tuple_test = (1,2,3,4,5,6,7,8,9,10,11)
list_test = [1,2,3,4,5,6,7,8,9,10,11]

assert exchange_first_last(string_test) == "dello worlh"
assert exchange_first_last(tuple_test) == (11,2,3,4,5,6,7,8,9,10,1)
assert remove_every_other(string_test) == "hlowrd"
assert remove_every_other(list_test) == [1,3,5,7,9,11]
assert first_last_four_every_other_remove(string_test) == "ow"
assert first_last_four_every_other_remove(tuple_test) == (5,7)
assert reverse(string_test) == "dlrow olleh"
assert reverse(list_test) == [11,10,9,8,7,6,5,4,3,2,1]
assert middle_last_first(tuple_test) == (4,5,6,7,8,9,10,11,1,2,3)
assert middle_last_first(list_test) == [4,5,6,7,8,9,10,11,1,2,3]



