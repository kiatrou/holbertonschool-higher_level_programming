#!/usr/bin/node
// Get the user arguments (excluding node path and script path)
const args = process.argv.slice(2);

// Check if no arguments or only one argument
if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  // Convert all arguments to integers
  const numbers = [];
  for (let i = 0; i < args.length; i++) {
    numbers.push(parseInt(args[i]));
  }

  // Find the biggest and second biggest
  const biggest = Math.max(...numbers);
  let secondBiggest = Math.min(...numbers);

  // Go through all numbers to find the second biggest
  for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] > secondBiggest && numbers[i] < biggest) {
      secondBiggest = numbers[i];
    }
  }

  console.log(secondBiggest);
}
