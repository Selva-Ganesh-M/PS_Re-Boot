#include <stdio.h>
#include <math.h>

int sum_of_digits(int number){
    if (!number){
        return 0;
    }
    number = floor(number/10);
    return sum_of_digits(number) + 1;
    
}

int main(){
    printf("Enter the value to find the number of digits: ");
    int number;
    scanf("%d", &number);
    int res = sum_of_digits(number);
    printf("The sum of digits of %d is %d\n", number, res);
    return 0;
}