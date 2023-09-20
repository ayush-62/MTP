/*
 * The Keccak sponge function, designed by Guido Bertoni, Joan Daemen,
 * Michaël Peeters and Gilles Van Assche. For more information, feedback or
 * questions, please refer to our website: http://keccak.noekeon.org/
 * Implementation by the designers,
 * hereby denoted as "the implementer".
 * To the extent possible under law, the implementer has waived all copyright
 * and related or neighboring rights to the source code in this file.
 * http://creativecommons.org/publicdomain/zero/1.0/
 *
 */

#include <stdlib.h>
#include <stdio.h>

typedef unsigned char UINT8;
typedef unsigned long long int UINT64;
#define nrRounds 24

#define GET_KRC_VAL(index) (KeccakRoundConstants[index])

UINT64 A[25];

static UINT64 KeccakRoundConstants[nrRounds] = {
    0x0000000000000001ULL,
    0x0000000000008082ULL,
    0x800000000000808aULL,
    0x8000000080008000ULL,
    0x000000000000808bULL,
    0x0000000080000001ULL,
    0x8000000080008081ULL,
    0x8000000000008009ULL,
    0x000000000000008aULL,
    0x0000000000000088ULL,
    0x0000000080008009ULL,
    0x000000008000000aULL,
    0x000000008000808bULL,
    0x800000000000008bULL,
    0x8000000000008089ULL,
    0x8000000000008003ULL,
    0x8000000000008002ULL,
    0x8000000000000080ULL,
    0x000000000000800aULL,
    0x800000008000000aULL,
    0x8000000080008081ULL,
    0x8000000000008080ULL,
    0x0000000080000001ULL,
    0x8000000080008008ULL
};

#define nrLanes 25
static unsigned char KeccakRhoOffsets[nrLanes] = {
    0,
    1,
    62,
    28,
    27,
    36,
    44,
    6,
    55,
    20,
    3,
    10,
    43,
    25,
    39,
    41,
    45,
    15,
    21,
    8,
    18,
    2,
    61,
    56,
    14
};

#define index(x, y) (((x)%5)+5*((y)%5))
#define ROL64(a, offset) ((offset != 0) ? ((((UINT64)a) << offset) ^ (((UINT64)a) >> (64-offset))) : a)

void theta(UINT64 *A)
{
    unsigned int x, y;
    UINT64 C[5], D[5];

    for(x=0; x<5; x++) {
        C[x] = 0; 
        for(y=0; y<5; y++) 
            C[x] ^= A[index(x, y)];
    }
    for(x=0; x<5; x++)
        D[x] = ROL64(C[(x+1)%5], 1) ^ C[(x+4)%5];
    for(x=0; x<5; x++)
        for(y=0; y<5; y++)
            A[index(x, y)] ^= D[x];
}

void rho(UINT64 *A)
{
    unsigned int x, y;

    for(x=0; x<5; x++) for(y=0; y<5; y++)
        A[index(x, y)] = ROL64(A[index(x, y)], KeccakRhoOffsets[index(x, y)]);
}

void pi(UINT64 *A)
{
    unsigned int x, y;
    UINT64 tempA[25];

    for(x=0; x<5; x++) for(y=0; y<5; y++)
        tempA[index(x, y)] = A[index(x, y)];
    for(x=0; x<5; x++) for(y=0; y<5; y++)
        A[index(0*x+1*y, 2*x+3*y)] = tempA[index(x, y)];
}

void chi(UINT64 *A)
{
    unsigned int x, y;
    UINT64 C[5];

    for(y=0; y<5; y++) { 
        for(x=0; x<5; x++)
            C[x] = A[index(x, y)] ^ ((~A[index(x+1, y)]) & A[index(x+2, y)]);
        for(x=0; x<5; x++)
            A[index(x, y)] = C[x];
    }
}

void iota(UINT64 *A, unsigned int indexRound)
{
    A[index(0, 0)] ^= GET_KRC_VAL(indexRound);
}


void kekka_coproc(UINT64 A[25])
{
    unsigned int i;
    for(i=0;i<nrRounds;i++) { 
        theta(A);
        rho(A);
        pi(A);
        chi(A);
        iota(A,i);
    }
}

int main(int argc, char** argv)
{

    A[0] = atoi(argv[1]);
    A[1] = atoi(argv[2]);
    A[2] = atoi(argv[3]);
    A[3] = atoi(argv[4]);
    A[4] = atoi(argv[5]);
    A[5] = atoi(argv[6]);
    A[6] = atoi(argv[7]);
    A[7] = atoi(argv[8]);
    A[8] = atoi(argv[9]);
    A[9] = atoi(argv[10]);
    A[10] = atoi(argv[11]);
    A[11] = atoi(argv[12]);
    A[12] = atoi(argv[13]);
    A[13] = atoi(argv[14]);
    A[14] = atoi(argv[15]);
    A[15] = atoi(argv[16]);
    A[16] = atoi(argv[17]);
    A[17] = atoi(argv[18]);
    A[18] = atoi(argv[19]);
    A[19] = atoi(argv[20]);
    A[20] = atoi(argv[21]);
    A[21] = atoi(argv[22]);
    A[22] = atoi(argv[23]);
    A[23] = atoi(argv[24]);
    A[24] = atoi(argv[25]);
    kekka_coproc(A);
    printf("%llu\n",A[0]);
    printf("%llu\n",A[1]);
    printf("%llu\n",A[2]);
    printf("%llu\n",A[3]);
    printf("%llu\n",A[4]);
    printf("%llu\n",A[5]);
    printf("%llu\n",A[6]);
    printf("%llu\n",A[7]);
    printf("%llu\n",A[8]);
    printf("%llu\n",A[9]);
    printf("%llu\n",A[10]);
    printf("%llu\n",A[11]);
    printf("%llu\n",A[12]);
    printf("%llu\n",A[13]);
    printf("%llu\n",A[14]);
    printf("%llu\n",A[15]);
    printf("%llu\n",A[16]);
    printf("%llu\n",A[17]);
    printf("%llu\n",A[18]);
    printf("%llu\n",A[19]);
    printf("%llu\n",A[20]);
    printf("%llu\n",A[21]);
    printf("%llu\n",A[22]);
    printf("%llu\n",A[23]);
    printf("%llu\n",A[24]);
}
