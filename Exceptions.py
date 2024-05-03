#Error and Exceptions
a = 5
print(a)


a = [1, 2, 3]
a.remove(1)
print(a)

try:
   a = 5/0
except Exception as e:
    print(e)

try:
    a = 5/1
    b = a + 10
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('Everthing is fine')
finally:
    print('cleaning up')


class ValueTooHighError(Exception):
    pass

def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')
try:
    test_value(200)
except ValueTooHighError as e:
    print(e)



class ValueTooHighError(Exception):
    pass
class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value
def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')
    if x < 5:
        raise ValueTooSmallError('value is too small', 1)

try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)































