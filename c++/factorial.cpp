#include <iostream>
using namespace std;

int main(){
	cout<<"Please enter a number to get its factorial\n";
	int number;
	cin>>number;
	for(int i = number-1; i>1; i--){
		number *= i;
	}
	cout<<"The factorial is: "<<number<<"\n";
}
