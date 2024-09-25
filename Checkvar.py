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

keys_string = ", ".join(var.keys())       # Separate var keys with commas for a cleaner look
print("Variable names: ", keys_string)    # Give user the keys to choose from
user_check = input("Enter the name of the variable that you want to check the value of: ")

if user_check in var:
    print("Variable {} is: {}".format(user_check, var[user_check])) # Removed quotes
else:
    print("I don't know your variable!")