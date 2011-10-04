#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "stack.h"


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

    if( !(s->data=malloc(sizeof(int) * MaxElements)) ) {
        printf("malloc failed!\n");
        return NULL;
    }

    s->capacity = MaxElements;

    MakeEmpty(s);

    return s;
}

void MakeEmpty( Stack S )
{
    S->top = -1;
    memset(S->data, 0, sizeof(*S->data));
}

void DisposeStack( Stack S )
{
    FAIL_ON_NULL(S)
    FAIL_ON_NULL(S->data)

    free(S->data);
    free(S);
}

void Push( int X, Stack S )
{
    FAIL_ON_NULL(S)

    if (IsFull(S)) {
        printf("Q full!\n");
        return;
    }

    S->data[++S->top] = X;
}

int Top( Stack S )
{
    FAIL_ON_NULL(S)

    return S->data[S->top];

}

void Pop( Stack S )
{
    FAIL_ON_NULL(S)

    if (IsEmpty(S)) {
        printf("Stack Empty\n");
        return;
    }

    S->top--;
}

int TopAndPop( Stack S )
{
    int top = Top(S);
    Pop(S);

    return top;
}

