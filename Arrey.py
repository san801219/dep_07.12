"""" Sort odd numbers at the list"""
from typing import Any
from ast import literal_eval

def check_elem_list(array:Any):
    """Chek incoming elements"""
    if not isinstance(array,list):
        raise TypeError(f'Invalid list type : {type(array)}')


def found_odd_elements(array:list)->list:
    """ Find odd elements"""
    odd_list=sorted([odd for odd in array if odd % 2 !=0])
    return odd_list


def change_odd_list(array:list)->list:
    """ Replace the odd elements at the array on the sorted odd elements """
    odd_list=found_odd_elements(array)
    j=0
    res_list=[]
    for elem in array:
        if elem % 2 !=0:
            elem = odd_list [j]
            res_list.append(odd_list[j])
            j+=1
        else:
            res_list.append(elem)
    return res_list


def main(array:list) -> list:
    """Main controller of sorting odd elements"""
    check_elem_list(array)
    found_odd_elements(array)
    change_odd_list(array)
    res_list=change_odd_list(array)
    return res_list

if __name__ == '__main__':  
    
    array = literal_eval(input('Enter your array : '))
    
    try:
        print(main(array))
    except TypeError as error:
        print(error)