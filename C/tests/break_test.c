/* test where does the "break" jump to, right outside the while or to the
 * outmost layer of control. Answer: just right outside the loop */
/* also test the behavior of the "break" in if. Answer: compiler doesn't like it */

#include <stdio.h>

int main()
{
    int a = 1;

    if (a) {
        char b[] = "hello";
        char *bp = b;
        while (bp != '\0') {
            putchar(*bp++);
            if (*bp == 'o') {
                printf("hit an o\n");
                break;
            }
        }
        //break;
        printf("return inside a\n");
    }
    printf("return outside a\n");
}
