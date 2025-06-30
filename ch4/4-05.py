# 4-05.py 
#make a list of numbers 1 to 1,000,000 inclusive.
million_nums = []
for i in range(1, 1_000_001):
	million_nums.append(i)

print(million_nums[0:3])
print(min(million_nums))
print(max(million_nums))

print(sum(million_nums))
print(f"Sum: {sum(million_nums):,}")