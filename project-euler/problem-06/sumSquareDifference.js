function sumSquareDifference(n) {
  return sumOfNumbersPowered(n) ** 2 - sumOfNumbersPowered(n, 2);
}

function sumOfNumbersPowered(n, power = 1) {
  let sum = 0;
  for (let i = 1; i <= n; i++) {
    sum += i ** power;
  }
  return sum;
}

if (require.main === module) {
  console.log(sumSquareDifference(100));
}

module.exports = sumSquareDifference;
