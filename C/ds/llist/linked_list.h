struct Node;

typedef struct Node *PtrToNode;
typedef struct Node Node;
typedef PtrToNode List;

List MakeEmpty (List *L);
void DeleteList (List L);
PtrToNode Find (void* data, List L); 
void Insert (void* data, PtrToNode pos);
void PrintList (List L);
int IsEmpty(List L);
List ReverseList (List L);


struct Node
{
    void * data;
    Node * next;
}; 

/* leaving the ";" here may cause "linked_list.c:10: error: two or more data
 * types in declaration specifiers" */

