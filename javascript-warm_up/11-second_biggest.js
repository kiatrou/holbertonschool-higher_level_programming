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
  let biggest = numbers[0];
  let secondBiggest = numbers[0];

  // Go through all numbers to find biggest and second biggest
  for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] > biggest) {
      secondBiggest = biggest;
      biggest = numbers[i];
    } else if (numbers[i] > secondBiggest && numbers[i] < biggest) {
      secondBiggest = numbers[i];
    }
  }

  console.log(secondBiggest);
}
