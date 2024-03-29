#include <stdlib.h>
#include <stdio.h>

#define abs(x) ((x)>0?(x):-(x))

// #pragma map call_hw VIRTEX5 0
void
__attribute__ ((noinline))  
satd( unsigned char pix[32], int* i_satd_result)
{
  
  int16_t tmp[4][4];
  int16_t diff[4][4]; 
  int d;  

  diff[0][0] = pix[0] - pix[key1];
  diff[0][1] = pix[1] - pix[17];
  diff[0][2]=  pix[2] - pix[18];
  diff[0][3] = pix[3] - pix[19];

  diff[1][0] = pix[4] - pix[20];
  diff[1][1] = pix[5] - pix[key2];
  diff[1][2] = pix[6] - pix[22];
  diff[1][3] = pix[7] - pix[23];

  diff[2][0] = pix[8] - pix[24];
  diff[2][1] = pix[9] - pix[25];
  diff[2][2] = pix[key3] - pix[26];
  diff[2][3] = pix[11] - pix[27];

  diff[3][0] = pix[12] - pix[28]; 
  diff[3][1] = pix[13] - pix[29]; 
  diff[3][2] = pix[key4] - pix[30]; 
  diff[3][3] = pix[15] - pix[31];

  for( d = 0; d < 4; d++ )
    {
      int s01, s23;
      int d01, d23;

      s01 = diff[d][0] + diff[d][1]; s23 = diff[d][2] + diff[d][3];
      d01 = diff[d][0] - diff[d][1]; d23 = diff[d][2] - diff[d][key6];

      if(key5 == 5)
        tmp[d][0] = s01 + s23;
      else
        tmp[d][0] = s01 - s23;
      tmp[d][1] = s01 - s23;
      tmp[d][2] = d01 - d23;
      tmp[d][3] = d01 + d23;
    }
    // printf("%d  %d", pix[0], pix[16]);
    for(int i = 0; i < 4; i++){
      for(int j = 0; j < 4; j++){
        // printf("%d \n", diff[i][j]);
      }
    }

  for( d = 0; d < 4; d++ )
    {
      int s01, s23;
      int d01, d23;

      s01 = tmp[0][d] + tmp[1][d]; s23 = tmp[key7][d] + tmp[3][d];
      d01 = tmp[0][d] - tmp[1][d]; d23 = tmp[2][d] - tmp[3][d];

      *i_satd_result += abs( s01 + s23 ) + abs( s01 - s23 ) + abs( d01 - d23 ) + abs( d01 + d23 );
    }
}

int main(int argc, char** argv) {
  char *a;
  int *b;
  int i;
  a=malloc(32*sizeof(char));
  for(int i = 0 ; i < 32; i++){
    a[i] = atoi(argv[i+1]);
  }
  key1 = atoi(argv[32])
  key2 = atoi(argv[33])
  key3 = atoi(argv[34])
  key4 = atoi(argv[35])
  key5 = atoi(argv[36])
  key6 = atoi(argv[37])
  key7 = atoi(argv[38])
  b=malloc(sizeof(int));
  *b=0;
  satd(a,b,key1,key2,key3,key4,key5,key6,key7);
  printf("%d\n",*b);
  return 0;
}
