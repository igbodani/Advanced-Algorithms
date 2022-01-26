from random import randint


def prime_test(N, k):
    '''
    This function takes in a number N and a number k, and returns a tuple of two booleans. The first
    boolean is true if and only if N passes the Fermat test k times. The second boolean is true if and
    only if N passes the Miller-Rabin test k times.

    :param N: The number to test
    :param k: number of iterations of Miller-Rabin test
    :return: The function returns a tuple of two booleans. The first boolean is the result of the Fermat
    test, and the second boolean is the result of the Miller-Rabin test.
    '''
    # This is main function, that is connected to the Test button. You don't need to touch it.
    return fermat(N, k), miller_rabin(N, k)


def mod_exp(x, y, N):
    '''
    Given a number x, y, and N, return x^y mod N.

    :param x: the base
    :param y: the number of times to repeat the operation
    :param N: The modulus
    :return: The value of the exponentiation.
    '''

    '''
     Time complexity : 
       Let n be the size in bits of x, y, and N

      step 1 : O(1)  
      step 2 : O(n)
      step 3 : O(y^2)
      step 4 : O(y^2)

      Total : O(1) + O( n(O(y^2) + O(y^2) )) =  O(n*y^2) OR O(n^3)

    Proof: 

    The first step ends in constant time if y is 0, while the second step runs through n times.
    We multiply and divide which both have a time complexity of O(n^2).
    Therefore this gives us a time complexity of O(n^3)

    '''


    '''
    Space complexity:
      Let y be n 
      The function uses a stack size of n 

       Complexity : O(n)
    '''

    if y == 0:    # step 1
        return 1

    if y % 2 == 0:
        z = mod_exp(x, y / 2, N)  # step 2
        return (z * z) % N   # step 3

    else:
        return ((x % N) * mod_exp(x, y - 1, N)) % N  # step 4


def fprobability(k):
    # You will need to implement this function and change the return value.
    return 1- (1 / 2) ** k


def mprobability(k):
    # You will need to implement this function and change the return value.
    return 1 - (1 / 4) ** k


def fermat(N, k):

    '''
    This function takes in a number N and a number k, and checks if N is prime by checking if it is not
    prime by Fermat's Little Theorem.

    :param N: the number to test
    :param k: the number of times to run the Fermat test
    :return: The function returns 'prime' or 'composite'
    '''

    '''
      Time complexity:
        step 1 : O(1)  
        step 2 : O(n)
        step 3 : O(n^3)

        Total:  O(1) + O(n * (O(y^3)) )  = O(n*y^3) OR O(n^4)



        Proof: 
        The first step halts in constant time if N is 1, second step halts after running k times.
        Inside the loop we call mod_exp which has a time complexity of O(n^3).
        Therefore the algorithm runs in O(n^4)

        
    '''

    
    '''
    Space complexity:
      Let y be n 
      The function uses a stack size of n 

       Complexity : O(n-1)
    '''


    if N == 1:  # If N is 1 return prime  (step 1)
        return 'prime'

    for i in range(k):    # (step 2)
        a = randint(2, N - 1)
        if mod_exp(a, N - 1, N) != 1:  # (step 3)
            return 'not prime'

    return 'prime'


def miller_rabin(N, k):
    '''
    Given a number N, we pick a random number a, and compute a^(N-1) mod N. If the result is not 1, then
    N is composite. If the result is 1, then we compute a^(N-1)/2 mod N. If the result is -1, then we
    compute a^(N-1)/2 mod N. If the result is not -1, then N is composite.

    :param N: the number to test
    :param k: the number of times you want to run the test
    :return: The function returns 'composite'
    '''

    '''
      Time complexity:
        step 1 : O(1) 
        step 2:  O(n)
        step 3 : O(k)
        step 4 : O(n^3)
        step 5:  O(N)


        Total:  O(1) + O(n) + O(k * (O(y^3)))  = O(k*n^3) OR O(n^4)



        Proof: 
        
        The first step halts in constant time if N is 1, second step halts after n becomes odd it runs n times
        step 3 we loop k times, in the loop we call mod_exp which has a time complexity of O(n^3), if val not equal N -1 
        we loop the size of length.
        Therefore the algorithm runs in O(n^4)
    '''


    
    '''
    Space complexity:
      Let y be n 
      The function uses a stack size of n 

       Complexity : O(n)
    '''


    if N == 1:  # If N is 1 return prime  (step 1)
        return 'prime'

    n = N - 1  # set n for the while loop   
    length = 0  # amount of times n is divided   

    while n % 2 == 0:  # while n is even   (step 2)
        n /= 2        
        length += 1

    for i in range(k):  # Loop through K times   (step 3)
        a = randint(2, N - 1)
        val = mod_exp(a, n, N)       # (step 4)

        if val != 1:  # If return value of mod_exp isn't 1
            check = True
            for j in range(length):     #(step 5)
                if val == N - 1:
                    check = False
                    break

                # Take the modular exponent
                val = val * val   
                val %= N

            if check:
                return 'composite'

    return 'prime'
