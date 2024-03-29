/*
 * the result shows the byte order. 0x080f is stored as 0f, 08
 */
#include <stdio.h>
#include <stdlib.h>

union word {
    short x;
    char  bytes[2];
};

int main()
{
    union word w;

    w.x = 0x080f;

    printf("1st byte is 0x%x, 2nd byte is 0x%x\n", w.bytes[0], w.bytes[1]);

    return 0;
}
