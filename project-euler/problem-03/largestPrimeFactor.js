function largestPrimeFactor(n) {
  if (n < 2) {
    return 0;
  }

  let largestPrime = 2;
  let largestFactor = largestPrime;
  while (n !== 1) {
    if (n % largestFactor === 0) {
      largestPrime = largestFactor;
      n /= largestPrime;
      continue;
    }
    largestFactor++;
  }
  return largestPrime;
}

module.exports = largestPrimeFactor;
