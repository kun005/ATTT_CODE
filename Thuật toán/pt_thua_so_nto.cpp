#include<stdio.h>
#include<math.h>
//O(logN)
void ptich(int n){
	for(int i = 2; i <= sqrt(n); i++){
		if(n % i == 0){
			// i la thua so nguyen to cua n
			while(n % i == 0){
				printf("%d ", i);
				n /= i;
			}
		}
	}
	//neu chua phan tich thua so nguyen to xong
	if(n != 1)
		printf("%d", n); 
}

 int main(){
 	int n;
 	scanf("%d", &n);
 	ptich(n);
 	
 }
