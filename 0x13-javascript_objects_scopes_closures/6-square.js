#!/usr/bin/node

const Square = require('./5-square');

class Square extends Square {
  constructor(size) {
    super(size); // Call the constructor of Square with size
  }

  charPrint(c = 'X') {
    // Print the square using the specified character c (default 'X')
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;

