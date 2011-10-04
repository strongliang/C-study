#include <stdio.h>

/*XXX: interesting use of macro K&R A12.3*/
#define TEST(q) if(!q) {\
                    printf("invalid "#q"\n"); \
                }


int main()
{
    void *ptr = NULL;

    TEST(ptr);

    return 0;
}
