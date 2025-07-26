#!/usr/bin/node
const argument = process.argv.slice(2);

// converts the first argument into an integer
const num = parseInt(argument[0]);

// Check if the conversion resulted in a valid number
// parseInt returns NaN if the string can't be converted to a number
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
