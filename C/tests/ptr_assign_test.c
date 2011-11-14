#include <stdio.h>

int main()
{
    int a;
    int *ptr_a, *ptr_b;

    ptr_a = ptr_b;

    printf("1: ptr_a = 0x%p, ptr_b = 0x%p\n", 
            ptr_a, ptr_b);

    ptr_b = &a;

    printf("2: ptr_a = 0x%p, ptr_b = 0x%p\n", 
            ptr_a, ptr_b);

    a = 10;

    printf("3: ptr_a = 0x%p, ptr_b = 0x%p\n", 
            ptr_a, ptr_b);
#if 0
    printf("*ptr_a = %d, *ptr_b = %d\n", 
            *ptr_a, *ptr_b);
#endif

    return 0;
}
