# Problem 05 — Smallest Multiple: Test Results & Improvement Notes

## Solution review (smallestMultiple.js)

Verified correct against the 6 required cases, an independent BigInt
gcd-fold reference for **every** `n` from 1 to 42, divisibility by every
`d ≤ n` at n = 2/6/10/20/30/40, exact per-prime exponents at n = 20, and
monotonicity. All passed — nothing in the required range is wrong.

### Why the solution is correct

It implements Route B from `problem_reasoning.md`: track the **largest
exponent seen per prime**, then multiply the prime powers out at the end.

- **The model is the right one.** Working in exponents rather than in
  products of whole numbers is what makes minimality reachable at all: a
  composite is never multiplied in wholesale, so each prime's exponent stays
  independent of how the numbers happened to be combined.
- **The update rule is exactly right.** `Math.max` per prime is
  `e_p = max{v_p(k)}`, and multiplying `p^e_p` at the end is the LCM by
  definition.
- **Trial division by divide-out terminates.** `temp` shrinks every step, and
  the `temp === 1` break stops as soon as the number is fully decomposed.
- **The ordering requirement is met by the spec, not by luck.** Integer-like
  keys come back in ascending numeric order from `Object.keys`, so candidates
  are always tried smallest-first, which is what trial division needs.
- **The `isPrime` branch is load-bearing.** It is the only place keys are
  *inserted*; the factorisation path can only *update* keys that already
  exist. Measured: deleting those two lines and changing nothing else makes
  the map stay empty forever and returns `1` for every `n`.
- **Minimality is proven, not assumed.** Divisibility plus the exact
  per-prime exponents at `n = 20` is a proof that the result is the LCM, so
  no candidate search is needed. Divisibility *alone* would only establish a
  common multiple, which is why testing both together is the useful check.

### Cost profile

- Runtime is dominated by re-scanning the whole prime list for every `i`,
  with no cut-off: 24,068,809 inner iterations at `n = 20,000` (the map holds
  2,262 primes by then), and `Object.keys` allocates a fresh array for each
  of the ~17,700 composites.
- Roughly 1,040 ms at `n = 20,000`. Adding only the square-root cut-off drops
  that to 241,368 iterations and ~19 ms; a `Map`-based rewrite with the same
  cut-off lands in the same place.
- None of this is required: Free Code Camp only asks for `n ≤ 20`, which is
  instant. The interesting part is that the redundancy is *incidental work*,
  not the primality test people usually blame — the `isPrime` pass costs
  ~2.5 ms of that 1,040 ms.

### Improvement suggestions (not applied)

1. **Drop the per-number sweep for the direct per-prime rule — the
   substantial simplification.** The notes already state the closed form:
   `e_p` is just the largest `e` with `p^e ≤ n`. So the whole inventory of
   partial state can go: no factoring of each `i`, no map of provisional
   exponents, no "register the prime" step, and therefore **no unguarded
   insertion at all** (see point 4 — that entire bug class disappears because
   nothing is discovered incrementally any more). Work becomes proportional
   to π(n) small power-ladders instead of n full factorisations, and the
   function reads as the mathematics: for each prime, take its largest power
   below the bound, multiply them together. The prime list itself is then the
   only support work, and at this size even trial division is fine.
2. **Keep the gcd fold in your pocket as the independent check, not as dead
   code.** `lcm(a, b) = a / gcd(a, b) · b` folded over 2..n is a genuinely
   different algorithm (Euclid, no factorisation, no prime list), which is
   what makes it valuable for cross-checking — the notes ask for exactly
   this. Two things make it pleasant in practice: divide **before**
   multiplying so intermediates stay small, and note that it generalises to
   arbitrary sets, whereas both the current code and point 1 are specific to
   the consecutive range 1..n.
3. **Add the square-root cut-off — one comparison for a ~100× reduction.**
   Once the candidate exceeds √`remaining`, `remaining` is necessarily prime,
   so the loop can stop. This is the single biggest win in the file and it is
   safe for the same reason the notes' self-verification works: the
   remaining value has no factor below the failed candidate, so it cannot be
   composite. Worth doing even though FCC does not need it, because the
   uncut loop is the difference between "rescan everything for every number"
   and a normal factorisation sweep.
4. **Make the insertion order-independent instead of relying on an unstated
   invariant.** `primes[i] = 1` is an unconditional write into a map that is
   otherwise carefully max-managed, and it is correct only because `i`
   ascends. Measured: reversing the loop to descending and changing nothing
   else returns 210 instead of 2520 at `n = 10`. The failure would be easy to
   miss, because the result stays divisible by most of the range and so still
   looks like a plausible answer. A guarded insert (only if absent, or via a
   max) costs nothing and removes the dependency; point 1 removes the
   situation entirely.
