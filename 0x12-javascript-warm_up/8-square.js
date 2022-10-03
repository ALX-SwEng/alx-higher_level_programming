#!/usr/bin/node

let num = Number(process.argv[2]);
const width = num;
if (isNaN(num)) {
  console.log('Missing size');
} else {
  while (num > 0) {
    let row = '';
    for (let i = 1; i < width; ++i) {
      row += 'X';
    }
    console.log(row);
    --num;
  }
}
