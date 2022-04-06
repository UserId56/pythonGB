def get_num(nums):
    for num in nums:
        if num % 2 != 0:
            yield num

generator_num = get_num(6)

print(next(generator_num))
