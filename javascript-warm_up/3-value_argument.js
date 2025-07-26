#!/usr/bin/node
const argument = process.argv.slice(2);

// If args[0] is undefined, it means no arguments were passed
if (argument[0] === undefined) {
  console.log('No argument');
} else {
  console.log(argument[0]);
}
