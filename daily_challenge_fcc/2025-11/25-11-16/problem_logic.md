# Rectangle Count Solution

To solve this problem, we need to determine the number of rectangles with integer dimensions that can fit inside a given rectangle of width $W$ and height $H$. The solution involves using a mathematical formula that derives the total number of such rectangles by considering all possible widths and heights of the smaller rectangles.

## Mathematical Insight

The number of rectangles of size $w \times h$ that can fit inside a $W \times H$ rectangle is given by $(W - w + 1) \times (H - h + 1)$. This is because there are $(W - w + 1)$ possible horizontal positions and $(H - h + 1)$ possible vertical positions for the top-left corner of the smaller rectangle.

To find the total number of all possible rectangles, we sum this expression over all possible $w$ (from 1 to $W$) and all possible $h$ (from 1 to $H$):

$$
S = \sum_{w=1}^{W} \sum_{h=1}^{H} (W - w + 1) (H - h + 1)
$$

This double sum can be simplified by recognizing that:

$$
\sum_{w=1}^{W} (W - w + 1) = \sum_{i=1}^{W} i = \frac{W(W+1)}{2}
$$

Similarly:

$$
\sum_{h=1}^{H} (H - h + 1) = \sum_{j=1}^{H} j = \frac{H(H+1)}{2}
$$

Thus, the total number of rectangles is:

$$
S = \frac{W(W+1) H(H+1)}{4}
$$

## Algorithmic Approach

The algorithm computes the value of $S$ using the formula above. Since $W$ and $H$ are positive integers, the product $W(W+1)$ is always even (as one of $W$ or $W+1$ is even), and similarly for $H(H+1)$. Therefore, the entire expression is always an integer, and integer division can be used.

### Code Implementation

The code implementation involves a simple function that takes the width $W$ and height $H$ as input, computes the formula, and returns the result using integer division.

```python
def rectangle_count(W, H):
    return (W * (W + 1) * H * (H + 1)) // 4
```

### Examples

1. For $W = 1$ and $H = 3$:

   $$
   \frac{1 \times 2 \times 3 \times 4}{4} = \frac{24}{4} = 6
   $$

   This matches the example provided.

2. For $W = 2$ and $H = 2$:

   $$
   \frac{2 \times 3 \times 2 \times 3}{4} = \frac{36}{4} = 9
   $$

   This confirms the formula with another case.

This approach efficiently computes the result in constant time, making it optimal for any values of $W$ and $H$.

---

## 🧠 The Problem and Formula, Simplified

The challenge is to count all the possible **sub-rectangles with integer-side lengths** that can fit inside a larger rectangle of a given width (W) and height (H).

The formula for the total number of such rectangles is:
**Total Rectangles = [W × (W + 1) × H × (H + 1)] / 4**

This formula works because it systematically counts all the different possible widths and heights a sub-rectangle can have.

*   **Choosing the Width:** Inside a rectangle of width `W`, how many different horizontal positions are there for a smaller rectangle of width `w`? There are `(W - w + 1)` possibilities. If you sum this for all `w` from 1 to W, you get `1 + 2 + 3 + ... + W`, which equals **W × (W + 1) / 2**.
*   **Choosing the Height:** The same logic applies vertically. The number of different vertical positions for a rectangle of height `h` is **H × (H + 1) / 2**.

Since every possible width can be paired with every possible height, you multiply these two sums together to get the total number of rectangles.

### 🔍 Resources to Deepen Your Understanding

The search results point to some more advanced mathematical concepts related to tiling. Here is a curated list of resources that will help you understand both the basic problem and its more complex relatives.

| Resource | Type | Key Focus Area | Why It's Useful |
| :--- | :--- | :--- | :--- |
| **Paper: "Simple Proofs of a Rectangle Tiling Theorem"** | Academic Article | Advanced Tiling Theorems | Explains a famous theorem: if all small tiles have one integer side, the big rectangle must also have one integer side. Great for seeing advanced, visual proofs (like the checkerboard method). |
| **Math Overflow Discussion** | Online Q&A | Deep Mathematical Connections | Experts discuss the deeper principles behind the tiling problem, including a proof using **double integrals**, connecting a geometric problem to calculus. |
| **Wolfram MathWorld: "Rectangle Tiling"** | Online Encyclopedia | Basic Combinatorics | A good, concise reference for the combinatorial formula you're using, confirming the mathematical foundation. |

### ➡️ How to Approach These Resources

1.  **Start with the Formula:** Make sure you are completely comfortable with the combinatorial explanation above. Try the formula on small examples (like a 2x2 grid) and draw the rectangles to see it in action.
2.  **Explore the "Whys":** Once the basics are solid, use the recommended resources to explore *why* these problems have such elegant solutions. The **checkerboard proof** and the **double integral proof** are beautiful examples of how mathematicians connect different areas of math.
3.  **Branch Out:** The paper and discussion also touch on the complexity of tiling (e.g., "NP-complete" problems), which is a major topic in computer science, showing how a simple-sounding problem can lead to very deep questions.

---

## 🎓 Tutorials and Articles
Here are some website tutorials that explain related concepts, which might help you build your understanding.

| Resource | Focus | Format | Key Details |
| :--- | :--- | :--- | :--- |
| **David Colson's Blog** | Rectangle Packing Algorithms | Text/Code | Explains algorithms like "Skyline Bottom-Left", includes code examples (C++), visuals, and compares performance. |
| **GeeksforGeeks - Tiling Problem** | Classic 2xN Tiling | Text/Code | Covers a fundamental problem, explains recursive and Dynamic Programming solutions (Python/Java/C++). |
| **Medium Article - Tiling Problem** | Dynamic Programming for Tiling | Text/Code | Explains the 2xN tiling problem with recursive, memoization, tabulation, and space-optimized solutions (Java). |

### 🔍 How to Find More Help
Since the search results are limited on video tutorials, you might have more success with these methods:

*   **Search on YouTube Directly**: Try using specific search phrases on YouTube such as:
    *   "Rectangle packing algorithm tutorial"
    *   "Dynamic Programming for tiling problems"
    *   "Introduction to combinatorial optimization"
*   **Explore Online Courses**: Platforms like Coursera, edX, and Khan Academy often have courses on algorithms that cover Dynamic Programming and combinatorial problems, which are the foundations of solving tiling and packing puzzles.
*   **Refine Your Focus**: If you have a more specific problem in mind (like a particular algorithm or problem type), letting me know could help me perform a more targeted search for you.