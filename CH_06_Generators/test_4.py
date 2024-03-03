# -----------------------------------------------------------------------------
# Bidirectional communication between a source and a destination generator examples
# -----------------------------------------------------------------------------


# def source(target):
#     for i in range(1, 6):
#         target.send(i)
#     target.close()


# def destination():
#     total = 0
#     while True:
#         value = yield total
#         if value is None:
#             break
#         total += value


# def main():
#     dest = destination()
#     next(dest)
#     source(dest)

#     # result = dest.send(None)
#     # print(f"Final result: {result}")

#     try:
#         dest.send(None)  # Signal the destination to finish
#     except StopIteration as e:
#         result = e.value  # Get the result from the StopIteration
#         print(f"Final result: {result}")


# if __name__ == "__main__":
#     main()


# # --------------------------------------------
# def source(target):
#     for i in range(1, 6):
#         target.send(i)
#     target.close()


# def destination():
#     total = 0
#     while True:
#         value = yield total
#         if value is None:
#             break
#         total += value


# def main():
#     dest = destination()
#     next(dest)  # Prime the destination generator
#     source(dest)

#     result = None
#     try:
#         result = dest.send(None)  # Signal the destination to finish
#     except StopIteration:
#         pass

#     print(f"Final result: {result}")


# if __name__ == "__main__":
#     main()


# --------------------------------------------
# def source(target):
#     for i in range(1, 6):
#         target.send(i)
#     target.close()


# def destination():
#     total = 0
#     while True:
#         value = yield total
#         if value is None:
#             break
#         total += value


# def main():
#     dest = destination()
#     next(dest)  # Prime the destination generator
#     source(dest)

#     try:
#         while True:
#             result = dest.send(None)  # Signal the destination to finish
#     except StopIteration:
#         pass

#     print(f"Final result: {result}")


# if __name__ == "__main__":
#     main()


# --------------------------------------------
# def source(target):
#     # Send numbers 1 to 5 to the target generator
#     for i in range(1, 6):
#         target.send(i)
#     target.close()

# def destination():
#     total = 0
#     while True:
#         try:
#             value = yield
#             if value is None:
#                 break
#             total += value
#         except GeneratorExit:
#             # Cleanup code when generator is closed
#             print("Destination closed.")
#             return total

# def main():
#     dest = destination()
#     next(dest)  # Prime the destination generator
#     source(dest)
#     # print("Shit")
#     try:
#         # Send None to signal end of input
#         dest.send(None)
#     except StopIteration as e:
#         result = e.value
#         print(f"Final result: {result}")

# if __name__ == "__main__":
#     main()


# --------------------------------------------
# def source(target):
#     # Send numbers 1 to 5 to the target generator
#     for i in range(1, 6):
#         target.send(i)
#     target.close()

# def destination():
#     total = 0
#     while True:
#         try:
#             value = yield
#             if value is None:
#                 break
#             total += value
#             print(total)
#         except GeneratorExit:
#             # Cleanup code when generator is closed
#             return total

# def main():
#     dest = destination()
#     next(dest)  # Prime the destination generator
#     total = source(dest)
#     print(total)

#     try:
#         # Send None to signal end of input
#         dest.send(None)
#     except StopIteration as e:
#         result = e.value
#         print(f"Final result: {result}")

# if __name__ == "__main__":
#     main()


# --------------------------------------------
# def source(target):
#     # Send numbers 1 to 5 to the target generator
#     for i in range(1, 6):
#         target.send(i)
#     target.close()

# def destination():
#     total = 0
#     while True:
#         try:
#             value = yield
#             if value is None:
#                 break
#             total += value
#             print(total)
#         except GeneratorExit:
#             # Cleanup code when generator is closed
#             return total

# def main():
#     dest = destination()
#     next(dest)  # Prime the destination generator
#     source(dest)

#     try:
#         # Send None to signal end of input
#         dest.send(None)
#     except StopIteration as e:
#         result = e.value
#         print(f"Final result: {result}")

# if __name__ == "__main__":
#     main()


# --------------------------------------------
# def source(target):
#     # Send numbers 1 to 5 to the target generator
#     for i in range(1, 6):
#         target.send(i)
#     target.close()

# def destination():
#     total = 0
#     while True:
#         try:
#             value = yield
#             if value is None:
#                 break
#             total += value
#         except GeneratorExit:
#             # Cleanup code when generator is closed
#             print(total)
#             return total

