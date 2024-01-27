
# Def a simple function
def add(x,y):
    return x+y
print(add(4,5))

# Def the same but with a lambda function
lambda x,y: x+y
# Single line expression that return what is compiled after the ":"
# No need for return and it's impossible to call them since they don't have a name (Anonymus functions)

# To call them you need to put them inside a variable
add2 = lambda x,y: x+y
print(add2(4,5))

# Or define the different component in the same line and associe it to a function like print()
print((lambda x,y: x+y)(4,5))

# Lambda functions a made to be passed inside a higher order function to gain code space lines instead of defining tons of little functions 
# Example :

# Def a high function that result into a list of new items after passing throug a function
def my_map(my_function, my_iter):
    result = []
    for item in my_iter :
        new_item = my_function(item)
        result.append(new_item)
    return(result)

# Def the list
nums = [3, 4, 5, 6, 7]

# Use the lambda as the function used in the higer function
cubed = my_map(lambda x: x**3, nums)

# The my_map function is taking our "nums" list as an input and applies our lambda function on each item of the list
# The function is called thanks to our my_map function and gives the operation to do (here to cube the numbers)
# Instead of defining a function that would cube all the numbers of the list the lambda function do the same but in one simple line

print(cubed)