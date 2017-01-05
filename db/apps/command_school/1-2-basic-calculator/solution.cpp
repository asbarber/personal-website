#include <iostream>
using namespace std;

int main()
{
	// Declare variables
	double lhs, rhs, result;
	char operation;

	// Prompt user for expression
	cout << "Calculator Program" << endl;
	cout << "Enter an expression: ";
	cin >> lhs >> operation >> rhs;

	// Evaluate expression
	if (operation == '+') 
	{
		result = lhs + rhs;
	}
	else if (operation == '-')
	{
		result = lhs - rhs;
	}
	else if (operation == '*')
	{
		result = lhs * rhs;
	}
	else if (operation == '/')
	{
		result = lhs / rhs;
	}
	else
	{
		cout << "Invalid expression!" << endl;

		// Exit the program!
		return 0;
	}

	// Output expression result
	cout << "result = " << result << endl;	
}