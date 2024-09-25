from Listvar import *
var = {
    'integer_var': integer_var,
    'float_var': float_var,
    'boolean_var': boolean_var
}

result = integer_var + float_var
result_with_bool = integer_var + float_var + boolean_var

print("Result: ", result)
print("Result with boolean", result_with_bool)  # Add new result with bool
guess = input("Enter the value of boolean: ")   # Prompt user to guess the bool from Listvar.py

if guess == 'True':                             # Convert to bool, because I haven't found another way and bool() doesn't work
    guess_bool = True
elif guess == 'False':
    guess_bool = False
else:
    guess_bool = None
    

if guess_bool is None:                          # Respond to user guess
    print("Invalid input. Please enter True or False.")
elif guess_bool == boolean_var:
    print("Correct!")
else:
    print("Not correct.")