#!/usr/bin/node

let num = Number(process.argv[2]);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  while (num > 0) {
    console.log('C is fun');
    --num;
  }
}
