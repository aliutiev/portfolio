#include <stdio.h>
#include <stdlib.h>

void swap(int *first, int *second);
void display_array(int *a, int n);

void selection_sort(int *a, int left, int right);
void quick_sort(int *a, int left, int right);
void copy_array(int *a, int *b, int n);
int is_sorted(int *a, int n);

void display_array(int *a, int n)
{
  int i; 
  for (i = 0; i < n; ++i) {
    if (i%10 == 0) printf("\n");
      printf("%3d ", *(a+i));
  }
  printf("\n"); 
}

void swap(int *first, int *second)
{
  int temp = *first;
  *first = *second;
  *second = temp;
}

void copy_array(int *a, int *b, int n)
{
  int i;

  for (i = 0; i < n-1; i++){
    b[i] = a[i];
  }    
}

int is_sorted(int *a, int n)
{
  int i;
  for (i = 0; i < n-1; i++){
    if(a[i]>a[i+1]){
      return 0; 
    }
  }
  return 1;
}

void selection_sort(int *a, int left, int right)
{
    int min_index, j;
    for (left; left < right; left++){
        min_index = left;
        for (j = left + 1; j < right+1; j++){
          if (a[j] < a[min_index]){
              min_index = j;
          }
        }
        swap(&a[min_index], &a[left]);
    }
}

void quick_sort( int *a, int m, int n) {
	int first, second, temp, index;
	if (m < n) {
		index = m;
		first = m;
		second = n;
		while (first < second) {
			while (a[first] <= a[index] && first < n)
				first++;
			while (a[second] > a[index])
				second--;
			if (first < second) {
				temp = a[first];
				a[first] = a[second];
				a[second] = temp;
			}
		}
		temp = a[index];
		a[index] = a[second];
		a[second] = temp;
		quick_sort( a,m, second - 1);
		quick_sort( a,second + 1, n);
	}

}