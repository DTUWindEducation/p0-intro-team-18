from functions import greet, goldilocks, square_list, fibonacci_stop, clean_pitch

# Test greet function
print("Testing greet function:")
greet("world")

# Test goldilocks function
print("Testing goldilocks function:")
goldilocks(139)
goldilocks(140)
goldilocks(150)
goldilocks(151)

# Test square_list function
print("\nTesting square_list function:")
print(square_list([1, 2, 3]))

# Test fibonacci_stop function
print("\nTesting fibonacci_stop function:")
print(fibonacci_stop(30))

# Test clean_pitch function
print("\nTesting clean_pitch function:")
print(clean_pitch([-1, 2, 6, 95], [1, 0, 0, 0]))