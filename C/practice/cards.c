#include <stdio.h>
#include <sys/time.h>

void swap(unsigned char arr[], int elem1, int elem2)
{
    unsigned char temp;
    temp = arr[elem1];
    arr[elem1] = arr[elem2];
    arr[elem2] = temp;

    return;
}

unsigned char suiteMark[4] = {0xc0, 0x80, 0x10, 0x00};

void shuffleDeck(unsigned char deck[])
{
    unsigned int card1, card2;
    struct timeval tv;

    gettimeofday(&tv, NULL); 
    card1 = (tv.tv_usec*3) % 52;

    gettimeofday(&tv, NULL); 
    card2 = (tv.tv_usec*7) % 52;

    if (card1 != card2) swap(deck, card1, card2);

    printf("just swapped deck[%d] and deck[%d]\n",
            card1, card2);
}

void initDeck(unsigned char deck[])
{
    int cardIdx = 0;
    int val;
    int i = 0, j = 0;

    for (i=0; i<4; i++) {
        val = 0;
        val |= suiteMark[i];
            //printf("i=%d, j=%d, suiteMark=%x, deck[%d]=%x\n", i, j, suiteMark[i], cardIdx, deck[cardIdx]);
        for (j=0; j<13; j++) {
            deck[cardIdx] = val + j; 
            //printf("i=%d, j=%d, suiteMark=%x, deck[%d]=%x\n", i, j, suiteMark[i], cardIdx, deck[cardIdx]);
            cardIdx++;
        }
    }

}

void printCard(unsigned char card)
{
    switch (card & 0xf0) {
        case 0xc0:
            printf("[S]");
            break;
        case 0x80:
            printf("[H]");
            break;
        case 0x10:
            printf("[C]");
            break;
        case 0x00:
            printf("[D]");
            break;
    }

    printf("%d, ", card & 0x0f);
}

void printDeck(unsigned char deck[])
{
    int i;

    for (i=0; i<52; i++) {
        printCard(deck[i]);
        if (!((i+1)%13)) printf("\n");
    }
    printf("\n");
}

int main(int argc, char *argv[])
{
    int i, shuffles;
    unsigned char deck[52];

    if (argc != 2) return 0;

    shuffles = atoi(argv[1]);

    initDeck(deck);

    printDeck(deck);

    //shuffle
    for (i=0; i<shuffles; i++) shuffleDeck(deck);

    printDeck(deck);

}
