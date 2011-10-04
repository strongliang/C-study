#include <assert.h>

typedef int ElementType;

#define FAIL_ON_NULL(p) if(!p) {\
                            printf("invalid "#p"\n"); \
                            assert(0);\
                        }

#ifndef _Tree_H
#define _Tree_H

struct TreeNode;
typedef struct TreeNode *Position;
typedef struct TreeNode *SearchTree;

SearchTree MakeEmpty( SearchTree T );
Position Find( ElementType X, SearchTree T );
Position FindMin( SearchTree T );
Position FindMax( SearchTree T );
SearchTree Insert( ElementType X, SearchTree T );
SearchTree Delete( ElementType X, SearchTree T );
ElementType Retrieve( Position P );
void PrintTree(SearchTree T);

#endif  /* _Tree_H */

