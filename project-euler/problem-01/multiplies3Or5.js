function multiplesOf3Or5(limit) {
  let sumOfMultiples = 0;
  for (let i = 1; i < limit; i++) {
    if (i % 3 === 0 || i % 5 === 0) {
      sumOfMultiples += i;
    }
  }
  return sumOfMultiples;
}

module.exports = multiplesOf3Or5;
