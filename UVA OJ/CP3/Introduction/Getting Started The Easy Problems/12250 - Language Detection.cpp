#include <bits/stdc++.h>
using namespace std;

int main(){

    string s;
    int cnt=1;

    while(cin >> s){
        if(s == "HELLO") cout << "Case " << cnt << ": ENGLISH" << "\n";
        else if(s == "HOLA") cout << "Case " << cnt << ": SPANISH" << "\n";
        else if(s == "HALLO") cout << "Case " << cnt << ": GERMAN" << "\n";
        else if(s == "BONJOUR") cout << "Case " << cnt << ": FRENCH" << "\n";
        else if(s == "CIAO") cout << "Case " << cnt << ": ITALIAN" << "\n";
        else if(s == "ZDRAVSTVUJTE") cout << "Case " << cnt << ": RUSSIAN" << "\n";
        else if(s == "#") return 0;
        else cout << "Case " << cnt << ": UNKNOWN" << "\n";
        cnt++;
    }

    return 0;
}
