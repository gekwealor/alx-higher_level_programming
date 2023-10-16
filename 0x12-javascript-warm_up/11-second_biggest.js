#!/usr/bin/node

const proc = require('process');
const argv = proc.argv.slice(2).map(value => parseInt(value));
let H = 0;
let SH = 0;

if (argv.length === 0 || argv.length === 1) {
  console.log(0);
} else {
  for (const v of argv) {
    H = v > H ? v : H;
  }
  for (const v of argv) {
    if (v === H) {
      continue;
    }
    SH = (SH < v) && (H > SH) ? v : SH;
  }
  console.log(SH);
}
