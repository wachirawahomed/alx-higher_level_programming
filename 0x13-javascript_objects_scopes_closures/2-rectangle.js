#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      // Initialize width and height attributes
      this.width = w;
      this.height = h;
    }
  }
};

