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
