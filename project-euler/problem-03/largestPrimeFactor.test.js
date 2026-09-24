const largestPrimeFactor = require("./largestPrimeFactor");

describe("largestPrimeFactor", () => {
  describe("problem examples", () => {
    it("should return 29 for the example in problem.md (13195)", () => {
      expect(largestPrimeFactor(13195)).toBe(29);
    });

    it("should return 6857 for the real Project Euler #3 input", () => {
      expect(largestPrimeFactor(600851475143)).toBe(6857);
    });
  });

  describe("prime inputs return the number itself", () => {
    it.each([2, 7, 13, 97])("should return %i", (n) => {
      expect(largestPrimeFactor(n)).toBe(n);
    });
  });

  describe("repeated factors", () => {
    it("should return 2 for a power of two (8)", () => {
      expect(largestPrimeFactor(8)).toBe(2);
    });

    it("should return 2 for a large power of two (1024)", () => {
      expect(largestPrimeFactor(1024)).toBe(2);
    });

    it("should return 5 for 360 = 2^3 * 3^2 * 5", () => {
      expect(largestPrimeFactor(360)).toBe(5);
    });
  });

  describe("largest factor above sqrt(n) — the trap case", () => {
    it("should return 17 for 34 (small * big)", () => {
      expect(largestPrimeFactor(34)).toBe(17);
    });

    it("should return 13 for 1001 = 7 * 11 * 13", () => {
      expect(largestPrimeFactor(1001)).toBe(13);
    });

    it("should return the bigger of two large primes (10007 * 10009)", () => {
      expect(largestPrimeFactor(10007 * 10009)).toBe(10009);
    });
  });

  describe("edge cases", () => {
    it("should return 0 for 0", () => {
      expect(largestPrimeFactor(0)).toBe(0);
    });

    it("should return 0 for 1", () => {
      expect(largestPrimeFactor(1)).toBe(0);
    });

    it("should return 0 for a negative number (-10)", () => {
      expect(largestPrimeFactor(-10)).toBe(0);
    });
  });

  describe("performance", () => {
    it("should handle the real PE #3 input well under a second", () => {
      const t0 = performance.now();
      expect(largestPrimeFactor(600851475143)).toBe(6857);
      expect(performance.now() - t0).toBeLessThan(1000);
    });
  });
});
