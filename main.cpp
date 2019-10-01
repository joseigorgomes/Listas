#include <iostream>

using namespace std;

int main()
{
    int soma =0;
    int lista [] = {1,2,3,4};
    for(int i =0;i<4;i++){
        soma = soma + lista[i];
    }
    float media = soma/4.0;
    cout<<"a media eh "<<media<<"!"<<endl;
    return 0;
}
