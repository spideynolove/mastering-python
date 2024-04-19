class Spam(object):
    eggs = 'my eggs'

Spam = type('Spam', (object,), dict(eggs='my eggs'))
print(type(Spam))

# ------------------------------------------------------------------------------

class Spam(object):
    eggs = 'my eggs'

spam = Spam()
print(spam.eggs)
# 'my eggs'
print(type(spam))
# <class '...Spam'>
print(type(Spam))
# <class 'type'>

Spam = type('Spam', (object,), dict(eggs='my eggs'))

spam = Spam()
print(spam.eggs)
# 'my eggs'
print(type(spam))
# <class '...Spam'>
print(type(Spam))
# <class 'type'>