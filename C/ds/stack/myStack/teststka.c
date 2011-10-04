#include <stdio.h>
#include "stack2.h"

int main( )
{
    Stack S;
    int i;

    S = CreateStack( 12 );
    for( i = 0; i < 10; i++ )
        Push( i, S );

    PrintStack(S);

#if 0
    while( !IsEmpty( S ) )
    {
        printf( "%d\n", Top( S ) );
        Pop( S );
    }
#endif
    for( i = 0; i < 5; i++ )
        Pop(S);

    PrintStack(S);

    DisposeStack( S );

    return 0;
}

