#include <stdio.h>
#include <stdlib.h>

struct _TNode {
    int data;
    struct _TNode *left;
    struct _TNode *right;
};

typedef struct _TNode* TNode;
typedef TNode Tree;

Tree treeAddNode (Tree tree, int node_data)
{
    if (tree == NULL) {
        tree = malloc(sizeof(struct _TNode));
        tree->data = node_data;
        tree->left = NULL;
        tree->right = NULL;
        
    } else if (node_data < tree->data) {
        tree->left = treeAddNode(tree->left, node_data);
    } else {
        tree->right = treeAddNode(tree->right, node_data);
    }

    return tree;
}

void treePrint (Tree tree, int depth)
{
    if (tree == NULL) return;
    if (tree->left) treePrint(tree->left, depth+1); 
    printf("data: %d, depth: %d\n", tree->data, depth); 
    if (tree->right) treePrint(tree->right, depth+1); 
}


int main (int argc, char* argv[])
{
    Tree tree = NULL;

    tree = treeAddNode(tree, 5);
    tree = treeAddNode(tree, 3);
    tree = treeAddNode(tree, 8);
    tree = treeAddNode(tree, 1);
    tree = treeAddNode(tree, 2);
    tree = treeAddNode(tree, 9);

    treePrint(tree, 0);

    return 0;
}

