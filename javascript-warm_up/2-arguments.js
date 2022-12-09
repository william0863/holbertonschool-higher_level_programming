#!/usr/bin/node
const test = process.argv;
if (test.length < 3) { console.log('No argument'); } else if (test.length === 3) { console.log('Argument found'); } else { console.log('Arguments found'); }
