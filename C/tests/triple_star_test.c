#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "test_defs.h"

int foo (char ***list) 
{
    int retstat = NO_ERR;

    *list = malloc(sizeof(char *) * 3);
    if (*list == NULL) {
        retstat = MALLOC_ERR;
    } else {
        int i;
        for (i=0; i<3; i++) {
            (*list)[i] = malloc(sizeof(char) * 10);
            if ((*list)[i] == NULL) {
                retstat = MALLOC_ERR;
                break;
            }
        }
        strncpy((*list)[0], "Hello", 9);
        strncpy((*list)[1], " World", 9);
        strncpy((*list)[2], "! Bye!\n", 9);
    }

    return retstat;
}

int main()
{
    int retstat = NO_ERR;
    char **list = NULL;

    if ((retstat=foo(&list)) != NO_ERR) {
        printf("retstat = %d\n", retstat);
    } else {
        int i;

        for (i=0; i<3; i++) {
            printf("%s", list[i]);
        }
        putchar('\n');

        //not freeing *list for simplicity
        free(list);
    }


    return 0;
}
