print("Please enter 5 numbers (int or float) separated by spaces. For example: 10.5 20 30 40 50")
user_input = input("Enter the numbers: ")
nums = list(map(float, user_input.split()))

if len(nums) != 5:    # Check if exactly five numbers are entered in the previous step
    print("Please enter exactly five numbers")
else:
    sum = sum(nums)
    average = sum / len(nums)

    print(f"Sum of the numbers: {sum}")
    print(f"Average: {average}")