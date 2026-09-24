# Problem 03 — Largest Prime Factor: Test Results & Improvement Notes

## Solution review (largestPrimeFactor.js)

Verified correct against 13 cases including the real Project Euler input
(`600851475143` → `6857`, runs in ~0.3 ms) and a large-prime timing probe
(`1000003`, ~12 ms). All passed.

### Why the solution is correct

It implements the "evict the smallest factor" strategy:

1. Try candidate divisors starting at 2. Whenever one divides `n`, record it
   as the current `largestPrime` and divide `n` by it, repeating with the
   **same** candidate until it no longer divides (handles repeated factors
   like 1024 = 2^10).
2. When a candidate stops dividing, move to the next candidate.

Three properties make this work without any explicit primality test:

- **All 2s are stripped before 4 is ever considered**, and likewise for
  every composite candidate: by the time candidate `c` is reached, no prime
  `< c` divides `n`, so no composite `< c` can either. The `%` check alone
  filters them — only primes ever assign `largestPrime`.
- **No √n stopping-bound problem**: the loop runs until `n === 1`, so the
  largest factor is found even when it lies *above* √n of the original input
  (e.g. `34 = 2 × 17` → 17, the classic trap for "scan down from √n" designs).
- **The final iteration self-registers** the leftover prime before `n`
  reaches 1, so no post-loop special-casing is needed.

### Cost profile

- Runtime is dominated by trial division up to the second-largest prime
  factor: `O(√n)` iterations worst case, `O(1)` extra memory.
- For the real PE #3 input (6857 is small) this is trivial — 0.3 ms.

### Optional refinements (not applied — the solution is already fast enough)

1. **Skip even candidates**: after stripping 2s, increment by 2
   (`largestFactor += largestFactor === 2 ? 1 : 2`), halving the iterations.
2. **Early exit**: when `largestFactor * largestFactor > n`, the remaining
   `n` is itself prime and is the answer — return it immediately. Irrelevant
   for PE #3's input, but the standard optimization for much larger inputs
   (e.g. RSA-style semiprimes where the smallest factor is enormous).

## Test suite (largestPrimeFactor.test.js)

Jest suite grouped by intent, mirroring the style of problem-01/problem-02:

- **problem examples** — the 13195 → 29 case from problem.md and the real
  input 600851475143 → 6857.
- **prime inputs** return the number itself (2, 7, 13, 97).
- **repeated factors** — powers of two and mixed powers catch off-by-one
  bugs in the re-try-same-candidate logic.
- **the √n trap** — `34 → 17` and a semiprime of two large primes
  (10007 × 10009) guard against anyone later "optimizing" the function with
  a bound or starting point at √n, the classic way this algorithm breaks.
- **edge cases** — 0, 1, and negatives all return 0 (defined behavior from
  the `n < 2` guard).
- **performance** — the real input must finish well under a second.

## Running the tests

From the repository's `project-euler/` directory (Jest 30 is already
installed there — problem-03 has no package.json of its own):

```bash
cd project-euler
npx jest problem-03        # this problem only
npm test                   # all problems
```

## Workspace hygiene note

While testing, I briefly created a nested `problem-03/package.json`,
`package-lock.json`, and `node_modules/` with a second Jest install. These
were removed — the parent `project-euler/` package.json is the single test
harness for all problems, and the source was converted from ESM
(`export function`) to CommonJS (`module.exports`) to match the convention
used by problem-01 and problem-02.
