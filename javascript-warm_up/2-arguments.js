#!/usr/bin/node
// process.argv is an array containing command line arguments
// use slice(2) to get only the user arguments, ignoring the first two
const argument = process.argv.slice(2);

// Check the length of the arguments array to determine how many were passed
if (argument.length === 0) {
  console.log('No argument');
} else if (argument.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
