#ifndef _TEST_DEFS_
#define _TEST_DEFS_

typedef enum {
    NO_ERR = 0,
    FOPEN_ERR = -1,
    FTELL_ERR = -2,
    FREAD_ERR = -3,
    MALLOC_ERR = -4,
    KW_NOT_FOUND = -5,
    NUM_NOT_FOUND = -6,
    INVALID_ARG_ERR = -7
} basic_errs_e;

#endif

