#define true 1
#include <assert.h>
#define false 0

#define Q_SIZE_MAX 100

#define FAIL_ON_NULL(q) if(!q) {\
                            printf("invalid "#q"\n"); \
                            assert(0);\
                        }

typedef struct {
    int capacity;
    int size;
    int in;
    int out;
    int *data;
} QueueRecord;

typedef QueueRecord *Queue;

int IsEmpty( Queue Q );
int IsFull( Queue Q );
Queue CreateQueue( int MaxElements );
void DisposeQueue( Queue Q );
void MakeEmpty( Queue Q );
void Enqueue( int X, Queue Q );
int Front( Queue Q );
void Dequeue( Queue Q );
int FrontAndDequeue( Queue Q );
