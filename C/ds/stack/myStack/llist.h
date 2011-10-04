#include <assert.h>

#define true 1
#define false 0

#define FAIL_ON_NULL(p) if(!p) {\
                            printf("invalid "#p"\n"); \
                            assert(0);\
                        }

struct ListRecord{
    int data;
    struct ListRecord *prev;
    struct ListRecord *next;
}; 

typedef struct ListRecord *List;
typedef List Position;
typedef List Node;


List CreateList();
void DisposeList(List *L);
void InsertInFront(List *L, int X);
void Remove(List *L, int X);
void Delete(List *L, Position P);
Position Advance(Position P);
Position Find(List L, int X);
void PrintList(List L);

