def add_two_numbers() -> int:
    nums = input().split(",")
    total = 0
    for num in nums:
        total += int(num)
    return total



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
