#!/usr/bin/node
const argument = process.argv.slice(2);

const x = parseInt(argument[0]);

let i;

if (isNaN(x)) {
  console.log('Missing number of occurences');
} else {
  for (i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
