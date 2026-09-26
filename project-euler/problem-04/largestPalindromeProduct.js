function largestPalindromeProduct(n) {
  const min = 10 ** (n - 1);
  const max = 10 ** n - 1;
  let result = 0;
  for (let i = min; i <= max; i++) {
    for (let j = i; j <= max; j++) {
      const product = i * j;
      if (isPalindrome(product)) {
        result = Math.max(result, product);
      }
    }
  }

  return result;
}

function isPalindrome(n) {
  const numStr = String(n);
  const numArr = [...numStr];

  return numStr === numArr.reverse().join("");
}

module.exports = largestPalindromeProduct;
