## Itertools library
import itertools

## this library contains several functions that are useful in functional programming!

## Count - counts infinitely up from a value
for i in itertools.count(3):
    print(i)
    if i>=11:
        break


## Cycle - infinitely iterates through an interable (list or string)
## Repeat - repeats an object, either infinitely or a specific number of times

## takewhile - takes items from an iterable while a predicate function remains true
## chain - combines several iterables into a long one
## accumulate - returns a running total of values in an iterable

nums = list(itertools.accumulate(range(8)))
print(nums)
ret = list(itertools.takewhile(lambda x: x <= 6, nums))
print(ret)

## itertools also has several combinatoric functions:
## `product` & `permutations`

letters = ("A", "B", "C")
print(list(itertools.product(letters, range(2))))
print(list(itertools.permutations(letters)))