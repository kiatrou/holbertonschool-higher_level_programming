#!/usr/bin/node
// Function that adds two numbers
function add (a, b) {
  return a + b;
}

// Get the user arguments (excluding node path and script path)
const args = process.argv.slice(2);

// Convert the first two arguments to integers
const firstInt = parseInt(args[0]);
const secondInt = parseInt(args[1]);

// Call the add function and print the result
console.log(add(firstInt, secondInt));
