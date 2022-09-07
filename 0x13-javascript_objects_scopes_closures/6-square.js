#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (k) {
    if (k === undefined) {
      k = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let m = '';
      for (let j = 0; j < this.width; j++) {
        m += k;
      }
      console.log(m);
    }
  }
}

module.exports = Square;
