#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "llist.h"

#define LIMIT 100
#define CUTOFF 50
int main ()
{
    int i;
    List L = CreateList();

    for (i=0; i<LIMIT; i++) {
        InsertInFront(&L, i);
    }

    PrintList(L);
    for (i=0; i<CUTOFF; i++) {
        Delete(&L, L);
    }

    DisposeList(&L);

    PrintList(L);

    return 0;
}

