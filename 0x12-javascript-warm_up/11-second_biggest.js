#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv.slice(2).map(Number);
  const sorted = args.sort((a, b) => b - a);
  console.log(sorted[1]);
}
