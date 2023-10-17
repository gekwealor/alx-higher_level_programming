#!/usr/bin/node

// A class Square that defines a square and inherits from Rectangle of 5-rectangle.js

const Rectangle = require('./4-rectangle');

// class notation, for defining class

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
