#!/usr/bin/node
// Recursive function to compute factorial
function factorial (n) {
  // Base cases: factorial of NaN, 0, or 1 is 1
  if (isNaN(n) || n <= 1) {
    return 1;
  }
  // Recursive case: n! = n * (n-1)!
  return n * factorial(n - 1);
}

// Get the user arguments (excluding node path and script path)
const args = process.argv.slice(2);

// Convert the first argument to an integer
const num = parseInt(args[0]);

// Compute and print the factorial
console.log(factorial(num));
