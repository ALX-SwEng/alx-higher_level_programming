#!/usr/bin/node

let size = Number(process.argv[2]);
const width = size;
if (isNaN(num)) {
  console.log('Missing size');
} else {
  while (size > 0) {
    let row = '';
    for (let i = 1; i <= size; ++i) {
      row += 'X';
    }
    console.log(row);
    --size;
  }
}
