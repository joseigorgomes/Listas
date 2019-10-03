#include <iostream>
using namespace std;

#define MAXN 1010

int n, vetor[MAXN];

void bubble_sort() {
    int ordered = 0;
    
    while(ordered == 0) {

        ordered = 1;

        for (int i = 0; i < n - 1; i++) {
            if (vetor[i] > vetor[i + 1]) {
                int temp = vetor[i];
                vetor[i] = vetor[i + 1];
                vetor[i + 1] = temp;
                ordered = 0;
            }
        }

    }
}

// You can test the function...
int main() {
    cout << "List's Size:" << endl;
    cin >> n;
    cout << "Numbers separated by space:" << endl;
    for (int i = 0; i < n; i++) cin >> vetor[i];  
    cout << endl;

    bubble_sort();

    cout << "Ordered Numbers:" << endl;
    for (int i = 0; i < n; i++) cout << vetor[i] << " ";
    cout << "\n";
    return 0;
}
