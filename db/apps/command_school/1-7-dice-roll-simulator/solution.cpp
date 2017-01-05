#include <iostream>
using namespace std;

// Ensures we have randomness in the dice
// CALL THIS FUNCTION ONCE AT THE TOP OF MAIN
void seedRandomness()
{
	srand(1337); 
	// srand(time(NULL)); <-- This is how we could have new random numbers every time we execute the program
}

// Returns a number in the range [low, high)
int getRandomNumberInRange(int low, int high)
{
	return rand() % (high - low) + low;
}

int main()
{
	int guess1;
	int guess2;

	// Random rolls
	int dice1 = getRandomNumberInRange(1, 6);
	int dice2 = getRandomNumberInRange(1, 6);
	int product = dice1 * dice2;

	// Get user guesses
	cout << "Guess the product of two dice!" << endl;
	cout << "player1 guess: ";
	cin >> guess1;
	cout << "player2 guess: ";
	cin >> guess2;

	// Output
	cout << "dice1: " << dice1 << endl;
	cout << "dice2: " << dice2 << endl;
	cout << "product = " << product << endl;

	if ( abs(product - guess1) < abs(product - guess2) )
	{
		cout << "player1 won!" << endl;
	}
	else if ( abs(product - guess1) > abs(product - guess2) )
	{
		cout << "player2 won!" << endl;
	}
	else {
		cout << "tie!" << endl;
	}
}