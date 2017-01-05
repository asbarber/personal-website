#include <iostream>
using namespace std;

// Convert the celsius temperature to fahrenheit
double toFahrenheit(double celsius)
{
	return celsius * 9.0 / 5.0 + 32;
}

// Convert the fahrenheit temperature to celsius
double toCelsius(double fahrenheit)
{
	return (fahrenheit - 32) * 5.0 / 9.0;
}

int main()
{
	double temperature;
	char units;

	cout << "Please enter your units [c/f]: ";
	cin >> units;

	cout << "Please enter a temperature: ";
	cin >> temperature;

	if (units == 'c')
	{
		cout << toFahrenheit(temperature) << " degrees F" << endl;
	}
	else if (units == 'f')
	{
		cout << toCelsius(temperature) << " degrees C" << endl;
	}
}
