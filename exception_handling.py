#Exception Handling

try:
    k = 5/0

except ZeroDivisionError:
    print('Division by zero (0) not allowed')

finally:
    print('This will print regardless\n')



# Implementation 2
def throw_exception(divisor):
    k = 50
    if (divisor == 0):
        raise Exception('Division by \'0\' is not allowed' )
    elif (divisor < 0):
        ans = k / divisor
        print(f"Division by a negative integer, that can be weird, but let's see the results: {ans}")
    else:
        pass

try:
    throw_exception(0)
except Exception as ex:
    print(ex)
else:
    print('This is executed when exception is not caught')
finally:
    print('This gets executed regardless')
print("\n")

