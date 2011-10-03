#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "test_defs.h"

#define MAX_LEN 80

int main(int argc, char* argv[])
{
    char *list = NULL;

    if((list=malloc(MAX_LEN * argc))==NULL) {
        //bad
        printf("bad\n");
    } else {
        int i = 0;

        for (; i<argc; i++) {
            strncpy(&list[i*MAX_LEN], argv[i], MAX_LEN-1);
            //strncpy((*list+i*MAX_LEN), argv[i], MAX_LEN-1);
            list[(i+1)*MAX_LEN-1] = 0;
        }
        for (i=0; i<argc; i++) {
            printf("list %d is %s\n", i, list+(i*MAX_LEN));
        }

        free(list);
    }

    return 0;
}

