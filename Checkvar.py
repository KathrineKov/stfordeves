from Listvar import *
var = {
    'integer_var': integer_var,
    'float_var': float_var,
    'complex_var': complex_var,
    'string_var': string_var,
    'boolean_var': boolean_var,
    'tuple_var': tuple_var,
    'list_var': list_var,
    'dict_var': dict_var,
    'set_var': set_var
}

user_check = input("Enter the name of the variable that you want to check: ")

if user_check in var:
    print("Variable '{}' is: {}".format(user_check, var[user_check]))
else:
    print("I don't know your variable!")