#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
 * check if the array is sorted
 */
int orderCheck(int arr[], int size)
{
    int i;

    for (i=0; i<size-1; i++) {
        if (arr[i] > arr[i+1]) {
            printf("disorder at %dth\n", i);
            return -1;
        }
    }
    return 0;
}

int* makeIntArr(char* arr_char[], int size)
{
    int i;
    int *arr_int;
    
    printf("1\n");
    arr_int = malloc(sizeof(int) * size);
    printf("2\n");


    for (i=1; i<size; i++) {
        *(arr_int + i - 1) = atoi(arr_char[i]);
        /*XXX: the following doesn't work*/
        /* *(arr_int + i) = atoi(arr_char[i+1]); */
    }
    printf("3\n");
    return arr_int;
}


int main(int argc, char *argv[])
{
    int i;
    int *arr_int;

    if (argc <= 1) return -1;

    arr_int = makeIntArr(argv, argc);

    for (i=0; i<argc-1; i++) {
        printf("%d, ", *(arr_int+i));
    }
    printf("\n");

    orderCheck(arr_int, argc-1);

    free(arr_int);

    return 0;
}
