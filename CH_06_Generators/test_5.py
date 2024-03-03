# -----------------------------------------------------------------------------
# States generator examples
# -----------------------------------------------------------------------------


# def custom_groupby():
#     current_key = None
#     current_group = []
#     try:
#         while True:
#             action = yield
#             if action is None:
#                 break
#             item, key_func = action
#             item_key = key_func(item)
            
#             print(current_group)

#             if item_key == current_key:
#                 current_group.append(item)
#             else:
#                 if current_key is not None:
#                     yield current_key, current_group
#                 current_key = item_key
#                 current_group = [item]

#     except GeneratorExit:
#         print("Closing the generator")
#         pass


# # Sample data
# data = [
#     {"name": "Alice", "age": 30},
#     {"name": "Bob", "age": 25},
#     {"name": "Charlie", "age": 30},
#     {"name": "David", "age": 25},
#     {"name": "Eve", "age": 30},
# ]

# # Create the custom grouping coroutine
# grouping = custom_groupby()
# next(grouping)  # Prime the coroutine

# # Group the data by the 'age' key using the custom coroutine
# for item in data:
#     grouping.send((item, lambda x: x["age"]))

# grouping.close()  # Close the coroutine

# # Iterate through the groups
# for key, group in grouping:
#     print(f"Age: {key}")
#     for person in group:
#         print(f"  {person['name']}")
#     print()


# Copilot error version  -----------------------------------------------------------------------------
# def custom_groupby():
#     current_key = None
#     current_group = []
#     while True:
#         action = yield
#         if action is None:
#             if current_group:
#                 yield current_key, current_group
#             return
#         item, key_func = action
#         item_key = key_func(item)

#         if item_key == current_key:
#             current_group.append(item)
#         else:
#             if current_key is not None:
#                 yield current_key, current_group
#             current_key = item_key
#             current_group = [item]


# # Sample data
# data = [
#     {"name": "Alice", "age": 30},
#     {"name": "Bob", "age": 25},
#     {"name": "Charlie", "age": 30},
#     {"name": "David", "age": 25},
#     {"name": "Eve", "age": 30},
# ]

# # Create the custom grouping coroutine
# grouping = custom_groupby()
# next(grouping)  # Prime the coroutine

# # Group the data by the 'age' key using the custom coroutine
# for item in data:
#     grouping.send((item, lambda x: x["age"]))

# # Send None to signal end of input and collect the groups into a list
# grouping.send(None)

# # Iterate through the groups
# try:
#     while True:
#         key, group = next(grouping)
#         print(f"Age: {key}")
#         for person in group:
#             print(f"  {person['name']}")
#         print()
# except StopIteration:
#     pass


# Copilot error version 2 -----------------------------------------------------------------------------
# def custom_groupby():
#     current_key = None
#     current_group = []
#     while True:
#         action = yield
#         if action is None:
#             break
#         item, key_func = action
#         item_key = key_func(item)

#         if item_key == current_key:
#             current_group.append(item)
#         else:
#             if current_key is not None:
#                 yield current_key, current_group
#             current_key = item_key
#             current_group = [item]
#     if current_group:
#         yield current_key, current_group


# # Sample data
# data = [
#     {"name": "Alice", "age": 30},
#     {"name": "Bob", "age": 25},
#     {"name": "Charlie", "age": 30},
#     {"name": "David", "age": 25},
#     {"name": "Eve", "age": 30},
# ]

# # Create the custom grouping coroutine
# grouping = custom_groupby()
# next(grouping)  # Prime the coroutine

# # Group the data by the 'age' key using the custom coroutine
# for item in data:
#     grouping.send((item, lambda x: x["age"]))

# # Send None to signal end of input
# grouping.send(None)

# # Iterate through the groups
# try:
#     while True:
#         key, group = next(grouping)
#         print(f"Age: {key}")
#         for person in group:
#             print(f"  {person['name']}")
#         print()
# except StopIteration:
#     pass


# Copilot error version 3 -----------------------------------------------------------------------------
# def custom_groupby():
#     current_key = None
#     current_group = []
#     while True:
#         action = yield
#         item, key_func = action
#         item_key = key_func(item)

#         if item_key == current_key:
#             current_group.append(item)
#         else:
#             if current_key is not None:
#                 yield current_key, current_group
#             current_key = item_key
#             current_group = [item]
#     if current_group:
#         yield current_key, current_group


# # Sample data
# data = [
#     {"name": "Alice", "age": 30},
#     {"name": "Bob", "age": 25},
#     {"name": "Charlie", "age": 30},
#     {"name": "David", "age": 25},
#     {"name": "Eve", "age": 30},
# ]

# # Create the custom grouping coroutine
# grouping = custom_groupby()
# next(grouping)  # Prime the coroutine

# # Group the data by the 'age' key using the custom coroutine
# for item in data:
#     grouping.send((item, lambda x: x["age"]))

# # Exhaust the generator and collect the groups into a list
# groups = []
# try:
#     while True:
#         groups.append(next(grouping))
# except StopIteration:
#     pass

# # Iterate through the groups
# for key, group in groups:
#     print(f"Age: {key}")
#     for person in group:
#         print(f"  {person['name']}")
#     print()


# Copilot error version 4 -----------------------------------------------------------------------------
# import itertools

# def custom_groupby():
#     current_key = None
#     current_group = []
#     while True:
#         action = yield
#         item, key_func = action
#         item_key = key_func(item)

#         if item_key == current_key:
#             current_group.append(item)
#         else:
#             if current_key is not None:
#                 yield current_key, current_group
#             current_key = item_key
#             current_group = [item]
#     if current_group:
#         yield current_key, current_group


# # Sample data
# data = [
#     {"name": "Alice", "age": 30},
#     {"name": "Bob", "age": 25},
#     {"name": "Charlie", "age": 30},
#     {"name": "David", "age": 25},
#     {"name": "Eve", "age": 30},
# ]

# # Create the custom grouping coroutine
# grouping = custom_groupby()
# next(grouping)  # Prime the coroutine

# # Group the data by the 'age' key using the custom coroutine
# for item in data:
#     grouping.send((item, lambda x: x["age"]))

# # Exhaust the generator and collect the groups into a list
# groups = list(itertools.islice(grouping, None))

# # Iterate through the groups
# for key, group in groups:
#     print(f"Age: {key}")
#     for person in group:
#         print(f"  {person['name']}")
#     print()


# Copilot another version  -----------------------------------------------------------------------------
def running_total():
    total = 0
    while True:
        x = yield total
        if x is None:
            break
        total += x

# Create the generator
totaler = running_total()
next(totaler)  # Prime the generator

# Send numbers to the generator and print the running total
for i in range(1, 6):
    print(totaler.send(i))

# Send None to signal end of input
try:
    totaler.send(None)
except StopIteration:
    pass