#!/usr/bin/node

let quantity = 0;
exports.logMe = function (item) {
  console.log(`${quantity}: ${item}`);
  quantity++;
};
