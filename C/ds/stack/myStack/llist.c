/*
 * how to, in the delete function, mark the L to be NULL when the last node is
 * removed?
 * We need to pass the List * to the delete
 * It took me a while to figure out how to remove the list. The tricky part is
 * how to leave no garbage after deleting
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "llist.h"


List CreateList()
{
    return NULL;
}

/*recursive*/
void DisposeList(List *L)
{
    if (NULL == *L) {
        return;
    } else {
        DisposeList(&((*L)->next));
    }
    free (*L);
    *L = NULL;
}

static int IsEmpty(List L)
{
    return NULL == L;
}

void InsertInFront(List *L, int X)
{
    Node newNode;

    if ( !(newNode=malloc(sizeof(struct ListRecord))) ) {
        printf("malloc failed!\n");
        return;
    }

    newNode->next = (*L);
    newNode->prev = NULL;
    newNode->data = X;

    /*if list not empty*/
    if (!IsEmpty(*L)) {
        (*L)->prev = newNode;
    } 

    *L = newNode;
}

void Delete(List *L, Position P)
{
    Position prevP; 
    Position nextP; 

    FAIL_ON_NULL(P)

    prevP = P->prev;
    nextP = P->next;

    if (!IsEmpty(prevP)) prevP->next = nextP;
    if (!IsEmpty(nextP)) nextP->prev = prevP;

    if (L && Advance(*L) == NULL && *L == P) {
        *L = NULL;
    } else if (L && *L==P) {
        *L = nextP;
    }

    free(P);
}

Position Advance(Position P)
{
    FAIL_ON_NULL(P)

    return P->next;
}

Position Find(List L, int X)
{
    if (IsEmpty(L)) {
        return NULL; /*not found*/
    }
    else if (L->data == X) {
        return L;    /*found*/
    }
    else {
        return Find(Advance(L), X); /*search*/
    }
}

void Remove(List *L, int X)
{
    Position P = Find(*L, X);
    Delete(L, P);
}

void PrintList(List L)
{
    if (NULL == L) {
        printf("\n");
    } else {
        printf("%d, ", L->data);
        PrintList(Advance(L));
    }
}

