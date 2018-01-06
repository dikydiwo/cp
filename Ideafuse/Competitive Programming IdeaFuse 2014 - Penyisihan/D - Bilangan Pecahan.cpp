#include <bits/stdc++.h>
using namespace std;

int main(){

    int a, b, gcd;

    scanf("%d %d", &a, &b);
    gcd = __gcd(a,b);

    if(gcd > 1){
        a /= gcd;
        b /= gcd;
        printf("%d %d\n", a, b);
    }else printf("Tidak\n");

    return 0;
}