#!/usr/bin/node

exports.converter = function (base) {
  // Function that converts a number from base 10 to another base

  return function (value) {
    return value.toString(base);
  };
};
