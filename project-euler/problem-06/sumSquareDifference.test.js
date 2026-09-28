const sumSquareDifference = require('./sumSquareDifference');

test('matches the worked example from the problem statement', () => {
  expect(sumSquareDifference(10)).toBe(2640);
});

test('returns 0 when there is nothing to subtract', () => {
  expect(sumSquareDifference(1)).toBe(0);
});

test('handles a small case by hand', () => {
  // (1 + 2)² - (1² + 2²) = 9 - 5 = 4
  expect(sumSquareDifference(2)).toBe(4);
});

test('solves the Project Euler target of n = 100', () => {
  expect(sumSquareDifference(100)).toBe(25164150);
});

test('agrees with a brute-force calculation for n = 1..50', () => {
  const bruteForce = (n) => {
    let sum = 0;
    let sumOfSquares = 0;
    for (let i = 1; i <= n; i++) {
      sum += i;
      sumOfSquares += i * i;
    }
    return sum * sum - sumOfSquares;
  };

  for (let n = 1; n <= 50; n++) {
    expect(sumSquareDifference(n)).toBe(bruteForce(n));
  }
});
