/**
 * Project Euler — Problem 2: Even Fibonacci Numbers (improved solution)
 *
 * Improvement over fiboEvenSum.js:
 *   The original (a) stores every Fibonacci term up to n in an array and
 *   (b) does a second reduce pass to filter out odd terms. Both are
 *   unnecessary: only every third term is even, and we never need the
 *   sequence itself — only the running sum.
 *
 * Key observation — where the even terms live:
 *   Fibonacci mod 2 is  1, 1, 0, 1, 1, 0, ...  so every third term is even.
 *   Writing E(k) for the k-th even term (2, 8, 34, 144, ...), the standard
 *   recurrence collapses to a direct jump between even terms:
 *
 *       E(k) = 4 * E(k-1) + E(k-2),   seeds E(0) = 0, E(1) = 2
 *
 *   (e.g. 34 = 4*8 + 2, 144 = 4*34 + 8). So we can iterate from one even
 *   term straight to the next: no modulo checks, no array, O(1) memory,
 *   and ~3x fewer loop iterations.
 *
 *   Edge cases: returns 0 for n < 2. (The original seeds its array with
 *   [1, 2] unconditionally, so it returns 2 for n = 0 and n = 1 even though
 *   the term 2 exceeds n — harmless for the Project Euler/FCC inputs, which
 *   all have n >= 8, but incorrect in general.)
 *
 * Complexity: O(log n) loop iterations, O(1) extra space.
 */

function fiboEvenSum(n) {
  let prev = 0; // E(0) — phantom seed so that 4*2 + 0 = 8 is the next even term
  let curr = 2; // E(1) — first even Fibonacci number
  let sum = 0;

  while (curr <= n) {
    sum += curr;
    const nextEven = 4 * curr + prev; // jump straight to the next even term
    prev = curr;
    curr = nextEven;
  }

  return sum;
}

/**
 * Bonus — O(log n) closed form via the identity
 *
 *       F(3) + F(6) + ... + F(3m)  =  (F(3m+2) - 1) / 2
 *
 * (check: 2 + 8 + 34 = 44 = (F(11) - 1)/2 = (89 - 1)/2). We find the largest
 * even Fibonacci E = F(3m) <= n together with its preceding term F(3m-1),
 * then return (2*E + F(3m-1) - 1) / 2, since F(3m+2) = 2*F(3m) + F(3m-1).
 *
 * Exact for n up to ~4e15 (the intermediates stay below 2^53); beyond that,
 * reach for BigInt.
 */
function fiboEvenSumClosedForm(n) {
  if (n < 2) return 0;

  let prev = 1; // F(2)
  let curr = 2; // F(3) — first even term
  while (3 * curr + 2 * prev <= n) {
    // advance the (F(3k-1), F(3k)) pair two spots:
    // F(3k+2) = 2*F(3k) + F(3k-1),  F(3k+3) = 3*F(3k) + 2*F(3k-1)
    [prev, curr] = [2 * curr + prev, 3 * curr + 2 * prev];
  }

  return (2 * curr + prev - 1) / 2;
}

module.exports = fiboEvenSum;
module.exports.fiboEvenSumClosedForm = fiboEvenSumClosedForm;
