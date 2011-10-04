/* 
 * generally, don't do sizeof(<var-name>), but instead, give a concrete size.
 * Because different types of variable may work with sizeof in different ways
 * if there is a ptr to a struct ptr_str, sizeof(*ptr_str) shows the size of
 * struct; but if there is a char ptr ptr_char, sizeof(*ptr_char) only shows 
 * the size of a single char. to get the size of an array, the array reference
 * has to be used, but sometimes in passing the array reference as parameter, I
 * use char *, which changes the sizeof behavior. So it's simpler just to use a
 * concrete #define size, or only use sizeof on structs
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>


typedef struct {
    char name[20];
    int age;
    char instr[20];
} * Musician;

int main()
{
    /*how to print out the largest int and what's the value of it*/
    unsigned int i=0xffffffff;
    int j=0xffffffff;
    printf("i=%d\n", i);
    printf("j=%u\n", i);

    /* tricky sizeof */
    int *intArr = malloc (sizeof(int *) * 10);
    char *charArr = malloc (sizeof(char *) * 10);
    int arr[10];
    /* both sizeof(intArr) and sizeof(*intArr) are of 4 bytes  */
    printf("sizeof(intArr) is %d\n", sizeof(intArr));
    printf("sizeof(*intArr) is %d\n", sizeof(*intArr));

    /* sizeof(charArr) is 4 and sizeof(*charArr) is 1*/
    printf("sizeof(charArr) is %d\n", sizeof(charArr));
    printf("sizeof(*charArr) is %d\n", sizeof(*charArr));

    printf("sizeof(arr) is %d\n", sizeof(arr));

    /*string, there is a '1' difference between sizeof and strlen*/
    char *str = "hello";
    char str2[] = "hello";
    unsigned char str3[] = "hello"; /*XXX: strlen expects char* not unsigned char*/
    int int_arr[] = {23, 15, 6, 27, 49, 11, 58};

    printf("sizeof(str) is %d\n", sizeof(str));
    printf("strlen(str) is %d\n", strlen(str));

    printf("sizeof(str2) is %d\n", sizeof(str2));
    printf("strlen(str2) is %d\n", strlen(str2));

    printf("strlen(str3) is %d\n", strlen(str3));

    printf("sizeof(int_arr)/sizeof(int) is %d\n", sizeof(int_arr)/sizeof(int));

    /*struct, need to malloc strong using sizeof(*strong)*/
    Musician strong;

    printf("sizeof(strong) is %d\n", sizeof(strong));
    printf("sizeof(*strong) is %d\n", sizeof(*strong));

    printf("sizeof(Musician) is %d\n", sizeof(Musician));

    /*printf("sizeof(*Musician) is %d\n", sizeof(*Musician)); XXX: illegal*/

    /*EOF*/
    int c; /*XXX: shouldn't be a char */
    printf("EOF is %d\n", EOF);
    while ((c=getchar()) != EOF) { /*XXX: ctrl+D*/
        putchar(c);
    }
    printf("got EOF");
    putchar('\n');


    return 0;
}
