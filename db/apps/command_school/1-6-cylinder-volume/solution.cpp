#include <iostream>
#include <cmath>
using namespace std;

int main()
{
	// Declare variables
	double V, w, h;
	const double PI = 3.1415;

	// Read user data
	cout << "width (m): ";
	cin >> w;
	cout << "height (m): ";
	cin >> h;

	// Calculate volume
	V = PI * pow(w/2, 2) * h;

	// Output the volume
	cout << "volume = " << V << endl;
}
