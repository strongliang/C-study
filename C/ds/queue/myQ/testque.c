#include <stdio.h>
#include "queue.h"

int main( )
{
    Queue Q;
    int i;

    Q = CreateQueue( 12 );

    FAIL_ON_NULL(Q->data)
    
    i=0;
    for( i = 0; i < 10; i++ )
        Enqueue( i, Q );

    while( !IsEmpty( Q ) )
    {
        printf( "%d\n", Front( Q ) );
        Dequeue( Q );
    }
    for( i = 0; i < 20; i++ )
        Enqueue( i, Q );

    while( !IsEmpty( Q ) )
    {
        printf( "%d\n", Front( Q ) );
        Dequeue( Q );
    }

    DisposeQueue( Q );
    return 0;
}

