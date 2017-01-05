#include <iostream>
#include <cmath>
using namespace std;

int main()
{
	// Declare variables
	double r;
	double area;
	double circumference;
	const double PI = 3.1415;

	// Read user data
	cout << "Radius (m): ";
	cin >> r;	

	// Calculations
	area = PI * pow(r, 2);
	circumference = 2 * PI * r;

	// Output data
	cout << "area = " << area << endl;
	cout << "circumference = " << circumference << endl;
}
