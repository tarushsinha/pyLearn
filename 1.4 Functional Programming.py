## Functional Programming

## Style of programming based around functions
## Key part of functional programming is higher-order functions
## Recall - higher-order functions take other functions as arguments, or return them as results

import math

def apply_twice(function, arg):
    return function(function(arg))

def square(x):
    return (x * x)

print(apply_twice(square, 2))

## Functional programming seeks to use pure functions
## Pure functions - no side effects, and return a value that depends only on their arguments
## Functions in math - like cos(x) for example will (for the same value of x) always return the same result:
def pure_func(x):
    return math.cos(x)

print(pure_func(0))

## More on Pure Functions --
## -> easier to reason & test
## -> easier to run in parallel
## -> more efficient via memoization (result can be stored & referred to next time function of that input is needed)

## Lambdas, & Lambda Calculus

## creating functions normally using def assigns it to a variable automatically
## other objects can be created on the fly anonymously, and the same can be done for functions with lambda syntax

## functions created using lambdas are known as "anonymous"
## Lambda functions aren't quite as powerful as named functions (tradeoff for anonymity)
## They can only do single expression work

def my_func(f, arg):
    return f(arg)

print(my_func(lambda x: 2*x*x, 5))


## Lambda functions can be assigned to variables, and used like normal functions:
two_times = lambda x: x * 2
print(two_times(4))

## the `map` & `filter` functions
## both operate on lists or iterables -

## map takes a function & an iterable, returns a new iterable with the function applied to each arg
nums = [11, 22, 33, 44, 55]
result = list(map(two_times,nums))
print(result)

## filter takes a function & an iterable and removes items that don't match the function predicate
## return all evens using a lambda function as the function predicate
fresult = list(filter(lambda x: x%2==0, nums))
print(fresult)

## Generators are a type of iterable - just like lists or tuples
## unlike lists, they don't allow indexing, but can be iterated through with for loops
## Generators are created using functions and the yield statement

def countdown():
    i = 5
    while i > 0:
        yield i
        i -= 1

for i in countdown():
    print(i)

## Because they yield one item at a time, generators don't have memory restrictions of lists and can be infinite
## Finite generators can be converted into lists by passing them as arguments to the list function:

def numbers(x):
    for i in range(x):
        if i%2 == 0:
            yield i
print(list(numbers(11)))

## Decorators provide a means to modify functions using other functions
## ideal when you need to extend functionality without modifying

def decor(func):
  def wrap():
    print("============")
    func()
    print("============")
  return wrap

def print_text():
  print("Hello world!")

decorated = decor(print_text)
decorated()

## or - use `@` to specify the decorator symbol

def redecor(func):
    def wrap():
        print("============")
        func()
        print("============")

    return wrap

@redecor
def p_text():
    print("Hello world!")

p_text()

## Recursion - core concept in functional programming
## important concept of recursion: self-reference (aka: functions calling themselves)


## classic example of recursive function is factorial function: (5! = 5 * 4 * 3 * 2 *1 or n! = n*(n-1)!)
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(5))

## Recursion - base case: the final step in a recursive loop
## Without a functioning base case, you run into an infinite looping scenario

## Sets - Sets are data structures similar to lists or dictionaries, created using curly braces {}.
## Sets share some functionality with lists, such as the use of the `in` command to check item membership
num_set = {1, 2, 3, 4, 5}
word_set = set(["spam", "eggs", "sausage"])

print(3 in num_set)
print("spam" not in word_set)

## Sets differ from lists in many ways, but share several options such as len()
## Sets are unordered - meaning they can't be indexed, and they can't contain duplicate elements
## Instead of List.append, we use Set.add
## remove method can remove a specific element, pop removes an arbitrary element

## Sets have faster lookup than lists

nms = {1, 2, 1, 3, 1, 4, 5, 6}
print(nms)
nms.add(-7)
nms.remove(3)
print(nms)

## Mathematical operations with Sets:
## Union `|`
## Intersection `&`
## Difference `-`
## Symmetric difference `^`

l1 = {1, 2, 3, 4, 5, 6}
l2 = {4, 5, 6, 7, 8, 9}

print(l1 | l2)
print(l1 & l2)
print(l1 - l2)
print(l2 - l1)
print(l1 ^ l2)