const nums: number[] = [];
for (let i = 0; i < 20; i++) {
  const rand = Math.floor(Math.random() * 101);
  nums.push(rand);
}
console.log(nums);

let sum = 0;
let maxPrime = 0;

const evens: number[] = [];
const odds: number[] = [];
const perfectSquares: number[] = [];
for (const num of nums) {
  if (num % 2 == 0) {
    // console.log("Even: ", num);
    evens.push(num);
  } else {
    // console.log("Odd: ", num);
    odds.push(num);
  }

  sum += num;

  if (isPrime(num) && num > maxPrime)
    maxPrime = num;

  if (isPerfectSquare(num))
    perfectSquares.push(num);
}

console.log("Evens:", evens);
console.log("Odds:", odds);
console.log("Perfect squres:", perfectSquares);
console.log("Sum:", sum);
console.log("Max prime:", maxPrime);

function isPrime(num: number): boolean {
  if (num === 2 || num === 3) return true;

  const lim = Math.floor(Math.sqrt(num));
  let i = 2;
  while (i < lim) {
    if (num % i == 0) {
      return false;
    }
    i += 1;
  }
  return true;
}

function isPerfectSquare(num: number): boolean {
  return Number.isInteger(Math.sqrt(num));
}