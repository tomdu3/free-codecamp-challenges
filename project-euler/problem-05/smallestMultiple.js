function smallestMult(n) {
  const primes = {};
  for (let i = 2; i <= n; i++) {
    if (isPrime(i)) {
      primes[i] = 1;
    } else {
      let temp = i;
      for (const p of Object.keys(primes)) {
        const prime = Number(p);
        let count = 0;
        while (temp % prime === 0) {
          temp = temp / prime;
          count++;
        }
        if (count > 0) {
          primes[prime] = Math.max(primes[prime], count);
        }
        if (temp === 1) {
          break;
        }
      }
    }
  }

  return Object.keys(primes).reduce(
    (acc, p) => acc * Number(p) ** primes[p],
    1,
  );
}

function isPrime(n) {
  if (n <= 1) return false;
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) return false;
  }
  return true;
}

if (require.main === module) {
  console.log(smallestMult(20));
}

module.exports = smallestMult;
