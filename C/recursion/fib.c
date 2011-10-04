#include <stdio.h>

int fib(int a)
{
    if (0 == a) return 0;
    if (1 == a) return 1;
    else {
        return fib(a-1) + fib(a-2);
    }
}

int main(int argc, char* argv[])
{
    int val;

    if (argc != 2) return -1;
    val = atoi(argv[1]);

    printf("fib(%d) = %d\n", val, fib(val));

    return 0;
}
