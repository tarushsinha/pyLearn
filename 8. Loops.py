## Loops - can be used to perform code on each item in a list
## each code operation on an item of the list is called an iteration

nums = [1, 2, 3, 4]
print(nums)

## if we want to square each number in nums, we can use a while loop, and a counter
numCounter = 0
while numCounter < len(nums):
    nums[numCounter] **= 2
    numCounter += 1

print(nums)

## for Loop - shortcuts for the cumbersome while loop. Think of this as the `foreach` loop in other languages
## a variation to the above while loop to square all the elements in nums -
ret = []
for num in nums:
    ret.append(num**2)
print(ret)

## for loops are commonly used to repeat code a number of times, can be combined with range objects
## unlike in 6. Control Structures.py we don't need to cast list on the range obj - because it isn't being indexed
for i in range(len(nums)):
    print(nums[i])
