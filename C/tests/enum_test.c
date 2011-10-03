#include <stdio.h>

enum ret_code {
    OK = 0,
    ERR = -1,
    ERR_SYS = -2,
    ERR_OTHER /* the value of it is -1 */
};

int main()
{
    printf("ERR_OTHER is %d\n", ERR_OTHER);

    return 0;
}

