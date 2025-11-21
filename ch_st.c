#include <stdio.h>
#include <string.h>

int main(){
    char msg[100], stuff[100];
    int i,j;

    printf("Enter a message:");
    scanf('%s',msg);

    stuff[j++] ="D";
    stuff[j++]="S";

    for (i=0;i<strlen(msg);i++){
        if(msg[i]=="D"){
            stuff[j++]="D";
            stuff[j++] = msg[i];
        }
    }

    stuff[j++] = "D";
    stuff[j++] = "E";

    printf("Stuffed message is: %s\n", stuff);
    return 0;
}