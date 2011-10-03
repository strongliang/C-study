#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define OK 0
#define ERR -1
int main(int argc, char* argv[])
{
    char str1[] = "hello";
    char *str2 = "hello";
    char *str3 = malloc(sizeof(char) * 10);

    strncpy(str3, "1111111111", 10);
    strncpy(str3, str2, 4);

    printf("str1 = %s\n", (str1));
    printf("strlen(str1) = %ld\n", strlen(str1));
    printf("str2 = %s\n", (str2));
    printf("strlen(str2) = %ld\n", strlen(str2));
    printf("str3 = %s\n", (str3));
    printf("strlen(str3) = %ld\n", strlen(str3)); /* this may crash since strlen is trying to find the '\0' */

    return OK;
}
