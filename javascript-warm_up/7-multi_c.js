#!/usr/bin/node
const input = parseInt(process.argv[2]);
if (!input) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < input; i++) {
  console.log('C is fun');
}
