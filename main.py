nums = [34565, 1, 2, 3, 123, 42, 1423]

max_num = nums[-1]

for num in nums:
    if max_num < num:
        max_num = num

print(max_num)