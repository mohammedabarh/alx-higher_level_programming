#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")
            else:
                element_1 = my_list_1[i]
                element_2 = my_list_2[i]
                result.append(element_1 / element_2)

        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except TypeError:
            print("wrong type")
            result.append(0)
        except IndexError as e:
            print(e)
            result.append(0)

    return result
