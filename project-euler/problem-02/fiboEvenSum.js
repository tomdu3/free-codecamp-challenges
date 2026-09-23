function fiboEvenSum(n) {
  const sequence = [1, 2]; // first two elements

  while (true) {
    const nextTerm =
      sequence[sequence.length - 1] + sequence[sequence.length - 2];
    if (nextTerm > n) {
      break;
    }
    sequence.push(nextTerm);
  }

  return sequence.reduce((acc, curr) => {
    return curr % 2 === 0 ? acc + curr : acc;
  }, 0);
}

module.exports = fiboEvenSum;
