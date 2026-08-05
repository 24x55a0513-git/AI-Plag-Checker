# Read the number of elements
n = int(input())

# Read the array
nums = list(map(int, input().split()))

# Initialize candidate and count
candidate = None
count = 0

# Boyer-Moore Voting Algorithm
for num in nums:
    if count == 0:
        candidate = num

    if num == candidate:
        count += 1
    else:
        count -= 1

# Print the majority element
print(candidate)
