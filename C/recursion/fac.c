#include <stdio.h>

int fac(int val)
{
    if (0 == val) return 1;

    return val * fac(val-1);
}


int main(int argc, char* argv[])
{
    int val;

    if (argc != 2) return -1;
    val = atoi(argv[1]);

    printf("fac(%d) = %d\n", val, fac(val));

    return 0;
}
