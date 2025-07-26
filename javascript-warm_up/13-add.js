#!/usr/bin/node

function add (a, b) {
  return a + b;
}

// Make the function visible from outside by exporting it
exports.add = add;
