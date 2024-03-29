#include <stdio.h>

/*
 * pay extra attention in the pivotSort termination condition
 * this program screwed me up for 30 minutes because of the the size.
 * I should have used size - 1 as the end of the array insteand of the size
 * itself; On the other hand, the print take the size instead of the actual index
 */


//quick sort

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

int pivotSort(int arr[], int start, int end, int pivot)
{
    int lPtr, rPtr; //two moving indexes that are used to pivot sort
    int pivotVal = arr[pivot];

    //swap pivot with the 1st element
    swap(arr, start, pivot);

    lPtr = start+1;
    rPtr = end;

    //while (rPtr > lPtr) {
    while (1) {
        while ((arr[rPtr]>=pivotVal) && (lPtr<rPtr)) rPtr--;

        while ((arr[lPtr]<pivotVal) && (lPtr<rPtr)) lPtr++; 

        if (lPtr == rPtr) break;

        swap(arr, lPtr, rPtr);

    }
    if (arr[lPtr] >= pivotVal) return start; //XXX: you may pick the smallest as pivot,
                                       //in which case you don't want to swap

    swap(arr, start, rPtr);

    //printArray(arr, start, end+1);

    return rPtr;
}
//XXX: sometimes the cutOff can mess it up, if it lands on one of the boundary.
//Check boundary
void quickSort(int arr[], int start, int end)
{
    /* both pivot and cutOff are the dividor of the array, one is before the
     * sort, the other is after the sort */
    int cutOff; 
    int pivot; 

    //printf("start = %d, end = %d\n", start, end);

    //1 element return;
    if (start == end) return; 
    //more elements, get the pivot
    pivot = getPivot(start, end);
    //pivot sort
    cutOff = pivotSort(arr, start, end, pivot);


    printf("start = %d, end=%d, cutOff = %d\n", start, end, cutOff);

    //recursive call on the 2 sub divisions of the array
    if (cutOff>start) quickSort(arr, start, cutOff-1);
    if (cutOff<end) quickSort(arr, cutOff+1, end);
}

//XXX: really should be a param
int tmp[100];

void merge(int arr[], int start, int end, int median)
{
    int lPtr, rPtr;
    int i = 0;

    lPtr = start;
    rPtr = median+1;

    //XXX: this is the crucial part, how to construct the correct tmp array. 
    //there could be a case: 1 side finished, the other side still have multiple
    //elements. 
    while ((lPtr<=median) && (rPtr<=end)) {

        if (arr[lPtr] <= arr[rPtr]) tmp[i++] = arr[lPtr++]; 

        if (arr[rPtr] < arr[lPtr]) tmp[i++] = arr[rPtr++];
    }

    //XXX: if one side has more elements, meaning those elements are all bigger
    //than the biggest of the other side, just use those to fill the rest of the
    //tmp array
    if (lPtr<median) while (lPtr<=median) tmp[i++] = arr[lPtr++];
    if (rPtr<end) while (rPtr<=end) tmp[i++] = arr[rPtr++];
    
    //XXX: this is a case where one side has just one element bigger
    tmp[i] = arr[median]>arr[end] ? arr[median] : arr[end];

    //printf("tmp: ");
    //printArray(tmp, 0, (end-start+1));

    //printf("end-start=%d\n", end-start);

    for (i=0; i<(end-start+1); i++) {
        arr[start+i] = tmp[i]; //XXX: don't do a start++ here, in fact, in the for loop
                                    //it's not a good idea to use that statement
                                    //either. the limit keep changing. always
                                    //just use a new variable
    }

    //printf("arr: ");
    //printArray(arr, start, end+1);

    return;
}

//merge sort
void mergeSort(int arr[], int start, int end)
{
    int median = getPivot(start, end);

    //1 element return;
    if (start == end) return;
    //2 element, sort and return
    if (start == (end-1)) {
        if (arr[start]>arr[end]) swap(arr, start, end);
        return;
    }
    //more elements, keep dividing
    mergeSort(arr, start, median);
    mergeSort(arr, median+1, end);

    //merge the two sub arrays just got sorted
    merge(arr, start, end, median);

    return;

}



int main(int argc, char *argv[])
{
    //int arr[] = {23, 15, 99, 6, 27, 49, 11, 0, 58, 22, 31, 5, 5, 110};
    //int arr[] = {23, 15, 6, 27, 49, 11, 58, 22, 110};
    int arr[] = {23, 15, 99, 6, 27, 27, 33, 54, 54, 54, 49, 11, 0, 58, 22, 31, 5, 5, 110};
    //int arr[] = {1, 2, 3};
    //int arr[] = {3, 2, 1};
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

//#if 0
    printf("=================MERGE=====================\n");
    mergeSort(arr, 0, size-1);
    printArray(arr, 0, size);
    printf("==============END OF MERGE=================\n");
//#endif

    return 0;
}