# def main():
#     dest = destination()
#     next(dest)  # Prime the destination generator
#     source(dest)

#     try:
#         # Send None to signal end of input
#         dest.send(None)
#     except StopIteration as e:
#         result = e.value
#         print(f"Final result: {result}")

# if __name__ == "__main__":
#     main()


# --------------------------------------------
# def source(target):
#     # Send numbers 1 to 5 to the target generator
#     for i in range(1, 6):
#         target.send(i)
#     target.close()

# def destination():
#     total = 0
#     while True:
#         try:
#             value = yield
#             if value is None:
#                 break
#             total += value
#         except GeneratorExit:
#             # Cleanup code when generator is closed
#             pass
#     yield total  # Yield the total when generator is closed

# def main():
#     dest = destination()
#     next(dest)  # Prime the destination generator
#     source(dest)

#     try:
#         # Send None to signal end of input
#         result = next(dest)
#     except StopIteration as e:
#         result = e.value
#         print(f"Final result: {result}")

# if __name__ == "__main__":
#     main()


# --------------------------------------------
# def source(target):
#     # Send numbers 1 to 5 to the target generator
#     for i in range(1, 6):
#         target.send(i)
#     target.close()

# def destination():
#     total = 0
#     while True:
#         try:
#             value = yield
#             if value is None:
#                 break
#             total += value
#         except GeneratorExit:
#             # Cleanup code when generator is closed
#             return total
#     yield total  # Yield the total when generator is closed

# def main():
#     dest = destination()
#     next(dest)  # Prime the destination generator
#     source(dest)

#     try:
#         # Send None to signal end of input
#         result = dest.send(None)
#     except StopIteration as e:
#         result = e.value
#         print(f"Final result: {result}")

# if __name__ == "__main__":
#     main()


# --------------------------------------------
# def source(target):
#     # Send numbers 1 to 5 to the target generator
#     for i in range(1, 6):
#         target.send(i)
#     target.close()

# def destination():
#     total = 0
#     print(total)
#     while True:
#         value = yield
#         if value is None:
#             break
#         total += value
#     return total

# def main():
#     dest = destination()
#     next(dest)  # Prime the destination generator
#     source(dest)

#     try:
#         # Send None to signal end of input
#         result = dest.send(None)
#     except StopIteration as e:
#         result = e.value
#         print(f"Final result: {result}")

# if __name__ == "__main__":
#     main()


# # Copilot version --------------------------------------------
# def source(target):
#     # Send numbers 1 to 5 to the target generator
#     for i in range(1, 6):
#         target.send(i)

# def destination():
#     total = 0
#     while True:
#         try:
#             value = yield
#             if value is None:
#                 break
#             total += value
#         except GeneratorExit:
#             # Cleanup code when generator is closed
#             return total
#     yield total  # Yield the total when generator is closed

# def main():
#     dest = destination()
#     next(dest)  # Prime the destination generator
#     source(dest)

#     try:
#         # Send None to signal end of input
#         result = dest.send(None)
#     except StopIteration as e:
#         result = e.value
#     print(f"Final result: {result}")

# if __name__ == "__main__":
#     main()


# # Fixed Copilot version --------------------------------------------
# def source(target):
#     # Send numbers 1 to 6 to the target generator
#     for i in range(1, 6):
#         target.send(i)

# def destination():
#     total = 0
#     while True:
#         value = yield
#         if value is None:
#             break
#         total += value
#     yield total  # Yield the total when generator is closed

# def main():
#     dest = destination()
#     next(dest)  # Prime the destination generator
#     source(dest)

#     try:
#         # Send None to signal end of input
#         result = dest.send(None)
#     except StopIteration as e:
#         result = e.value
#     print(f"Final result: {result}")

# if __name__ == "__main__":
#     main()


# Self fix version --------------------------------------------
def source(target):
    # Send numbers 1 to 5 to the target generator
    for i in range(1, 6):
        target.send(i)
    # target.close()

def destination():
    total = 0
    while True:
        try:
            value = yield
            if value is None:
                break
            total += value
        except GeneratorExit:
            # Cleanup code when generator is closed
            pass
    yield total  # Yield the total when generator is closed

def main():
    dest = destination()
    next(dest)  # Prime the destination generator
    source(dest)

    try:
        # Send None to signal end of input
        result = dest.send(None)
    except StopIteration as e:
        result = e.value
    print(f"Final result: {result}")

if __name__ == "__main__":
    main()