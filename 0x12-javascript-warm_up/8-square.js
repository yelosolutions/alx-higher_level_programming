#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (Number.isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0, k; i < size; i++) {
    k = '';
    for (let j = 0; j < size; j++) {
      k += 'X';
    }
    console.log(k);
  }
}
