# Table of Contents

- [Table of Contents](#table-of-contents)
- [Overview](#overview)
- [The async and await statements](#the-async-and-await-statements)
- [single-threaded parallel processing](#single-threaded-parallel-processing)
- [Concepts of asyncio](#concepts-of-asyncio)
- [Futures and tasks](#futures-and-tasks)
  - [Futures:](#futures)
  - [Tasks:](#tasks)
- [Event loops](#event-loops)
  - [What Is an Event Loop?](#what-is-an-event-loop)
  - [Key Concepts and Features:](#key-concepts-and-features)
  - [Example of Using an Event Loop:](#example-of-using-an-event-loop)
  - [Real-World Applications:](#real-world-applications)
- [Processes](#processes)
  - [Overview of `asyncio.create_subprocess_exec`:](#overview-of-asynciocreate_subprocess_exec)
  - [Example:](#example)
  - [Overview of `asyncio.create_subprocess_shell`:](#overview-of-asynciocreate_subprocess_shell)
  - [Example:](#example-1)

# Overview

- A framework for writing asynchronous, non-blocking code using the `async` and `await` syntax. 
- It allows you to write concurrent code that can efficiently handle I/O-bound and network-bound operations without blocking the entire program. `asyncio` is especially useful for building scalable network servers, clients, and other asynchronous applications.

1. **Async Functions**:

   In `asyncio`, you define asynchronous functions using the `async` keyword. These functions can be paused at `await` points, allowing other tasks to run concurrently without blocking the main program.

   ```python
   import asyncio

   async def main():
       print("Hello")
       await asyncio.sleep(1)
       print("World")

   asyncio.run(main())
   ```

2. **Event Loop**:

   `asyncio` relies on an event loop to manage and coordinate asynchronous tasks. You can think of the event loop as a scheduler that executes async functions and manages their execution.

   ```python
   import asyncio

   async def main():
       print("Hello")
       await asyncio.sleep(1)
       print("World")

   asyncio.run(main())
   ```

   The `asyncio.run()` function is used to run the `main` coroutine within an event loop.

3. **Concurrency with `asyncio.gather`**:

   You can execute multiple asynchronous tasks concurrently using `asyncio.gather`. This function allows you to await multiple coroutines and gather their results.

   ```python
   import asyncio

   async def task1():
       await asyncio.sleep(1)
       return "Task 1 done"

   async def task2():
       await asyncio.sleep(2)
       return "Task 2 done"

   async def main():
       result1, result2 = await asyncio.gather(task1(), task2())
       print(result1)
       print(result2)

   asyncio.run(main())
   ```

4. **Asynchronous I/O**:

   `asyncio` is well-suited for I/O-bound operations, such as making network requests or reading/writing files, without blocking the program's execution. You can use `await` with I/O functions to make them non-blocking.

   ```python
   import asyncio
   import aiohttp

   async def fetch_url(url):
       async with aiohttp.ClientSession() as session:
           async with session.get(url) as response:
               return await response.text()

   async def main():
       result = await fetch_url("https://example.com")
       print(result)

   asyncio.run(main())
   ```

5. **Error Handling**:

   Asynchronous code can raise exceptions just like synchronous code. You can use `try` and `except` blocks to handle errors within async functions.

   ```python
   import asyncio

   async def main():
       try:
           result = await async_function_that_may_raise_exception()
       except Exception as e:
           print(f"An error occurred: {e}")

   asyncio.run(main())
   ```

6. **Non-blocking Event Loops**:

   You can use the `asyncio` event loop to manage non-blocking I/O, timers, and scheduling tasks to run at specific times.

   ```python
   import asyncio

   async def main():
       print("Start")
       await asyncio.sleep(1)
       print("Middle")
       await asyncio.sleep(1)
       print("End")

   asyncio.run(main())
   ```

7. **Real-World Applications**:

   `asyncio` is commonly used for building asynchronous web servers, web scrapers, chat applications, and any application that needs to handle many concurrent connections efficiently.

# The async and await statements

The `async` and `await` statements are fundamental to asynchronous programming in Python, enabling the creation of non-blocking, concurrent code. They are part of Python's `asyncio` framework and provide a more readable and structured way to work with asynchronous tasks.

1. **`async` Statement**:

   - The `async` keyword is used to define asynchronous functions, also known as coroutines. These functions can be paused and resumed at `await` points, allowing other coroutines to run concurrently.

   - Asynchronous functions are defined with the `async` keyword before the `def` keyword.

   - Example of defining an asynchronous function:

     ```python
     async def my_coroutine():
         # Asynchronous code here
     ```

2. **`await` Statement**:

   - The `await` keyword is used inside asynchronous functions to pause execution until a coroutine or a future completes. It can only be used inside `async` functions.

   - When `await` is used, it yields control back to the event loop, allowing other tasks to run while waiting for the awaited coroutine or future to finish.

   - Example of using `await` to wait for another coroutine:

     ```python
     async def foo():
         await asyncio.sleep(1)
         print("After 1 second")

     async def main():
         await foo()
         print("Main function completed")

     asyncio.run(main())
     ```

3. **Concurrency and Event Loop**:

   - Asynchronous functions run concurrently within an event loop. The event loop is responsible for scheduling and managing the execution of coroutines.

   - When an asynchronous function is called using `await`, it registers itself with the event loop, and control is returned to the event loop until the awaited task completes.

   - The event loop runs tasks as long as they are non-blocking. When a task is blocked (e.g., waiting for I/O or sleeping), the event loop can switch to other tasks.

4. **Error Handling**:

   - You can use `try` and `except` blocks to handle exceptions raised within asynchronous functions, just like in synchronous code.

   - To handle exceptions raised by awaited tasks, you can use `try` and `except` blocks around the `await` statement.

   - Example of error handling within an async function:

     ```python
     async def fetch_data():
         try:
             result = await some_async_function()
             print(result)
         except Exception as e:
             print(f"An error occurred: {e}")
     ```

5. **Nested Coroutines**:

   - You can call one asynchronous function from another. This allows you to compose complex asynchronous workflows.

   - Remember that when you call an async function from another, you should use `await` to wait for its completion.

   - Example of calling an async function from another:

     ```python
     async def outer_coroutine():
         result = await inner_coroutine()
         print(result)

     async def inner_coroutine():
         await asyncio.sleep(1)
         return "Inner coroutine completed"
     ```

6. **Async for Loops**:

   - Python introduced async for loops (PEP 492) to iterate over asynchronous iterators and asynchronously process elements. This is particularly useful when dealing with I/O-bound operations.

   - Example of an async for loop:

     ```python
     async def process_items():
         async for item in async_iterator():
             # Process item asynchronously
     ```

   - You can use `asyncio.gather` to run multiple async tasks concurrently within an async for loop.

# single-threaded parallel processing

Single-threaded parallel processing with `asyncio` allows you to execute multiple asynchronous tasks concurrently in a single thread, which is particularly useful for I/O-bound operations. Here's an example that demonstrates single-threaded parallel processing using `asyncio`:

```python
import asyncio

# Asynchronous function to simulate I/O-bound task
async def fetch_url(url):
    await asyncio.sleep(1)  # Simulate a non-blocking I/O operation
    return f"Data from {url}"

# Main function to run multiple fetch_url tasks concurrently
async def main():
    urls = ["https://example.com", "https://google.com", "https://python.org"]

    # Create a list of tasks that fetch URLs concurrently
    tasks = [fetch_url(url) for url in urls]

    # Gather and await the results of all tasks
    results = await asyncio.gather(*tasks)

    # Process the results
    for i, result in enumerate(results):
        print(f"Result {i+1}: {result}")

if __name__ == "__main__":
    asyncio.run(main())
```

# Concepts of asyncio

1. **Event Loop**:

   - The event loop is at the core of `asyncio`. It acts as a scheduler for managing and coordinating asynchronous tasks.
   
   - The event loop runs in a single thread and decides which tasks to execute, when to pause and resume tasks, and when to switch between tasks.

2. **Coroutines**:

   - Coroutines are functions defined with the `async` keyword. They are non-blocking and can be paused and resumed at `await` points.
   
   - Coroutines are used to define asynchronous tasks. They are scheduled to run on the event loop.

3. **Tasks**:

   - Tasks are a higher-level abstraction over coroutines. They are used to schedule and manage the execution of coroutines.
   
   - You can create tasks using the `asyncio.create_task()` function.

4. **Futures**:

   - Futures are placeholders for results that will be available in the future. They are used to represent the eventual outcome of an asynchronous operation.
   
   - You can await a future to get its result once it's available.

5. **`await` Statement**:

   - The `await` keyword is used inside asynchronous functions to pause execution until a coroutine or future completes.
   
   - It allows other tasks to run while waiting for the awaited operation to finish.

6. **`async with` and `async for`**:

   - `async with` and `async for` allow you to work with asynchronous context managers and asynchronous iterators, respectively.

   - These constructs are used for resource management and iterating over asynchronous sequences.

7. **Concurrency**:

   - `asyncio` enables concurrency by running multiple tasks concurrently within a single thread.
   
   - While one task is blocked (e.g., waiting for I/O), the event loop can switch to executing another task.

8. **`asyncio.gather()`**:

   - The `asyncio.gather()` function is used to run multiple asynchronous tasks concurrently and gather their results.
   
   - It allows you to execute several coroutines and collect their results in one go.

9. **Error Handling**:

   - Exception handling in `asyncio` is similar to regular Python code. You can use `try` and `except` blocks to handle exceptions raised within asynchronous functions.

10. **Non-Blocking I/O**:

    - `asyncio` is particularly well-suited for I/O-bound operations (e.g., network requests, file I/O) where tasks spend most of their time waiting for external resources.

11. **`asyncio.sleep()`**:

    - The `asyncio.sleep()` function is used to introduce a non-blocking delay or sleep within an asynchronous task.

12. **`asyncio.Queue`**:

    - `asyncio` provides an asynchronous queue, `asyncio.Queue`, for managing data between asynchronous tasks.

13. **Real-World Applications**:

    - `asyncio` is commonly used for building asynchronous web servers, web scrapers, chat applications, and any application that needs to handle many concurrent connections efficiently.

# Futures and tasks

- essential concepts in `asyncio` for managing asynchronous operations and coordinating the execution of coroutines.

## Futures:

1. **Definition**:

   - A Future in `asyncio` is a placeholder for the result of an asynchronous operation that will be available in the future.
   
   - It represents the eventual outcome (success or failure) of an asynchronous computation.

2. **Creation**:

   - You can create a Future object using `asyncio.Future()` or by using the `loop.create_future()` method, where `loop` is the event loop.

   ```python
   import asyncio
   
   loop = asyncio.get_event_loop()
   future = loop.create_future()
   ```

3. **Setting a Result**:

   - You can set the result of a Future using the `future.set_result(result)` method, where `result` is the value that the Future will hold upon completion.

   ```python
   future.set_result(42)
   ```

4. **Setting an Exception**:

   - If an error occurs during the asynchronous operation, you can set an exception using the `future.set_exception(exception)` method, where `exception` is an exception instance.

   ```python
   future.set_exception(ValueError("Something went wrong"))
   ```

5. **Awaiting a Future**:

   - You can use the `await` keyword to wait for the result of a Future. When you `await` a Future, it suspends the coroutine until the Future is resolved (either with a result or an exception).

   ```python
   result = await some_future
   ```

6. **Callbacks**:

   - You can attach callbacks to a Future using `add_done_callback(callback)`. These callbacks are called when the Future is resolved.

   ```python
   def callback(future):
       if future.exception():
           print(f"Future raised an exception: {future.exception()}")
       else:
           print(f"Future result: {future.result()}")

   some_future.add_done_callback(callback)
   ```

## Tasks:

1. **Definition**:

   - A Task in `asyncio` is a higher-level abstraction over coroutines. It represents the execution of a coroutine in the event loop.
   
   - Tasks are used to schedule and manage the execution of coroutines.

2. **Creation**:

   - You can create a Task using the `asyncio.create_task()` function, which takes a coroutine as an argument.

   ```python
   async def my_coroutine():
       # Async code here

   task = asyncio.create_task(my_coroutine())
   ```

3. **Cancellation**:

   - You can cancel a Task using the `task.cancel()` method. This sends a cancellation request to the Task, but it's up to the coroutine to respond to the cancellation.

   ```python
   task.cancel()
   ```

4. **`asyncio.gather()`**:

   - The `asyncio.gather()` function is often used to run multiple coroutines concurrently and gather their results as Tasks. It returns a list of Tasks representing the execution of the provided coroutines.

   ```python
   async def foo():
       # Async code

   async def bar():
       # Async code

   tasks = asyncio.gather(foo(), bar())
   ```

5. **`await` with Tasks**:

   - You can `await` a Task just like you would with a coroutine. This suspends the current coroutine until the Task is complete.

   ```python
   result = await some_task
   ```

6. **Error Handling**:

   - Error handling with Tasks is similar to handling exceptions in regular coroutines. You can use `try` and `except` blocks to handle exceptions raised during Task execution.

7. **Task States**:

   - A Task can be in various states, including pending, running, done, and cancelled. You can check the state using `task.done()`, `task.running()`, etc.

   ```python
   if task.done():
       print("Task is done")
   ```

# Event loops

- A fundamental concept in asynchronous programming with `asyncio` in Python. 
- They are responsible for managing and coordinating the execution of asynchronous tasks (coroutines and functions) and are crucial for building efficient and non-blocking applications.

## What Is an Event Loop?

An event loop is the core component of `asyncio`. It is a specialized control flow that continuously checks for and dispatches events in an asynchronous program. Events can include the completion of I/O operations, timers, user interactions, or other asynchronous tasks. The event loop decides which task to run next based on the availability of events and whether tasks are waiting for those events.

## Key Concepts and Features:

1. **Single-Threaded**:

   - An event loop typically runs in a single thread, making it suitable for concurrency without the complexity of multiple threads.

   - This single-threaded nature simplifies synchronization and makes it easier to reason about concurrency.

2. **Concurrency**:

   - Event loops enable concurrent execution of asynchronous tasks. While one task is blocked, waiting for an event (e.g., I/O operation or sleep), the event loop can switch to another task, allowing efficient use of system resources.

3. **Task Scheduling**:

   - The event loop schedules tasks for execution. Tasks can be coroutines (created with `async def`), functions, or futures.

   - Tasks are scheduled to run when they are created using `asyncio.create_task()` or explicitly scheduled with `loop.create_task()`.

4. **`await` and Task Coordination**:

   - The `await` keyword is used to pause a task's execution until a specific event (e.g., another task's completion or a timer) occurs.

   - Event loops allow you to coordinate tasks using `await`, enabling non-blocking and efficient multitasking.

5. **Event Sources**:

   - Event loops are designed to work with various event sources, including I/O operations (e.g., reading/writing to files or sockets), timers (e.g., `asyncio.sleep()`), and external triggers (e.g., signals).

   - These event sources provide the events that the event loop manages.

6. **Event Queue**:

   - An event loop maintains an event queue, which stores pending events waiting to be processed.

   - When an event occurs (e.g., data is ready to be read from a socket), it is added to the event queue.

7. **Main Event Loop**:

   - An `asyncio` program typically has one main event loop that is created using `asyncio.get_event_loop()` or `asyncio.new_event_loop()`.

   - The main event loop is responsible for executing the program's tasks and managing the event queue.

8. **Running the Event Loop**:

   - The main event loop is started using `loop.run_until_complete()` or `loop.run_forever()`.

   - You can run the event loop until a specific task is complete or run it indefinitely to handle events continuously.

9. **Error Handling**:

   - Event loops provide mechanisms for handling exceptions and errors within asynchronous tasks, including unhandled exceptions raised within tasks.

   - Error handling ensures that failures in one task do not disrupt the operation of other tasks.

## Example of Using an Event Loop:

```python
import asyncio

async def main():
    print("Start")
    await asyncio.sleep(1)
    print("Middle")
    await asyncio.sleep(1)
    print("End")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
```

## Real-World Applications:

Event loops are widely used in various applications, including:

- Asynchronous web servers and web frameworks (e.g., aiohttp, FastAPI).
- Networking applications (e.g., chat servers, proxies).
- Web scraping and data fetching.
- GUI applications with asynchronous behavior.
- Efficiently handling many concurrent connections, such as in microservices architectures.

# Processes

`asyncio.create_subprocess_exec` is a function provided by the `asyncio` library in Python. It allows you to create and manage subprocesses asynchronously, which is particularly useful for running external commands or processes from your Python code in an asynchronous way. 

## Overview of `asyncio.create_subprocess_exec`:

- **Purpose**: The primary purpose of `asyncio.create_subprocess_exec` is to launch and interact with external processes asynchronously, which means you can start a process and continue executing other tasks without blocking the event loop.

- **Usage**: You can use this function to run shell commands or execute other Python scripts as separate subprocesses.

- **Asynchronous Execution**: Unlike the synchronous `subprocess` module, which blocks while waiting for a process to complete, `asyncio.create_subprocess_exec` allows you to initiate a process and await its completion asynchronously, making it suitable for scenarios where you need to run processes concurrently without blocking your application.

- **Features**: This function offers various features for interacting with the subprocess, including capturing its output, providing input to the process, and handling errors.

- **Communication**: You can communicate with the subprocess using pipes to send and receive data between your Python code and the external process.

## Example:

Here's a simple example that demonstrates how to use `asyncio.create_subprocess_exec` to run an external command and capture its output asynchronously:

```python
import asyncio

async def run_command():
    # Define the command to run (e.g., "ls" to list files in the current directory).
    command = "ls"

    # Create a subprocess asynchronously.
    process = await asyncio.create_subprocess_exec(
        command,
        stdout=asyncio.subprocess.PIPE,  # Capture standard output.
        stderr=asyncio.subprocess.PIPE,  # Capture standard error.
    )

    # Wait for the process to complete and capture its output.
    stdout, stderr = await process.communicate()

    # Print the captured output.
    print(f"Standard Output:\n{stdout.decode()}")
    print(f"Standard Error:\n{stderr.decode()}")

if __name__ == "__main__":
    asyncio.run(run_command())
```

## Overview of `asyncio.create_subprocess_shell`:

- **Purpose**: The primary purpose of `asyncio.create_subprocess_shell` is to execute shell commands or scripts as subprocesses asynchronously, allowing you to start and interact with external processes without blocking the event loop.

- **Usage**: You can use this function when you need to run shell commands or scripts that require shell features like environment variables, piping, or shell-specific syntax.

- **Asynchronous Execution**: Similar to `asyncio.create_subprocess_exec`, `asyncio.create_subprocess_shell` allows you to initiate a subprocess and await its completion asynchronously, making it suitable for running processes concurrently without blocking your application.

- **Features**: This function offers various features for interacting with the subprocess, including capturing its output, providing input to the process, and handling errors.

- **Communication**: You can communicate with the subprocess using pipes to send and receive data between your Python code and the external process, just like with `asyncio.create_subprocess_exec`.

## Example:

Here's a simple example that demonstrates how to use `asyncio.create_subprocess_shell` to run a shell command asynchronously and capture its output:

```python
import asyncio

async def run_command():
    # Define the shell command to run (e.g., "ls -l" to list files in long format).
    command = "ls -l"

    # Create a subprocess asynchronously.
    process = await asyncio.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,  # Capture standard output.
        stderr=asyncio.subprocess.PIPE,  # Capture standard error.
    )

    # Wait for the process to complete and capture its output.
    stdout, stderr = await process.communicate()

    # Print the captured output.
    print(f"Standard Output:\n{stdout.decode()}")
    print(f"Standard Error:\n{stderr.decode()}")

if __name__ == "__main__":
    asyncio.run(run_command())
```