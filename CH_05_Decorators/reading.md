# Table of contents

- [Table of contents](#table-of-contents)
- [Overview](#overview)
  - [Key Concepts:](#key-concepts)
  - [Basic Decorator Example:](#basic-decorator-example)
  - [Common Use Cases:](#common-use-cases)
  - [Decorator Stacks:](#decorator-stacks)
  - [Creating Decorators with Arguments:](#creating-decorators-with-arguments)
  - [Decorator Libraries:](#decorator-libraries)
- [Some more advanced decorators examples](#some-more-advanced-decorators-examples)
  - [1. Authentication and Authorization:](#1-authentication-and-authorization)
  - [2. Performance Profiling:](#2-performance-profiling)
  - [3. Cache Function Results:](#3-cache-function-results)
  - [4. API Rate Limiting:](#4-api-rate-limiting)
- [Decorating functions](#decorating-functions)
  - [1. Basic Function Decoration:](#1-basic-function-decoration)
  - [2. Decorating Functions with Arguments:](#2-decorating-functions-with-arguments)
  - [3. Decorator with Arguments:](#3-decorator-with-arguments)
  - [4. Function Metadata Preservation:](#4-function-metadata-preservation)
  - [5. Method Decoration:](#5-method-decoration)
  - [6. Chaining Multiple Decorators:](#6-chaining-multiple-decorators)
  - [7. Real-World Use Case: Timing Function Execution:](#7-real-world-use-case-timing-function-execution)
- [functools.wraps decorator](#functoolswraps-decorator)
  - [1. Basic Usage:](#1-basic-usage)
  - [2. Method Decoration:](#2-method-decoration)
  - [3. Decorator with Arguments:](#3-decorator-with-arguments-1)
  - [4. Decorator with Class Methods:](#4-decorator-with-class-methods)
  - [5. Stacking Decorators:](#5-stacking-decorators)
- [When debugging using decorators](#when-debugging-using-decorators)
  - [Complex Real-World Example: Profiling Function Execution](#complex-real-world-example-profiling-function-execution)
  - [How Decorators Are Useful in Debugging and Profiling:](#how-decorators-are-useful-in-debugging-and-profiling)
- [Decorating class functions](#decorating-class-functions)
  - [Basic Method Decoration:](#basic-method-decoration)
  - [Method Decoration with Arguments:](#method-decoration-with-arguments)
  - [Method Decoration with Class Attributes:](#method-decoration-with-class-attributes)
  - [Stacking Multiple Decorators on a Method:](#stacking-multiple-decorators-on-a-method)
  - [Complex Real-World Example: Authentication and Authorization:](#complex-real-world-example-authentication-and-authorization)
- [Decorating classes](#decorating-classes)
  - [Class Decorators for Adding Attributes:](#class-decorators-for-adding-attributes)
  - [Complex Real-World Example: Singleton Pattern:](#complex-real-world-example-singleton-pattern)
  - [Metaclasses for Class Modification:](#metaclasses-for-class-modification)
  - [Complex Real-World Example: Model-View-Controller (MVC) Framework:](#complex-real-world-example-model-view-controller-mvc-framework)
- [Memoization using decorators](#memoization-using-decorators)
- [functools.lru\_cache alternatives?](#functoolslru_cache-alternatives)
- [Decorators with (optional) arguments](#decorators-with-optional-arguments)
  - [Basic Decorator Factory with Optional Arguments:](#basic-decorator-factory-with-optional-arguments)
  - [Complex Real-World Example: Authorization Decorator Factory:](#complex-real-world-example-authorization-decorator-factory)
  - [Decorator Factory with Optional Configuration:](#decorator-factory-with-optional-configuration)
- [__init__ and __call__ version](#init-and-call-version)
- [classmethod, staticmethod and @property](#classmethod-staticmethod-and-property)
  - [1. `classmethod`:](#1-classmethod)
  - [2. `staticmethod`:](#2-staticmethod)
  - [3. `property`:](#3-property)
- [Singletons](#singletons)
- [Implementing the singleton pattern using the `@functools.wraps` decorator](#implementing-the-singleton-pattern-using-the-functoolswraps-decorator)
- [functools.singledispatch](#functoolssingledispatch)
- [Contextmanager](#contextmanager)
- [Validation, type checks, and conversions](#validation-type-checks-and-conversions)
  - [1. Validation Decorator:](#1-validation-decorator)
  - [2. Type Check Decorator:](#2-type-check-decorator)
  - [3. Data Conversion Decorator:](#3-data-conversion-decorator)
- [ignore Useless warnings](#ignore-useless-warnings)

# Overview

- A powerful and flexible **feature** in Python that allow you to **modify or enhance** the behavior of **functions** or methods **without changing their** source **code**. 
- They are essentially functions that wrap other functions or methods to **extend or modify** their **functionality**. 
- Decorators are commonly used for **tasks** such as **logging, authorization, validation**, and more.

## Key Concepts:

1. **Decorator Function:** A decorator is a regular Python function that takes another function as its argument and typically returns a new function that adds some functionality to the original function.

2. **Function Wrapping:** Decorators wrap functions or methods, allowing you to execute code before and/or after the wrapped function. This is achieved by defining a wrapper function inside the decorator.

3. **Use of "@" Syntax:** Decorators are often applied using the "@" syntax followed by the decorator function name above the function or method to be decorated. This makes the code more readable and intuitive.

## Basic Decorator Example:

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

Output:
```
Something is happening before the function is called.
Hello!
Something is happening after the function is called.
```

## Common Use Cases:

1. **Logging:** Decorators can be used to log function calls, including arguments and return values.

2. **Authorization:** You can use decorators to check whether a user is authorized to access certain parts of your application.

3. **Caching:** Decorators can cache the results of expensive function calls to improve performance.

4. **Validation:** Decorators can validate function arguments before executing the function.

5. **Timing:** Measure the execution time of functions using decorators.

## Decorator Stacks:

- You can apply **multiple decorators** to a single function. 
- They are **executed in the order** in which they are applied, **from top to bottom**

```python
@decorator1
@decorator2
def my_function():
    pass
```

## Creating Decorators with Arguments:

- You can create decorators that accept arguments by **adding an extra layer of nested functions**. 
- This allows you to customize the behavior of the decorator. 

## Decorator Libraries:

Python has a rich ecosystem of decorator libraries, including `functools.wraps` for preserving the original function's **metadata**, and libraries like Flask and Django that provide decorators for building web applications.

# Some more advanced decorators examples

## 1. Authentication and Authorization:

- You can use decorators to enforce authentication and authorization in web applications. 
- For example, in a Flask web application, you can create a decorator that checks if a user is logged in and has the necessary permissions to access a particular route:

```python
from functools import wraps
from flask import Flask, request, redirect, url_for

app = Flask(__name__)

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated:
            return redirect(url_for('login'))
        return func(*args, **kwargs)
    return wrapper

@app.route('/dashboard')
@login_required
def dashboard():
    return 'Welcome to the dashboard!'
```

## 2. Performance Profiling:

You can create a decorator to profile the execution time of functions:

```python
import time

def profile_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds to execute.")
        return result
    return wrapper

@profile_execution_time
def expensive_function():
    # Some time-consuming task
    time.sleep(2)

expensive_function()
```

The `profile_execution_time` decorator measures and prints the time taken by `expensive_function` to execute.

## 3. Cache Function Results:

Decorators can be used to implement a caching mechanism for functions, which can be especially useful for expensive calculations:

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

result = fibonacci(100)  # Cached result for faster subsequent calls
```

The `@lru_cache` decorator memoizes the results of the `fibonacci` function, improving performance for repeated calculations.

## 4. API Rate Limiting:

For web APIs, decorators can enforce rate limiting to prevent abuse:

```python
from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)

def rate_limit(limit, per):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = f"rate_limit_{request.remote_addr}_{func.__name__}"
            current_time = int(time.time())
            if not redis.exists(key):
                redis.setex(key, per, current_time)
                return func(*args, **kwargs)
            else:
                last_request_time = int(redis.get(key))
                if current_time - last_request_time >= per:
                    redis.setex(key, per, current_time)
                    return func(*args, **kwargs)
                else:
                    return jsonify(message="Rate limit exceeded"), 429
        return wrapper
    return decorator

@app.route('/api/resource')
@rate_limit(limit=5, per=60)  # Allow 5 requests per minute
def protected_resource():
    return jsonify(message="You have access to the protected resource.")
```

# Decorating functions

- Using decorators, which are functions that modify the behavior of other functions or methods. 
- Decorators are a powerful tool for adding functionality to functions without modifying their source code. 

## 1. Basic Function Decoration:

In its simplest form, a decorator is a function that takes another function as an argument and returns a modified version of that function.

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

Output:
```
Something is happening before the function is called.
Hello!
Something is happening after the function is called.
```

## 2. Decorating Functions with Arguments:

You can create decorators that work with functions taking arguments by using `*args` and `**kwargs`:

```python
def arg_printer(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}, Keyword arguments: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@arg_printer
def add(a, b):
    return a + b

result = add(3, 5)
# Output: Arguments: (3, 5), Keyword arguments: {}
# result is 8
```

## 3. Decorator with Arguments:

Decorators themselves can take arguments by adding an extra layer of nested functions.

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

Output:
```
Hello, Alice!
Hello, Alice!
Hello, Alice!
```

The `repeat` decorator takes an argument `n` and repeats the decorated function call `n` times.

## 4. Function Metadata Preservation:

When creating decorators, it's essential to preserve the metadata (e.g., function name and docstring) of the original function. You can use the `functools.wraps` decorator for this purpose:

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before the function is called.")
        result = func(*args, **kwargs)
        print("After the function is called.")
        return result
    return wrapper

@my_decorator
def my_function():
    """This is the docstring."""
    print("Hello!")

print(my_function.__name__)  # Output: my_function
print(my_function.__doc__)   # Output: This is the docstring.
```

The `@wraps(func)` decorator preserves the metadata of `my_function`.

## 5. Method Decoration:

You can decorate class methods as well. 

```python
class MyClass:
    def __init__(self, value):
        self.value = value

    @arg_printer
    def print_value(self):
        print(f"Value: {self.value}")

obj = MyClass(42)
obj.print_value()
# Output: Arguments: (<MyClass object at 0x...>,), Keyword arguments: {}
# Value: 42
```

## 6. Chaining Multiple Decorators:

You can apply multiple decorators to a single function, and they are executed in the order they are applied:

```python
@decorator1
@decorator2
def my_function():
    pass
```

## 7. Real-World Use Case: Timing Function Execution:

- A real-world use case where a decorator is used to measure the execution time of a function:

```python
import time

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds to execute.")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(2)

slow_function()
# Output: slow_function took 2.0000 seconds to execute.
```

# functools.wraps decorator

- A powerful tool for preserving the metadata (e.g., function name, docstring, and annotations) of a wrapped function. 

## 1. Basic Usage:

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # Preserve metadata
    def wrapper(*args, **kwargs):
        print("Before the function is called.")
        result = func(*args, **kwargs)
        print("After the function is called.")
        return result
    return wrapper

@my_decorator
def my_function():
    """This is the docstring."""
    print("Hello!")

print(my_function.__name__)  # Output: my_function
print(my_function.__doc__)   # Output: This is the docstring.
```

## 2. Method Decoration:

```python
from functools import wraps

def log_args_and_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

class Calculator:
    @log_args_and_result
    def add(self, a, b):
        return a + b

calc = Calculator()
result = calc.add(3, 5)
# Output:
# Calling add with arguments: (<Calculator object at 0x...>, 3, 5), {}
# add returned: 8
```

## 3. Decorator with Arguments:

```python
from functools import wraps

def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
                print(f"Function {func.__name__} called {n} times, result: {result}")
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    return f"Hello, {name}!"

greet("Alice")
# Output:
# Function greet called 3 times, result: Hello, Alice!
# Function greet called 3 times, result: Hello, Alice!
# Function greet called 3 times, result: Hello, Alice!
```

## 4. Decorator with Class Methods:

```python
from functools import wraps

def log_class_method_calls(cls_method):
    @wraps(cls_method)
    def wrapper(self, *args, **kwargs):
        print(f"Calling {cls_method.__name__} of {self.__class__.__name__} with arguments: {args}, {kwargs}")
        result = cls_method(self, *args, **kwargs)
        print(f"{cls_method.__name__} of {self.__class__.__name__} returned: {result}")
        return result
    return wrapper

class MyClass:
    @log_class_method_calls
    def my_method(self, x):
        return 2 * x

obj = MyClass()
result = obj.my_method(5)
# Output:
# Calling my_method of MyClass with arguments: (5,), {}
# my_method of MyClass returned: 10
```

## 5. Stacking Decorators:

```python
from functools import wraps

def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Decorator 1 before")
        result = func(*args, **kwargs)
        print("Decorator 1 after")
        return result
    return wrapper

def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Decorator 2 before")
        result = func(*args, **kwargs)
        print("Decorator 2 after")
        return result
    return wrapper

@decorator1
@decorator2
def my_function():
    print("Function")

my_function()
# Output:
# Decorator 1 before
# Decorator 2 before
# Function
# Decorator 2 after
# Decorator 1 after
```

# When debugging using decorators

- Decorators are incredibly useful in many aspects of software development, including debugging, code organization, and adding cross-cutting concerns to functions and methods. 
- They offer a clean and modular way to extend or modify the behavior of functions without altering their source code. 

## Complex Real-World Example: Profiling Function Execution

- Let's say you're working on a large Python codebase, and you want to profile the execution time of various functions to identify performance bottlenecks. 
- Using decorators, you can create a profiling decorator that logs the execution time of functions.
- This can be especially valuable in complex applications where optimizing specific functions is critical.

```python
import time
from functools import wraps

def profile_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds to execute.")
        return result
    return wrapper

# Usage example:
@profile_execution_time
def complex_algorithm(n):
    """A complex algorithm we want to profile."""
    result = 0
    for i in range(n):
        result += i
    return result

@profile_execution_time
def another_complex_function():
    """Another complex function to profile."""
    time.sleep(2)

# Calling the decorated functions
result = complex_algorithm(1000000)
another_complex_function()

# Output:
# complex_algorithm took 0.0100 seconds to execute.
# another_complex_function took 2.0000 seconds to execute.
```

## How Decorators Are Useful in Debugging and Profiling:

1. **Clean Codebase:** Decorators keep your codebase clean and maintainable by separating profiling logic from the core functionality of your functions. You don't need to clutter your functions with profiling code.

2. **Reusability:** You can easily reuse the `profile_execution_time` decorator to profile other functions in your codebase without duplicating profiling code.

3. **Consistency:** Profiling is applied consistently to functions with minimal effort. It ensures that all relevant functions are profiled consistently.

4. **Debugging:** If you encounter performance issues, you can quickly identify which functions are taking the most time and focus your debugging efforts on those areas.

5. **Production vs. Development:** You can enable or disable profiling selectively in different environments (e.g., development vs. production) by toggling the use of the decorator.

6. **Documentation:** The `functools.wraps` decorator helps preserve function metadata, including docstrings, making it easier to understand the purpose of each function.

**In complex applications**
- profiling decorators like this one can be invaluable for pinpointing performance bottlenecks and optimizing critical code paths. 
- They demonstrate how decorators provide a powerful and modular way to extend and enhance your codebase, making it more maintainable and easier to debug.

# Decorating class functions

- Also known as methods, is similar to decorating regular functions. 
- Decorators are functions that take another function (or method) as an argument and return a new function that can extend or modify the behavior of the original method. 

## Basic Method Decoration:

- Decorating a class method just like a regular function:

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the method is called.")
        result = func(*args, **kwargs)
        print("After the method is called.")
        return result
    return wrapper

class MyClass:
    @my_decorator
    def my_method(self):
        print("Hello from my_method!")

obj = MyClass()
obj.my_method()
```

## Method Decoration with Arguments:

- Decorating class methods that take arguments by using `*args` and `**kwargs`:

```python
def arg_printer(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}, Keyword arguments: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

class Calculator:
    @arg_printer
    def add(self, a, b):
        return a + b

calc = Calculator()
result = calc.add(3, 5)
```

## Method Decoration with Class Attributes:

- Decorating methods that access class attributes requires a slightly different approach:

```python
def log_attribute_access(func):
    def wrapper(self, *args, **kwargs):
        print(f"Accessing attribute '{func.__name__}'")
        return func(self, *args, **kwargs)
    return wrapper

class Person:
    def __init__(self, name):
        self.name = name

    @log_attribute_access
    def greet(self):
        return f"Hello, my name is {self.name}."

person = Person("Alice")
message = person.greet()
```

## Stacking Multiple Decorators on a Method:

- Can apply multiple decorators to a single class method, and they are executed in the order they are applied:

```python
@decorator1
@decorator2
def my_method(self):
    pass
```

## Complex Real-World Example: Authentication and Authorization:

Decorators are often used for authentication and authorization in web applications. 

```python
from functools import wraps
from flask import request, redirect, url_for

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated:
            return redirect(url_for('login'))
        return func(*args, **kwargs)
    return wrapper

class User:
    def __init__(self, username, authenticated=False):
        self.username = username
        self.authenticated = authenticated

current_user = User("Alice", authenticated=True)

class App:
    @login_required
    def dashboard(self):
        return f"Welcome to the dashboard, {current_user.username}!"

app = App()
dashboard_page = app.dashboard()
```

# Decorating classes

- Involves adding functionality or modifying the behavior of a class as a whole, rather than individual methods. 
- This can be done by creating a metaclass or using class decorators.

## Class Decorators for Adding Attributes:

- Used to add attributes or modify the behavior of classes. 
- They work similarly to function decorators but are applied to classes.

```python
def add_attribute(cls):
    cls.new_attribute = "Added by decorator"
    return cls

@add_attribute
class MyClass:
    pass

obj = MyClass()
print(obj.new_attribute)  # Output: "Added by decorator"
```

## Complex Real-World Example: Singleton Pattern:

A common use case for class decorators is implementing the Singleton pattern, where only one instance of a class should exist.

```python
def singleton(cls):
    instances = {}

    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class DatabaseConnection:
    def __init__(self, connection_string):
        self.connection_string = connection_string

db1 = DatabaseConnection("db_connection_string_1")
db2 = DatabaseConnection("db_connection_string_2")

print(db1 is db2)  # Output: True
```

## Metaclasses for Class Modification:

- Metaclasses are a more advanced way to modify classes at a higher level. 
- They allow you to control the creation and behavior of classes themselves.

```python
class MyMeta(type):
    def __init__(cls, name, bases, attrs):
        cls.new_attribute = "Added by metaclass"
        super().__init__(name, bases, attrs)

class MyClass(metaclass=MyMeta):
    pass

obj = MyClass()
print(obj.new_attribute)  # Output: "Added by metaclass"
```

## Complex Real-World Example: Model-View-Controller (MVC) Framework:

- A complex real-world example of metaclasses is building a simplified MVC framework. 
- The metaclass defines the base behavior of controllers, which handle HTTP requests and interact with models and views:

```python
class ControllerMeta(type):
    def __init__(cls, name, bases, attrs):
        if "routes" not in attrs:
            cls.routes = {}
        super().__init__(name, bases, attrs)

class BaseController(metaclass=ControllerMeta):
    def __init__(self, request):
        self.request = request

    @classmethod
    def add_route(cls, route, method):
        def decorator(handler):
            cls.routes[(route, method)] = handler
            return handler
        return decorator

class UserController(BaseController):
    @BaseController.add_route("/user/profile", "GET")
    def profile(self):
        return f"User profile for {self.request.user}"

class ArticleController(BaseController):
    @BaseController.add_route("/article/view/<int:article_id>", "GET")
    def view(self, article_id):
        return f"Viewing article {article_id}"

# Example usage in a web framework
request = {"user": "Alice", "method": "GET"}
user_controller = UserController(request)
article_controller = ArticleController(request)

print(user_controller.routes)  # Output: {('/user/profile', 'GET'): <function UserController.profile at 0x...>}
print(article_controller.routes)  # Output: {('/article/view/<int:article_id>', 'GET'): <function ArticleController.view at 0x...>}
```

# Memoization using decorators

- A technique used to optimize expensive function calls by caching their results. 
- It's particularly useful when a function is called multiple times with the same inputs, as it can save computation time. 
- Using decorators, you can easily implement memoization for functions. 

1. **Recursive Functions with Overlapping Subproblems:**
   Recursive functions like Fibonacci or factorial can benefit from memoization to avoid redundant calculations.

   ```python
   from functools import lru_cache

   @lru_cache(maxsize=None)
   def fibonacci(n):
       if n <= 1:
           return n
       else:
           return fibonacci(n-1) + fibonacci(n-2)
   ```

2. **Computation-Intensive Functions:**
   Functions that perform complex and time-consuming computations, such as mathematical or scientific calculations, can be significantly sped up with memoization.

   ```python
   from functools import lru_cache

   @lru_cache(maxsize=None)
   def expensive_computation(x, y):
       # Expensive computation
       return result
   ```

3. **I/O Operations:**
   Functions that involve reading from a file or making network requests can benefit from memoization to store and reuse results.

   ```python
   from functools import lru_cache

   @lru_cache(maxsize=None)
   def fetch_data(url):
       # Fetch data from the internet
       return data
   ```

4. **Dynamic Programming:**
   In dynamic programming problems, memoization is often used to store and reuse intermediate results in a top-down approach.

   ```python
   from functools import lru_cache

   @lru_cache(maxsize=None)
   def knapsack(items, capacity):
       # Solve knapsack problem with memoization
       return max_value
   ```

5. **Database Queries:**
   When working with databases, memoization can be used to cache query results to avoid hitting the database multiple times for the same query.

   ```python
   from functools import lru_cache

   @lru_cache(maxsize=None)
   def query_database(query):
       # Execute a database query and return results
       return results
   ```

6. **Web Scraping:**
   In web scraping tasks, memoization can store the results of HTTP requests and parsing to reduce the load on the web server and speed up subsequent requests.

   ```python
   from functools import lru_cache

   @lru_cache(maxsize=None)
   def scrape_webpage(url):
       # Fetch and parse webpage
       return data
   ```

7. **Function Calls with Immutable Arguments:**
   Any function that takes immutable arguments and has a deterministic output can be memoized for performance improvement.

   ```python
   from functools import lru_cache

   @lru_cache(maxsize=None)
   def calculate_hash(data):
       # Calculate and return a hash value
       return hash(data)
   ```

8. **Simulations and Games:**
   In simulations or game AI, memoization can store computed states to avoid reevaluating the same state multiple times.

   ```python
   from functools import lru_cache

   @lru_cache(maxsize=None)
   def evaluate_game_state(board):
       # Evaluate the game state with memoization
       return score
   ```

9. **Machine Learning Model Predictions:**
   For machine learning models, memoization can be used to store and reuse predictions for the same input data.

   ```python
   from functools import lru_cache

   @lru_cache(maxsize=None)
   def predict(model, data):
       # Make predictions using the model with memoization
       return predictions
   ```

10. **Custom Caching Logic:**
    You can also implement custom memoization strategies using decorators, tailoring the cache behavior to your specific needs.

    ```python
    def custom_memoization_decorator(func):
        cache = {}

        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items()))
            if key in cache:
                return cache[key]
            result = func(*args, **kwargs)
            cache[key] = result
            return result

        return wrapper
    ```

# functools.lru_cache alternatives?

The `functools.lru_cache` is a built-in Python decorator that provides a simple and efficient way to implement memoization with a least recently used (LRU) cache. It's commonly used because it offers several advantages:

1. **Efficiency:** `lru_cache` is highly efficient due to its LRU eviction policy. It automatically removes the least recently used items from the cache when it reaches its specified size (`maxsize` argument), ensuring that the cache doesn't grow indefinitely.

2. **Ease of Use:** It's easy to apply `lru_cache` as a decorator to any function or method. You can set the cache size and customize its behavior with optional arguments.

3. **Automatic Cache Maintenance:** `lru_cache` handles cache maintenance, including adding, updating, and evicting items, without manual intervention.

4. **Thread-Safe:** `lru_cache` is thread-safe, making it suitable for multi-threaded or multi-process applications without the need for additional synchronization.

However, if you prefer not to use `lru_cache` or need more flexibility in your memoization strategy, you can implement custom memoization logic using dictionaries or other data structures. 

```python
def custom_memoization_decorator(func):
    cache = {}

    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key in cache:
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result

    return wrapper
```

With this custom decorator, you can control the memoization strategy, cache eviction policy, and other aspects of caching based on your specific requirements. This approach provides more flexibility but may require additional code to handle cache management.

# Decorators with (optional) arguments

- Allow you to create more flexible decorators that can be configured with different settings or behaviors depending on how they are used. 
- To implement decorators with optional arguments, you need to create a decorator factory—a function that returns a decorator.

## Basic Decorator Factory with Optional Arguments:

- A function that returns a decorator. 
- It can accept optional arguments and customize the decorator's behavior.

```python
def my_decorator_factory(arg1, arg2):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Decorator with arguments: {arg1}, {arg2}")
            result = func(*args, **kwargs)
            return result
        return wrapper
    return my_decorator

@my_decorator_factory("foo", "bar")
def my_function():
    print("Function")

my_function()
```

## Complex Real-World Example: Authorization Decorator Factory:

- Creating an authorization decorator factory that allows specifying different access levels for different functions:

```python
def authorization_decorator_factory(access_level):
    def authorization_decorator(func):
        def wrapper(*args, **kwargs):
            user = args[0].user  # Assuming the first argument is a user object
            if user.has_access(access_level):
                return func(*args, **kwargs)
            else:
                raise PermissionError("Access denied")

        return wrapper
    return authorization_decorator

class User:
    def __init__(self, access_level):
        self.access_level = access_level

    def has_access(self, required_level):
        return self.access_level >= required_level

class SecureApp:
    def __init__(self, user):
        self.user = user

    @authorization_decorator_factory(2)  # Requires access level 2
    def sensitive_operation(self):
        print("Sensitive operation performed")

user = User(access_level=3)
app = SecureApp(user)
app.sensitive_operation()
```

## Decorator Factory with Optional Configuration:

- Decorator factories can also accept optional configuration settings, allowing you to fine-tune the decorator's behavior:

```python
def timer_decorator_factory(unit="seconds"):
    def timer_decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time

            if unit == "milliseconds":
                print(f"Execution time: {execution_time * 1000} ms")
            elif unit == "seconds":
                print(f"Execution time: {execution_time} s")
            else:
                raise ValueError("Invalid unit")

            return result
        return wrapper
    return timer_decorator

@timer_decorator_factory(unit="milliseconds")
def slow_function():
    time.sleep(1)

slow_function()
```

# __init__ and __call__ version

- Creating decorators using classes in Python involves defining a class that implements the `__init__` and `__call__` methods. 
- The `__init__` method initializes the decorator with any optional arguments, and the `__call__` method is where the actual decoration takes place. 
- An example of creating a class-based decorator with `functools.update_wrapper` instead of `functools.wraps` for better control:

```python
import functools

class MyDecorator:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def __call__(self, func):
        @functools.wraps(func)  # This ensures the decorated function retains its original metadata
        def wrapper(*args, **kwargs):
            print(f"Decorator with arguments: {self.arg1}, {self.arg2}")
            result = func(*args, **kwargs)
            return result
        functools.update_wrapper(wrapper, func)  # Manually update wrapper's metadata
        return wrapper

# Using the class-based decorator with optional arguments
@MyDecorator("foo", "bar")
def my_function():
    """My function docstring"""
    print("Function")

my_function()

print("Function name:", my_function.__name__)  # Output: "my_function"
print("Function docstring:", my_function.__doc__)  # Output: "My function docstring"
```

Best practices for class-based decorators:

1. Always define the `__init__` method to accept any optional configuration arguments for the decorator.

2. Implement the `__call__` method to perform the actual decoration, including creating a wrapper function that calls the original function.

3. Use `functools.wraps` or `functools.update_wrapper` to ensure that the decorated function retains its original metadata, such as name and docstring. This helps maintain code readability and documentation.

4. Apply the class-based decorator to functions or methods using the `@` syntax, just like you would with function-based decorators.

- Class-based decorators provide a structured and reusable way to decorate functions or methods while allowing for configuration and customization. 
- The use of `functools.update_wrapper` ensures that the decorator maintains the original function's metadata, which is a best practice for maintaining code quality and documentation.

# classmethod, staticmethod and @property

- Using various decorators to modify the behavior or properties of class methods. 
- Three commonly used class function decorators are `classmethod`, `staticmethod`, and `property`.

## 1. `classmethod`:

- Used to define a method that operates on the class itself rather than on instances of the class. 
- It takes the class as its first argument (usually named `cls`) instead of an instance (usually named `self`). 
- Class methods are often used for utility methods, factory methods, or methods that need access to class-level attributes or behavior.

```python
class MyClass:
    class_variable = "I am a class variable"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @classmethod
    def class_method(cls):
        return cls.class_variable

# Usage:
obj = MyClass("Instance data")
print(MyClass.class_method())  # Output: "I am a class variable"
```

## 2. `staticmethod`:

- Used to define a method that does not depend on the class or instance state. 
- It behaves like a regular function but is defined within the class's namespace for organization purposes. 
- Static methods do not take the class or instance as their first argument, making them similar to functions defined outside the class.

```python
class MyClass:
    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @staticmethod
    def static_method():
        return "I am a static method"

# Usage:
obj = MyClass("Instance data")
print(MyClass.static_method())  # Output: "I am a static method"
```

## 3. `property`:

- Used to define getter and setter methods for class attributes. 
- It allows you to encapsulate attribute access and provide custom logic when getting or setting the attribute's value.

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero.")
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

# Usage:
temp = Temperature(25)
print(temp.celsius)  # Output: 25
print(temp.fahrenheit)  # Output: 77.0

temp.celsius = 30
print(temp.fahrenheit)  # Output: 86.0

# Attempting to set an invalid temperature
temp.celsius = -300  # Raises a ValueError
```

# Singletons

- Ensuring that a class has only one instance, is a common application of decorating classes in Python. - You can use decorators to ensure that a class is instantiated only once and reuse the existing instance for subsequent calls. 

```python
def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class DatabaseConnection:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connect()  # Simulate connecting to a database

    def connect(self):
        print(f"Connected to database: {self.connection_string}")

    def query(self, sql):
        print(f"Executing query: {sql}")

# Usage
db1 = DatabaseConnection("db_connection_string_1")
db2 = DatabaseConnection("db_connection_string_2")

# Both db1 and db2 refer to the same instance
print(db1 is db2)  # Output: True

db1.query("SELECT * FROM table1")
```

# Implementing the singleton pattern using the `@functools.wraps` decorator 

```python
import functools

def singleton(cls):
    instances = {}

    @functools.wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class DatabaseConnection:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connect()  # Simulate connecting to a database

    def connect(self):
        print(f"Connected to database: {self.connection_string}")

    def query(self, sql):
        print(f"Executing query: {sql}")

# Usage
db1 = DatabaseConnection("db_connection_string_1")
db2 = DatabaseConnection("db_connection_string_2")

# Both db1 and db2 refer to the same instance
print(db1 is db2)  # Output: True

db1.query("SELECT * FROM table1")
```

# functools.singledispatch

- Single dispatch is a form of polymorphism where the implementation of a function is determined by the type of a single argument. 
- Python doesn't have built-in support for single dispatch, but you can implement it using the `functools.singledispatch` decorator. 
- This decorator allows you to define specialized implementations of a function for different argument types. 

```python
from functools import singledispatch

@singledispatch
def process_data(data):
    """Fallback function for unsupported data types."""
    raise NotImplementedError("Unsupported data type")

@process_data.register(int)
def process_int(data):
    """Specialized function for integers."""
    print(f"Processing integer: {data}")

@process_data.register(str)
def process_str(data):
    """Specialized function for strings."""
    print(f"Processing string: {data}")

@process_data.register(list)
def process_list(data):
    """Specialized function for lists."""
    print(f"Processing list with {len(data)} elements")

# Usage
process_data(42)  # Output: Processing integer: 42
process_data("Hello")  # Output: Processing string: Hello
process_data([1, 2, 3])  # Output: Processing list with 3 elements

# Unsupported data type (will raise a NotImplementedError)
process_data(3.14)
```

# Contextmanager

- context managers are typically implemented using classes that define `__enter__` and `__exit__` methods. 
- However, you can also create context managers using decorators in combination with generator functions. 
- This approach allows you to define a context manager using the `with` statement and the `@contextmanager` decorator from the `contextlib` module.

```python
from contextlib import contextmanager

@contextmanager
def my_context_manager():
    # Code to enter the context (equivalent to __enter__)
    print("Entering the context")
    yield  # This is where the context begins

    # Code to exit the context (equivalent to __exit__)
    print("Exiting the context")

# Usage
with my_context_manager():
    print("Inside the context")
```
When you run this code, it produces the following output:

```
Entering the context
Inside the context
Exiting the context
```

The `@contextmanager` decorator simplifies the creation of context managers by allowing you to use generator functions. This approach is particularly useful when you need to set up and tear down resources or perform cleanup tasks, such as file handling, database connections, or acquiring and releasing locks.

# Validation, type checks, and conversions

- Decorators can be used to implement validation, type checks, and data conversions in Python. 
- They provide a way to add additional functionality to functions or methods, including checking input parameters and modifying return values. 

## 1. Validation Decorator:

You can create a decorator that checks if certain conditions are met before a function is executed. For example, you can create a validation decorator to check if an argument meets specific criteria.

```python
def validate_positive_arg(func):
    def wrapper(arg):
        if arg < 0:
            raise ValueError("Argument must be positive")
        return func(arg)
    return wrapper

@validate_positive_arg
def calculate_square_root(x):
    return x ** 0.5

result = calculate_square_root(25)  # Valid input
print(result)  # Output: 5.0

# Raises a ValueError due to negative input
result = calculate_square_root(-25)
```

## 2. Type Check Decorator:

- A decorator that checks the types of function arguments and return values to ensure they match the expected types.

```python
def type_check(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError("Arguments must be integers")
        result = func(*args, **kwargs)
        if not isinstance(result, int):
            raise TypeError("Result must be an integer")
        return result
    return wrapper

@type_check
def add_numbers(a, b):
    return a + b

result = add_numbers(10, 5)  # Valid input
print(result)  # Output: 15

# Raises a TypeError due to non-integer input
result = add_numbers(10, "5")
```

## 3. Data Conversion Decorator:

- A decorator that converts data types, allowing a function to accept different types of input and return a standardized type.

```python
def convert_to_int(func):
    def wrapper(arg):
        if isinstance(arg, str):
            arg = int(arg)
        return func(arg)
    return wrapper

@convert_to_int
def double_number(x):
    return x * 2

result = double_number(5)  # Valid input
print(result)  # Output: 10

# Converts the string "7" to an integer before doubling it
result = double_number("7")
print(result)  # Output: 14
```

# ignore Useless warnings

- Using decorators along with the `functools` and `warnings` libraries to ignore or suppress specific warnings in Python.
- This can be helpful when you want to silence certain types of warnings temporarily within a specific function or method. 

```python
import functools
import warnings

def ignore_warnings(warning_filter):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with warnings.catch_warnings():
                warnings.filterwarnings("ignore", category=warning_filter)
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

# Usage
@ignore_warnings(DeprecationWarning)
def some_function():
    warnings.warn("This is a deprecated warning", DeprecationWarning)
    print("Function executed")

some_function()  # The DeprecationWarning will be ignored
```