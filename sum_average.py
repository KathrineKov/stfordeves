from statistics import mean, pvariance as var, median, pstdev
try:
    user_input = input("Enter the numbers separated by space: ")
    nums = [float(num) for num in user_input.split()]
    if len(nums) == 0:
        raise ValueError('No numbers, try again!')
    print(f"Sum of the numbers: {round(sum(nums), 2)}")
    print(f"Average: {round(mean(nums),2)}")
    print(f'Variance : {round(var(nums),2)}')
    print(f'Median : {round(median(nums),2)}')
    print(f'Standard deviation: {round(pstdev(nums),2)}')
except ValueError as e:
    print(e)