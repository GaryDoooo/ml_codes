#include <stdio.h>
#include <cmath>
#include <cstring>
#include <iostream>
using namespace std;
int main() {
    string one_line;
    while (cin >> one_line) {
        // cout << endl << one_line << endl;
        int counter   = 0;
        string buffer = "";
        for (int i = 0; i < one_line.size(); i++) {
            char c = one_line[i];
            if (c == ',') {
                if (++counter == 1) cout << buffer << "/";
                if (counter == 3) {
                    // cout << buffer << endl;
                    int e = stoi(buffer, nullptr, 10);
                    cout << 32 - log(e) / log(2) << ",";
                }
                buffer = "";
            } else
                buffer += c;
        }
    }
    return 0;
}

