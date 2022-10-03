#!/usr/bin/node

let num = Number(process.argv[2]);
const width = num;
if (isNaN(num)) {
  console.log('Missing size');
} else {
  while (num > 0) {
    for (let i = 1; i < width; ++i) {
      console.log('x');
    }
    --num;
  }
}
