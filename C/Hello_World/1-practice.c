#include <stdio.h>

/**
 * main - this function prints 1-100, adopting the FizzBuzz principles in rev.
 *
 * Return: Always 0.
 */
int main(void)
{
	int i;

	for (i = 100; i >= 1; i--)
	{
		if (i % 3 == 0 && i % 5 == 0)
			printf("HelloWorld ");
		else if (i % 3 == 0)
			printf("Hello ");
		else if (i % 5 == 0)
			printf("World ");
		else
			printf("%d ", i);

	}
	return (0);
}
