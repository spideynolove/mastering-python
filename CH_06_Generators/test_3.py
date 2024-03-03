# import asyncio

# async def read_file(file_name):
#     # need pip install aiofiles
#     async with aiofiles.open(file_name, mode='r') as file:
#         content = await file.read()
#     return content

# async def main():
#     file_names = ["file1.txt", "file2.txt", "file3.txt"]
#     tasks = [read_file(file_name) for file_name in file_names]
#     results = await asyncio.gather(*tasks)
#     for file_name, content in zip(file_names, results):
#         print(f"Content from {file_name}:\n{content}")

# asyncio.run(main()


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


# --------------------------------------------
def my_generator():
    try:
        while True:
            yield "Next item"
    except GeneratorExit:
        print("Generator closed")

gen = my_generator()
next(gen)  # Advance to the first yield statement
gen.close()  # Close the generator


# --------------------------------------------
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


# --------------------------------------------
def my_generator():
    try:
        for i in range(5):
            yield i
    finally:
        print("Cleanup code executed")

gen = my_generator()
for item in gen:
    print(item)
gen.close()