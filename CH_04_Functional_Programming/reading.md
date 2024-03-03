# Table of Contents

- [Table of Contents](#table-of-contents)
- [Overview](#overview)
  - [Key Concepts in Functional Programming:](#key-concepts-in-functional-programming)
  - [Functional Programming Tools in Python:](#functional-programming-tools-in-python)
  - [Benefits of Functional Programming in Python:](#benefits-of-functional-programming-in-python)
- [Examples](#examples)
    - [Lambda Functions:](#lambda-functions)
    - [`map`:](#map)
    - [`filter`:](#filter)
    - [`reduce` (Requires `functools` import in Python 3):](#reduce-requires-functools-import-in-python-3)
    - [List Comprehensions:](#list-comprehensions)
    - [Generators:](#generators)
  - [Dict Comprehensions:](#dict-comprehensions)
    - [Basic Dict Comprehension:](#basic-dict-comprehension)
    - [Filtering with Dict Comprehension:](#filtering-with-dict-comprehension)
  - [Set Comprehensions:](#set-comprehensions)
    - [Basic Set Comprehension:](#basic-set-comprehension)
    - [Filtering with Set Comprehension:](#filtering-with-set-comprehension)
- [When using?](#when-using)
- [list comprehensions](#list-comprehensions-1)
  - [Basic List Comprehension Syntax:](#basic-list-comprehension-syntax)
  - [Example 1: Squaring Numbers:](#example-1-squaring-numbers)
  - [Filtering with List Comprehension:](#filtering-with-list-comprehension)
  - [Multiple Expressions and Nested List Comprehensions:](#multiple-expressions-and-nested-list-comprehensions)
  - [Benefits of List Comprehensions:](#benefits-of-list-comprehensions)
  - [Potential Downsides:](#potential-downsides)
- [dict comprehensions](#dict-comprehensions-1)
  - [Basic Dict Comprehension Syntax:](#basic-dict-comprehension-syntax)
  - [Example 1: Creating a Dictionary of Squares:](#example-1-creating-a-dictionary-of-squares)
  - [Filtering with Dict Comprehension:](#filtering-with-dict-comprehension-1)
  - [Multiple Expressions and Nested Dict Comprehensions:](#multiple-expressions-and-nested-dict-comprehensions)
  - [Benefits of Dict Comprehensions:](#benefits-of-dict-comprehensions)
  - [Potential Downsides:](#potential-downsides-1)
- [set comprehensions](#set-comprehensions-1)
  - [Basic Set Comprehension Syntax:](#basic-set-comprehension-syntax)
  - [Example 1: Creating a Set of Unique Vowels:](#example-1-creating-a-set-of-unique-vowels)
  - [Filtering with Set Comprehension:](#filtering-with-set-comprehension-1)
  - [Benefits of Set Comprehensions:](#benefits-of-set-comprehensions)
  - [Potential Downsides:](#potential-downsides-2)
- [lambda functions](#lambda-functions-1)
  - [Basic Lambda Function Syntax:](#basic-lambda-function-syntax)
  - [Example 1: Creating a Simple Lambda Function:](#example-1-creating-a-simple-lambda-function)
  - [Use Cases for Lambda Functions:](#use-cases-for-lambda-functions)
  - [Limitations of Lambda Functions:](#limitations-of-lambda-functions)
  - [When to Use Lambda Functions:](#when-to-use-lambda-functions)
- [Mathematics behind lambda function](#mathematics-behind-lambda-function)
  - [Lambda Calculus Basics:](#lambda-calculus-basics)
  - [Recursive Functions in Lambda Calculus:](#recursive-functions-in-lambda-calculus)
  - [The Y Combinator:](#the-y-combinator)
  - [Using the Y Combinator for Recursion:](#using-the-y-combinator-for-recursion)
- [functools.partial](#functoolspartial)
  - [Basic `functools.partial` Usage:](#basic-functoolspartial-usage)
  - [Example: Using `functools.partial` to Create a Customized Function:](#example-using-functoolspartial-to-create-a-customized-function)
  - [Complex Example: Using `functools.partial` in a Real-World Scenario:](#complex-example-using-functoolspartial-in-a-real-world-scenario)
- [functools.partial examples](#functoolspartial-examples)
  - [Creating customized functions](#creating-customized-functions)
  - [Creating a heap using `functools.partial`](#creating-a-heap-using-functoolspartial)
- [functools.reduce](#functoolsreduce)
  - [Basic `functools.reduce` Syntax:](#basic-functoolsreduce-syntax)
  - [Example 1: Summing a List of Numbers:](#example-1-summing-a-list-of-numbers)
  - [Example 2: Finding the Maximum Value in a List:](#example-2-finding-the-maximum-value-in-a-list)
  - [Example 3: Calculating the Factorial of a Number:](#example-3-calculating-the-factorial-of-a-number)
  - [Handling Initializer:](#handling-initializer)
- [itertools accumulate](#itertools-accumulate)
  - [Basic `itertools.accumulate` Syntax:](#basic-itertoolsaccumulate-syntax)
  - [Example 1: Summing a List of Numbers:](#example-1-summing-a-list-of-numbers-1)
  - [Example 2: Finding the Running Maximum:](#example-2-finding-the-running-maximum)
  - [Example 3: Custom Accumulation:](#example-3-custom-accumulation)
- [itertools chain](#itertools-chain)
  - [Basic `itertools.chain` Syntax:](#basic-itertoolschain-syntax)
  - [Example 1: Combining Lists:](#example-1-combining-lists)
  - [Example 2: Combining Multiple Iterables:](#example-2-combining-multiple-iterables)
- [itertool combinations](#itertool-combinations)
  - [Basic `itertools.combinations` Syntax:](#basic-itertoolscombinations-syntax)
  - [Example 1: Generating Combinations from a List:](#example-1-generating-combinations-from-a-list)
  - [Example 2: Generating Combinations from a String:](#example-2-generating-combinations-from-a-string)
  - [Example 3: Generating Combinations of a Different Length:](#example-3-generating-combinations-of-a-different-length)
- [itertools.combinations Extends](#itertoolscombinations-extends)
  - [Combinations with Tuples:](#combinations-with-tuples)
  - [Combinations with Sets:](#combinations-with-sets)
  - [Combinations with Dictionaries:](#combinations-with-dictionaries)
  - [Combinations of Multiple Iterables:](#combinations-of-multiple-iterables)
- [itertool compress](#itertool-compress)
  - [Basic `itertools.compress` Syntax:](#basic-itertoolscompress-syntax)
  - [Example 1: Filtering Elements with `itertools.compress`:](#example-1-filtering-elements-with-itertoolscompress)
  - [Example 2: Filtering Numbers with `itertools.compress`:](#example-2-filtering-numbers-with-itertoolscompress)
  - [Example 3: Filtering Characters in a String:](#example-3-filtering-characters-in-a-string)
- [itertool dropwhile/takewhile](#itertool-dropwhiletakewhile)
  - [`itertools.dropwhile` Function:](#itertoolsdropwhile-function)
  - [Example 1: Using `itertools.dropwhile`:](#example-1-using-itertoolsdropwhile)
  - [`itertools.takewhile` Function:](#itertoolstakewhile-function)
  - [Example 2: Using `itertools.takewhile`:](#example-2-using-itertoolstakewhile)
- [itertool count](#itertool-count)
  - [Basic `itertools.count` Syntax:](#basic-itertoolscount-syntax)
  - [Example 1: Generating an Infinite Sequence of Numbers:](#example-1-generating-an-infinite-sequence-of-numbers)
  - [Example 2: Generating a Sequence with a Custom Step:](#example-2-generating-a-sequence-with-a-custom-step)
- [itertool islice](#itertool-islice)
  - [Basic `itertools.islice` Syntax:](#basic-itertoolsislice-syntax)
  - [Example 1: Slicing a List-Like Iterable:](#example-1-slicing-a-list-like-iterable)
  - [Example 2: Slicing a String:](#example-2-slicing-a-string)
  - [Example 3: Slicing with a Step:](#example-3-slicing-with-a-step)

# Overview

- A [programming paradigm](https://en.wikipedia.org/wiki/Programming_paradigm) that treats computation as the evaluation of mathematical functions and avoids changing state and mutable data. 
- In Python, functional programming is supported but not enforced, as Python is a multi-paradigm language.

## Key Concepts in Functional Programming:

1. **First-Class and Higher-Order Functions:**
   - Functions in Python are first-class citizens, which means they can be assigned to variables, passed as arguments to other functions, and returned as values from other functions.
   - Higher-order functions are functions that take other functions as arguments or return functions as results.

2. **Pure Functions:**
   - Pure functions have two key properties:
     - They always produce the same output for the same input (deterministic).
     - They have no side effects, meaning they do not modify any external state or data.

3. **Immutability:**
   - In functional programming, data is typically immutable, which means once a data structure is created, it cannot be changed. Instead, new data structures are created with modifications.

4. **Referential Transparency:**
   - Referential transparency means that a function call can be replaced with its result without changing the program's behavior.

5. **Avoiding Loops:**
   - In functional programming, iteration is often done using recursion or higher-order functions like `map`, `filter`, and `reduce`, rather than explicit loops.

## Functional Programming Tools in Python:

1. **Lambda Functions:**
   - Lambda functions (anonymous functions) allow you to create small, throwaway functions without a formal `def` statement.

2. **`map`, `filter`, and `reduce`:**
   - These built-in functions are commonly used in functional programming:
     - `map(function, iterable)` applies a function to each item in an iterable.
     - `filter(function, iterable)` filters items from an iterable based on a function's condition.
     - `reduce(function, iterable)` accumulates values from an iterable using a function.

3. **`functools` Module:**
   - The `functools` module provides tools for working with functions and higher-order functions. It includes features like memoization (caching function results) and function composition.

4. **List Comprehensions:**
   - List comprehensions provide a concise way to create lists based on existing lists, applying functions to each element.

5. **Generators and Iterators:**
   - Generators and iterators enable lazy evaluation and allow you to work with potentially infinite sequences of data.

6. **`itertools` Module:**
   - The `itertools` module offers a collection of functions for creating iterators and working with them efficiently.

## Benefits of Functional Programming in Python:

1. **Readability and Maintainability:**
   - Functional code tends to be more concise and easier to read, as it focuses on expressing what should be done rather than how it should be done.

2. **Predictability:**
   - Pure functions lead to more predictable behavior, making debugging and testing easier.

3. **Parallelism and Concurrency:**
   - Functional code is often more amenable to parallel and concurrent processing because it avoids shared mutable state.

4. **Reusable and Testable:**
   - Functional components are typically more modular and reusable, which promotes easier testing and code organization.

5. **Mathematical Abstractions:**
   - Functional programming aligns closely with mathematical concepts, making it suitable for mathematical modeling and certain problem domains.

6. **Functional Libraries:**
   - Python has several functional libraries like `numpy`, `pandas`, and `itertools` that provide functional-style tools for data manipulation and processing.

# Examples

### Lambda Functions:

```python
# Lambda function to square a number
square = lambda x: x**2
result = square(5)
print(result)  # Output: 25
```

### `map`:

```python
# Using map to double each element in a list
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # Output: [2, 4, 6, 8, 10]
```

### `filter`:

```python
# Using filter to find even numbers in a list
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]
```

### `reduce` (Requires `functools` import in Python 3):

```python
from functools import reduce

# Using reduce to find the product of elements in a list
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120
```

### List Comprehensions:

```python
# Using list comprehension to create a list of squares
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)  # Output: [1, 4, 9, 16, 25]
```

### Generators:

```python
# Using a generator to create an infinite sequence of even numbers
def even_numbers():
    n = 0
    while True:
        yield n
        n += 2

# Create a generator object
evens = even_numbers()

# Print the first 5 even numbers
for _ in range(5):
    print(next(evens))
# Output: 0, 2, 4, 6, 8
```

## Dict Comprehensions:

### Basic Dict Comprehension:

```python
# Creating a dictionary of squares using a dict comprehension
numbers = [1, 2, 3, 4, 5]
squares = {x: x**2 for x in numbers}
print(squares)
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### Filtering with Dict Comprehension:

```python
# Creating a dictionary of squares only for even numbers using a dict comprehension
numbers = [1, 2, 3, 4, 5]
squares = {x: x**2 for x in numbers if x % 2 == 0}
print(squares)
# Output: {2: 4, 4: 16}
```

## Set Comprehensions:

### Basic Set Comprehension:

```python
# Creating a set of unique vowels using a set comprehension
text = "hello world"
vowels = {char for char in text if char in "aeiou"}
print(vowels)
# Output: {'e', 'o'}
```

### Filtering with Set Comprehension:

```python
# Creating a set of unique even numbers from a list using a set comprehension
numbers = [1, 2, 3, 4, 5]
evens = {x for x in numbers if x % 2 == 0}
print(evens)
# Output: {2, 4}
```

# When using?

- You should not always use functional programming, as it is just one of several programming paradigms available in Python. 
- The choice of whether to use functional programming depends on the specific requirements of your project and the problem you are trying to solve. 
- Here are some considerations for when to use functional programming:

1. **Data Transformation and Processing:** Functional programming is well-suited for tasks that involve transforming or processing data. Functions like `map`, `filter`, and `reduce` can simplify data manipulation.

2. **Parallelism and Concurrency:** Functional programming can make it easier to reason about and implement parallel and concurrent algorithms, as it avoids shared mutable state.

3. **Immutable Data:** When you need to ensure that data remains unchanged after creation, functional programming's emphasis on immutability can be beneficial.

4. **Mathematical and Algorithmic Problems:** Functional programming aligns closely with mathematical concepts and can be a natural fit for solving mathematical and algorithmic problems.

5. **Functional Libraries:** If you are using libraries or frameworks that encourage or require functional programming, such as NumPy or Pandas for data analysis, then adopting functional programming practices may be beneficial.

6. **Code Clarity and Maintainability:** In some cases, functional programming can lead to more concise and self-explanatory code, making it easier to maintain and debug.

7. **Testing:** Pure functions in functional programming are easier to test since they have no side effects, which simplifies unit testing.

However, there are situations where functional programming may not be the best choice:

1. **Performance:** In some cases, functional programming can introduce overhead due to the creation of new data structures instead of modifying existing ones. This can impact performance-critical applications.

2. **Complex State Management:** If your application relies heavily on complex state management, object-oriented programming or other paradigms may be more suitable.

3. **Team Familiarity:** If your development team is more experienced with other programming paradigms, it may be more efficient to stick with what they are comfortable with.

4. **Project Constraints:** The choice of programming paradigm may also depend on project constraints and requirements, such as legacy code compatibility or integration with existing systems.

# list comprehensions

- A concise and expressive way to create lists in Python. 
- They allow you to generate a new list by applying an expression to each item in an iterable (e.g., a list, tuple, or range) and optionally filtering items based on a condition. 
- List comprehensions are a Pythonic way to replace explicit loops when creating lists.

## Basic List Comprehension Syntax:

The basic syntax of a list comprehension consists of the following parts:

```python
new_list = [expression for item in iterable]
```

- `new_list`: The resulting list.
- `expression`: The operation or transformation applied to each item in the iterable.
- `item`: A variable that represents each element in the iterable.
- `iterable`: The source of data, such as a list or range.

## Example 1: Squaring Numbers:

```python
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
# Result: [1, 4, 9, 16, 25]
```

## Filtering with List Comprehension:

You can add a conditional statement to filter items before they are included in the new list.

```python
numbers = [1, 2, 3, 4, 5]
even_numbers = [x for x in numbers if x % 2 == 0]
# Result: [2, 4]
```

## Multiple Expressions and Nested List Comprehensions:

List comprehensions can include multiple expressions and even be nested within each other.

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [x for row in matrix for x in row]
# Result: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Benefits of List Comprehensions:

1. **Conciseness:** List comprehensions provide a more compact and readable way to create lists compared to explicit loops.

2. **Readability:** They make the code more self-explanatory, as the intent (what you want to create) is separated from the implementation (how you create it).

3. **Performance:** In many cases, list comprehensions can be faster than equivalent explicit loops.

## Potential Downsides:

1. **Complexity:** List comprehensions can become hard to read and understand when they involve complex expressions or multiple conditional statements.

2. **Limited to Lists:** While list comprehensions are powerful for creating lists, they are not suitable for other data structures like dictionaries or sets.

# dict comprehensions

- like list comprehensions, provide a concise and expressive way to create dictionaries in Python. 
- They allow you to generate a new dictionary by specifying key-value pairs in a single line of code.

## Basic Dict Comprehension Syntax:

The basic syntax of a dict comprehension consists of the following parts:

```python
new_dict = {key_expression: value_expression for item in iterable}
```

- `new_dict`: The resulting dictionary.
- `key_expression`: The operation or transformation applied to each item in the iterable to generate keys.
- `value_expression`: The operation or transformation applied to each item in the iterable to generate values.
- `item`: A variable that represents each element in the iterable.
- `iterable`: The source of data, such as a list, tuple, or range.

## Example 1: Creating a Dictionary of Squares:

```python
numbers = [1, 2, 3, 4, 5]
squares_dict = {x: x**2 for x in numbers}
# Result: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

## Filtering with Dict Comprehension:

You can add a conditional statement to filter items before they are included in the new dictionary.

```python
numbers = [1, 2, 3, 4, 5]
even_squares_dict = {x: x**2 for x in numbers if x % 2 == 0}
# Result: {2: 4, 4: 16}
```

## Multiple Expressions and Nested Dict Comprehensions:

Dict comprehensions can include multiple expressions for keys and values and can be nested within each other.

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_dict = {(i, j): matrix[i][j] for i in range(3) for j in range(3)}
# Result: {(0, 0): 1, (0, 1): 2, (0, 2): 3, (1, 0): 4, (1, 1): 5, (1, 2): 6, (2, 0): 7, (2, 1): 8, (2, 2): 9}
```

## Benefits of Dict Comprehensions:

1. **Conciseness:** Dict comprehensions provide a more compact and readable way to create dictionaries compared to explicit loops.

2. **Readability:** They make the code more self-explanatory by separating the key and value generation from the implementation details.

3. **Performance:** In many cases, dict comprehensions can be faster than equivalent explicit loops.

## Potential Downsides:

1. **Complexity:** Dict comprehensions can become less readable when they involve complex expressions or multiple conditional statements for key-value generation.

2. **Limited to Dictionaries:** While dict comprehensions are powerful for creating dictionaries, they are not suitable for creating other data structures like lists or sets.

# set comprehensions

- Like list and dict comprehensions, provide a concise and expressive way to create sets in Python. 
- They allow you to generate a new set by specifying elements in a single line of code.

## Basic Set Comprehension Syntax:

The basic syntax of a set comprehension consists of the following parts:

```python
new_set = {expression for item in iterable}
```

- `new_set`: The resulting set.
- `expression`: The operation or transformation applied to each item in the iterable.
- `item`: A variable that represents each element in the iterable.
- `iterable`: The source of data, such as a list, tuple, or range.

## Example 1: Creating a Set of Unique Vowels:

```python
text = "hello world"
vowels = {char for char in text if char in "aeiou"}
# Result: {'e', 'o'}
```

## Filtering with Set Comprehension:

You can add a conditional statement to filter items before they are included in the new set.

```python
numbers = [1, 2, 3, 4, 5]
even_numbers_set = {x for x in numbers if x % 2 == 0}
# Result: {2, 4}
```

## Benefits of Set Comprehensions:

1. **Conciseness:** Set comprehensions provide a more compact and readable way to create sets compared to explicit loops.

2. **Readability:** They make the code more self-explanatory by separating the element generation from the implementation details.

3. **Performance:** In many cases, set comprehensions can be faster than equivalent explicit loops.

## Potential Downsides:

1. **Complexity:** Set comprehensions can become less readable when they involve complex expressions or multiple conditional statements for element generation.

2. **Limited to Sets:** While set comprehensions are powerful for creating sets, they are not suitable for creating other data structures like lists or dictionaries.

# lambda functions

- Also known as anonymous functions or lambda expressions, are a concise way to create small, throwaway functions in Python. 
- They are typically used for simple operations or transformations and are defined using the `lambda` keyword. 
- Lambda functions have a compact syntax and are often used when a full function definition is unnecessary or would be overly verbose.

## Basic Lambda Function Syntax:

The basic syntax of a lambda function consists of the following parts:

```python
lambda arguments: expression
```

- `lambda`: The keyword used to define a lambda function.
- `arguments`: The input arguments or parameters of the lambda function.
- `expression`: The operation or calculation to be performed using the input arguments, and its result is returned.

## Example 1: Creating a Simple Lambda Function:

```python
# Define a lambda function that squares its input
square = lambda x: x**2
result = square(5)
# Result: 25
```

## Use Cases for Lambda Functions:

1. **Sorting:** Lambda functions are commonly used with functions like `sorted()` or `max()` to specify custom sorting or key functions.

   ```python
   students = [("Alice", 24), ("Bob", 20), ("Eve", 22)]
   students_sorted = sorted(students, key=lambda student: student[1])
   # Result: [('Bob', 20), ('Eve', 22), ('Alice', 24)]
   ```

2. **Filtering:** Lambda functions can be used with functions like `filter()` to filter items from an iterable based on a condition.

   ```python
   numbers = [1, 2, 3, 4, 5, 6]
   even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
   # Result: [2, 4, 6]
   ```

3. **Mapping:** Lambda functions are often used with functions like `map()` to apply a function to each item in an iterable.

   ```python
   numbers = [1, 2, 3, 4, 5]
   squared_numbers = list(map(lambda x: x**2, numbers))
   # Result: [1, 4, 9, 16, 25]
   ```

4. **Simple Transformations:** For small, one-off transformations, lambda functions can be more concise than defining a separate named function.

## Limitations of Lambda Functions:

Lambda functions have some limitations:

- They are limited to single expressions and cannot contain multiple statements or complex logic.
- They are typically used for small, specific tasks and are not suitable for larger functions.
- They are less readable than full function definitions when the logic is complex.

## When to Use Lambda Functions:

- Use lambda functions when you need a small, one-off function for a specific task, such as sorting, filtering, or mapping. 
- They are particularly useful when the function logic is simple and the brevity of a lambda expression enhances code readability.

# Mathematics behind lambda function

- Lambda calculus is a formal system in mathematical logic and computer science that underlies the concept of lambda functions in programming languages like Python. 
- The Y combinator is a higher-order function in lambda calculus that plays a crucial role in understanding recursion and function definitions without named functions. 
- To understand the Y combinator, it's helpful to have some background in lambda calculus and functional programming.

## Lambda Calculus Basics:

Lambda calculus is a minimalist formal system that consists of three basic elements:

1. **Variables:** Represented by symbols like `x`, `y`, or `z`.
2. **Abstractions (Lambda Abstractions):** Functions or anonymous functions represented using lambda notation like `(λx. x + 1)` which denotes a function that takes `x` as input and returns `x + 1`.
3. **Applications:** Function application, where one function is applied to another, like `(λx. x + 1)(2)` which results in `3`.

## Recursive Functions in Lambda Calculus:

In lambda calculus, defining recursive functions can be challenging because it lacks named functions. However, the Y combinator provides a way to define recursive functions using anonymous functions.

## The Y Combinator:

The Y combinator is a higher-order function that takes a function `f` as an argument and returns a fixed point of `f`, which is a value `x` such that `f(x) = x`. In other words, the Y combinator finds the result of applying a function to itself.

The Y combinator is typically defined as follows:

```python
Y = λf. (λx. f (x x)) (λx. f (x x))
```

In this definition:
- `λf` is a lambda abstraction that takes a function `f` as an argument.
- `(λx. f (x x))` represents the function `λx. f (x x)`, which takes an argument `x` and applies `x` to itself to form `(x x)`. This is the core of the Y combinator, where `f` is applied to `(x x)`.
- `(λx. f (x x)) (λx. f (x x))` applies the function defined above to itself, resulting in the fixed point of `f`.

## Using the Y Combinator for Recursion:

The Y combinator can be used to define recursive functions in lambda calculus. 

```python
factorial = Y(λf. λn. if (n == 0) then 1 else n * f(n - 1))
```

# functools.partial

- A Python function that allows you to create a new function by fixing a certain number of arguments of an existing function, effectively "partial" application. 
- It's useful when you want to create a simplified version of a function with some arguments pre-set.

## Basic `functools.partial` Usage:

The `functools.partial` function takes at least two arguments: the original function and one or more positional or keyword arguments to "fix" or "freeze." The resulting function can be called with the remaining arguments.

```python
from functools import partial

new_func = partial(original_func, arg1, arg2, ...)
```

- `new_func`: The new function with some arguments pre-set.
- `original_func`: The original function to be partially applied.
- `arg1`, `arg2`, ...: Arguments from the original function to be fixed.

## Example: Using `functools.partial` to Create a Customized Function:

Let's say we have a function `calculate` that performs a complex mathematical calculation, and we want to create a simplified version of it by fixing one of the arguments:

```python
def calculate(a, b, c):
    return a * b + c

# Create a partial function with 'a' fixed as 2
custom_calculate = partial(calculate, 2)

# Now, 'custom_calculate' is equivalent to a function 'calculate' with 'a' fixed as 2
result = custom_calculate(3, 4)
# Result: 2 * 3 + 4 = 10
```

## Complex Example: Using `functools.partial` in a Real-World Scenario:

Let's use `functools.partial` in a more complex real-world scenario involving a hypothetical function for calculating the total cost of a shopping cart with discounts for specific items.

```python
from functools import partial

def calculate_total_cost(cart, discount_rate, apply_discount):
    total = sum(item['price'] for item in cart)
    if apply_discount:
        total *= (1 - discount_rate)
    return total

# Create partial functions with different discount rates
apply_10_percent_discount = partial(calculate_total_cost, discount_rate=0.10, apply_discount=True)
apply_20_percent_discount = partial(calculate_total_cost, discount_rate=0.20, apply_discount=True)

# Shopping cart
shopping_cart = [
    {'item': 'item1', 'price': 10},
    {'item': 'item2', 'price': 20},
    {'item': 'item3', 'price': 30},
]

# Calculate total cost with different discounts
total_cost_10_percent = apply_10_percent_discount(shopping_cart)
total_cost_20_percent = apply_20_percent_discount(shopping_cart)

print(f"Total cost with 10% discount: ${total_cost_10_percent}")
print(f"Total cost with 20% discount: ${total_cost_20_percent}")
```

In this complex example, we use `functools.partial` to create two partial functions, `apply_10_percent_discount` and `apply_20_percent_discount`, with different discount rates. We then apply these partial functions to the shopping cart to calculate the total cost with different discounts.

# functools.partial examples

## Creating customized functions

- `functools.partial` can be used effectively to create customized functions for use with the `heapq` module in Python. 
- The `heapq` module provides functions for creating and manipulating heaps (priority queues) in a list.
- Let's create a scenario where you have a list of tasks with priorities, and you want to use `heapq` to manage the tasks based on their priorities. 
- We'll use `functools.partial` to create a customized comparison function for the tasks based on their priorities.

```python
import heapq
from functools import partial

# Define a custom task class with a priority property
class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def __lt__(self, other):
        # Define the comparison based on priorities
        return self.priority < other.priority

# Create a list of tasks
tasks = [
    Task("Task A", 3),
    Task("Task B", 1),
    Task("Task C", 2),
]

# Define a partial function for comparing tasks based on priority
compare_tasks = partial(lambda x, y: x.priority < y.priority)

# Create a heap (priority queue) using the partial function as the comparison key
heapq.heapify(tasks, key=compare_tasks)

# Add a new task to the heap
new_task = Task("Task D", 0)
heapq.heappush(tasks, new_task)

# Pop tasks from the heap (in priority order)
while tasks:
    task = heapq.heappop(tasks)
    print(f"Task: {task.name}, Priority: {task.priority}")
```

## Creating a heap using `functools.partial` 

to customize the comparison function. Unfortunately, creating a heap directly with `functools.partial` isn't a common approach because the `heapq` module relies on standard comparison functions (e.g., `<` and `>` operators) rather than key functions.

However, you can achieve a similar effect by creating a custom heap class that uses `functools.partial` to customize the comparison function.

```python
import heapq
from functools import partial

# Create a custom heap class with a customized comparison function
class CustomHeap:
    def __init__(self, key_func):
        self.heap = []
        self.key_func = key_func

    def push(self, item):
        heapq.heappush(self.heap, item)

    def pop(self):
        return heapq.heappop(self.heap)

    def peek(self):
        if self.heap:
            return self.heap[0]

    def __len__(self):
        return len(self.heap)

# Define a comparison function using functools.partial
priority_key = partial(lambda task: task.priority)

# Create a custom heap with the customized comparison function
custom_heap = CustomHeap(key_func=priority_key)

# Add tasks to the custom heap
custom_heap.push(Task("Task A", 3))
custom_heap.push(Task("Task B", 1))
custom_heap.push(Task("Task C", 2))

# Pop tasks from the custom heap (in priority order)
while len(custom_heap) > 0:
    task = custom_heap.pop()
    print(f"Task: {task.name}, Priority: {task.priority}")
```

# functools.reduce

- A built-in Python function that allows you to apply a **binary function** (a function that takes two arguments) cumulatively to the items of an iterable, from left to right, reducing the iterable to a single accumulated result. 
- It is often used to perform operations like **summation**, **product** calculation, finding the **maximum** or **minimum** value, or any other **binary operation** that combines elements sequentially.

## Basic `functools.reduce` Syntax:

The basic syntax of `functools.reduce` is as follows:

```python
functools.reduce(function, iterable[, initializer])
```

- `function`: The binary function to be applied cumulatively to the items of the iterable. It should take two arguments and return a single result.
- `iterable`: The iterable (e.g., a list, tuple, or string) whose elements will be reduced cumulatively.
- `initializer` (optional): An optional initial value for the reduction. If provided, the reduction starts with this initial value; otherwise, the first two elements of the iterable are used.

## Example 1: Summing a List of Numbers:

```python
import functools

numbers = [1, 2, 3, 4, 5]
sum_result = functools.reduce(lambda x, y: x + y, numbers)
# Result: 15 (1 + 2 + 3 + 4 + 5)
```

## Example 2: Finding the Maximum Value in a List:

```python
import functools

numbers = [3, 6, 1, 8, 4, 7]
max_result = functools.reduce(lambda x, y: x if x > y else y, numbers)
# Result: 8 (maximum value in the list)
```

## Example 3: Calculating the Factorial of a Number:

```python
import functools

def factorial(x, y):
    return x * y

n = 5
factorial_result = functools.reduce(factorial, range(1, n + 1))
# Result: 120 (5! = 5 * 4 * 3 * 2 * 1 = 120)
```

## Handling Initializer:

You can provide an optional `initializer` as the third argument to `functools.reduce`. If provided, the reduction starts with this initial value. For example:

```python
import functools

numbers = [1, 2, 3, 4, 5]
product_result = functools.reduce(lambda x, y: x * y, numbers, 10)
# Result: 1200 (10 * 1 * 2 * 3 * 4 * 5)
```

# itertools accumulate

- A Python module that provides an iterator that performs a running (cumulative) calculation on an iterable. 
- It is similar to `functools.reduce`, but instead of producing a single result at the end, it yields the intermediate results at each step of the iteration. 
- `itertools.accumulate` is useful when you want to see the cumulative effect of a binary operation applied to the elements of an iterable. 

## Basic `itertools.accumulate` Syntax:

The basic syntax of `itertools.accumulate` is as follows:

```python
itertools.accumulate(iterable, func=operator.add)
```

- `iterable`: The input iterable whose elements will be used in the cumulative calculation.
- `func` (optional): The binary function (e.g., `operator.add`, `operator.mul`, or a custom function) used for the cumulative calculation. It defaults to addition (`operator.add`).

## Example 1: Summing a List of Numbers:

```python
import itertools

numbers = [1, 2, 3, 4, 5]
cumulative_sum = itertools.accumulate(numbers)
# Result: [1, 3, 6, 10, 15]
```

## Example 2: Finding the Running Maximum:

```python
import itertools

numbers = [3, 6, 1, 8, 4, 7]
running_max = itertools.accumulate(numbers, max)
# Result: [3, 6, 6, 8, 8, 8]
```

## Example 3: Custom Accumulation:

```python
import itertools

def custom_accumulate(a, b):
    return a * 2 + b

numbers = [1, 2, 3, 4, 5]
custom_result = itertools.accumulate(numbers, custom_accumulate)
# Result: [1, 4, 11, 26, 57]
```

# itertools chain

- A Python module that provides an iterator for flattening (combining) multiple iterables into a single iterable. 
- It allows you to iterate over the elements of multiple sequences as if they were a single sequence. 
- This is useful when you have multiple iterables to process sequentially without creating a new combined data structure.

## Basic `itertools.chain` Syntax:

The basic syntax of `itertools.chain` is as follows:

```python
itertools.chain(iterable1, iterable2, ...)
```

- `iterable1`, `iterable2`, ...: The input iterables that you want to combine into a single iterable.

## Example 1: Combining Lists:

```python
import itertools

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
combined_iterable = itertools.chain(list1, list2)
# Result: [1, 2, 3, 'a', 'b', 'c']
```

## Example 2: Combining Multiple Iterables:

```python
import itertools

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
colors = ('red', 'green', 'blue')
combined_iterable = itertools.chain(numbers, letters, colors)
# Result: [1, 2, 3, 'a', 'b', 'c', 'red', 'green', 'blue']
```

# itertool combinations

- A Python module that provides an iterator for generating combinations of elements from an iterable, taken `r` at a time, without repetition. 
- Combinations are subsets of a given iterable where the order of elements does not matter. 
- This is useful for tasks like finding all possible combinations of elements for a given length, such as selecting items for a team or generating permutations.

## Basic `itertools.combinations` Syntax:

The basic syntax of `itertools.combinations` is as follows:

```python
itertools.combinations(iterable, r)
```

- `iterable`: The input iterable from which combinations are generated.
- `r`: The length of each combination.

## Example 1: Generating Combinations from a List:

```python
import itertools

colors = ['red', 'green', 'blue']
combinations = itertools.combinations(colors, 2)
# Result: [('red', 'green'), ('red', 'blue'), ('green', 'blue')]
```

## Example 2: Generating Combinations from a String:

```python
import itertools

text = 'abc'
combinations = itertools.combinations(text, 2)
# Result: [('a', 'b'), ('a', 'c'), ('b', 'c')]
```

## Example 3: Generating Combinations of a Different Length:

```python
import itertools

numbers = [1, 2, 3, 4]
combinations = itertools.combinations(numbers, 3)
# Result: [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
```

# itertools.combinations Extends

- `itertools.combinations` can be used with any iterable, including tuples, sets, and dictionaries, as long as the elements of the iterable are hashable. 
- However, it's important to note that the elements themselves are treated as values, and order does not matter in combinations.

## Combinations with Tuples:

```python
import itertools

tuple_example = (1, 2, 3, 4)
combinations = itertools.combinations(tuple_example, 2)
# Result: [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
```

## Combinations with Sets:

```python
import itertools

set_example = {'a', 'b', 'c'}
combinations = itertools.combinations(set_example, 2)
# Result: [('a', 'b'), ('a', 'c'), ('b', 'c')]
```

## Combinations with Dictionaries:

You can use `itertools.combinations` with dictionaries, but keep in mind that dictionaries are not ordered in Python versions before Python 3.7. Starting from Python 3.7, dictionaries are guaranteed to maintain insertion order.

```python
import itertools

dict_example = {'name': 'Alice', 'age': 30, 'city': 'New York'}
combinations = itertools.combinations(dict_example, 2)
# Result: [('name', 'age'), ('name', 'city'), ('age', 'city')]
```

## Combinations of Multiple Iterables:

You can also generate combinations of elements from multiple iterables, such as lists or tuples.

```python
import itertools

list1 = [1, 2]
list2 = ['a', 'b']
combinations = itertools.combinations(list1 + list2, 3)
# Result: [(1, 2, 'a'), (1, 2, 'b')]
```

You can use a similar approach with `zip` to generate combinations from multiple sequences:

```python
import itertools

sequence1 = [1, 2, 3]
sequence2 = ['a', 'b', 'c']
combinations = itertools.combinations(zip(sequence1, sequence2), 2)
# Result: [((1, 'a'), (2, 'b')), ((1, 'a'), (3, 'c')), ((2, 'b'), (3, 'c'))]
```

`itertools.combinations` is a versatile tool for generating combinations from various types of iterables, and you can use it with multiple iterables as needed.

# itertool compress

- A Python module that provides an iterator for filtering elements from an iterable based on the values in a corresponding selector iterable. 
- It returns an iterator that yields only those elements from the input iterable for which the corresponding element in the selector iterable is `True`. 
- This allows you to filter elements conditionally from one iterable based on another iterable's truth values.

## Basic `itertools.compress` Syntax:

The basic syntax of `itertools.compress` is as follows:

```python
itertools.compress(data, selectors)
```

- `data`: The input iterable from which elements are selected or filtered.
- `selectors`: The selector iterable containing truth values that determine whether elements from `data` are included in the output.

## Example 1: Filtering Elements with `itertools.compress`:

```python
import itertools

data = ['a', 'b', 'c', 'd', 'e']
selectors = [True, False, True, False, True]

filtered_data = itertools.compress(data, selectors)
# Result: ['a', 'c', 'e']
```

## Example 2: Filtering Numbers with `itertools.compress`:

```python
import itertools

numbers = [1, 2, 3, 4, 5]
selectors = [True, False, True, False, True]

filtered_numbers = itertools.compress(numbers, selectors)
# Result: [1, 3, 5]
```

## Example 3: Filtering Characters in a String:

```python
import itertools

text = 'abcdef'
selectors = [True, False, True, False, True, False]

filtered_text = ''.join(itertools.compress(text, selectors))
# Result: 'ace'
```

# itertool dropwhile/takewhile

`itertools.dropwhile` and `itertools.takewhile` are two Python modules that provide iterators for filtering elements from an iterable based on a specified condition. These functions allow you to control which elements are included in the output by specifying a predicate function. Here are the details of `itertools.dropwhile` and `itertools.takewhile`:

## `itertools.dropwhile` Function:

- `itertools.dropwhile` drops elements from the beginning of an iterable as long as a specified condition (predicate) is `True`. 
- Once the condition becomes `False` for the first time, it includes all the remaining elements. 

```python
itertools.dropwhile(predicate, iterable)
```

- `predicate`: A function that takes an element from the iterable as an argument and returns `True` or `False` based on a condition.
- `iterable`: The input iterable from which elements are filtered.

## Example 1: Using `itertools.dropwhile`:

```python
import itertools

numbers = [1, 3, 5, 2, 4, 6]
filtered_numbers = itertools.dropwhile(lambda x: x < 4, numbers)
# Result: [5, 2, 4, 6]
```

## `itertools.takewhile` Function:

- `itertools.takewhile` returns elements from the beginning of an iterable as long as a specified condition (predicate) is `True`. 
- Once the condition becomes `False` for the first time, it stops including elements. 

```python
itertools.takewhile(predicate, iterable)
```

- `predicate`: A function that takes an element from the iterable as an argument and returns `True` or `False` based on a condition.
- `iterable`: The input iterable from which elements are filtered.

## Example 2: Using `itertools.takewhile`:

```python
import itertools

numbers = [1, 3, 5, 2, 4, 6]
filtered_numbers = itertools.takewhile(lambda x: x < 4, numbers)
# Result: [1, 3]
```

# itertool count

- A Python module that provides an iterator for generating an infinite sequence of numbers, starting from a specified start value and incremented by a specified step value. 
- It is a simple but powerful tool for creating iterators that produce an unbounded sequence of numbers. 

## Basic `itertools.count` Syntax:

The basic syntax of `itertools.count` is as follows:

```python
itertools.count(start=0, step=1)
```

- `start` (optional): The initial value of the counter. It defaults to 0 if not provided.
- `step` (optional): The value by which the counter is incremented on each iteration. It defaults to 1 if not provided.

## Example 1: Generating an Infinite Sequence of Numbers:

```python
import itertools

# Generate an infinite sequence of numbers starting from 1
counter = itertools.count(start=1)

# Generate the first 5 numbers in the sequence
numbers = [next(counter) for _ in range(5)]
# Result: [1, 2, 3, 4, 5]
```

## Example 2: Generating a Sequence with a Custom Step:

```python
import itertools

# Generate a sequence of even numbers starting from 0 with a step of 2
even_counter = itertools.count(start=0, step=2)

# Generate the first 5 even numbers in the sequence
even_numbers = [next(even_counter) for _ in range(5)]
# Result: [0, 2, 4, 6, 8]
```

# itertool islice

- A Python module that provides a way to slice or extract a portion of elements from an iterable, similar to how Python's built-in `slice` notation works for lists and strings. 
- It allows you to create an iterator that produces elements from an iterable within a specified range or slice.

## Basic `itertools.islice` Syntax:

The basic syntax of `itertools.islice` is as follows:

```python
itertools.islice(iterable, start, stop, step=1)
```

- `iterable`: The input iterable from which elements are sliced.
- `start`: The index at which to start slicing (inclusive).
- `stop`: The index at which to stop slicing (exclusive).
- `step` (optional): The step size or increment for slicing. It defaults to 1 if not provided.

## Example 1: Slicing a List-Like Iterable:

```python
import itertools

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
slice_result = itertools.islice(data, 2, 7)
# Result: [3, 4, 5, 6, 7]
```

## Example 2: Slicing a String:

```python
import itertools

text = "Python is fun"
slice_result = itertools.islice(text, 7, 10)
# Result: 'is '
```

## Example 3: Slicing with a Step:

```python
import itertools

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
slice_result = itertools.islice(data, 1, 9, 2)
# Result: [2, 4, 6, 8]
```