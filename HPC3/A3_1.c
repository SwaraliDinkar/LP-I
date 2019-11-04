#include<stdio.h>
#include<omp.h>
#include<stdlib.h>



int main(int argc,char *argv[])
{
      int size= 1<<8;
      int a[size];
          for (int i=0;i<size;i++)
          {
             a[i]=rand()%size;
          }

      int N=size;
      double start,end;
      start=omp_get_wtime();
          for(int i=0;i<N-1;i++)
          {
               #pragma omp parallel for
               for (int j=0;j<N-i-1;j++)
               {
                  int temp;
                   if(a[j]>a[j+1])
                   {
                    temp=a[j];
                    a[j]=a[j+1];
                    a[j+1]=temp;
                   }
               }
          }
      end=omp_get_wtime();
      for (int i=0;i<size;i++)
          {
             printf("%d \\t",a[i]);
          }

      printf("\\n--------\\nTime Required=%f",end-start);
}


