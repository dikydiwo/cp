#include <bits/stdc++.h>
using namespace std;

int main(){

    string s;
    char kata[10]="ideafuse";
    bool bol = false;
    int ans;

    getline(cin, s);
    int len = s.length();
    for(int i=0; i<len; i++){
        if(s[i] == 'i'){
            if(s[i+1] == 'd' && s[i+2] == 'e' && s[i+3] == 'a' && s[i+4] == 'f' &&
               s[i+5] == 'u' && s[i+6] == 's' && s[i+7] == 'e'){
                    bol = true;
                    ans = i+1;
                    break;
            }else ans = -1;
        }
    }
    cout << ans << endl;

    return 0;
}