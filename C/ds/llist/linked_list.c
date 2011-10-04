#include <stdio.h>
#include <stdlib.h>

#include "linked_list.h"

#define TRUE 1
#define FALSE 0

void fatal(char * msg);

List MakeEmpty(List *L)
{
    if (!(*L=malloc(sizeof(struct Node)))) fatal("malloc failure");

    (*L)->next = NULL;
    (*L)->data = 0;

    return *L;
}

void DeleteList (List L)
{

    if (L->next == NULL) {
        return;
    }
    
    DeleteList (L->next);

    
    printf("freeing %d\n", (int)L->next->data);

    free (L->next);

    return;
}

PtrToNode Find (void* data, List L) 
{
    /* found */
    //if (!memcmp(&L->data, &data, sizeof(void*)))
    if (L->data == data) {
        printf("found %d\n", (int)data);
        return L;
    }

    /* not found */
    if (!L->next) {
        return NULL;
    }

    return Find(data, L->next);
}

void Insert(void* data, PtrToNode pos)
{
    PtrToNode tmpNode;
    if (!(tmpNode=malloc(sizeof(Node)))) fatal("malloc failure");

    tmpNode->next = pos->next;
    tmpNode->data = data;

    pos->next = tmpNode;

    printf("inserting %d\n", (int)pos->next->data);

    return;
}
void PrintList(List L)
{
    printf("%d,", (int)L->data);

    if (L->next == NULL) {
        printf("\n");
        return;
    }

    PrintList(L->next);

    printf("\n");
    
    return;
}

int IsEmpty(List L)
{
    return (L->next) ? FALSE : TRUE;
}

void doReverse (List *L, List *newHead)
{
    if (!(*L)->next) {
        *newHead = *L;
        return;
    }

    doReverse(&(*L)->next, newHead);

    (*L)->next->next = *L;

    return;
}

List ReverseList (List L)
{
    List newHead;

    doReverse (&L, &newHead);

    L->next = NULL;

    return newHead;

}

void fatal(char *msg)
{
    printf("%s\n", msg);
    
    exit(0);
}


