/*
 * #1 error, confuse if(!Ptr), this means if(Ptr==NULL)
 * The use of recursion is worth studying in tree
 * The Delete function is a piece of gold
 */
#include "tree.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

struct TreeNode {
    ElementType data;
    Position left;
    Position right;
}; 


SearchTree MakeEmpty( SearchTree T )
{
    if (T) {
        T->data = 0;
        T->left = NULL;
        T->right = NULL;
    }

    return NULL;
}


#if 0
Position FindParent( ElementType X, SearchTree Parent, SearchTree Child )
{
    FAIL_ON_NULL(Child)

    if (Child->data == X) { /*found*/
        return Parent; /*for the root, use itself as the Parent*/
    } else {
        if (!Child->left && Child->data<=X) 
            return Find(X, Child, Child->left);
        else if (!Child->right && Child->data>X) 
            return Find(X, Child, Child->right);
    }

    /* if not found */
    return NULL;
}
#endif

Position Find( ElementType X, SearchTree T )
{
    if (!T) return NULL;

    if (T->data == X) 
        return T;
    else {
        if (X > T->data) return Find(X, T->right);
        if (X <= T->data) return Find(X, T->left);
    }
    return NULL;
}

Position FindMin( SearchTree T )
{
    FAIL_ON_NULL(T)

    if (!T->left) 
        return T;
    else 
        return FindMin(T->left);
}
Position FindMax( SearchTree T )
{
    FAIL_ON_NULL(T)

    if (!T->right)
        return T;
    else 
        return FindMax(T->right);        
}

SearchTree Insert( ElementType X, SearchTree T )
{
    if (!T) {
        T = malloc(sizeof(struct TreeNode)); 
        FAIL_ON_NULL(T)
        T->data = X;

    } else {
        if (X > T->data)
            T->right = Insert(X, T->right);
        else if (X <= T->data)
            T->left = Insert(X, T->left);
    }

    return T;
/*XXX:my logic*/
#if 0
    if (X > T->data) {
        /* if there is no right child */
        if (!T->right) {
            newNode = malloc(sizeof(struct TreeNode)); 
            MakeEmpty(newNode);
            newNode->data = X;

            T->right = newNode;
            return T->right;
        } else { /* else insert to the right child */
            return Insert(X, T->right);
        }
    } else if (X <= T->data) {
        /* if there is no left child */
        if (!T->left) {
            newNode = malloc(sizeof(struct TreeNode)); 
            MakeEmpty(newNode);
            newNode->data = X;

            T->left = newNode;
            return T->left;
        } else { /* else insert to the right child */
            return Insert(X, T->left);
        }
    }
#endif
}

SearchTree Delete( ElementType X, SearchTree T )
{
    Position tempCell;
    if (!T) {
        printf("element not found!\n");
    } else {
        if (T->data == X) {
            if (T->left && T->right) {
                tempCell = FindMin(T->right);
                T->data = tempCell->data;
                T->right = Delete(tempCell->data, T->right); 
            } else {
                if (T->left) {
                    tempCell = T->left;
                    free(T);
                    T = tempCell;
                } else if (T->right) {
                    tempCell = T->right;
                    free(T);
                    T = tempCell;
                } else {
                    free(T);
                    T = NULL;
                }
            }
        } else if (X > T->data) {
            T->right = Delete(X, T->right);
        } else if (X <= T->data) {
            T->left = Delete(X, T->left);
        }
    }
    
    return T;
}

ElementType Retrieve( Position P )
{
    FAIL_ON_NULL(P)

    return P->data;
}

void PrintTree(SearchTree T)
{

    if (!T) return;


    PrintTree(T->left);
    printf("%d, ", T->data);

    PrintTree(T->right);
    
}

