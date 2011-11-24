/* two ways to init a struct var */
#include <stdio.h>

typedef struct {
    int a;
    char b;
} blah;


int main()
{
    blah my_blah = { .a=10, .b='c'};
    blah my_blah2 = { 20, 'b'};

    printf("my_blah.a = %d, my_blah.b=%c\n",
            my_blah.a, my_blah.b);
    printf("my_blah.a = %d, my_blah.b=%c\n",
            my_blah2.a, my_blah2.b);
    return 0;
}

