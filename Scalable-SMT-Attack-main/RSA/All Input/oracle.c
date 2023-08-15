#include<stdio.h>
#include<math.h>
#include <stdlib.h>

int prime[]={2,3,5,7,11,13,17,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,191,193,197,199,211,223,227,229,233,239,241};
int ptr=15;
int n;
int public_key;
int private_key;
int coded[16];
int gcd(int a, int b)
{
    if (a == 0)
        return b;
    return gcd(b % a, a);
}
int pickrandomprime()
{
   int ret=prime[ptr];
   ptr++;
   return ret;
}
void setkeys()
{
   int prime1 = pickrandomprime(); // first prime number
   int prime2 = pickrandomprime(); // second prime number
   // to check the prime numbers selected
   // cout<<prime1<<" "<<prime2<<endl;
   n = prime1 * prime2;
   int fi = (prime1 - 1) * (prime2 - 1);
   int e = 0;
   e = e + (fi %13);
   public_key = e;
}

int encrypt()
{
    for(int i=0;i<16;i++)
    {
       int e = public_key;
       long long int encrpyted_text = 1;
       while (e--) {
          encrpyted_text *= coded[i];
          encrpyted_text %= n;
       }
       coded[i]=encrpyted_text;
    }
}
int main(int argc, char** argv)
{
  coded[0]= atoi(argv[1]);
  coded[1]= atoi(argv[2]);
  coded[2]= atoi(argv[3]);
  coded[3]= atoi(argv[4]);
  coded[4]= atoi(argv[5]);
  coded[5]= atoi(argv[6]);
  coded[6]= atoi(argv[7]);
  coded[7]= atoi(argv[8]);
  coded[8]= atoi(argv[9]);
  coded[9]= atoi(argv[10]);
  coded[10]= atoi(argv[11]);
  coded[11]= atoi(argv[12]);
  coded[12]= atoi(argv[13]);
  coded[13]= atoi(argv[14]);
  coded[14]= atoi(argv[15]);
  coded[15]= atoi(argv[16]);

  setkeys();
  encrypt();

  printf("%d\n",coded[0]);
  printf("%d\n",coded[1]);
  printf("%d\n",coded[2]);
  printf("%d\n",coded[3]);
  printf("%d\n",coded[4]);
  printf("%d\n",coded[5]);
  printf("%d\n",coded[6]);
  printf("%d\n",coded[7]);
  printf("%d\n",coded[8]);
  printf("%d\n",coded[9]);
  printf("%d\n",coded[10]);
  printf("%d\n",coded[11]);
  printf("%d\n",coded[12]);
  printf("%d\n",coded[13]);
  printf("%d\n",coded[14]);
  printf("%d\n",coded[15]);



  return 0;
}
