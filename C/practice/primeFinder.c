#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int checkPrime(int primeCandidate)
{
    int divider;

    for (divider=2; divider<=sqrt(primeCandidate); divider++) { 
        //XXX: it's crucial to have the <= here, or else 4, 5, whose /2 are 2, will just fall thru to return 0
        if (!(primeCandidate % divider)) return -1;
    }
    return 0;
}
    
int checkPrime2(int primeCandidate, int curNum, int *primes)
{
    int i = 0;
    int limit = sqrt(primeCandidate);

    for (i = 0; i<curNum; i++) {
        if (!(primeCandidate % *(primes+i))) return -1;
        if (*(primes+i) > limit) break;
    }

    return 0;
}

int findPrime(int numOfPrime, int *primes)
{
    int tmpPrime = 2; //start from 2
    int curNum = 1; 

    if (numOfPrime == 1) return 2;

    for (tmpPrime=3; curNum<numOfPrime; tmpPrime++) {
        //if (!checkPrime(tmpPrime)) {
        if (!checkPrime2(tmpPrime, curNum, primes)) {
            //printf ("%dth, %d\n", curNum, tmpPrime);
            *(primes+curNum) = tmpPrime;
            curNum++;
            if (curNum==numOfPrime) 
                return tmpPrime;
        }
    }
}

int main(int argc, char *argv[])
{
    int *primes = NULL;
    int nthPrimeNum = 0;
    int thePrime = 0;
    int i = 0;

    if (argc != 2) return 0;

    nthPrimeNum = atoi(argv[1]);

    primes = malloc(sizeof(*primes) * nthPrimeNum);
    *primes = 2;

    thePrime = findPrime(nthPrimeNum, primes);

    printf("\nthe %dth prime is %d\n", nthPrimeNum, thePrime);

    for (i=0; i<nthPrimeNum; i++) {
        printf("%d, ", primes[i]); 
    }
    printf("\n");

    free(primes); //XXX: will this leak memory?
    
    return 0;
}

