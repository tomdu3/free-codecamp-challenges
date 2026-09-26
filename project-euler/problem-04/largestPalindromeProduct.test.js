const largestPalindromeProduct = require("./largestPalindromeProduct");

describe("largestPalindromeProduct", () => {
  it("should return a number", () => {
    expect(typeof largestPalindromeProduct(2)).toBe("number");
  });
  it("should return 9009", () => {
    expect(largestPalindromeProduct(2)).toBe(9009);
  });
  it("should return 906609", () => {
    expect(largestPalindromeProduct(3)).toBe(906609);
  });
});
