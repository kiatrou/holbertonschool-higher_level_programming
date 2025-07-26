#!/usr/bin/node
const argument = process.argv.slice(2);

const size = parseInt(argument[0]);

let row;
let col;
let line;

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (row = 0; row < size; row++) {
    line = '';
    for (col = 0; col < size; col++) {
      line += 'X';
    }
    console.log(line);
  }
}
