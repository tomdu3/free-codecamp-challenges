# Problem 5: Smallest multiple — reasoning notes

> Guidance for building the solution myself. No solution code here — hints and
> thinking only. The `n = 20` answer is deliberately **not** recorded, so it has
> to be derived and verified rather than looked up.

## Understanding the problem

"Smallest positive number evenly divisible by all of 1..20" is asking for the
**least common multiple (LCM) of the set {1, 2, ..., 20}**.

Two properties are demanded at once, and they pull in opposite directions:

1. **Divisibility** — the answer must be a multiple of every number in range.
2. **Minimality** — it must be the *smallest* such number.

The freeCodeCamp version is `smallestMult(n)`, generalized to 1..n. The problem
statement supplies `2520` for `n = 10`, which is a free built-in test case —
use it as ground truth long before touching `n = 20`.

**Design consequence:** before writing a loop, decide what a *candidate* is.
If a candidate can't be shrunk or grown piece by piece, there's no way to reason
about minimality — so pin down the candidate and the pruning rule *before*
writing the loop (see the traps below).

## The core reframe: stop thinking "numbers", start thinking "primes"

Every integer > 1 factors uniquely into primes (Fundamental Theorem of
Arithmetic). Write `v_p(x)` for "how many times prime `p` appears in `x`".

The rule that unlocks everything:

> `k` divides `X`  ⟺  for **every** prime `p`, `v_p(X) ≥ v_p(k)`.

Note what this rule does *not* mention: the order of multiplication, or which
composite numbers were multiplied to produce `X`. **Only per-prime exponents
matter.** That is the whole reason "keep a list of numbers and delete some"
struggles — it can't express "keep fewer copies of prime 2".

Apply the rule to the entire range. For the answer `L`:

- It must satisfy `v_p(L) ≥ v_p(k)` for every `k` in 1..n.
- The smallest value that works is the max over the range:

```
e_p = max{ v_p(k) : 1 ≤ k ≤ n }
L   = ∏ p^(e_p)   over all primes p ≤ n
```

