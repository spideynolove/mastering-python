# Table of contents

- [Table of contents](#table-of-contents)
- [What are generators?](#what-are-generators)
  - [Generator best practices](#generator-best-practices)
  - [Advantages and disadvantages](#advantages-and-disadvantages)
  - [Pipelines](#pipelines)
  - [tee](#tee)
  - [Generating](#generating)
  - [Context managers](#context-managers)
- [Coroutines](#coroutines)
  - [Examples](#examples)
  - [Priming](#priming)
  - [exceptions](#exceptions)
  - [Bidirectional pipelines](#bidirectional-pipelines)
  - [states](#states)

# What are generators?

- Generators in Python are a type of **iterable**, similar to lists or tuples, but with a crucial difference. 
- While lists and tuples store all their elements in memory, generators generate values on-the-fly as you iterate over them, **one at a time**. 
- This means that generators are **memory-efficient** and particularly useful when **dealing with large datasets** or when you **don't** want to **load all** data into memory **at once**.
- Generators are created using **functions or expressions** that contain one or more `yield` statements. 
- When a function with `yield` is called, it **doesn't execute immediately**; instead, it returns a generator **object**, which **can be iterated** over. 
- **Each time** you iterate over the generator (e.g., with a `for` loop), the function's code is **executed until** it encounters a `yield` statement. 
- At that point, the value following `yield` is **returned**, and the function's state is **paused**. 
- When the generator is iterated **again**, the function **resumes** execution from where it left off, continuing until the next `yield`.

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Create a generator
countdown_gen = countdown(5)

# Iterate over the generator
for num in countdown_gen:
    print(num)
```

Generators are commonly used for:
- Processing **large** datasets or files **line-by-line**, **without reading** the **entire** file **into memory**.
- Implementing **infinite sequences** (e.g., Fibonacci sequence).
- Generating data on-the-fly for computational tasks.
- **Reducing memory usage** in memory-intensive applications.
- Implementing custom iterators.

## Generator best practices

1. **Use Generator Expressions:** Generator expressions are concise and memory-efficient. When you only need to generate values on-the-fly, prefer generator expressions over list comprehensions. For example:

    ```python
    # List comprehension (eager evaluation)
    squares = [x ** 2 for x in range(1, 1000000)]

    # Generator expression (lazy evaluation)
    squares_gen = (x ** 2 for x in range(1, 1000000))
    ```

2. **Lazy Loading:** When reading data from files or databases, load and process data lazily, one chunk or line at a time, rather than loading the entire dataset into memory. This is especially useful for large log files or databases.

3. **Context Managers:** Use context managers (the `with` statement) when working with files or external resources to ensure that resources are properly closed after use. This is essential for generators that read from files.

4. **Chunking:** For very large datasets, process data in smaller chunks or batches. This prevents memory overflow and allows you to process large datasets incrementally.

5. **Filter and Transform:** Use generator functions to filter, transform, or preprocess data as it's generated. This can help reduce the memory footprint by discarding unnecessary data early in the pipeline.

6. **Pipelining:** Chain multiple generator functions together in a pipeline to process data sequentially. This allows for modular and readable code while avoiding loading the entire dataset at once.

7. **Caching:** If you need to reuse data from a generator, consider caching it in memory or using a data structure like a deque (double-ended queue) to store recent values. Be cautious with caching, as it can increase memory usage.

8. **Itertools:** The `itertools` library provides a collection of efficient and memory-friendly functions for working with iterators and generators. Explore functions like `itertools.islice`, `itertools.groupby`, and `itertools.chain`.

9. **Generator Pipelines:** Create complex processing pipelines by chaining together multiple generators. This allows you to build efficient data processing workflows without loading the entire dataset into memory.

10. **Parallel Processing:** In some cases, you can use libraries like `concurrent.futures` or `multiprocessing` to process data in parallel, especially when processing steps are independent.

11. **Memory Profiling:** Use memory profiling tools (e.g., `memory-profiler` library) to monitor and optimize memory usage in your generator code.

12. **Testing and Debugging:** Test your generator functions thoroughly, as debugging can be more challenging due to lazy evaluation. Tools like `pdb` (Python Debugger) can help.

13. **Documentation:** Clearly document how to use your generators, including any dependencies, expected input formats, and the purpose of each generator.

## Advantages and disadvantages 

**Advantages:**

1. **Memory Efficiency:** Generators are memory-efficient because they produce values on-the-fly as needed, rather than storing all values in memory. This is especially advantageous when dealing with large datasets or infinite sequences.

2. **Lazy Evaluation:** Generators use lazy evaluation, meaning they compute values only when requested. This can lead to faster startup times and reduced memory overhead, as not all values are computed upfront.

3. **Infinite Sequences:** Generators are well-suited for generating infinite sequences or streams of data, such as random numbers, sensor readings, or log records, without consuming infinite memory.

4. **Iterative Processing:** Generators enable iterative processing of data. You can process data one item at a time, which is useful for pipelining and filtering data efficiently.

5. **Custom Iterators:** You can create custom iterators with generators, allowing you to define how to iterate over a particular data source or structure.

6. **Improved Readability:** Generators can improve code readability by separating data generation from data processing, leading to cleaner and more modular code.

**Disadvantages:**

1. **Performance Overhead:** Generators can introduce a slight performance overhead due to the function call and state management associated with each iteration. In most cases, this overhead is negligible, but for performance-critical tasks, it's worth considering.

2. **Statefulness:** Generator functions maintain internal state, which can make them less predictable than pure functions. Modifying a generator's state or reusing a generator that has already been exhausted can lead to unexpected behavior.

3. **Limited Random Access:** Generators are inherently sequential. Unlike lists or arrays, you cannot easily access elements at arbitrary positions. This limitation can be a drawback when random access is essential.

4. **Complexity:** Generator code can be more complex to write and understand compared to simple list comprehensions or for loops. Generators require a good understanding of Python's iteration and generator protocols.

5. **Debugging Challenges:** Debugging code that involves generators can be more challenging because of lazy evaluation. Variables and states might not have the expected values at certain breakpoints.

6. **Not Suitable for All Use Cases:** Generators are ideal for processing sequences of data or streaming data sources. However, they may not be the best choice for data structures that require efficient random access, such as large arrays.

## Pipelines 

- Using generators in pipelines is an effective way to **process data** sequentially, **one step at a time**, while maintaining memory efficiency. 
- Pipelines are a series of data processing steps, where each step takes input from the previous step and produces output for the next step. 
- Generators can be particularly useful in building such pipelines for data processing.

```python
# Step 1: Read data from a file and preprocess it
def read_and_preprocess(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            # Preprocess the data (e.g., remove whitespace, convert to lowercase)
            cleaned_data = line.strip().lower()
            yield cleaned_data

# Step 2: Tokenize the preprocessed data
def tokenize_data(data):
    for sentence in data:
        # Tokenize the sentence into words
        tokens = sentence.split()
        yield tokens

# Step 3: Count word frequencies
def count_word_frequencies(tokens):
    word_count = {}
    for token_list in tokens:
        for token in token_list:
            if token in word_count:
                word_count[token] += 1
            else:
                word_count[token] = 1
    yield word_count

# Step 4: Filter words with high frequencies
def filter_words(word_counts, threshold=5):
    filtered_words = {word: count for word, count in word_counts.items() if count >= threshold}
    yield filtered_words

# Step 5: Output the final result
def output_result(filtered_words):
    for word, count in filtered_words.items():
        print(f"{word}: {count}")

# Define the input file path
input_file = 'sample.txt'

# Create a generator pipeline
data_pipeline = output_result(
    filter_words(
        count_word_frequencies(
            tokenize_data(
                read_and_preprocess(input_file)
            )
        )
    )
)

# Execute the pipeline
for _ in data_pipeline:
    pass
```

## tee 

- The `itertools.tee` function in Python's `itertools` library allows you to create **multiple independent iterators** (generators) from a single input iterator. 
- This is useful when you want to process the same data stream in **parallel** or when you need to use the same data multiple times in different parts of your program without reiterating the original iterator.

```python
import itertools

# Create an example input iterator (generator)
def data_stream():
    for i in range(1, 6):
        yield i

# Use itertools.tee to create two independent iterators
iter1, iter2 = itertools.tee(data_stream(), 2)

# Process data using the first iterator
print("First Iterator:")
for item in iter1:
    print(item)

# Process data using the second iterator
print("\nSecond Iterator:")
for item in iter2:
    print(item)
```

```
First Iterator:
1
2
3
4
5

Second Iterator:
1
2
3
4
5
```

Keep in mind the following points when using `itertools.tee`:

- Each iterator produced by `itertools.tee` is independent, meaning they don't share state or interfere with each other.
- `itertools.tee` creates shallow copies of the original iterator, so it's memory-efficient.
- Be cautious when using `tee` with very large data streams, as it creates multiple copies in memory, which can lead to increased memory usage.
- Once an iterator has been exhausted (iterated over completely), it cannot be reused. You'll need to create a new iterator using `itertools.tee` if you want to process the same data again.

## Generating 

- You can use generators to **filter, modify, add, or remove items** from an existing data stream efficiently. 
- Generators allow you to perform these operations lazily, meaning that you **only process and generate items as needed**, which can **save memory and improve performance**. 

1. **Filtering Items**:

   To filter items from a generator, you can use a generator expression with a conditional expression. For example, let's filter out even numbers from a generator:

   ```python
   original_data = (x for x in range(1, 11))
   filtered_data = (x for x in original_data if x % 2 != 0)

   for item in filtered_data:
       print(item)
   ```

2. **Modifying Items**:

   To modify items in a generator, you can use a generator expression with a transformation function. For instance, let's square each number in a generator:

   ```python
   original_data = (x for x in range(1, 6))
   squared_data = (x**2 for x in original_data)

   for item in squared_data:
       print(item)
   ```

   `squared_data` contains squared values of numbers from the `original_data` generator.

3. **Adding Items**:

   To add items to a generator, you can use the `itertools.chain` function to concatenate multiple generators. For example, let's add an extra sequence of numbers to an existing generator:

   ```python
   import itertools

   original_data = (x for x in range(1, 6))
   additional_data = (x for x in range(6, 11))
   combined_data = itertools.chain(original_data, additional_data)

   for item in combined_data:
       print(item)
   ```

   The `combined_data` generator contains all numbers from 1 to 10.

4. **Removing Items**:

   To remove items from a generator, you can use a generator expression with a conditional filter that excludes unwanted items. For instance, let's remove numbers divisible by 3 from a generator:

   ```python
   original_data = (x for x in range(1, 11))
   filtered_data = (x for x in original_data if x % 3 != 0)

   for item in filtered_data:
       print(item)
   ```

## Context managers 

- Context managers, often used with the `with` statement, are a convenient way to **manage resources** like files, network connections, and locks. 
- Python's `contextlib` module provides **decorators** and functions for creating context managers. 
- When combined with generators, you can create custom, advanced context managers with concise code.

1. **Creating a Custom Context Manager with `contextlib.contextmanager`**:

   Suppose you want to create a custom context manager to measure the execution time of a block of code. You can use `contextlib.contextmanager` and a generator function to achieve this:

   ```python
   from contextlib import contextmanager
   import time

   @contextmanager
   def timing():
       start_time = time.time()
       yield
       end_time = time.time()
       elapsed_time = end_time - start_time
       print(f"Elapsed time: {elapsed_time:.4f} seconds")

   # Usage of the custom context manager
   with timing():
       # Code block to measure execution time
       for _ in range(1000000):
           pass
   ```

2. **Chaining Context Managers with `contextlib.ExitStack`**:

   The `contextlib.ExitStack` class allows you to dynamically manage multiple context managers. It's particularly useful when you have a variable number of resources to manage. Here's an example that reads and processes multiple files:

   ```python
   from contextlib import ExitStack

   def process_file(file_name):
       with open(file_name, 'r') as file:
           return file.read()

   files_to_process = ['file1.txt', 'file2.txt', 'file3.txt']

   with ExitStack() as stack:
       file_handles = [stack.enter_context(open(file, 'r')) for file in files_to_process]
       for file_handle in file_handles:
           data = file_handle.read()
           # Process data here
   ```

   The `ExitStack` is used to manage the open file contexts, ensuring that they are properly closed when the block exits, even if an exception occurs.

3. **Combining Generators and Context Managers for Resource Management**:

   Generators can be used within context managers to manage resources. For instance, you might use a generator to read lines from a file and a context manager to handle the file's lifecycle:

   ```python
   from contextlib import contextmanager

   @contextmanager
   def file_reader(file_name):
       try:
           with open(file_name, 'r') as file:
               yield file
       except FileNotFoundError:
           yield None

   def process_lines(file_name):
       with file_reader(file_name) as file:
           if file:
               for line in file:
                   # Process each line
                   print(line.strip())

   process_lines('sample.txt')
   ```

# Coroutines 

- A type of function that can **pause** their **execution**, **yield** control **back** to the **caller**, and **later** resume from where they left off. 
- While coroutines are a broader concept, they are often implemented using generators in Python, specifically with the `yield` keyword. 
- Coroutines are useful for **asynchronous** programming, cooperative **multitasking**, and handling tasks that involve **waiting** for external **events**, such as **I/O operations**. 

1. **Generator vs. Coroutine**:

   - A generator is a function that produces a sequence of values lazily, using the `yield` keyword. It allows you to iterate over a series of values one at a time.
   - A coroutine is a more general concept that extends the capabilities of generators. Coroutines can both yield values and receive values (send) from the calling code.

2. **Creating a Coroutine**:

   To create a coroutine using generators, you define a function with the `async` keyword and use the `yield` keyword to pause execution. You can also use the `await` keyword to asynchronously wait for values from other coroutines or asynchronous tasks.

   ```python
   async def my_coroutine():
       while True:
           value = await some_async_function()
           yield value
   ```

3. **Running a Coroutine**:

   Coroutines are typically executed by an event loop or an asynchronous framework, such as asyncio. The event loop schedules and manages the execution of multiple coroutines concurrently.

   ```python
   import asyncio

   async def main():
       coro1 = my_coroutine()
       coro2 = my_coroutine()
       await asyncio.gather(coro1(), coro2())

   asyncio.run(main())
   ```

4. **Yielding and Sending Values**:

   Coroutines can yield values using `yield`, and they can receive values from the caller using the `await` keyword combined with the `send` method.

   ```python
   async def echo():
       while True:
           received = await asyncio.to_thread(input, "Enter a value: ")
           sent = yield received
           print(f"Received: {sent}")

   async def main():
       coroutine = echo()
       await coroutine.__anext__()  # Advance the coroutine to the first `yield`
       while True:
           value = await coroutine.asend(None)
           if value == 'exit':
               break

   asyncio.run(main())
   ```

5. **Asynchronous I/O**:

   Coroutines are commonly used for asynchronous I/O operations, such as reading and writing files, making network requests, and interacting with databases. They allow you to perform I/O operations without blocking the entire program, enabling concurrent execution.

6. **Concurrency and Parallelism**:

   Coroutines can be used for concurrency, where multiple tasks run concurrently but not necessarily in parallel. To achieve parallelism (true multi-core execution), you can combine coroutines with Python's `concurrent.futures` or third-party libraries like `asyncio` for asynchronous parallelism.

## Examples

1. **Asynchronous Web Scraping with aiohttp**:

   This example demonstrates how to use coroutines for asynchronous web scraping using the `aiohttp` library:

   ```python
   import aiohttp
   import asyncio

   async def fetch_url(url):
       async with aiohttp.ClientSession() as session:
           async with session.get(url) as response:
               return await response.text()

   async def scrape_websites(urls):
       tasks = [fetch_url(url) for url in urls]
       results = await asyncio.gather(*tasks)
       return results

   async def main():
       urls = ["https://example.com", "https://example.org", "https://example.net"]
       results = await scrape_websites(urls)
       for url, content in zip(urls, results):
           print(f"Content from {url}: {len(content)} bytes")

   asyncio.run(main())
   ```

2. **Producer-Consumer Pattern with asyncio.Queue**:

   This example demonstrates a producer-consumer pattern using coroutines and `asyncio.Queue` for concurrent task processing:

   ```python
   import asyncio

   async def producer(queue):
       for i in range(1, 6):
           await asyncio.sleep(1)  # Simulate slow production
           await queue.put(f"Item {i}")

   async def consumer(queue):
       while True:
           item = await queue.get()
           if item is None:
               break
           print(f"Consumed: {item}")
           queue.task_done()

   async def main():
       queue = asyncio.Queue()
       producer_task = asyncio.create_task(producer(queue))
       consumer_task = asyncio.create_task(consumer(queue))

       await asyncio.sleep(3)  # Let the producer work for a while
       await queue.join()  # Wait for all items to be consumed
       await queue.put(None)  # Signal the consumer to exit
       await asyncio.gather(producer_task, consumer_task)  # Wait for tasks to finish

   asyncio.run(main())
   ```
   A producer (`producer`) that adds items to a queue and a consumer (`consumer`) that consumes items concurrently.

3. **Asynchronous File I/O**:

   Using coroutines with asynchronous file I/O can improve file handling in programs that require reading or writing multiple files simultaneously. This example reads multiple files asynchronously:

   ```python
   import asyncio

   async def read_file(file_name):
       async with aiofiles.open(file_name, mode='r') as file:
           content = await file.read()
       return content

   async def main():
       file_names = ["file1.txt", "file2.txt", "file3.txt"]
       tasks = [read_file(file_name) for file_name in file_names]
       results = await asyncio.gather(*tasks)
       for file_name, content in zip(file_names, results):
           print(f"Content from {file_name}:\n{content}")

   asyncio.run(main())
   ```
   `read_file` asynchronously reads the content of each file concurrently.

## Priming 

- Priming generators is a technique that involves **automatically** advancing a generator to its **first** `yield` statement when it is created. 
- This can be achieved using a decorator, such as `functools.wraps`, to wrap the generator function.

```python
import functools

def primed(generator_func):
    @functools.wraps(generator_func)
    def wrapper(*args, **kwargs):
        generator = generator_func(*args, **kwargs)
        next(generator)  # Advance to the first `yield` statement
        return generator
    return wrapper

# Define a generator function
@primed
def my_generator():
    yield "First item"
    yield "Second item"
    yield "Third item"

# Create and use the primed generator
gen = my_generator()
for item in gen:
    print(item)
```

## exceptions 

- Generators in Python can be explicitly closed and can also be used to raise exceptions when needed.

1. **Closing a Generator**:

   You can close a generator manually using the `generator.close()` method. This is often used to signal to the generator that it should exit gracefully. When a generator is closed, any subsequent attempts to `yield` values will raise a `GeneratorExit` exception. Here's an example:

   ```python
   def my_generator():
       try:
           while True:
               yield "Next item"
       except GeneratorExit:
           print("Generator closed")

   gen = my_generator()
   next(gen)  # Advance to the first yield statement
   gen.close()  # Close the generator
   ```

2. **Raising Exceptions in a Generator**:

   You can raise exceptions within a generator by using the `raise` statement. This can be useful when you want to signal errors or exceptional conditions during the generator's execution. Here's an example:

   ```python
   def my_generator():
       try:
           for i in range(5):
               if i == 3:
                   raise ValueError("Value 3 encountered")
               yield i
       except ValueError as e:
           print(f"Error: {e}")

   gen = my_generator()
   for item in gen:
       print(item)
   ```

3. **Closing a Generator with a `finally` Block**:

   You can also use a `finally` block within a generator to ensure that certain cleanup operations are performed, whether the generator is closed manually or not. Here's an example:

   ```python
   def my_generator():
       try:
           for i in range(5):
               yield i
       finally:
           print("Cleanup code executed")

   gen = my_generator()
   for item in gen:
       print(item)
   gen.close()  # Closing the generator also triggers the finally block
   ```

## Bidirectional pipelines 

- Using generators can be implemented to create a two-way data flow between two or more functions or generators. 
- This allows data to flow in both directions, enabling complex data processing scenarios. 

Let's consider a scenario where we want to create a bidirectional pipeline to process and modify data between two functions: `source` and `destination`.

```python
def source(target):
    for i in range(1, 6):
        target.send(i)
    target.close()

def destination():
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value

def main():
    dest = destination()
    next(dest)  # Prime the destination generator
    source(dest)

    result = dest.send(None)  # Signal the destination to finish
    print(f"Final result: {result}")

if __name__ == "__main__":
    main()
```

```
Final result: 15
```

## states 

```python
def custom_groupby():
    current_key = None
    current_group = []

    try:
        while True:
            action = yield
            if action is None:
                break
            item, key_func = action
            item_key = key_func(item)

            if item_key == current_key:
                current_group.append(item)
            else:
                if current_key is not None:
                    yield current_key, current_group
                current_key = item_key
                current_group = [item]

    except GeneratorExit:
        pass

# Sample data
data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 30},
    {"name": "David", "age": 25},
    {"name": "Eve", "age": 30},
]

# Create the custom grouping coroutine
grouping = custom_groupby()
next(grouping)  # Prime the coroutine

# Group the data by the 'age' key using the custom coroutine
for item in data:
    grouping.send((item, lambda x: x["age"]))

grouping.close()  # Close the coroutine

# Iterate through the groups
for key, group in grouping:
    print(f"Age: {key}")
    for person in group:
        print(f"  {person['name']}")
    print()
```