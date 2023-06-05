#include <stdlib.h>
#include <stdio.h>
//key_1 = 5 , key_2 = 12 , key_3 = 6 , key_4 = 3
void motion( int in1,  int in2,  int in3,  int in4,  int in5,  int in6,  int in7, int in8, int in9, int in10, int key_1, int key_2 , int key_3 , int key_4 ,int *out1,  int *out2,  int *out3)
{
    int mult1 = in1 * in2;
    int mult2 = in1 * (2*key_1);
    int mult3 = in3 * (4 + key_2);
    int mult4 = in4 * in5;
    int mult5 = in3 * in2;
    int mult6 = in2 * in5;
    int mult7 = in3 * in6;
    int mult8 = in4 * in7;
    int mult9 = in4 * in8;
    int mult10 = in6 * in9;
    int mult11 = in6 * in8;
    int mult12 = in7 * in9;
    int mult13 = in7 * in8;
    int mult14 = in9 * in10;

    int add1 = in1 * mult2;
    int add2 = (2*key_3 + 3) * mult4;
    int add3;
    int add4;
    int add5;
    if(add1>add2)
    {
    int add3 = in5 * mult8;
    int add4 = mult10 * in4;
    int add5 = in10 * mult14;
    }
    else
    {
    int add3 = in5 + mult8;
    int add4 = mult10 *in3;
    int add5 = in10 / mult14;
    }

    int add6 = mult1 + add1;
   *out1 = add6;

    int add7 = mult3 + add2;
    int add8 = mult5 + add7;

    int add10 = mult7 + add3;
    int add9 = mult6 + add10;

    int shf1 = add9 << 3;
   *out2 = add8 + shf1;

    int add13 = mult9 + add4;
    int add11 = add13 + mult11;

    int add15 = mult13 + add5;
    int add14 = mult12 + add15;

    int shf2 = add14 >> key_4;
   *out3 = add11 + shf2;
}

int main(int argc, char** argv)
{
    int in1 = atoi(argv[1]);
    int in2 = atoi(argv[2]);
    int in3 = atoi(argv[3]);
    int in4 = atoi(argv[4]);
    int in5 = atoi(argv[5]);
    int in6 = atoi(argv[6]);
    int in7 = atoi(argv[7]);
    int in8 = atoi(argv[8]);
    int in9 = atoi(argv[9]);
    int in10 = atoi(argv[10]);

    int out1, out2, out3;

   motion(in1, in2, in3, in4, in5, in6, in7, in8, in9, in10, 5 , 12 , 6 , 3 , &out1, &out2, &out3);

   printf("%d\n", out1);
   printf("%d\n", out2);
   printf("%d\n", out3);

   return 0;
}