**Why this is provably minimal** (state this in your own words before coding —
it's what tells you when to stop optimizing): lowering any single `e_p` by 1
breaks divisibility for whichever number in the range achieved that maximum.
Because the primes are independent, no adjustment to another exponent can
compensate. So no smaller candidate exists.

## Computing `e_p`

You can't scan and remember a max directly, but you don't need to. Ask instead:
*which number ≤ n contains the most copies of `p`?*

- Getting one more `p` means multiplying by `p` again.
- So the winner is the **largest power of `p` that does not exceed `n`**.

Equivalently: `e_p` is the largest `e` with `p^e ≤ n`.

Worked for `n = 10` (cross-check against the statement's `2520`):

| prime p | powers ≤ 10 | e_p | contribution |
| ------- | ----------- | --- | ------------ |
| 2       | 2, 4, 8 (16 > 10) | 3 | 8 |
| 3       | 3, 9 (27 > 10)    | 2 | 9 |
| 5       | 5                  | 1 | 5 |
| 7       | 7                  | 1 | 7 |

Product = `8 × 9 × 5 × 7 = 2520`. ✔ The model now predicts the statement's own
example, so it's validated before `n = 20` is attempted.

## The building blocks

**Block 1: enumerate primes up to n.** Trial division up to `√k` is plenty at
this size — the same idea already used in problem 3. No sieve needed.

**Block 2: for one prime, find its largest power ≤ n.** Start at `power = p`,
then keep multiplying while `power × p ≤ n`. When the next multiplication
would overshoot, `power` is `p^(e_p)`.

**Block 3: combine.** Multiply the per-prime contributions together.

## Two equivalent routes (write one, cross-check with the other)

**Route A — per prime (needs prime enumeration):**

1. Find every prime `p` from 2 to `n`.
2. For each, compute the largest `p^e ≤ n` (Block 2).
3. Multiply all those powers together.

**Route B — per number (needs no primality test):**

1. Keep a map `prime → largest exponent seen so far`, initially empty.
2. For each `k` from 2 to `n`, factorize `k` by trial division.
3. For each `(p, exp)` pair found, update the map only if `exp` is larger than
   what is stored.
4. Finally multiply `p^map[p]` across all keys.

A is shorter and leans on primes; B leans on factorization and never needs to
decide whether a number is prime. Whichever route you pick, verify the other
agrees — that's a strong independent check.

## A genuinely different route worth knowing

LCM has a pairwise identity:

> `lcm(a, b) = a × b / gcd(a, b)`

LCM is associative, so it can be folded across the range: start at 1 and, for
each `k` in 2..n, replace the accumulator with `lcm(accumulator, k)`. This
needs `gcd`, which Euclid's algorithm supplies (repeated `a mod b` until it
reaches 0).

One caution: divide **before** multiplying (`(a / gcd) * b`) so intermediate
values stay small. This route is valuable because it generalizes to arbitrary
sets of numbers, whereas Route A is specific to the consecutive range 1..n.

## The traps (questions to answer before coding)

1. **The pruning-unit question.** If the running state is "factors gathered from
   2..n", what exactly is allowed to leave that state when a new number arrives
   that is a multiple of an existing entry? Hint: removing `4` because `8`
   arrived is legitimate, but which *unit* is actually being compared — a whole
   number from the range, or a power of a single prime? Conclusion: the thing
   that gets pruned has to be the exponent of one prime. Get this wrong and the
   result is still divisible by everything (a common multiple, so the obvious
   check passes) while never being the *smallest* one — the model has to be
   right before any test can catch it.

2. **The "is it an exact power?" question.** A stricter rule — replace only when
   `i` is an exact power of an existing factor, say via
   `(Math.log(i) / Math.log(factor)) % 1 === 0` — removes *fewer* entries than
   divisibility does, so what happens to the product when entries are never
   removed? And is the float comparison even reliable? Hint: evaluate
   `Math.log(9) / Math.log(3)` and compare it to `2`. Conclusion: never test
   `=== 0` on a computed float ratio, and prefer integer arithmetic to
   logarithms for a question about divisibility.

3. **The model question.** Is the answer "a product of a subset of the numbers
   from 2..n"? If so, `4`, `6`, `8` and `10` can coexist and inject far more 2s
   than any one of them requires, and the product can only ever be *a* common
   multiple, never the least. Ask instead: *how many copies of each prime does
   the most demanding number in the range need?* That single reframing is the
   solution (see the core reframe above) — it is the question to answer before
   choosing any data structure.

4. **The representability question.** Which value has to stay an exact integer:
   the running product, the final product, or neither? `Number` arithmetic is
   exact only up to 2^53, and the *product* is what grows, not the individual
   factors. Hint: `n = 20` is comfortably inside the bound, but push `n` up and
   the product leaves it — at which point a wrong answer and a formatting
   question look identical. Conclusion: decide up front whether the answer is
   better kept factored as per-prime powers (exact at any `n`, never
   multiplied), computed in `BigInt`, or bounded with a documented limit.

5. **The iteration question.** If the state is an array being mutated with
   `splice(indexOf(value), 1)` while it is also being iterated, what guarantees
   the next index still refers to the same element? Hint: this is fragile under
   any model, and the fragility is invisible at small `n`. Conclusion: drive the
   state off a keyed structure (`Map`/object) so updates are addressed by key
   rather than by position.

## Self-verification (run before asking for review)

1. **Divisibility:** `L % d === 0` for every `d` in 1..n.
2. **Minimality:** for every prime `p ≤ n`, confirm `v_p(L)` equals the largest
   `e` with `p^e ≤ n`. Checks (1) + (2) together *prove* `L` is the LCM — there
   is no need to hunt for smaller candidates.
3. **Ground truth warm-ups:** verify by hand, then freeze as tests:
   `n = 2 → 2`, `n = 4 → 12`, `n = 6 → 60`, and `n = 10 → 2520` (from the
   problem statement).
4. **Cross-check:** Route A, Route B, and the gcd fold must all agree at
   `n = 20`.

## Edge cases to decide explicitly

- `n = 1` → the empty product, i.e. `1`.
- What should `n ≤ 0` do? Define it rather than letting a reducer throw on an
  empty array.
- Keep the final multiplication in integer arithmetic; avoid any route that
  multiplies much larger than necessary before dividing.

## Suggested path (matching the workflow from problems 1–4)

1. Re-derive the `n = 10` table above by hand, then check the model against
   `n = 6 → 60`.
2. Implement Route A (primes + largest power) and make it correct first.
3. Write `smallestMultiple.test.js` in the style of problems 1–4: the `2520`
   example, the hand-checked warm-ups, edge cases (1, 0, negatives), and
   agreement with the gcd fold.
4. Add the divisibility + minimality checker from *Self-verification* and run
   it at `n = 20`.
5. Only then compare against Route B / the gcd fold, and optionally do the
   usual test-and-improvement pass.

Run tests from the repository's `project-euler/` directory (Jest is installed
there; these problem folders have no package.json of their own):

```bash
cd project-euler
npx jest problem-05   # this problem only
npm test              # all problems
```
