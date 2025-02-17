# Question 1
def greet(name):
    print(f"Hello, {name}!")

greet('world')

# Question 2
def goldilocks(bed_length):
    if bed_length < 140:
        print("Too small!")
    elif bed_length > 150:
        print("Too large!")
    else:
        print("Just right. :)")

## Test
goldilocks(139)
goldilocks(140)
goldilocks(151)
goldilocks(150)

# Question 3
## Option 1
def square_list(numbers):
    squared_numbers = []
    for num in numbers:
        squared_numbers.append(num ** 2)
    return squared_numbers
print(square_list([1, 2, 3]))

## Option 2
def square_list(numbers):
    return [num ** 2 for num in numbers]

print(square_list([1, 2, 3]))

# Question 4
def fibonacci_stop(max_value):
    fib_sequence = [1,1]

    while True:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        if next_fib > max_value:
            break
        fib_sequence.append(next_fib)

    return fib_sequence

##test
print(fibonacci_stop(30))


# Question 5
def clean_pitch(pitch_angles, status_signals):
    cleaned_data = []
    for pitch, status in zip(pitch_angles, status_signals):
        if (pitch <0 or pitch > 90) and status > 0:
            cleaned_data.append(-999)
        else:
            cleaned_data.append(pitch)
    return cleaned_data

##test 
x = [-1, 2, 6, 95]
status = [1, 0, 0, 0]
print(clean_pitch(x, status))
