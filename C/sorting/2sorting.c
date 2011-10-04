#include <stdio.h>


void printArray(int arr[], int start, int end)
{
    int i;

    for(i=start; i<end; i++) {
        printf("[%d] %d, ", i, arr[i]);
    }
    printf("\n");
}

void swap(int arr[], int elem1, int elem2)
{
    int temp;
    temp = arr[elem1];
    arr[elem1] = arr[elem2];
    arr[elem2] = temp;

    return;
}

int getPivot(int start, int end)
{
    return (start + end) / 2;
}

static int partition(int arr[], int start, int end)
{
    int lh, rh;
    int pivot, pivotVal;

    //init the handlers
    lh = start + 1;
    rh = end;
    //get pivot
    pivot = getPivot(start, end);
    pivotVal = arr[pivot];
    //swap pivot with the 1st element
    swap(arr, start, pivot);
    //sort the partitions
    while (1) {
        while ((arr[rh]>=pivotVal) && (rh>lh)) rh--;
        while ((arr[lh]<pivotVal) && (rh>lh)) lh++;

        if (rh==lh) break;

        swap(arr, lh, rh);
    }
    if (arr[lh] >= pivotVal) return start; //XXX: you may pick the smallest as pivot,
                                       //in which case you don't want to swap
    //swap back pivot with the 1st element
    swap(arr, start, lh);

    return rh;
    
}
void quickSort(int arr[], int start, int end)
{
    int boundary;

    //1 element return;
    if (start == end) return; 

    //more elements, partition
    boundary = partition(arr, start, end);

    if (boundary > start) quickSort(arr, start, boundary-1);
    if (boundary < end) quickSort(arr, boundary+1, end);

    return;
}

int main(int argc, char *argv[])
{
    //int arr[] = {23, 15, 99, 6, 27, 49, 11, 0, 58, 22, 31, 5, 5, 110};
    //int arr[] = {23, 15, 6, 27, 49, 11, 58, 22, 110};
    int arr[] = {23, 15, 99, 6, 27, 27, 33, 54, 54, 54, 49, 11, 0, 58, 22, 31, 5, 5, 110};
    //int arr[] = {1, 2, 3};
    //int arr[] = {3, 2, 1};
    //int arr[] = {3, 1, 2};
    int size = sizeof(arr)>>2;

    //printf("size = %d\n", size);

    printf("=================INIT=====================\n");
    printArray(arr, 0, size);
//#if 0
    printf("=================QUICK=====================\n");
    quickSort(arr, 0, size-1);
    printArray(arr, 0, size);
    printf("==============END OF QUICK=================\n");
//#endif

#if 0
    printf("=================MERGE=====================\n");
    mergeSort(arr, 0, size-1);
    printArray(arr, 0, size);
    printf("==============END OF MERGE=================\n");
#endif

    return 0;
}

