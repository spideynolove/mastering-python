# Table of Contents

- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [list](#list)
  - [Basics of Lists:](#basics-of-lists)
    - [Creating Lists:](#creating-lists)
    - [Accessing List Elements:](#accessing-list-elements)
    - [Modifying Lists:](#modifying-lists)
    - [List Operations:](#list-operations)
  - [Advanced List Operations:](#advanced-list-operations)
    - [List Comprehensions:](#list-comprehensions)
    - [Nested Lists:](#nested-lists)
    - [List Methods:](#list-methods)
    - [List Copying:](#list-copying)
  - [Advanced Applications:](#advanced-applications)
- [dict](#dict)
  - [Basics of Dictionaries:](#basics-of-dictionaries)
    - [Creating Dictionaries:](#creating-dictionaries)
    - [Accessing Dictionary Values:](#accessing-dictionary-values)
    - [Modifying Dictionaries:](#modifying-dictionaries)
  - [Advanced Dictionary Operations:](#advanced-dictionary-operations)
    - [Dictionary Comprehensions:](#dictionary-comprehensions)
    - [Nested Dictionaries:](#nested-dictionaries)
    - [Dictionary Methods:](#dictionary-methods)
    - [Handling Missing Keys:](#handling-missing-keys)
  - [Advanced Applications:](#advanced-applications-1)
- [set](#set)
  - [Basics of Sets:](#basics-of-sets)
    - [Creating Sets:](#creating-sets)
    - [Adding and Removing Elements:](#adding-and-removing-elements)
  - [Basic Set Operations:](#basic-set-operations)
  - [Advanced Set Operations:](#advanced-set-operations)
    - [Set Comprehensions:](#set-comprehensions)
    - [Frozen Sets:](#frozen-sets)
  - [Advanced Applications:](#advanced-applications-2)
- [tuple](#tuple)
  - [Basics of Tuples:](#basics-of-tuples)
    - [Creating Tuples:](#creating-tuples)
    - [Accessing Tuple Elements:](#accessing-tuple-elements)
    - [Immutable Nature:](#immutable-nature)
  - [Advanced Tuple Operations:](#advanced-tuple-operations)
    - [Tuple Packing and Unpacking:](#tuple-packing-and-unpacking)
    - [Tuple Concatenation:](#tuple-concatenation)
  - [Advanced Applications:](#advanced-applications-3)
- [ChainMap](#chainmap)
  - [Basics of ChainMap:](#basics-of-chainmap)
    - [Importing ChainMap:](#importing-chainmap)
    - [Creating a ChainMap:](#creating-a-chainmap)
    - [Accessing Values:](#accessing-values)
    - [Updating Values:](#updating-values)
  - [Advanced ChainMap Operations:](#advanced-chainmap-operations)
    - [Reversing the ChainMap:](#reversing-the-chainmap)
    - [Nested ChainMaps:](#nested-chainmaps)
    - [Creating a New ChainMap:](#creating-a-new-chainmap)
    - [Accessing Parent Maps:](#accessing-parent-maps)
  - [Advanced Applications of ChainMap:](#advanced-applications-of-chainmap)
    - [Configuration and Defaults:](#configuration-and-defaults)
    - [Context Managers:](#context-managers)
    - [Merging Dictionaries:](#merging-dictionaries)
    - [Managing Configuration Layers:](#managing-configuration-layers)
- [Counter](#counter)
  - [Basics of Counter:](#basics-of-counter)
    - [Importing Counter:](#importing-counter)
    - [Creating a Counter:](#creating-a-counter)
    - [Accessing Counts:](#accessing-counts)
    - [Counter Operations:](#counter-operations)
  - [Advanced Counter Operations:](#advanced-counter-operations)
    - [Elements and Values:](#elements-and-values)
    - [Most Common Elements:](#most-common-elements)
    - [Subtracting Counters:](#subtracting-counters)
  - [Advanced Applications of Counter:](#advanced-applications-of-counter)
    - [Word Frequency Count:](#word-frequency-count)
    - [Anagrams Detection:](#anagrams-detection)
    - [Combining Lists:](#combining-lists)
    - [Inventory Management:](#inventory-management)
    - [Finding Differences:](#finding-differences)
- [Defaultdict](#defaultdict)
  - [Basics of Defaultdict:](#basics-of-defaultdict)
    - [Importing Defaultdict:](#importing-defaultdict)
    - [Creating a Defaultdict:](#creating-a-defaultdict)
    - [Accessing Default Values:](#accessing-default-values)
  - [Advanced Defaultdict Operations:](#advanced-defaultdict-operations)
    - [Setting the Default Factory:](#setting-the-default-factory)
    - [Using Defaultdict with Nested Data Structures:](#using-defaultdict-with-nested-data-structures)
    - [Creating Defaultdict of Lists:](#creating-defaultdict-of-lists)
  - [Advanced Applications of Defaultdict:](#advanced-applications-of-defaultdict)
    - [Counting Elements:](#counting-elements)
    - [Grouping Data:](#grouping-data)
    - [Creating Sparse Matrices:](#creating-sparse-matrices)
    - [Handling Missing Data:](#handling-missing-data)
- [OrderedDict](#ordereddict)
  - [Basics of OrderedDict:](#basics-of-ordereddict)
    - [Importing OrderedDict:](#importing-ordereddict)
    - [Creating an OrderedDict:](#creating-an-ordereddict)
    - [Accessing Values:](#accessing-values-1)
    - [Maintaining Insertion Order:](#maintaining-insertion-order)
  - [Advanced OrderedDict Operations:](#advanced-ordereddict-operations)
    - [Reordering Keys:](#reordering-keys)
    - [Popping Items:](#popping-items)
  - [Advanced Applications of OrderedDict:](#advanced-applications-of-ordereddict)
    - [Preserving JSON Object Order:](#preserving-json-object-order)
    - [Ordered Configuration Settings:](#ordered-configuration-settings)
    - [Creating a Cache with Limited Size:](#creating-a-cache-with-limited-size)
    - [Ordered Database Queries:](#ordered-database-queries)
- [deque](#deque)
  - [Basics of Deque:](#basics-of-deque)
    - [Importing Deque:](#importing-deque)
    - [Creating a Deque:](#creating-a-deque)
    - [Append and Pop Operations:](#append-and-pop-operations)
  - [Advanced Deque Operations:](#advanced-deque-operations)
    - [Rotating Elements:](#rotating-elements)
    - [Limiting the Deque Size:](#limiting-the-deque-size)
  - [Advanced Applications of Deque:](#advanced-applications-of-deque)
    - [Queue Implementation:](#queue-implementation)
    - [Stack Implementation:](#stack-implementation)
    - [Sliding Window:](#sliding-window)
    - [Reversing a String:](#reversing-a-string)
- [heapq](#heapq)
  - [Basics of heapq:](#basics-of-heapq)
    - [Importing heapq:](#importing-heapq)
    - [Creating a Heap:](#creating-a-heap)
    - [Insertion and Extraction:](#insertion-and-extraction)
  - [Advanced heapq Operations:](#advanced-heapq-operations)
    - [Heap Replacement:](#heap-replacement)
    - [Finding N Largest or Smallest Elements:](#finding-n-largest-or-smallest-elements)
  - [Advanced Applications of heapq:](#advanced-applications-of-heapq)
    - [Merging Multiple Sorted Sequences:](#merging-multiple-sorted-sequences)
    - [K-Smallest or K-Largest Elements in a Stream:](#k-smallest-or-k-largest-elements-in-a-stream)
    - [Dijkstra's Shortest Path Algorithm:](#dijkstras-shortest-path-algorithm)
    - [Huffman Coding:](#huffman-coding)
- [bisect](#bisect)
  - [Basics of `bisect`:](#basics-of-bisect)
    - [Importing `bisect`:](#importing-bisect)
    - [Inserting Elements:](#inserting-elements)
    - [Finding Positions:](#finding-positions)
  - [Advanced `bisect` Operations:](#advanced-bisect-operations)
    - [Finding Positions for Left and Right Insertions:](#finding-positions-for-left-and-right-insertions)
    - [Handling Custom Sort Order:](#handling-custom-sort-order)
    - [Managing Lists of Tuples or Objects:](#managing-lists-of-tuples-or-objects)
  - [Advanced Applications of `bisect`:](#advanced-applications-of-bisect)
    - [Maintaining a Running Median:](#maintaining-a-running-median)
    - [Searching in a Sorted Matrix:](#searching-in-a-sorted-matrix)
    - [Finding the Longest Increasing Subsequence:](#finding-the-longest-increasing-subsequence)
- [NamedTuple](#namedtuple)
  - [Basics of NamedTuple:](#basics-of-namedtuple)
    - [Importing NamedTuple:](#importing-namedtuple)
    - [Creating a NamedTuple:](#creating-a-namedtuple)
    - [Accessing NamedTuple Fields:](#accessing-namedtuple-fields)
  - [Advanced NamedTuple Operations:](#advanced-namedtuple-operations)
    - [Immutable Fields:](#immutable-fields)
    - [Converting NamedTuple to Dictionary:](#converting-namedtuple-to-dictionary)
    - [Replacing Values:](#replacing-values)
  - [Advanced Applications of NamedTuple:](#advanced-applications-of-namedtuple)
    - [Data Structures:](#data-structures)
    - [NamedTuple as Return Type:](#namedtuple-as-return-type)
    - [Enumerations:](#enumerations)
    - [CSV Parsing:](#csv-parsing)
- [Enum](#enum)
  - [Basics of Enum:](#basics-of-enum)
    - [Importing Enum:](#importing-enum)
    - [Creating an Enum:](#creating-an-enum)
    - [Accessing Enum Members:](#accessing-enum-members)
    - [Enum Iteration:](#enum-iteration)
  - [Advanced Enum Operations:](#advanced-enum-operations)
    - [Enum Integers:](#enum-integers)
    - [Enum Names:](#enum-names)
    - [Auto-Numbering Members:](#auto-numbering-members)
    - [Comparing Enums:](#comparing-enums)
  - [Advanced Applications of Enum:](#advanced-applications-of-enum)
    - [Enum as a Switch/Case:](#enum-as-a-switchcase)
    - [Enum for Configuration Settings:](#enum-for-configuration-settings)
    - [Enum as Flags:](#enum-as-flags)
    - [Enum for State Machines:](#enum-for-state-machines)
- [Time complexity – the big O notation](#time-complexity--the-big-o-notation)
  - [Basics of Time Complexity and Big O Notation:](#basics-of-time-complexity-and-big-o-notation)
    - [Understanding Big O Notation:](#understanding-big-o-notation)
    - [Analyzing Algorithms:](#analyzing-algorithms)
    - [Constants and Lower-Order Terms:](#constants-and-lower-order-terms)
  - [Advanced Time Complexity Analysis:](#advanced-time-complexity-analysis)
    - [Best, Worst, and Average Cases:](#best-worst-and-average-cases)
    - [Amortized Analysis:](#amortized-analysis)
    - [Space Complexity:](#space-complexity)
  - [Python Example Code:](#python-example-code)
    - [O(1) - Constant Time:](#o1---constant-time)
    - [O(n) - Linear Time:](#on---linear-time)
    - [O(n^2) - Quadratic Time:](#on2---quadratic-time)
    - [O(log n) - Logarithmic Time:](#olog-n---logarithmic-time)
    - [O(n log n) - Linearithmic Time:](#on-log-n---linearithmic-time)
    - [O(2^n) - Exponential Time:](#o2n---exponential-time)

# Introduction

- In Python, "**containers**" and "**collections**" refer to data structures that are used to store and organize multiple values or objects. 
- These data structures are **fundamental** in programming and are essential for various tasks, such as managing data, iterating over elements, and performing operations like searching and sorting. 
- Python provides a rich set of built-in container and collection types, each with its own characteristics and use cases.

1. **Lists**:
   - Lists are ordered collections of items.
   - They are mutable, which means you can add, remove, or modify elements.
   - Elements can be of different data types.
   - Lists are defined using square brackets `[]`.

   ```python
   my_list = [1, 2, 3, "Python", True]
   ```

2. **Tuples**:
   - Tuples are similar to lists but are immutable, meaning their elements cannot be changed after creation.
   - They are often used for representing fixed collections of items.
   - Tuples are defined using parentheses `()`.

   ```python
   my_tuple = (1, 2, 3, "Python", True)
   ```

3. **Sets**:
   - Sets are unordered collections of unique items.
   - They are mutable, so you can add or remove items, but the items themselves are immutable (e.g., numbers, strings).
   - Sets are defined using curly braces `{}` or the `set()` constructor.

   ```python
   my_set = {1, 2, 3, 3, 4}  # Duplicate values are automatically removed
   ```

4. **Dictionaries**:
   - Dictionaries are collections of key-value pairs.
   - They are unordered, but you access values by their keys.
   - Keys must be unique and immutable (strings, numbers, tuples), while values can be of any type.
   - Dictionaries are defined using curly braces `{}` with key-value pairs separated by colons.

   ```python
   my_dict = {"name": "Alice", "age": 30, "is_student": False}
   ```

5. **Lists of Lists (Nested Lists)**:
   - You can create complex data structures by nesting lists within lists.
   - This allows you to represent multi-dimensional data.
   
   ```python
   matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
   ```

6. **String**:
   - While not a traditional container, strings are sequences of characters and can be iterated over like other containers.
   - You can access individual characters in a string using indexing.
   
   ```python
   my_string = "Python"
   ```

7. **Collections Module**:
   - Python's `collections` module provides specialized container datatypes, including `namedtuple`, `deque`, `Counter`, and `defaultdict`, which offer additional functionality beyond standard containers.

   ```python
   from collections import namedtuple, deque, Counter, defaultdict
   ```

# list

## Basics of Lists:

- A list is a fundamental data structure in Python used to store an ordered collection of items. 
- Lists are mutable, meaning you can add, remove, or modify elements within them. 
- Lists are defined using square brackets `[]` and can contain elements of different data types.

### Creating Lists:

You can create lists in several ways:

```python
# Creating an empty list
my_list = []

# Creating a list with elements
fruits = ["apple", "banana", "cherry"]

# Lists can contain mixed data types
mixed_list = [1, "apple", True, 3.14]
```

### Accessing List Elements:

List elements are accessed by their index, starting from 0 for the first element. You can use indexing to retrieve specific elements or slices of the list.

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])      # Output: "apple"
print(fruits[1])      # Output: "banana"

# Slicing a list
subset = fruits[1:3]  # Output: ["banana", "cherry"]
```

### Modifying Lists:

Lists are mutable, so you can modify their elements.

```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "orange"  # Change "banana" to "orange"
fruits.append("grape")  # Add "grape" to the end
fruits.remove("apple")  # Remove "apple"
```

### List Operations:

- operations on lists: such as finding the length, checking membership, and concatenating lists.

```python
fruits = ["apple", "banana", "cherry"]
length = len(fruits)       # Length of the list (3)
is_apple_in_list = "apple" in fruits  # True
combined_list = fruits + ["grape", "kiwi"]  # Concatenation
```

## Advanced List Operations:

### List Comprehensions:

List comprehensions provide a concise way to create new lists based on existing lists. They are often used for filtering and transforming data.

```python
numbers = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in numbers]  # [1, 4, 9, 16, 25]
even_numbers = [x for x in numbers if x % 2 == 0]  # [2, 4]
```

### Nested Lists:

Lists can be nested to create multi-dimensional data structures.

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])  # Accessing an element (6)
```

### List Methods:

Python provides various built-in methods for working with lists, including `append`, `extend`, `insert`, `pop`, `remove`, `sort`, and more.

```python
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits.extend(["grape", "kiwi"])
fruits.insert(1, "mango")
removed_fruit = fruits.pop(2)
fruits.remove("banana")
fruits.sort()  # In-place sorting
```

### List Copying:

Be cautious when copying lists. Assigning one list to another creates a reference, not a copy. To create a new list, use slicing or the `copy` method.

```python
original_list = [1, 2, 3]
shallow_copy = original_list[:]  # Creates a shallow copy
deep_copy = original_list.copy()  # Creates a deep copy
```

## Advanced Applications:

Lists are used extensively in Python for a wide range of applications. Here are a few examples:

**1. Data Storage**:

Lists are commonly used to store and manipulate data, such as user inputs, sensor readings, or database records.

```python
# Storing user input in a list
user_data = []
while True:
    user_input = input("Enter data (or 'exit' to quit): ")
    if user_input == 'exit':
        break
    user_data.append(user_input)

print("User data:", user_data)
```

**2. Iteration**:

Lists are often iterated over using loops, comprehensions, or iterators.

```python
# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Using a list comprehension for iteration
squares = [x ** 2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]
```

**3. Stacks and Queues**:

Lists can be used to implement stack and queue data structures using `append` and `pop`.

```python
# Using a list as a stack (Last-In-First-Out)
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
top_item = stack.pop()  # Removes and returns the top item (3)

# Using a list as a queue (First-In-First-Out)
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
first_item = queue.popleft()  # Removes and returns the first item (1)
```

**4. Data Filtering and Transformation**:

List comprehensions and built-in functions like `filter` and `map` are used for data manipulation.

```python
# Using list comprehensions for filtering and transformation
numbers = [1, 2, 3, 4, 5, 6]
evens = [x for x in numbers if x % 2 == 0]  # Filter even numbers
squares = [x ** 2 for x in numbers]  # Square each number

# Using 'filter' and 'map' for the same operations
def is_even(x):
    return x % 2 == 0

even_numbers = list(filter(is_even, numbers))
squared_numbers = list(map(lambda x: x ** 2, numbers))
```

**5. Sorting and Searching**:

Lists can be sorted using the `sort` method or the `sorted` function. Searching is done using methods like `index` or loops.

```python
# Sorting a list
numbers = [4, 1, 3, 2, 5]
numbers.sort()  # In-place sorting
sorted_numbers = sorted(numbers)  # Creates a new sorted list

# Searching in a list
fruits = ["apple", "banana", "cherry"]
index = fruits.index("banana")  # Find the index of "banana" (1)
```

**6. Graphs and Matrices**:

Lists of lists are used to represent graphs and matrices in various algorithms and applications.

```python
# Creating a graph as an adjacency list using lists of lists
graph = [[1, 2], [0, 2, 3], [0, 1, 3], [1, 2]]

# Accessing neighbors of a node
node = 2
neighbors = graph[node]  # Neighbors of node 2 are [0, 1, 3]

# Representing a matrix using a list of lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
element = matrix[1][2]  # Accessing element at row 1, column 2 (6)
```

# dict

## Basics of Dictionaries:

- A dictionary in Python is an unordered collection of key-value pairs. 
- Dictionaries are used to store and retrieve data in a structured way. Each key in a dictionary is unique, and it maps to a specific value. 
- Dictionaries are defined using curly braces `{}` and key-value pairs separated by colons `:`.

### Creating Dictionaries:

You can create dictionaries in several ways:

```python
# Creating an empty dictionary
my_dict = {}

# Creating a dictionary with key-value pairs
person = {"name": "Alice", "age": 30, "is_student": False}

# Using the 'dict' constructor
book = dict(title="Python 101", author="John Doe")
```

### Accessing Dictionary Values:

You can access values in a dictionary by specifying the key in square brackets or using the `get` method.

```python
person = {"name": "Alice", "age": 30, "is_student": False}
name = person["name"]  # Accessing value by key
age = person.get("age")  # Using 'get' method
```

### Modifying Dictionaries:

Dictionaries are mutable, so you can add, update, or remove key-value pairs.

```python
person = {"name": "Alice", "age": 30}
person["city"] = "New York"  # Adding a new key-value pair
person["age"] = 31  # Updating the value for an existing key
del person["age"]  # Removing a key-value pair
```

## Advanced Dictionary Operations:

### Dictionary Comprehensions:

Similar to list comprehensions, dictionary comprehensions allow you to create dictionaries in a concise way.

```python
# Creating a dictionary using a comprehension
squared_dict = {x: x ** 2 for x in range(1, 6)}  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### Nested Dictionaries:

Dictionaries can be nested to create complex data structures.

```python
# Nested dictionaries
person = {
    "name": "Alice",
    "address": {
        "street": "123 Main St",
        "city": "New York"
    }
}
city = person["address"]["city"]  # Accessing a nested value
```

### Dictionary Methods:

Python provides several built-in methods for working with dictionaries, including `keys`, `values`, `items`, and more.

```python
person = {"name": "Alice", "age": 30, "is_student": False}
keys = person.keys()  # Get keys
values = person.values()  # Get values
items = person.items()  # Get key-value pairs as tuples
```

### Handling Missing Keys:

You can handle missing keys using the `get` method or a default value.

```python
person = {"name": "Alice", "age": 30}
city = person.get("city", "Unknown")  # Using a default value ("Unknown")
```

## Advanced Applications:

Dictionaries are used in various advanced applications in Python:

**1. Counting Elements in a List:**

Dictionaries are often used to count the frequency of elements in a list.

```python
words = ["apple", "banana", "cherry", "apple", "cherry"]
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Result: {'apple': 2, 'banana': 1, 'cherry': 2}
```

**2. Configurations and Settings:**

Dictionaries are used to store configuration settings for applications.

```python
app_config = {
    "debug_mode": True,
    "log_level": "INFO",
    "max_connections": 100
}
```

**3. JSON Data:**

Dictionaries are commonly used to work with JSON data in Python.

```python
import json

json_data = '{"name": "Alice", "age": 30}'
data_dict = json.loads(json_data)  # Convert JSON to dictionary
```

**4. Mapping Values:**

Dictionaries are used for mapping values, such as converting state abbreviations to full names.

```python
state_abbreviations = {
    "CA": "California",
    "NY": "New York",
    "TX": "Texas"
}
state_name = state_abbreviations.get("CA")  # Get full state name
```

**5. Caching and Memoization:**

Dictionaries can be used for caching and memoization to store previously computed results to improve performance.

```python
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    result = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    memo[n] = result
    return result
```

# set

## Basics of Sets:

- A set in Python is an unordered collection of unique elements. 
- Sets are commonly used to store distinct values and perform operations like union, intersection, and difference. 
- Sets are defined using curly braces `{}` or the `set()` constructor.

### Creating Sets:

You can create sets in several ways:

```python
# Creating an empty set
my_set = set()

# Creating a set with elements
fruits = {"apple", "banana", "cherry"}

# Using the 'set' constructor
colors = set(["red", "green", "blue"])
```

### Adding and Removing Elements:

Sets are mutable, so you can add and remove elements.

```python
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")  # Adding an element
fruits.remove("banana")  # Removing an element
```

## Basic Set Operations:

Sets support common set operations, such as union, intersection, difference, and membership testing.

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

union_result = A | B  # Union: {1, 2, 3, 4, 5, 6}
intersection_result = A & B  # Intersection: {3, 4}
difference_result = A - B  # Difference: {1, 2}
is_subset = A.issubset(B)  # Check if A is a subset of B: False
```

## Advanced Set Operations:

### Set Comprehensions:

Similar to list comprehensions, set comprehensions allow you to create sets in a concise way.

```python
# Creating a set using a comprehension
squared_set = {x ** 2 for x in range(1, 6)}  # {1, 4, 9, 16, 25}
```

### Frozen Sets:

A frozen set is an immutable version of a set and can be used as a dictionary key.

```python
frozen_set = frozenset([1, 2, 3])
```

## Advanced Applications:

Sets are used in various advanced applications in Python:

**1. Removing Duplicates:**

Sets are often used to remove duplicate elements from a list.

```python
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
```

**2. Membership Testing:**

Sets are efficient for checking whether an item exists in a large collection of items.

```python
word_set = {"apple", "banana", "cherry", "date"}
is_in_set = "banana" in word_set  # True
```

**3. Finding Unique Values:**

Sets can be used to find unique values in a dataset.

```python
data = [1, 2, 2, 3, 4, 4, 5]
unique_values = set(data)
```

**4. Set Operations in Data Analysis:**

Sets are valuable for performing operations like intersection, union, and difference in data analysis.

```python
sales_team = {"Alice", "Bob", "Charlie", "David"}
marketing_team = {"Charlie", "Eve", "Frank"}

# Finding team members in both sales and marketing
common_members = sales_team & marketing_team  # Intersection
```

**5. Removing Common Elements:**

Sets can be used to remove common elements from two lists.

```python
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
unique_elements = set(list1) - set(list2)  # Remove common elements
```

**6. Set Operations in Graph Algorithms:**

Sets are used in graph algorithms to perform operations like finding connected components and detecting cycles.

```python
nodes = {1, 2, 3, 4, 5}
edges = {(1, 2), (2, 3), (4, 5)}

# Detecting cycles in a graph
def has_cycle(nodes, edges):
    visited = set()
    for node in nodes:
        if node not in visited:
            if dfs(node, None):
                return True
    return False
```

# tuple

## Basics of Tuples:

- An ordered, immutable collection of elements. 
- Tuples are similar to lists, but unlike lists, tuples cannot be modified once created. 
- Tuples are defined using parentheses `()` and can contain elements of different data types.

### Creating Tuples:

You can create tuples in several ways:

```python
# Creating an empty tuple
my_tuple = ()

# Creating a tuple with elements
fruits = ("apple", "banana", "cherry")

# Using the 'tuple' constructor
colors = tuple(["red", "green", "blue"])
```

### Accessing Tuple Elements:

Tuple elements are accessed by their index, starting from 0 for the first element. You can use indexing to retrieve specific elements.

```python
fruits = ("apple", "banana", "cherry")
first_fruit = fruits[0]  # Accessing the first element ("apple")
second_fruit = fruits[1]  # Accessing the second element ("banana")
```

### Immutable Nature:

Tuples are immutable, meaning you cannot modify their elements after creation. However, you can create a new tuple with modified elements.

```python
fruits = ("apple", "banana", "cherry")
# The following line will raise a TypeError
# fruits[0] = "orange"
```

## Advanced Tuple Operations:

### Tuple Packing and Unpacking:

Tuples allow for packing and unpacking multiple values in a single line.

```python
# Tuple packing
point = (3, 4)

# Tuple unpacking
x, y = point
```

### Tuple Concatenation:

You can concatenate tuples using the `+` operator to create a new tuple.

```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result_tuple = tuple1 + tuple2  # Result: (1, 2, 3, 4, 5, 6)
```

## Advanced Applications:

Tuples are used in various advanced applications in Python:

**1. Function Return Values:**

Tuples are often used to return multiple values from a function.

```python
def divide_and_remainder(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

result = divide_and_remainder(10, 3)
# Result: (3, 1)
```

**2. Named Tuples:**

Named tuples provide a convenient way to create tuples with named fields.

```python
from collections import namedtuple

# Defining a named tuple type
Person = namedtuple("Person", ["name", "age", "city"])
person = Person("Alice", 30, "New York")

# Accessing fields by name
name = person.name
age = person.age
```

**3. Tuple Slicing:**

Tuples support slicing to access portions of the tuple.

```python
my_tuple = (1, 2, 3, 4, 5)
subset = my_tuple[1:4]  # Result: (2, 3, 4)
```

**4. Packing and Unpacking in Loops:**

Tuples are often used for packing and unpacking values in loops.

```python
points = [(1, 2), (3, 4), (5, 6)]
for x, y in points:
    print(f"Point: ({x}, {y})")
```

**5. Immutable Dictionary Keys:**

Tuples are used as dictionary keys because they are immutable.

```python
locations = {("40.7128", "-74.0060"): "New York", ("34.0522", "-118.2437"): "Los Angeles"}
```

**6. Function Arguments:**

Tuples can be used to pass a variable number of arguments to a function.

```python
def sum_values(*args):
    return sum(args)

result = sum_values(1, 2, 3, 4, 5)  # Result: 15
```

# ChainMap

- The `collections.ChainMap` type in Python is a dictionary-like object that represents a list of dictionaries or other mapping objects. 
- It allows you to create a chain of dictionaries and perform lookups and updates as if they were a single dictionary.

## Basics of ChainMap:

### Importing ChainMap:

To use `ChainMap`, you need to import it from the `collections` module:

```python
from collections import ChainMap
```

### Creating a ChainMap:

You can create a `ChainMap` by providing one or more dictionaries as arguments during initialization. The order of dictionaries determines the lookup precedence.

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

chain_map = ChainMap(dict1, dict2)
```

### Accessing Values:

You can access values in a `ChainMap` using standard dictionary access methods like `[key]` or `.get(key)`.

```python
value_a = chain_map["a"]  # Accessing 'a' from dict1
value_b = chain_map["b"]  # Accessing 'b' from dict1 (first occurrence)
value_c = chain_map.get("c")  # Accessing 'c' from dict2
```

### Updating Values:

`ChainMap` is mutable, and you can update values in the first dictionary in the chain. If the key is not found in the first dictionary, it will add the key-value pair.

```python
chain_map["a"] = 10  # Updating 'a' in dict1
chain_map["d"] = 5   # Adding 'd' to dict1
```

## Advanced ChainMap Operations:

### Reversing the ChainMap:

You can reverse the order of dictionaries in a `ChainMap` using the `.reverse()` method. This changes the lookup precedence.

```python
chain_map.reverse()
```

### Nested ChainMaps:

You can nest `ChainMap` objects to create more complex chains of dictionaries.

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"c": 5, "d": 6}

chain_map1 = ChainMap(dict1, dict2)
chain_map2 = ChainMap(dict3, chain_map1)
```

### Creating a New ChainMap:

You can create a new `ChainMap` that includes an additional dictionary while keeping the original chain intact.

```python
dict4 = {"e": 7, "f": 8}
new_chain_map = chain_map.new_child(dict4)
```

### Accessing Parent Maps:

You can access the parent maps of a `ChainMap` using the `.parents` attribute.

```python
parent_maps = chain_map.parents  # Gets all parent maps (excluding the first)
```

## Advanced Applications of ChainMap:

### Configuration and Defaults:

`ChainMap` is useful for managing configuration settings and providing default values.

```python
default_config = {"debug": False, "max_connections": 100}
user_config = {"debug": True, "port": 8080}

config = ChainMap(user_config, default_config)
```

### Context Managers:

`ChainMap` is used in context managers for managing state.

```python
from contextlib import contextmanager

@contextmanager
def config_context(config):
    original_config = config.copy()
    yield config
    config.clear()
    config.update(original_config)

with config_context(config):
    # Inside the context, 'config' can be modified freely
    config["debug"] = True

# After the context, 'config' is restored to its original state
```

### Merging Dictionaries:

`ChainMap` can be used to merge dictionaries efficiently.

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"c": 5, "d": 6}

merged_dict = dict1.copy()
merged_dict.update(dict2)
merged_dict.update(dict3)
```

### Managing Configuration Layers:

In applications with multiple configuration layers (e.g., user, environment, system), `ChainMap` simplifies managing these configurations.

```python
# Representing configuration layers as ChainMaps
user_config = {"debug": True, "port": 8080}
env_config = {"port": 9090}
sys_config = {"debug": False, "max_connections": 100}

config_chain = ChainMap(user_config, env_config, sys_config)
```

# Counter

- The `collections.Counter` type in Python is a dictionary-like object specifically designed for counting the occurrences of elements in an iterable. 
- It provides a convenient way to perform counting and is widely used for various tasks. .

## Basics of Counter:

### Importing Counter:

To use `Counter`, you need to import it from the `collections` module:

```python
from collections import Counter
```

### Creating a Counter:

You can create a `Counter` by passing an iterable (e.g., a list or a string) as an argument. It counts the occurrences of each element in the iterable.

```python
word_count = Counter(["apple", "banana", "cherry", "apple"])
```

### Accessing Counts:

You can access the counts of elements using dictionary-like syntax or the `.get()` method.

```python
count_apple = word_count["apple"]  # Accessing the count of 'apple' (2)
count_banana = word_count.get("banana", 0)  # Accessing the count of 'banana' with a default of 0
```

### Counter Operations:

`Counter` supports various operations like addition, subtraction, and intersection, making it useful for combining counts from multiple sources.

```python
counter1 = Counter(["a", "b", "c", "a"])
counter2 = Counter(["a", "b", "b", "c"])

# Addition (element-wise)
combined_counter = counter1 + counter2  # {"a": 3, "b": 3, "c": 2}

# Subtraction (element-wise)
subtracted_counter = counter1 - counter2  # {"a": 0, "b": 0, "c": 0}

# Intersection (minimum count)
intersection_counter = counter1 & counter2  # {"a": 1, "b": 1, "c": 1}
```

## Advanced Counter Operations:

### Elements and Values:

You can obtain the unique elements and their corresponding counts from a `Counter`.

```python
elements = word_count.elements()  # Returns an iterator of elements
unique_elements = list(elements)  # ['apple', 'apple', 'banana', 'cherry']
```

### Most Common Elements:

You can find the most common elements and their counts using the `.most_common()` method.

```python
most_common = word_count.most_common(2)  # Get the top 2 most common elements
# [('apple', 2), ('banana', 1)]
```

### Subtracting Counters:

You can subtract one `Counter` from another to compute the difference in counts.

```python
inventory1 = Counter(apples=5, bananas=3, cherries=2)
inventory2 = Counter(apples=2, cherries=1, grapes=4)

remaining_inventory = inventory1 - inventory2
# {'apples': 3, 'bananas': 3, 'cherries': 1, 'grapes': -4}
```

## Advanced Applications of Counter:

### Word Frequency Count:

`Counter` is commonly used to count the frequency of words in a text document.

```python
text = "This is a simple text document. This text is used for demonstration."
words = text.split()
word_count = Counter(words)
```

### Anagrams Detection:

`Counter` can be used to detect anagrams by comparing the character counts of two words.

```python
def are_anagrams(word1, word2):
    return Counter(word1) == Counter(word2)

result = are_anagrams("listen", "silent")  # True
```

### Combining Lists:

`Counter` can efficiently combine multiple lists of elements.

```python
list1 = ["a", "b", "c", "a"]
list2 = ["b", "b", "c", "d"]
combined_counter = Counter(list1) + Counter(list2)
# {'a': 2, 'b': 3, 'c': 2, 'd': 1}
```

### Inventory Management:

`Counter` can be used to manage inventory by keeping track of items and quantities.

```python
current_inventory = Counter(apples=10, bananas=5, oranges=7)
sales = Counter(apples=2, bananas=3, grapes=4)

remaining_inventory = current_inventory - sales
```

### Finding Differences:

`Counter` can find the differences between two datasets, such as comparing expected and actual outcomes.

```python
expected_outcome = Counter(success=100, failure=20)
actual_outcome = Counter(success=90, failure=25)

difference = expected_outcome - actual_outcome
```

# Defaultdict

- The `collections.defaultdict` type in Python is a dictionary-like object that allows you to specify a default value for keys that don't exist in the dictionary. 
- It's particularly useful when you want to create a dictionary with default values for all keys.

## Basics of Defaultdict:

### Importing Defaultdict:

To use `defaultdict`, you need to import it from the `collections` module:

```python
from collections import defaultdict
```

### Creating a Defaultdict:

You can create a `defaultdict` by providing a default factory function, which determines the default value for missing keys. Common factory functions include `int`, `list`, `set`, and `lambda`.

```python
# Creating a defaultdict with int factory (default value is 0)
int_dict = defaultdict(int)

# Creating a defaultdict with list factory (default value is an empty list)
list_dict = defaultdict(list)

# Creating a defaultdict with lambda factory (default value is "Unknown")
default_value = lambda: "Unknown"
name_dict = defaultdict(default_value)
```

### Accessing Default Values:

When you access a missing key in a `defaultdict`, it automatically creates the key and assigns the default value determined by the factory function.

```python
int_dict["count"] += 1  # Accessing and updating a missing key ("count")
# int_dict now contains {"count": 1}

list_dict["items"].append("apple")  # Accessing and updating a missing key ("items")
# list_dict now contains {"items": ["apple"]}

name = name_dict["John"]  # Accessing a missing key ("John")
# name is "Unknown"
```

## Advanced Defaultdict Operations:

### Setting the Default Factory:

You can change the default factory of a `defaultdict` at any time using the `.default_factory` attribute.

```python
name_dict.default_factory = lambda: "Anonymous"
name = name_dict["Mary"]  # Accessing a missing key ("Mary")
# name is "Anonymous"
```

### Using Defaultdict with Nested Data Structures:

`Defaultdict` is particularly useful when dealing with nested data structures.

```python
nested_dict = defaultdict(dict)

# Accessing and updating nested keys
nested_dict["user"]["name"] = "Alice"
nested_dict["user"]["age"] = 30
# nested_dict now contains {"user": {"name": "Alice", "age": 30}}
```

### Creating Defaultdict of Lists:

A common use case is to create a `defaultdict` of lists to collect items by category or key.

```python
item_dict = defaultdict(list)

# Adding items to categories
item_dict["fruits"].append("apple")
item_dict["fruits"].append("banana")
item_dict["vegetables"].append("carrot")
# item_dict now contains {"fruits": ["apple", "banana"], "vegetables": ["carrot"]}
```

## Advanced Applications of Defaultdict:

### Counting Elements:

`Defaultdict` can be used to count the occurrences of elements in an iterable.

```python
from collections import defaultdict

word_count = defaultdict(int)
text = "This is a sample text. This text is used for demonstration."
words = text.split()

for word in words:
    word_count[word] += 1
```

### Grouping Data:

You can use `defaultdict` to group data based on a shared attribute or key.

```python
from collections import defaultdict

user_data = [
    {"name": "Alice", "city": "New York"},
    {"name": "Bob", "city": "Los Angeles"},
    {"name": "Charlie", "city": "New York"},
]

grouped_users = defaultdict(list)

for user in user_data:
    grouped_users[user["city"]].append(user["name"])
```

### Creating Sparse Matrices:

`Defaultdict` can be used to efficiently create sparse matrices.

```python
from collections import defaultdict

sparse_matrix = defaultdict(dict)

# Setting non-zero values
sparse_matrix[0][1] = 5
sparse_matrix[1][2] = 3
```

### Handling Missing Data:

`Defaultdict` can be used to handle missing data gracefully in data processing tasks.

```python
from collections import defaultdict

data = [
    {"user_id": 1, "product_id": 101, "quantity": 3},
    {"user_id": 2, "product_id": 102, "quantity": 2},
    # ...
]

user_product_counts = defaultdict(int)

for entry in data:
    user_id = entry["user_id"]
    product_id = entry["product_id"]
    quantity = entry["quantity"]
    user_product_counts[(user_id, product_id)] += quantity
```

# OrderedDict

- The `collections.OrderedDict` type in Python is a dictionary-like object that maintains the order of keys as they are inserted. 
- It provides a way to create dictionaries with predictable key order, which can be useful in various scenarios.

## Basics of OrderedDict:

### Importing OrderedDict:

To use `OrderedDict`, you need to import it from the `collections` module:

```python
from collections import OrderedDict
```

### Creating an OrderedDict:

You can create an `OrderedDict` by providing key-value pairs using the `dict()` constructor or by passing an iterable of key-value pairs.

```python
# Creating an OrderedDict using key-value pairs
ordered_dict = OrderedDict({"a": 1, "b": 2, "c": 3})

# Creating an OrderedDict using an iterable of key-value pairs
items = [("x", 10), ("y", 20), ("z", 30)]
ordered_dict = OrderedDict(items)
```

### Accessing Values:

You can access values in an `OrderedDict` using dictionary-like syntax.

```python
value_a = ordered_dict["a"]  # Accessing the value associated with key "a"
value_b = ordered_dict.get("b")  # Using the get() method
```

### Maintaining Insertion Order:

The order of keys in an `OrderedDict` is preserved based on the order in which they were inserted.

```python
ordered_dict["d"] = 4  # Adding a new key-value pair
# The order remains "a", "b", "c", "d"
```

## Advanced OrderedDict Operations:

### Reordering Keys:

You can reorder keys in an `OrderedDict` using the `.move_to_end()` method. This method moves a key to either the beginning (if `last` is `False`) or the end (if `last` is `True`) of the key order.

```python
ordered_dict.move_to_end("b", last=False)  # Moving "b" to the front
# The order becomes "b", "a", "c", "d"
```

### Popping Items:

You can pop items from an `OrderedDict` while maintaining the key order using the `.popitem()` method. By default, it removes and returns the last key-value pair, but you can specify `last=False` to remove and return the first key-value pair.

```python
key, value = ordered_dict.popitem()
# Removes and returns the last key-value pair ("d", 4)
```

## Advanced Applications of OrderedDict:

### Preserving JSON Object Order:

`OrderedDict` is useful for preserving the order of keys when working with JSON objects. This ensures that serialized JSON data maintains a predictable key order.

```python
import json

data = OrderedDict({"name": "Alice", "age": 30, "city": "New York"})
json_data = json.dumps(data)
# Result: '{"name": "Alice", "age": 30, "city": "New York"}'
```

### Ordered Configuration Settings:

`OrderedDict` is valuable when you want to ensure that configuration settings are processed in a specific order.

```python
config = OrderedDict()
config["debug"] = True
config["port"] = 8080
config["log_level"] = "INFO"
```

### Creating a Cache with Limited Size:

`OrderedDict` can be used to create a cache with a limited number of items. When the cache exceeds its size, the least recently used item can be removed.

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)  # Remove the first (least recently used) item
        self.cache[key] = value
```

### Ordered Database Queries:

In database applications, `OrderedDict` can be used to represent query results while preserving the order of columns.

```python
from collections import OrderedDict

def execute_query(sql_query):
    # Execute SQL query and fetch results
    cursor.execute(sql_query)
    columns = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()

    results = [OrderedDict(zip(columns, row)) for row in rows]
    return results
```

# deque

- The `collections.deque` type in Python is a double-ended queue that provides fast and efficient append and pop operations from both ends of the deque. 
- It is particularly useful when you need to implement a queue or a stack efficiently.

## Basics of Deque:

### Importing Deque:

To use `deque`, you need to import it from the `collections` module:

```python
from collections import deque
```

### Creating a Deque:

You can create a `deque` by providing an iterable (e.g., a list) as an argument during initialization.

```python
# Creating a deque from a list
my_deque = deque([1, 2, 3, 4, 5])
```

### Append and Pop Operations:

`deque` supports fast `append` and `pop` operations from both ends.

```python
# Append to the right end
my_deque.append(6)

# Append to the left end
my_deque.appendleft(0)

# Pop from the right end
right_element = my_deque.pop()

# Pop from the left end
left_element = my_deque.popleft()
```

## Advanced Deque Operations:

### Rotating Elements:

You can rotate the elements in a `deque` to the right or left using the `.rotate()` method.

```python
my_deque = deque([1, 2, 3, 4, 5])

# Rotate elements to the right by 2 positions
my_deque.rotate(2)  # [4, 5, 1, 2, 3]

# Rotate elements to the left by 1 position
my_deque.rotate(-1)  # [5, 1, 2, 3, 4]
```

### Limiting the Deque Size:

You can create a bounded `deque` with a maximum size, and when the size is exceeded, elements are automatically removed from the opposite end.

```python
# Creating a bounded deque with a maximum size of 3
bounded_deque = deque(maxlen=3)

bounded_deque.append(1)
bounded_deque.append(2)
bounded_deque.append(3)

# Exceeding the maximum size
bounded_deque.append(4)
# bounded_deque now contains [2, 3, 4]
```

## Advanced Applications of Deque:

### Queue Implementation:

`deque` can be used to efficiently implement a queue, where elements are inserted at one end and removed from the other end.

```python
from collections import deque

queue = deque()

# Enqueue (insert) elements
queue.append(1)
queue.append(2)
queue.append(3)

# Dequeue (remove) elements
element = queue.popleft()  # Removes and returns 1
```

### Stack Implementation:

`deque` can also be used to implement a stack, where elements are inserted and removed from the same end.

```python
from collections import deque

stack = deque()

# Push (insert) elements
stack.append(1)
stack.append(2)
stack.append(3)

# Pop (remove) elements
element = stack.pop()  # Removes and returns 3
```

### Sliding Window:

`deque` is useful for implementing sliding window algorithms efficiently.

```python
from collections import deque

def sliding_window_max(nums, k):
    max_values = []
    window = deque()

    for i, num in enumerate(nums):
        # Remove elements that are out of the current window
        while window and window[0] < i - k + 1:
            window.popleft()

        # Remove elements that are smaller than the current number
        while window and nums[window[-1]] < num:
            window.pop()

        window.append(i)
        
        if i >= k - 1:
            max_values.append(nums[window[0]])

    return max_values
```

### Reversing a String:

`deque` can be used to efficiently reverse a string.

```python
from collections import deque

def reverse_string(s):
    char_deque = deque(s)
    reversed_s = ""

    while char_deque:
        reversed_s += char_deque.pop()

    return reversed_s
```

# heapq

- The `heapq` module in Python provides a collection of efficient heap queue algorithms, often referred to as heaps. 
- Heaps are a specialized data structure that allows for efficient insertion, deletion, and retrieval of the smallest (or largest) element in a collection.

## Basics of heapq:

### Importing heapq:

To use `heapq`, you don't need to import any specific module as it is part of the Python standard library. You can use it directly in your code.

```python
import heapq
```

### Creating a Heap:

You can create a heap in the form of a list and use `heapq` functions to manage it. By default, `heapq` creates a min-heap (the smallest element is at the top). To create a max-heap (the largest element at the top), you can negate the values or use a custom comparison function.

```python
# Creating a min-heap
heap = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Converting a list into a min-heap in-place
heapq.heapify(heap)
```

### Insertion and Extraction:

You can insert elements into the heap using the `heappush()` function and extract the smallest element using the `heappop()` function.

```python
# Inserting elements
heapq.heappush(heap, 0)

# Extracting the smallest element
smallest = heapq.heappop(heap)
```

## Advanced heapq Operations:

### Heap Replacement:

You can replace the smallest element in the heap with a new value using the `heapreplace()` function.

```python
# Replace the smallest element with a new value
heapq.heapreplace(heap, 7)
```

### Finding N Largest or Smallest Elements:

You can find the N largest or smallest elements in a collection using the `nlargest()` and `nsmallest()` functions.

```python
largest_3 = heapq.nlargest(3, heap)
smallest_3 = heapq.nsmallest(3, heap)
```

## Advanced Applications of heapq:

### Merging Multiple Sorted Sequences:

You can efficiently merge multiple sorted sequences using the `heapq.merge()` function.

```python
seq1 = [1, 4, 7]
seq2 = [2, 5, 8]
seq3 = [3, 6, 9]

merged = list(heapq.merge(seq1, seq2, seq3))
```

### K-Smallest or K-Largest Elements in a Stream:

You can efficiently find the K-smallest or K-largest elements in a stream of data using a min-heap or max-heap.

```python
import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.k = k
        
        for num in nums:
            self.add(num)
    
    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        
        return self.min_heap[0]
```

### Dijkstra's Shortest Path Algorithm:

Dijkstra's algorithm can be implemented efficiently using a priority queue, which is often implemented using a min-heap.

```python
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances
```

### Huffman Coding:

Huffman coding, used for data compression, can be implemented efficiently using a min-heap.

```python
import heapq
from collections import defaultdict

def huffman_encoding(data):
    freq_dict = defaultdict(int)
    for char in data:
        freq_dict[char] += 1

    priority_queue = [(freq, [char]) for char, freq in freq_dict.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        freq1, chars1 = heapq.heappop(priority_queue)
        freq2, chars2 = heapq.heappop(priority_queue)
        combined_chars = chars1 + chars2
        combined_freq = freq1 + freq2
        heapq.heappush(priority_queue, (combined_freq, combined_chars))

    huffman_tree = priority_queue[0]
    return huffman_tree[1]

def huffman_decoding(data, huffman_tree):
    decoded_data = ""
    while data:
        for char in huffman_tree:
            if data.startswith(char):
                decoded_data += huffman_tree[char]
                data = data[len(char):]
                break
    return decoded_data
```

# bisect

- The `bisect` module in Python provides a way to efficiently insert items into and find items within a sorted sequence (usually a list). 
- It uses a binary search algorithm to achieve this efficiently.

## Basics of `bisect`:

### Importing `bisect`:

To use `bisect`, you need to import it from the `bisect` module:

```python
import bisect
```

### Inserting Elements:

The primary use of `bisect` is to insert elements into a sorted sequence while maintaining the sorted order.

```python
my_list = [1, 3, 4, 7, 9]
bisect.insort(my_list, 5)  # Insert 5 while keeping the list sorted
```

### Finding Positions:

You can use `bisect` to find the insertion position of an element in a sorted sequence. It returns the index where the element should be inserted to maintain the sorted order.

```python
position = bisect.bisect(my_list, 6)  # Find the insertion position of 6
```

## Advanced `bisect` Operations:

### Finding Positions for Left and Right Insertions:

`bisect` provides two functions to find insertion positions:

- `bisect.bisect_left()` returns the position for left insertion (i.e., before any existing elements equal to the given value).
- `bisect.bisect_right()` returns the position for right insertion (i.e., after all existing elements equal to the given value).

```python
left_position = bisect.bisect_left(my_list, 6)
right_position = bisect.bisect_right(my_list, 6)
```

### Handling Custom Sort Order:

You can use the `key` argument in `bisect` functions to specify a custom sorting order based on a key function.

```python
my_list = ["apple", "banana", "cherry", "date", "fig"]
# Sort by the length of the strings
bisect.insort(my_list, "kiwi", key=len)
```

### Managing Lists of Tuples or Objects:

You can use `bisect` with lists of tuples or custom objects by providing a `key` function that extracts the sorting key.

```python
points = [(1, 2), (3, 4), (5, 6)]
new_point = (4, 5)

# Sort based on the distance from the new_point
bisect.insort(points, new_point, key=lambda point: ((point[0] - new_point[0])**2 + (point[1] - new_point[1])**2)**0.5)
```

## Advanced Applications of `bisect`:

### Maintaining a Running Median:

`bisect` can be used to efficiently maintain a running median in a stream of numbers.

```python
import bisect

class RunningMedian:
    def __init__(self):
        self.data = []

    def add_number(self, num):
        bisect.insort(self.data, num)

    def get_median(self):
        n = len(self.data)
        if n % 2 == 0:
            mid1 = n // 2
            mid2 = mid1 - 1
            return (self.data[mid1] + self.data[mid2]) / 2
        else:
            mid = n // 2
            return self.data[mid]
```

### Searching in a Sorted Matrix:

`bisect` can be applied to search for elements in a sorted matrix efficiently.

```python
import bisect

def search_matrix(matrix, target):
    if not matrix:
        return False

    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1

    while left <= right:
        mid = (left + right) // 2
        mid_element = matrix[mid // cols][mid % cols]

        if mid_element == target:
            return True
        elif mid_element < target:
            left = mid + 1
        else:
            right = mid - 1

    return False
```

### Finding the Longest Increasing Subsequence:

`bisect` can be used to find the longest increasing subsequence of a sequence of numbers efficiently.

```python
import bisect

def longest_increasing_subsequence(nums):
    lis = []
    for num in nums:
        index = bisect.bisect_left(lis, num)
        if index == len(lis):
            lis.append(num)
        else:
            lis[index] = num
    return len(lis)
```

# NamedTuple

- NamedTuples are a convenient way to create simple classes to represent data. 
- They are similar to regular tuples, but each field has a name, which makes the code more self-documenting and readable. 
- NamedTuples are part of the `collections` module in Python.

## Basics of NamedTuple:

### Importing NamedTuple:

To use NamedTuple, you need to import it from the `collections` module:

```python
from collections import namedtuple
```

### Creating a NamedTuple:

You can create a NamedTuple by defining a template or a blueprint for it. This is done using the `namedtuple()` function, which takes the name of the NamedTuple and a sequence of field names as arguments.

```python
# Defining a NamedTuple template
Person = namedtuple("Person", ["name", "age"])

# Creating instances of NamedTuple
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
```

### Accessing NamedTuple Fields:

You can access the fields of a NamedTuple using dot notation.

```python
print(person1.name)  # Accessing the 'name' field
print(person2.age)   # Accessing the 'age' field
```

## Advanced NamedTuple Operations:

### Immutable Fields:

NamedTuples, like regular tuples, are immutable, which means you can't change their values once they're assigned.

```python
# This will result in an error
person1.age = 31
```

### Converting NamedTuple to Dictionary:

You can convert a NamedTuple to a dictionary using the `_asdict()` method.

```python
person_dict = person1._asdict()
# Result: {'name': 'Alice', 'age': 30}
```

### Replacing Values:

You can create a new NamedTuple with some fields replaced using the `_replace()` method.

```python
new_person = person1._replace(age=31)
# Result: Person(name='Alice', age=31)
```

## Advanced Applications of NamedTuple:

### Data Structures:

NamedTuples are useful for defining lightweight data structures. For example, you can use them to represent points in a 2D plane.

```python
Point = namedtuple("Point", ["x", "y"])
point = Point(2, 3)
```

### NamedTuple as Return Type:

You can use NamedTuples to return multiple values from a function in a structured way.

```python
def get_person_details():
    return Person("Alice", 30)

person = get_person_details()
print(person.name)  # 'Alice'
print(person.age)   # 30
```

### Enumerations:

You can use NamedTuples to create enumerations or constants.

```python
Status = namedtuple("Status", ["SUCCESS", "FAILURE", "PENDING"])
status = Status(0, 1, 2)

# Usage:
if some_condition:
    current_status = status.SUCCESS
```

### CSV Parsing:

NamedTuples can be used to parse CSV data, where each row represents a record with named fields.

```python
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)  # Assuming the first row is the header
    Record = namedtuple("Record", header)
    for row in reader:
        record = Record(*row)
        print(record.name, record.age)
```

# Enum

- In Python, the `enum` module provides support for creating enumerations, which are a set of named values representing distinct members of a group. 
- Enums enhance code readability and maintainability by giving names to constant values.

## Basics of Enum:

### Importing Enum:

To use `enum`, you need to import it from the `enum` module:

```python
from enum import Enum, auto
```

### Creating an Enum:

You can create an Enum class by subclassing `Enum` and defining the members as class attributes.

```python
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
```

### Accessing Enum Members:

You can access the members of an Enum using dot notation.

```python
favorite_color = Color.GREEN
print(favorite_color)  # Color.GREEN
```

### Enum Iteration:

You can iterate over the members of an Enum using a `for` loop.

```python
for color in Color:
    print(color)
# Color.RED
# Color.GREEN
# Color.BLUE
```

## Advanced Enum Operations:

### Enum Integers:

Each Enum member has an associated integer value. You can access it using `.value`.

```python
red_value = Color.RED.value  # 1
```

### Enum Names:

You can access the names of Enum members using `.name`.

```python
blue_name = Color.BLUE.name  # 'BLUE'
```

### Auto-Numbering Members:

You can use the `auto()` function to automatically assign unique values to Enum members.

```python
class Direction(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()
```

### Comparing Enums:

You can compare Enum members using `==` or `is`.

```python
if some_direction == Direction.NORTH:
    print("Going North")
```

## Advanced Applications of Enum:

### Enum as a Switch/Case:

You can use Enums to implement a switch/case-like behavior in Python, where each Enum member corresponds to a specific action or behavior.

```python
class Operation(Enum):
    ADD = 1
    SUBTRACT = 2
    MULTIPLY = 3
    DIVIDE = 4

def perform_operation(a, b, operation):
    if operation == Operation.ADD:
        return a + b
    elif operation == Operation.SUBTRACT:
        return a - b
    elif operation == Operation.MULTIPLY:
        return a * b
    elif operation == Operation.DIVIDE:
        if b != 0:
            return a / b
    raise ValueError("Invalid operation")

result = perform_operation(10, 5, Operation.ADD)
```

### Enum for Configuration Settings:

Enums can be used to define configuration settings with meaningful names.

```python
class LogLevel(Enum):
    DEBUG = auto()
    INFO = auto()
    WARNING = auto()
    ERROR = auto()

current_log_level = LogLevel.INFO
```

### Enum as Flags:

Enums can be used to create flag-like structures where each member represents a bit in a bitfield.

```python
class Permissions(Enum):
    READ = 1
    WRITE = 2
    EXECUTE = 4

user_permissions = Permissions.READ | Permissions.WRITE
if user_permissions & Permissions.WRITE:
    print("User can write")
```

### Enum for State Machines:

Enums are useful for defining states and transitions in a state machine.

```python
class State(Enum):
    INITIAL = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()

current_state = State.INITIAL

# State transition
if some_condition:
    current_state = State.IN_PROGRESS
```

# Time complexity – the big O notation

- Time complexity is a way to measure the efficiency of an algorithm by analyzing how its runtime grows as the input size increases. 
- The Big O notation, often denoted as O(f(n)), provides an upper bound on the growth rate of an algorithm's runtime in relation to the input size. 

## Basics of Time Complexity and Big O Notation:

### Understanding Big O Notation:

- Big O notation describes the upper limit of the runtime of an algorithm in the worst-case scenario. It provides a way to compare algorithms' efficiency.
- Big O notation uses mathematical functions to represent how the runtime scales with the input size. For example, O(1) means constant time, while O(n) represents linear time.
- Common time complexities:
  - O(1): Constant time
  - O(log n): Logarithmic time
  - O(n): Linear time
  - O(n log n): Linearithmic time
  - O(n^2): Quadratic time
  - O(2^n): Exponential time
  - O(n!): Factorial time

### Analyzing Algorithms:

To analyze the time complexity of an algorithm, you count the number of basic operations (e.g., comparisons, assignments, iterations) that an algorithm performs as a function of the input size.

### Constants and Lower-Order Terms:

In Big O notation, constants and lower-order terms are dropped. For example, O(2n^2 + 3n + 1) simplifies to O(n^2).

## Advanced Time Complexity Analysis:

### Best, Worst, and Average Cases:

- Algorithms can have different time complexities in best-case, worst-case, and average-case scenarios.
- It's often crucial to analyze the worst-case time complexity as it guarantees that the algorithm will perform efficiently for all inputs.

### Amortized Analysis:

- Some algorithms have varying runtimes but have an average time complexity that is better than the worst case.
- Amortized analysis calculates the average cost of a sequence of operations and can show that, on average, each operation has a certain time complexity.

### Space Complexity:

- While Big O notation is primarily used for time complexity analysis, you can also analyze the space complexity of algorithms.
- Space complexity describes how the memory usage scales with the input size.

## Python Example Code:

Let's explore some Python examples to demonstrate common time complexities using Big O notation:

### O(1) - Constant Time:

```python
def constant_time_example(lst):
    return lst[0]

# Regardless of the list size, this function takes constant time.
```

### O(n) - Linear Time:

```python
def linear_time_example(lst, target):
    for item in lst:
        if item == target:
            return True
    return False

# The time complexity is O(n) because it scales linearly with the list size.
```

### O(n^2) - Quadratic Time:

```python
def quadratic_time_example(lst):
    result = []
    for i in lst:
        for j in lst:
            result.append(i + j)

# The time complexity is O(n^2) because it involves nested loops.
```

### O(log n) - Logarithmic Time:

```python
def binary_search(lst, target):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Binary search has a time complexity of O(log n) due to halving the search space in each step.
```

### O(n log n) - Linearithmic Time:

```python
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

# Merge sort has a time complexity of O(n log n) due to the divide-and-conquer strategy.
```

### O(2^n) - Exponential Time:

```python
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# The recursive Fibonacci algorithm has a time complexity of O(2^n).
```