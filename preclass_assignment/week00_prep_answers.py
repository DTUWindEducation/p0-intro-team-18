# Question 1
def greet(person):
    """
    This Function prints to the inputted person

    Args:
        person (str): The person that you would like to say to
    """
    print("Hello, " + person+ "!")
    
greet('world')


# Question 2
def goldilocks(bedSize):
    """
    This function determines prints if a given bed size is too small, too large
    or just right for goldilocks 

    Args:
        bedSize (int): the size of the proposed bed
    """
    if bedSize<140:
        print("Too small.")
    elif bedSize>150:
        print("Too large.")
    else:
        print("Just right. :)")

goldilocks(139)
goldilocks(140)
goldilocks(150)
goldilocks(151)


# Question 3
def square_list(num_list):
    """
    This function takes in a list of numbers of size n and returns the square of each number
    in a list of size n

    Args:
        num_list (list): a list of numbers

    Returns:
        list: a list of each number squared
    """
    sqd_list=[]
    for number in num_list:
        squared = number**2
        sqd_list.append(squared)
    return sqd_list
    
print(square_list([1, 2, 3]))


#Question 4
def fibonacci_stop(max_num):
    """
    This function returns a list of all the numbers in the fibonacci sequence that are less than or equal to
    the inputted max_num.

    Args:
        max_num (int): the upper limit to the value of any element in the fibbonaci sequence

    Returns:
        list: an ordered list of numbers in the fibbonacci sequence that are less than or equal to max_num
    """
    current_val=1
    prev_val=0
    temp_current_val=-1
    seq_list=[]
    while current_val <= max_num:
        temp_current_val=current_val
        current_val+=prev_val
        prev_val=temp_current_val
        
        seq_list.append(prev_val)
    return seq_list
    
print(fibonacci_stop(30))

#Question 5
def clean_pitch(x, status):
    """
    Compares the inputted x and status lists element-wise. If the status element is 1 then the 
    corresponding element in the x list is checked to see if it is beween [0, 90]. If it is then
    that x element is added to the output list if not then -999 is added to the output list.

    Args:
        x (list): list of angles
        status (list): list of whether a measurement is valid
        
    Returns:
        list: a list of cleaned angle values
    """
    cleaned_x=[]
    for index in range(len(x)):
        if (x[index]>90 or x[index]<0) and status[index]>0:
            cleaned_x.append(-999)
        elif status[index]<0:
            cleaned_x.append("Invalid Status")
        else:
            cleaned_x.append(x[index])
    return cleaned_x
    
print(clean_pitch([-1, 2, 6, 95], [1, 0, 0, 0]))