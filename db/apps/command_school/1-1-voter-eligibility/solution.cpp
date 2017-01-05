#include <iostream>
using namespace std;

int main()
{
	int age;
	int MIN_ELIGIBLE_AGE = 18;

	cout << "Please enter your age in years: ";
	cin >> age;

	if (age >= MIN_ELIGIBLE_AGE)
	{
		cout << "You are old enough to vote! \
				Support our nation and go vote!" << endl;
	}
	else
	{
		cout << "You are too young to vote!" << endl;
	}
}