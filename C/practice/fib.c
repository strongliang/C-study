/* 
 * concept of dynamic programming 
 * 
 */

#include <stdio.h>
#include <stdlib.h>

unsigned long fib(int n)
{
    unsigned long prevVal, curVal; 
    unsigned long newVal;
    int i=0;
    
    if (n == 0) return 0;
    if (n == 1) return 1;

    prevVal = 0;
    curVal = 1;
    newVal = 1;

    for (i=1; i<n; i++) { //XXX: make sure it's n-1 times, 
       newVal = prevVal + curVal; 
       prevVal = curVal;
       curVal = newVal;
    }

    return newVal;
}

int main(int argc, char *argv[])
{

    int target = 0;

    if (argc!=2) { return 0; }
    
    target = atoi(argv[1]);

    //printf("fib(%d) = %lu\n", target, fib(target));
    printf("fib(%d) = %lu\n", target, fib(target));

    return 0;
}

