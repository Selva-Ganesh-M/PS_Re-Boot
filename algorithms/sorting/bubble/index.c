#include <stdio.h>

void bubble_sort(int arr[], int size){
    for (int i=0; i<size; i++){
        int swapped  = 0;
        for (int j=0; j<size-i-1; j++){
            if (arr[j]>arr[j+1]){
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
                swapped = 1;
            }
        }
        if (!swapped){
            break;
        }
    }
}

int main(){
    int arr[5] = {5, 4, 3, 2, 1};
    int size = sizeof(arr)/sizeof(arr[0]);
    bubble_sort(arr, size);
    for (int i=0; i<size; i++){
        printf("%d\t", arr[i]);
    }
    return 0;
}