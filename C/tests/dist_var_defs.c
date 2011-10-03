/* at the beginning of some control block (if, else, switch), new vars can be
 * defined. however, "case" is not one of them */
int main()
{
    int i = 0;
    switch (i) {
        int k = 10;
        case 0:
            //int j = 1; //can't init in case statement
            break;
        default:
            break;
    }
    return 0;
}
