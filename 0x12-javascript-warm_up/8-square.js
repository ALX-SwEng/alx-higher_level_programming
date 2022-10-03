#!/usr/bin/node

let size = Number(process.argv[2]);
const width = size;
if (isNaN(size)) {
  console.log('Missing size');
} else {
  while (size > 0) {
    let row = '';
    for (let i = 1; i <= width; ++i) {
      row += 'X';
    }
    console.log(row);
    --size;
  }
}
