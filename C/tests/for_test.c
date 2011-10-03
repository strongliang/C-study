#include <stdio.h>

int main() 
{
    int idx = 0;

    for (idx++; idx++<10; idx++) {
        printf("idx = %d\n", idx);
    }

    return 0;
}
