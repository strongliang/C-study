#include <stdio.h>

#define A 'A'
#define B 'B'
#define C 'C'

void moveDisc (char start_axis, char end_axis) 
{
    printf("from %c to %c\n", start_axis, end_axis);
}

void moveTower (int num_of_disc, char start_axis, char end_axis, char tmp_axis)
{
    if (1 == num_of_disc) {
        moveDisc(start_axis, end_axis);
    } else {
        moveTower (num_of_disc-1, start_axis, tmp_axis, end_axis);
        moveDisc (start_axis, end_axis);
        moveTower (num_of_disc-1, tmp_axis, end_axis, start_axis);
    }
}

int main (int argc, char* argv[])
{
    if (argc != 2) return;
    
    int num_of_disc = atoi(argv[1]);
    char start_axis = A;
    char end_axis = B;
    char tmp_axis = C;

    moveTower(num_of_disc, start_axis, end_axis, tmp_axis);

    return 0;
}
