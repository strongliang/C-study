#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct {
    unsigned int a : 1;
    unsigned int b : 1;
    unsigned int c : 1;
} flag1;

struct {
    unsigned int a : 1;
    unsigned int b : 1;
} flag2;

struct {
    unsigned int a : 1;
} flag3;

struct {
    unsigned int a : 1,
                 : 2;
} flag4;

#if 0
//this guy doesn't compile
struct {
    unsigned int a : 1;
    unsigned int b : 20;
    unsigned int c : 33;
} flag5;
#endif
struct {
    unsigned int a : 1;
    unsigned int b : 20;
    unsigned int c : 31;
} flag6;

/* total size is 64 bits, but b2 crosses word boundary */
/* on a mac, the result is 12 bytes, meaning no boundary crossing*/
struct {
    unsigned int a : 1;
    unsigned int b : 20;
    unsigned int b2 : 12;
    unsigned int c : 31;
} flag7;

static void hex_dump(void *data, size_t size)
{
    /* dumps size bytes of *data to stdout. Looks like:
     * [0000] 75 6E 6B 6E 6F 77 6E 20
     *                  30 FF 00 00 00 00 39 00 unknown 0.....9.
     * (in a single line of course)
     */

    unsigned char *p = data;
    unsigned char c;
    int n;
    char bytestr[4] = {0};
    char addrstr[10] = {0};
    char hexstr[ 16*3 + 5] = {0};
    char charstr[16*1 + 5] = {0};
    for(n=1;n<=size;n++) {
        if (n%16 == 1) {
            /* store address for this line */
            snprintf(addrstr, sizeof(addrstr), "%.4lx",
               ((unsigned long int)p-(unsigned long int)data) );
        }
            
        c = *p;
        if (isalnum(c) == 0) {
            c = '.';
        }

        /* store hex str (for left side) */
        snprintf(bytestr, sizeof(bytestr), "%02X ", *p);
        strncat(hexstr, bytestr, sizeof(hexstr)-strlen(hexstr)-1);

        /* store char str (for right side) */
        snprintf(bytestr, sizeof(bytestr), "%c", c);
        strncat(charstr, bytestr, sizeof(charstr)-strlen(charstr)-1);

        if(n%16 == 0) { 
            /* line completed */
            printf("[%4.4s]   %-50.50s  %s\n", addrstr, hexstr, charstr);
            hexstr[0] = 0;
            charstr[0] = 0;
        } else if(n%8 == 0) {
            /* half line: add whitespaces */
            strncat(hexstr, "  ", sizeof(hexstr)-strlen(hexstr)-1);
            strncat(charstr, " ", sizeof(charstr)-strlen(charstr)-1);
        }
        p++; /* next byte */
    }

    if (strlen(hexstr) > 0) {
        /* print rest of buffer if not empty */
        printf("[%4.4s]   %-50.50s  %s\n", addrstr, hexstr, charstr);
    }
}

int main()
{
    printf("sizeof(int) is %ld\n", sizeof(int));
    printf("sizeof(flag1) is %ld\n", sizeof(flag1));
    printf("sizeof(flag2) is %ld\n", sizeof(flag2));
    printf("sizeof(flag3) is %ld\n", sizeof(flag3));
    printf("sizeof(flag4) is %ld\n", sizeof(flag4));
    //printf("sizeof(flag5) is %ld\n", sizeof(flag5));
    printf("sizeof(flag6) is %ld\n", sizeof(flag6));
    flag6.a = 1;
    flag6.c = 0x11;
    printf("sizeof(flag7) is %ld\n", sizeof(flag7));

    hex_dump(&flag6, sizeof(flag6));


    return 0;
}
