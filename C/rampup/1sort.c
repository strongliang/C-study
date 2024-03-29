/*
 * Mistakes;
 * . sizeof(arr) is not the number of elements
 * . in the outter for loop, use size
 * . in the inner for loop, use size -1
 */
#include <stdio.h>

/*
 * swap  two numbers in a array
 */
void swap(int arr[], int left, int right)
{
    int temp;

    temp = arr[left];
    arr[left] = arr[right];
    arr[right] = temp;
}
/*
 * every time, moves the biggest to the end
 */
void bubbleSort(int arr[], int size)
{
   int i, j;
   int done;

   for (i=0; i<size; i++) {
       done = 1;
       for (j=0; j<size-1-i; j++) {
           if (arr[j] > arr[j+1]) {
               done = 0;
               swap (arr, j, j+1);
           }
       }
       if (done) 
           break;
   }
   printf("stopped at %d's iter\n", i+1);
}

void printArray(int arr[], int size)
{
    int i;

    for (i=0; i<size-1; i++) {
        printf("%c", arr[i]);
    }
    printf("\n");
    for (i=0; i<size-1; i++) {
        printf("%d, ", arr[i]);
    }
    printf("\n");
}

int main ()
{
    /*int arr[] = {23, 15, 99, 6, 27, 27, 33, 54, 54, 54, 49, 11, 0, 58, 22, 31,
     * 5, 5, 110};*/
     int arr[] = {'H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!'};
    int size = sizeof(arr) / sizeof(int);
    printArray(arr, size);

    bubbleSort(arr, size);

    printArray(arr, size);
    return 0;
}

