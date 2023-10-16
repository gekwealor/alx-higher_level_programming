#!/usr/bin/node

const integers = require('process');
const a = parseInt(integers.argv[2]);
const b = parseInt(integers.argv[3]);

function add (a, b) {
  console.log(a + b);
}
add(a, b);
