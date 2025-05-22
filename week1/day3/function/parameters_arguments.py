# Python function with parameters

#Parameters: These are the names listed in the function definition.
            #They act as placeholders for the values that will be passed into the function when it's called.
#Syntax:
#def function_name(parameter: data_type) -> return_type:
    # body of the function
    # return expression

#Example:
def greet(name, message): # 'name' and 'message' are parameters
    print(f"Hello {name}!, {message}")


#Python Function Arguments
#Arguments are the values passed inside the parenthesis of the function.
#A function can have any number of arguments separated by a comma.

# A simple Python function to check
# whether number is even or odd
def evenOdd(number):
    if (number % 2 == 0):
        print("even")
    else:
        print("odd")

evenOdd(2)
evenOdd(3)


# Types of Python Function Arguments
# Python supports various types of arguments that can be passed at the time of the function call.
# In Python, we have the following function argument types:
# 1. Default argument
# 2. Keyword argument
# 3. Positional argument
# 4. Arbitrary argument
# 5. Arbitrary keyword argument