/* 
 * Hashtable is an array, when inserting an element, the index of the array
 * where the element should go to is calculated by a hashing function. When
 * retrieving an element, the index can be calculated thru the same hashing
 * function. Since there are more possible elements than there are indexes,
 * multiple elements will have the same index, which needs to be managed. I
 * think, the hashtable can be designed as an array of linkedlist. 
 */

#include <stdio.h>
#include <stdlib.h>

/* my verson */
int hashing (char* input)
{
    char *pchar;
    int asciiSum=0; //XXX: don't forget the =0, or else garbage will be there
    int hashVal=0;
    char buf[100];
    char *pbuf = buf;

    pchar = input;

    while (*pchar != 0) { //XXX: don't forget the *
        asciiSum += *pchar; 
        pbuf += sprintf (pbuf, "%d(%c) + ", *pchar, *pchar); //XXX: %c is int,
                                                             //%s is ptr
        pchar++; //XXX: if the ++ is put in the while loop, then the first char
                 //is skipped
    }

    sprintf (pbuf-2, "= %d\n", asciiSum);
    printf ("%s\n", buf);

    hashVal = asciiSum % 10;
    return hashVal;
}

/* by the book */
int hash (const char *key, int tableSize) //XXX: tableSize is best a prime
{
    int hashVal = 0;

    while (*key != '\0') {
        hashVal += *key++;
    }
    return hashVal % tableSize;
}


