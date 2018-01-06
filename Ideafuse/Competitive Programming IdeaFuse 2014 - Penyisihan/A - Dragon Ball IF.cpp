#include <bits/stdc++.h>
using namespace std;

int main(){

    int n, p;
    char kata[15] = "kamehameha";

    scanf("%d", &n);
    for(int i=0; i<n; i++){
        scanf("%d", &p);
        for(int j=0; j<10; j++){
            if(kata[j] == 'a' || kata[j] == 'e'){
                for(int k=0; k<p; k++){
                    printf("%c", kata[j]);
                }
            }else printf("%c", kata[j]);
        }
        printf("\n");
    }

    return 0;
}