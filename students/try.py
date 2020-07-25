# lis=[1,2,3,4,5]
# def multiplyByTen(numbers):
#     for x in numbers:
#         index_of_x=numbers.index(x)
#         valueMultiplied=x*10;
#         numbers.remove(x)
#         numbers.insert(index_of_x,valueMultiplied)
#     return numbers


# print(multiplyByTen(lis))
def is_prime(number):
    if number <= 1:
        return False
    
    for factor in range(2, number):
        if number % factor == 0:
            return False

    return True

def list_primes(start,end):
    prime_list=[] #create an empty list of primes in a given range
    for number in range(start, end):
        if is_prime(number):
            prime_list.append(number)
    return prime_list

print(list_primes(3,65))
            
            #print('%d is prime' % number)



def mersenne_number(p):
    p=2**p;
    return p-1;

def mersennes():
    mersennes=[]
    for i in list_primes(3,65):
        mersennes.append(mersenne_number(i))

    return mersennes
def sieve(n):
    sieves=[]
    # Create a boolean array "prime[0..n]" and initialize 
    # all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    prime = [True for i in range(n + 1)] 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    # Print all prime numbers 
    for p in range(n + 1): 
        if prime[p]: 
            sieves.append(p)
    return  sieves
#print(mersenne_number(2));


