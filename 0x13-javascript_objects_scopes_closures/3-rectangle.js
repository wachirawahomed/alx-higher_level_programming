#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      // If width or height is not positive, create an empty object
      return {};
    } else {
      // Initialize width and height attributes
      this.width = w;
      this.height = h;
    }
  }

  print () {
    // Print the rectangle using character 'X'
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
