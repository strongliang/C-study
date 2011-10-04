#include "tree.h"
#include <stdio.h>

int main( )
{
    SearchTree T;
    Position P;
    int i;
    int j = 0;

    T = MakeEmpty( NULL );
    for( i = 0; i < 50; i++, j = ( j + 7 ) % 50 )
        T = Insert( j, T );

    PrintTree(T);    
    printf("\n");

    for( i = 0; i < 50; i++ )
        if( ( P = Find( i, T ) ) == NULL || Retrieve( P ) != i )
            printf( "1 Error at %d\n", i );

    for( i = 0; i < 50; i += 2 )
        T = Delete( i, T );

    PrintTree(T);    

    for( i = 1; i < 50; i += 2 )
        if( ( P = Find( i, T ) ) == NULL || Retrieve( P ) != i )
            printf( "2 Error at %d\n", i );

    for( i = 0; i < 50; i += 2 )
        if( ( P = Find( i, T ) ) != NULL )
            printf( "3 Error at %d\n", i );

    printf( "Min is %d, Max is %d\n", Retrieve( FindMin( T ) ),
               Retrieve( FindMax( T ) ) );

    return 0;
}

