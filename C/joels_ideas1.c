#include <stdio.h>
#include <stdlib.h>

typedef enum {
    NO_ERR = 0,
    ERR_MALLOC
} ret_code_e;

int main()
{
    int *ptr_a = NULL;
    ret_code_e retstat = NO_ERR;

    ptr_a = malloc(sizeof(*ptr_a));

    printf("sizeof(int) is %ld\n", sizeof(int));
    printf("sizeof(*ptr_a) is %ld, sizeof(ptr_a) is %ld\n",
            sizeof(*ptr_a), sizeof(ptr_a));
    if (ptr_a == NULL) {
        printf("ptr_b didn't get malloced\n");
        retstat = ERR_MALLOC;
    } else {
        int *ptr_b = NULL;
        ptr_b = malloc(sizeof(*ptr_b));
        if (ptr_b == NULL) {
            printf("ptr_b didn't get malloced\n");
            retstat = ERR_MALLOC;
        } else {
            printf("everything good\n");
            free(ptr_b);
        }
        free(ptr_a);
    }

    switch (retstat) {
        char msg[] = "no error";
        case NO_ERR:
            break;

        case ERR_MALLOC:
            break;

        default:
            break;
    }

    return retstat;
}
