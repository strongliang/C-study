#include <stdio.h>
#include <stdlib.h>
#include "test_defs.h"

int main(int argc, char* argv[])
{
    basic_errs_e retstats = NO_ERR;

    if (argc != 2) {
        retstats = INVALID_ARG_ERR;
    } else {
        int result; /* conversion result */
        if ((result=atoi(argv[1]))==0) {
            char *input_ptr = argv[1];
            while (result==0 && *input_ptr!='\n' && *input_ptr!=EOF) {
                result = atoi(++input_ptr);
            }
        } else {
            /* happy */
        }
        printf("intput: %s\n result: %d\n", argv[1], result);
    }

    if (retstats) printf("retstats: %d\n", retstats);

    return retstats;
}

