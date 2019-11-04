#
# I am building a function that will take in a list of inputs representing stock prices
# over many days and will prompt the user with how they would like to evaluate these prices
# 
#

def menu():
    """A function that simply prints the menu"""
    print()
    print("(0) Input a new list")
    print("(1) Print the current list")
    print("(2) Find the average price")
    print("(3) Find the standard deviation")
    print("(4) FInd the minimum and its day")
    print("(5) FInd the maximum and its day")
    print("(6) Your IT investment plan")
    print("(9) Quit")
    print()




def find_average(L):
    result = 0
    for i in range(len(L)):
        result += L[i]
    return result/ len(L)

def find_standard_deviation(L):
    ave = find_average(L)
    result = 0
    for i in range(len(L)):
        result += (L[i] - ave)**2
    return (result / len(L)) ** 0.5

def find_min(L):
    """find min uses a loop to return the minimum of L.
       Argument L: a nonempty list of numbers.
       Return value: the smallest value in L.
    """
    result = L[0]
    for x in L:
        if x < result:
            result = x
    return result

def find_min_loc(L):
    """find min loc uses a loop to return the minimum of L
            and the location (index or day) of that minimum.
        Argument L: a nonempty list of numbers.
        Results:  the smallest value in L, its location (index)
    """
    minval = L[0]
    minloc = 0

    for i in list(range(len(L))):
        if L[i] < minval:  # a smaller one was found!
            minval = L[i]
            minloc = i
    return minval, minloc


def find_max(L):
    """find max uses a loop to return the maximum of L.
       Argument L: a nonempty list of numbers.
       Return value: the largest value in L.
    """
    result = L[0]
    for x in L:
        if x > result:
            result = x
    return result

def find_max_loc(L):
    """find max loc uses a loop to return the maximum of L
            and the location (index or day) of that maximum.
        Argument L: a nonempty list of numbers.
        Results:  the largest value in L, its location (index)
    """
    maxval = L[0]
    maxloc = 0

    for i in list(range(len(L))):
        if L[i] > maxval:  # a larger one was found!
            maxval = L[i]
            maxloc = i
    return maxval, maxloc

def max_difference(L):
    """max difference will accept a list and return the largest difference in which the 
       larger value must come after the smaller one
       output will be a string with the first argument being the location of the small 
       value and the second argument being the location of the larger value
    """
    maxdiff = abs(L[1] - L[0])
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            if L[j] - L[i] >= maxdiff:
                if j > i:
                    maxdiff = L[j] - L[i]
    return maxdiff


def max_difference_loc(L):
    """max difference loc will accept a list and return the location of the values that
       create the largest difference in which the larger value must come after the smaller one
       output will be a string with the first argument being the location of the small 
       value and the second argument being the location of the larger value
    """
    maxdiff = abs(L[1] - L[0])
    loc = []
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            if L[j] - L[i] >= maxdiff:
                if j > i:
                    loc = [i,j]
                    maxdiff = L[j] - L[i]
    return loc


def max_difference_val(L):
    """max difference value will use the location produced by max difference loc and 
       return the values that occupy each location
       output will be a list of the smaller value then larger value
    """
    n = max_difference_loc(L)
    return [ L[n[0]], L[n[1]] ]





def main():
    """The main user-interaction loop"""
    secret_value = 2.0

    L = [30, 10, 20]  # an initial list

    while True:     # the user-interaction loop
        print("\n\nThe list is", L)
        menu()
        choice = input("Choose an option: ")

        #
        # "Clean and check" the user's input
        # 
        try:
            choice = int(choice)   # make into an int!
        except:
            print("I didn't understand your input! Continuing...")
            continue

        # run the appropriate menu option
        #
        if choice == 9:    # We want to quit
            break          # Leaves the while loop altogether

        elif choice == 0:  # We want to continue...
            newL = choice = input('enter your list of stock prices: ')
            try: 
                newL = eval(newL)   # eval runs Python's interpreter! Note: Danger!
                if type(newL) != type([]): 
                    L = newL
                    print("That didn't seem like a list. Not changing L.")
                else: 
                    L = newL  # Here, things were OK, so let's set our list, L to be newL
                    print('Your list has been changed!')
            except:
                newL = L
                print("I didn't understand your input. Not changing L.")
            continue       # Goes back to the top of the while loop

        elif choice == 1:  # We want to enter a new list
            print('The list is', L)


        elif choice == 2:  # Predict and add the next element
            n = find_average(L) # Get the next element from the predict function
            print("The average of all the values in your list is", n)
        

        elif choice == 3:  # Unannounced menu option!
            m = find_standard_deviation(L)
            print("The standard deviation of L is", m)     

        elif choice == 4:  # Unannounced menu option (slightly more interesting...)
            n = find_min(L)
            m = find_min_loc(L)
            print("Your list has a minimum value of", n, "that occurs on day", m[1])

        elif choice == 5:  # Another unannounced menu option (even more interesting...)
            n = find_max(L)
            m = find_max_loc(L)
            print("Your list has a maximum value of", n, "that occurs on day", m[1])

        elif choice == 6:
            a = max_difference(L)
            b = max_difference_loc(L)
            c = max_difference_val(L)
            print('Your TTS investment plan is to')
            print()
            print('Buy on day', b[0], 'at price', c[0])
            print('Sell on day', b[1], 'at price', c[1])
            print()
            print('For a total profit of', a )
            
        
        else:
            print(choice, " ?      That's not on the menu!")

    print()
    print("See you yesterday!")
