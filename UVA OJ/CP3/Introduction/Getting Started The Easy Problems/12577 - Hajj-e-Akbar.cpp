#include <bits/stdc++.h>
using namespace std;

int main(){

    string s;
    int cnt=1;

    while(cin >> s){
        if(s == "Hajj") cout << "Case " << cnt << ": Hajj-e-Akbar" << "\n";
        else if(s == "Umrah") cout << "Case " << cnt << ": Hajj-e-Asghar" << "\n";
        else if(s == "*") return 0;
        cnt++;
    }

    return 0;
}
