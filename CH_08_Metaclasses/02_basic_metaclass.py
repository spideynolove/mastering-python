# The metaclass definition, note the inheritance of type instead
# of object
class MetaSpam(type):
    # Notice how the __new__ method has the same arguments
    # as the type function we used earlier?
    def __new__(metaclass, name, bases, namespace):
        name = 'SpamCreatedByMeta'
        bases = (int,) + bases  # wtf
        namespace['eggs'] = 1
        return type.__new__(metaclass, name, bases, namespace)


# First, the regular Spam:
class Spam(object):
    pass


"""
print(Spam.__name__)
'Spam'
print(issubclass(Spam, int))
# False
print(Spam.eggs)
# Traceback (most recent call last):
#     ...
# AttributeError: type object 'Spam' has no attribute 'eggs'
"""

# Now the meta-Spam
# TypeError: multiple bases have instance lay-out conflict
# class Spam(float, metaclass=MetaSpam):

class Spam(object, metaclass=MetaSpam):
    pass


print(Spam.__name__)
# 'SpamCreatedByMeta'
print(issubclass(Spam, int))
# True
print(Spam.eggs)
# 1
