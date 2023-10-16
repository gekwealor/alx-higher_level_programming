#!/usr/bin/node

const { argv } = require('process');
const num = parseInt(argv[2]);
const printC = (value) => {
  for (; value > 0; value--) console.log('C is fun');
};

Number.isInteger(num) ? printC(num) : console.log('Missing numder of occurrence');
