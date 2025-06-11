#include <stdio.h>

int main(){
int x = 5;
int y = 10;
if(x < y){
x = x + 1;
}else{ 
y = y - 1;
}
while(x < y){
printf("%d", x);
x = x + 1;
}
printf("%d", x);
printf("%d", y);
return 0;
}