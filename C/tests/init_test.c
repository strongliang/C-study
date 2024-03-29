/* local vars have undefined values, though if you define some local ints, they
 * may all appear to be 0. The easiest way to check upon this is to declare an
 * array that's big and dump out the value of it. (see local_arr_dump) */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int i_g;
static i_s;
char str_g[10000];
//char *str_p = malloc (100); //cannot do this

void print_arr(char *arr, size_t size)
{
    int i;
    for (i=0; i<size; i++) {
        //putchar(*arr++);
        printf("%0x", *arr++);
        if ((i+1)%32 == 0) putchar('\n');
    }
}
int main()
{
    int i_a;
    char str_a[10000];
    char *str_p = malloc(10000);
    strncpy(str_p, "hello", 6);
    free(str_p);
    str_p = malloc(10000);

    printf("i_g = %d, "
           "i_s = %d, "
           "i_a = %d, ",
           i_g,
           i_s,
           i_a);

    putchar('\n');

    printf("sizeof(str_a) is: %ld\n", sizeof(str_a));
    printf("sizeof(str_g) is: %ld\n", sizeof(str_g));
    printf("sizeof(\"hello\") is: %ld\n", sizeof("hello"));

    printf("\n===local array===\n");
    print_arr(str_a, sizeof(str_a));
    printf("\n===global array===\n");
    print_arr(str_g, sizeof(str_g));
    printf("\n===malloc array===\n");
    print_arr(str_p, 10000);

    return 0;
}