5. **Decide the numeric contract rather than inheriting it.** The final
   multiplication is in `Number`, so results are exact only through `n = 42`;
   at `n = 43` it returns 941958815880242**2000** where the true LCM is
   941958815880242**1600**. (`n = 41` and 42 are exact by luck: a 58-bit
   value needs only 2^5 trailing zeros and the LCM happens to have exactly
   that; the 64-bit value at 43 would need 2^11 and has 2^5, so it rounds.)
   Out of scope for FCC, but a documented ceiling is one line, and the
   factored form — returning the prime powers and letting the caller
   multiply — is exact for any `n` at zero cost. `BigInt` is the third
   option if callers want a plain number back.
6. **Make the boundary behaviour deliberate.** `n ≤ 1`, `n = 0`, and
   negatives all return `1`, and `5.5` returns the same as `5`. Both are
   defensible (1 is the empty product, and flooring the bound is harmless
   here), but both are *implicit*: they fall out of a loop that never runs
   and a reducer's initial value. Either state them in a comment plus a test,
   or reject non-integers and negatives explicitly — the point is that a
   reader should not have to derive the contract from behaviour.
7. **If this function gets called repeatedly, reuse the state instead of
   rebuilding it.** The exponent map for a bound `m` is a prefix of the map
   for any larger bound, so a test sweep of 40 inputs recomputes the same
   work 40 times. Priming the map once and extending it is pure upside for
   sweeps while leaving the single-call path unchanged — optional, and only
   worth it if a caller actually sweeps.

Minor nits, if the file is touched anyway: `primes` actually holds exponents
(so something like `primePower` or `maxExponentByPrime` names the idea);
`isPrime(n)` shadows the outer `n`, which means "the range bound" everywhere
else in the file; the `count > 0` guard around the max update can collapse to
a single comparison; `Math.sqrt(n)` is recomputed on every iteration of the
helper's loop; and this file uses 2-space indentation while the test files
use 4.

## Test suite (smallestMultiple.test.js)

Jest suite in the style of problem-01/problem-04; **6 tests, all passing**.
Each of the checklist items maps to one test, named exactly as the
requirement reads: the return type for `smallestMult(5)`, then 5 → 60,
7 → 420, 10 → 2520, 13 → 360360, 20 → 232792560.

Beyond the checklist, a scratch suite (22 tests, all passing, not committed)
was used to establish the claims above. It was grouped by intent:

- **divisibility** — every `d ≤ n` divides the result, at n = 2/6/10/20/30/40.
- **minimality** — at `n = 20`, the exponent of each prime ≤ 20 equals the
  largest `e` with `p^e ≤ n`. This is the check that turns "a common
  multiple" into "the least common multiple"; divisibility alone cannot tell
  the least one apart from any larger common multiple.
- **independent cross-check** — agreement with the gcd fold for `n = 1..40`.
- **warm-ups** — `2 → 2`, `3 → 6`, `4 → 12`, `6 → 60`, `8 → 840`,
  `9 → 2520`, `12 → 27720`, frozen after checking them by hand.
- **boundaries** — `0`, `1`, `-1`, `-5` all return `1`; `5.5` behaves like
  `5`, documenting the truncation rather than leaving it unstated.
- **numeric ceiling** — exactness through `n = 42` verified against a BigInt
  reference, which pins the boundary from point 5 above.

Of those, the **minimality** and **cross-check** groups are the ones worth
keeping permanently — they are what make the suite a proof rather than a
table of remembered answers. The single test that proves least-ness
(the per-prime exponent check at `n = 20`) costs less than a millisecond.

## Running the tests

From the repository's `project-euler/` directory (Jest 30 is already
installed there — problem-05 has no package.json of its own):

```bash
cd project-euler
npx jest problem-05                  # this problem only
npx jest smallestMultiple.test.js    # this file, named explicitly
npm test                             # all problems
```

Note that a bare `npx jest` inside `problem-05/` runs **every** problem's
suite (currently 5 suites / 39 tests), because Jest walks up and finds the
root config first.

## Workspace hygiene note

No package.json, lockfile or `node_modules/` was created here — the parent
`project-euler/` remains the single test harness. Two small edits were made
to the source so it can be required by Jest at all: `module.exports =
smallestMult` was added, and the existing `console.log(smallestMult(20))`
was wrapped in a `require.main === module` guard so it no longer fires during
test runs. The scratch suite mentioned above was created as
`improvement-tests.tmp.test.js` and deleted after the measurements; nothing
else was touched.
