#include <stdio.h>
#include <string.h>
int main() {
// make temporary varaible to store user entered username and PWord
    char tempUN[50],tempPass[50],permUN[50];
    int verification1=0,n,withdraw,deposit;
// create array of usernames
char username[3][50] = {"ram","hari","sita"};
// create array of passwords
char password[3][50] = {"12345","hari123","password"};
// array for Unique identifer for each username
char uniqueID[3] = {'a','b','c'};
int id;
// array of balance available in their account
int balance[3] = {1000,2000,3000};
// ask for username and password
printf("Enter Your username: ");
scanf("%s",tempUN);
printf("Enter Your password: ");
scanf("%s",tempPass);
// Check if username and password matches with the data we have
for(int i=0;i<3;i++){
verification1 = strcmp(tempUN, username[i]);
        if (verification1 == 0) {
            // Username matches, copy it to permUN
            strcpy(permUN, username[i]);
            n=i;
            break;
        }
}
int passcheck =strcmp(tempPass,password[n]);
if(passcheck ==0){
    printf("Opening Bank balance\n");
    //show the user's balance
    printf("Balance = %d\n",balance[n]);
// use 'W' to withdraw and 'D' to deposit the amount from the balance.
printf("Enter '1' to withdraw and '2' to deposit: ");
scanf("%d",&id);
if(id==1){
    printf("Withdraw amount = ");
    scanf("%d",&withdraw);
    balance[n]= balance[n] - withdraw;
    printf("new balance = %d", balance[n]);
}
else if(id==2){
    printf("deposit amount: ");
    scanf("%d",&deposit);
    balance[n]=balance[n]+ deposit;
    printf("new balance=%d",balance[n]);
}
}
else{
    printf("wrong username or password");
}

    return 0;
}