#
#try:
	# It's a place where
	# you can do something 
    # without asking for permission.
#except:
	# It's a spot dedicated to 
    # solemnly begging for forgiveness.
#
#except ZeroDivisionError | ValueError | TypeError | AttributeError | SyntaxError
#
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)
except (ValueError, ZeroDivisionError, TypeError, AttributeError, SyntaxError):
    print('I do not know what to do.')
except:
    print('Division by zero is not allowed in our Universe')