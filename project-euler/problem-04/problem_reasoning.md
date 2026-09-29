# Problem 4: Largest palindrome product — reasoning notes

> Guidance for building the solution myself. No solution code here — hints and thinking only.

## Understanding the problem

Find the **largest number that is simultaneously**:

1. A palindrome (reads the same forwards and backwards)
2. Expressible as a product of two 3-digit numbers (i.e., two numbers in 100–999)

The freeCodeCamp version is usually `largestPalindromeProduct(n)` — the largest palindrome that's a product of two *n*-digit numbers. The problem statement gives `9009 = 91 × 99` as the n=2 case, which is a perfect built-in test case. The answer for n=3 is a 6-digit number, so every candidate has an **even** number of digits — that fact matters for the 11 optimization below.

## The building blocks

**Block 1: Palindrome detection.** A helper that answers "is this number a palindrome?" — convert to a string and compare it against its reversed self. Write it as its own reusable function.

**Block 2: Generating candidates.** A double loop over factors `i` and `j` in [100, 999], computing `i * j`, keeping the largest palindromic product seen. Two things to get right:

- **Loop with `j` starting from `i`, not 100.** Multiplication is commutative, so `123 × 456` and `456 × 123` are the same product. Constraining `j ≥ i` roughly halves ~900,000 combinations to ~405,000.
- **Track a running max, don't return early** — see the first trap below.

## The traps (questions to answer before coding)

1. **The early-return trap.** If `i` iterates 999 → 100 and, for each `i`, `j` iterates 999 → 100, why is returning the *first* palindrome found wrong? Hint: compare products like `995 × 583` vs `993 × 913` — when does a smaller outer factor produce a *bigger* product? Conclusion: keep a running maximum.

2. **The safe-break question.** Even with a running max, when can the loop break early? If `i × 999` is smaller than the best palindrome found so far, can any later `i` do better?

## Optimizations to explore (optional, in order of payoff)

1. **Descending search with early break** — search top-down and stop once no remaining pair can beat the current best. What invariant makes the break correct?
2. **The 11 trick** — every palindrome with an even number of digits is divisible by 11. So if `a × b` is such a palindrome, 11 divides `a` or `b`. How could that reshape the loops (skip factors, restructure iteration)?
3. **Build the palindrome first, then verify** — generate 6-digit palindromes top-down (mirror the first half) and test "does this factor into two 3-digit numbers?" Fewer candidates, but the factoring check has subtleties (what's the valid range for one factor given the other?).

For a ~400k-iteration search in JS, even the naive version finishes in milliseconds — optimize for *learning*, not speed.

## Suggested path (matching the workflow from problems 1–3)

1. Write `isPalindrome` + brute force with a running max; make it correct first.
2. Write the test file like problems 1–3: the `9009` example, the n=3 case, and edge cases (what should n=1 return? decide and document).
3. Do the usual test-and-improvement pass with the descending-search and/or 11 optimizations.
