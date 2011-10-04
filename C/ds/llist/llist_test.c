#include <stdio.h>

#include "linked_list.h"

int main()
{
    List list1;
    List list2;

    MakeEmpty(&list1);

    printf("IsEmpty() returns %d\n", IsEmpty(list1));

//#if 0
    PrintList(list1);

    Insert((void*)1, list1);
    Insert((void*)2, list1->next);
    Insert((void*)3, Find((void *)2, list1));

    PrintList(list1);
    list2 = ReverseList(list1);
    PrintList(list2);
//#endif

    DeleteList(list1);


    return 0;
}

