# ==================================================================
# title           :n_complexity 
# description     :
# author          :srattigan
# date            :11/02/2019
# version         :1.0
# notes           :change from last version
# python_version  :3.7  
# file_version    :1.00
# ==================================================================

# imports


# globals and constants


# functions
def linear_time(num):
    """
    (int)-> None
    Prints all the numbers up to and including the number received.
    The runtime of this function scales linearly with the size of
    the input number
    """
    counter = 1
    while counter <= num:
        print(counter)
        counter += 1



# main body

if __name__ == "__main__":
    linear_time(10)