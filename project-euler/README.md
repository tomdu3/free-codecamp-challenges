# Project Euler

My solutions to the [Project Euler](https://www.freecodecamp.org/learn/project-euler) challenges from freeCodeCamp.

Project Euler is a series of challenging mathematical/computer programming problems. These problems range in difficulty and, for many, the experience is inductive chain learning — solving one problem exposes a new concept that makes a previously inaccessible problem solvable. The freeCodeCamp course is split into five sets covering problems 1 to 480, using concepts such as the Fibonacci sequence, prime number theory, combinatorics, Pascal's pyramid, the RSA algorithm, the binomial theorem, Hamming numbers, the Collatz sequence, combinatorial game theory, bitwise operations, and more.

> NOTE: As presented in the freeCodeCamp course, these challenges are JavaScript-only. The original problems at [projecteuler.net](https://projecteuler.net) are language-agnostic and can be solved in any language — only the freeCodeCamp adaptation constrains you to JavaScript.

## freeCodeCamp vs. projecteuler.net

These are the same problems, but the two platforms present them quite differently:

- **projecteuler.net** — each problem poses one fixed question with a single numeric answer (e.g. a specific limit). You solve it in any language, submit just the answer, and the site only tells you whether it is correct. Progress is tracked on your account.
- **freeCodeCamp** — each problem is rewritten as a JavaScript function that takes the limit/input as a parameter (like `multiplesOf3Or5(number)` here) and returns the result. There is no single answer to submit; instead your function is graded by automated tests run against several inputs, and the challenges form part of the certification curriculum.

So the maths is identical, but projecteuler.net asks for _one answer_ while freeCodeCamp asks for _a reusable solution_.

## Repository layout

Each problem lives in its own `problem-NN/` directory and typically contains:

- `problem.md` – the problem statement
- `<solution>.js` – the implementation
- `<solution>.test.js` – the Jest test suite
- `problem_reasoning.md` / `improvement-and-tests.md` – notes and optimizations (where present)

## Running the tests

```bash
npm install
npm test          # run the full Jest suite once
npm run test:watch  # re-run tests on change
```

You can also run a single problem's tests, e.g.:

```bash
npx jest problem-01
```

## Solved challenges

| #                                       | Problem                    | Directory                    | Key concepts                            | Difficulty | Tests |
| --------------------------------------- | -------------------------- | ---------------------------- | --------------------------------------- | :--------: | :---: |
| [1](https://projecteuler.net/problem=1) | Multiples of 3 or 5        | [`problem-01`](./problem-01) | Modular arithmetic, inclusion–exclusion |     5%     |  ✅   |
| [2](https://projecteuler.net/problem=2) | Even Fibonacci Numbers     | [`problem-02`](./problem-02) | Fibonacci sequence, iteration, parity   |     5%     |  ✅   |
| [3](https://projecteuler.net/problem=3) | Largest Prime Factor       | [`problem-03`](./problem-03) | Prime factorization, trial division     |     5%     |  ✅   |
| [4](https://projecteuler.net/problem=4) | Largest Palindrome Product | [`problem-04`](./problem-04) | Brute force, palindromes                |     5%     |  ✅   |
| [5](https://projecteuler.net/problem=5) | Smallest Multiple          | [`problem-05`](./problem-05) | Least common multiple, GCD, primes      |     5%     |  ✅   |
| [6](https://projecteuler.net/problem=6) | Sum Square Difference      | [`problem-06`](./problem-06) | Arithmetic series, closed-form sums     |     5%     |  ✅   |

Difficulty is the rating published on each Project Euler problem page (the share of members who have solved it). Every problem in this early set sits at the 5% floor, so treat the ratings as “beginner” rather than as a way to rank these six against each other.

## Copyright

### Problems

&copy; freeCodeCamp.org. Content licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

### Solutions

&copy; Tomislav Dukez, 2026.
