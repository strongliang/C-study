#include <assert.h>
#include "llist.h"

#define true 1
#define false 0

typedef struct {
    int capacity;
    int top;
    List data;
} StackRecord;

typedef StackRecord *Stack;

int IsEmpty( Stack S );
int IsFull( Stack S );
Stack CreateStack( int MaxElements );
void DisposeStack( Stack S );
void MakeEmpty( Stack S );
void Push( int X, Stack S );
int Top( Stack S );
void Pop( Stack S );
int TopAndPop( Stack S );
void PrintStack( Stack S );

