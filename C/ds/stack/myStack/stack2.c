#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "stack2.h"

int IsEmpty( Stack S )
{
    return S->top < 0;
}


int IsFull( Stack S )
{
    return S->capacity - 1 == S->top;
}

Stack CreateStack( int MaxElements )
{
    Stack s;

    if ( !(s=malloc(sizeof(StackRecord))) ) {
        printf("malloc failed!\n");
        return NULL;
    }

    /*We don't need to create the first Node coz the list doesn't have a header*/
#if 0
    if( !(s->data=malloc(sizeof(struct ListRecord))) ) {
        printf("malloc failed!\n");
        return NULL;
    }
#endif

    s->capacity = MaxElements;

    MakeEmpty(s);

    return s;
}

void MakeEmpty( Stack S )
{
    S->top = -1;
    S->data = NULL;
}

void DisposeStack( Stack S )
{
    FAIL_ON_NULL(S)
    
    /*DisposeList takes care of this*/
#if 0
    FAIL_ON_NULL(S->data)
#endif

    DisposeList(&S->data);
    free(S);
}

void Push( int X, Stack S )
{
    FAIL_ON_NULL(S)

    if (IsFull(S)) {
        printf("Q full!\n");
        return;
    }

    S->top++;
    InsertInFront(&S->data, X);
}

int Top( Stack S )
{
    FAIL_ON_NULL(S)

    return S->data->data;

}

void Pop( Stack S )
{
    FAIL_ON_NULL(S)

    if (IsEmpty(S)) {
        printf("Stack Empty\n");
        return;
    }

    S->top--;
    Delete(&S->data, S->data); 
}

int TopAndPop( Stack S )
{
    int top = Top(S);
    Pop(S);

    return top;
}

void PrintStack( Stack S )
{
    PrintList(S->data);
}

