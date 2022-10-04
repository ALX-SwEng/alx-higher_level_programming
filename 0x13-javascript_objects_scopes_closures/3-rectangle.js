#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      [this.height, this.width] = [h, w];
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
};
