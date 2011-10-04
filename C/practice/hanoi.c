#include <stdio.h>

void moveSingle(char start, char finish)
{
    printf("%c -> %c\n", start, finish);
}

void moveTower(int n, char start, char finish, char temp)
{
    if (n == 1) moveSingle(start, finish);
    else {
        moveTower(n-1, start, temp, finish);
        moveSingle(start, finish);
        moveTower(n-1, temp, finish, start);
    }
}


int main(int argc, char *argv[])
{
    int target;
    char start='A';
    char finish='B';
    char temp='C';


    if (argc != 2) return 0;

    target = atoi(argv[1]);

    moveTower(target, start, finish, temp);

    return 0;
}

