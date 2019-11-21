#function that tells you if a number is prime or not ---------------------------------------
def prime(number):
    if number == 1:
        return False

    divis = pow(2,number) - 2
    if divis%number == 0:
        return True
    else:
        return False


def IsPrime(number):
    if number == 1:
        return False

    for val in list_of_primes:
        if number % val == 0 and val != number:
            return False
    return True


#MAIN PROGRAM --------------------------------------------------------------------------------
slength = 99999

#lengthBUF
step = 1
oldsize = 0
size = 1
diagonal = 1
gap = 1
diag = [1]
primes = []
list_of_primes = []

#Setting up the prime list ----------------------------------------------

for i in range(1,100000):
    if prime(i) == True:
        list_of_primes.append(i)

print("Done with list of primes\n")

#finding diagonal
for ibuf in range(1,slength+1,2):
    print("----------------------------")
    
    #print the step ------------------
    #print("Step:" + str(step))
    step += 1
    
    #print the side length -----------
    print("side length:" + str(ibuf))
    
    #print the number of diagonals----
    #print("diagonal:" + str(diagonal))
    diagonal += 4
    
    #print size ----------------------
    oldsize = size
    size = pow(ibuf,2)
    #print("size:" + str(size))
    #print("oldsize:" + str(oldsize))
    #print("gap:" + str(gap))


    #populate a list with the diagonal numbers -----------------------
    for ibuff in range(oldsize + gap, size + 1, gap):
        diag.append(ibuff)
    gap = ibuf + 1
    #print(diag)

    #copying a list and working with primes --------------------------
    for x in diag[-4:]:
        if IsPrime(x) == True:
            primes.append(x)

    #print (primes)

    #finding the percentage ------------------------------------------
    ratio = len(primes) / len(diag)
    print("Percent: ", ratio)

    if ratio < 0.100000000000 and ibuf > 7:
        print("We found it! It's.... ", ibuf)
        break


#for all in list_of_primes:
#    print(all)


print("\nDONE")
