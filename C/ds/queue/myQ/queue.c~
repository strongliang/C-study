#include <stdio.h>
#include <stdlib.h>
#include "queue.h"

/*return true or false*/
int IsEmpty( Queue Q )
{
    return Q->size==0;
}


/*return true or false*/
int IsFull( Queue Q )
{
    return Q->capacity==Q->size; 
}

/*return a Queue or NULL*/
Queue CreateQueue( int MaxElements )
{
    Queue q = NULL;

    if (MaxElements > Q_SIZE_MAX) {
        printf("%d is too big!\n", MaxElements);
        return NULL;
    }

    if(!(q = malloc( sizeof(*q))) ) {
        printf("malloc failed!\n");
        return NULL;
    }
    
    if(!(q->data = malloc( sizeof(int)*MaxElements)) ) {
        printf("malloc failed!\n");
        return NULL;
    }

    q->capacity = MaxElements;
    q->size = 0;
    q->out = 0;
    q->in = 0;

    return q;

}

void DisposeQueue( Queue Q )
{
    FAIL_ON_NULL(Q);
    FAIL_ON_NULL(Q->data);

    free(Q->data);
    free(Q);
}

int Front( Queue Q )
{
    FAIL_ON_NULL(Q);

    return Q->data[Q->out];
}

void Enqueue( int X, Queue Q )
{
    FAIL_ON_NULL(Q);

    if (IsFull(Q)) {
        printf("Q full!\n");
        return;
    }
    
    Q->data[Q->in] = X;
    /*in should never meet out, in which case the queue is overflown*/
    if (Q->in==Q->capacity-1) {
        Q->in = 0;
    } else {
        Q->in++;
    }

    Q->size++;
}

void Dequeue( Queue Q )
{
    FAIL_ON_NULL(Q);

    if (IsEmpty(Q)) {
        printf("Q Empty\n");
        return;
    }

    if (Q->out==Q->capacity-1) {
        Q->out = 0;
    } else {
        Q->out++;
    }

    Q->size--;
}

int FrontAndDequeue( Queue Q )
{
    int front = Front(Q);
    Dequeue(Q);

    return front;
}


