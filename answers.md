# CMPS 2200 Assignment 02

## Answers

**Name:** Shiqian Zhang

Place all written answers from `assignment-02.md` here for easier grading.

## 1. Asymptotic notation

### a) T(n) = 2T(n/3) + 1

Using the Master Method,

```math
a=2,\qquad b=3,\qquad f(n)=1.
```

We compare $f(n)$ with

```math
n^{\log_3 2}.
```

Since

```math
1=O\left(n^{\log_3 2-\epsilon}\right)
```

for some $\epsilon>0$, the recursive part dominates.

Therefore,

```math
T(n)=\Theta\left(n^{\log_3 2}\right).
```

---

### b) T(n) = 5T(n/4) + n

Here,

```math
a=5,\qquad b=4,
```

so

```math
n^{\log_4 5}.
```

Since

```math
\log_4 5>1,
```

$n^{\log_4 5}$ grows faster than $n$.

Therefore,

```math
T(n)=\Theta\left(n^{\log_4 5}\right).
```

---

### c) T(n) = 7T(n/7) + n

Here,

```math
a=7,\qquad b=7.
```

Thus,

```math
n^{\log_7 7}=n.
```

The recursive contribution and the nonrecursive contribution have
the same asymptotic order.

Therefore, this is the balanced case of the Master Method:

```math
T(n)=\Theta(n\log n).
```

---

### d) T(n) = 9T(n/3) + n^2

Here,

```math
a=9,\qquad b=3.
```

Therefore,

```math
n^{\log_3 9}=n^2.
```

Since the recursive and nonrecursive terms have the same order, this
is again the balanced case.

Therefore,

```math
T(n)=\Theta(n^2\log n).
```

---

### e) T(n) = 8T(n/2) + n^3

Here,

```math
a=8,\qquad b=2.
```

Thus,

```math
n^{\log_2 8}=n^3.
```

The two terms have the same asymptotic order.

Therefore,

```math
T(n)=\Theta(n^3\log n).
```

---

### f) T(n) = 49T(n/25) + n^(3/2) log n

For the recursive part,

```math
n^{\log_{25}49}.
```

We have

```math
\log_{25}49
=
\frac{\log 49}{\log 25}
=
\frac{\log 7}{\log 5}
\approx 1.209.
```

The nonrecursive term is

```math
n^{3/2}\log n,
```

which grows polynomially faster than
$n^{\log_{25}49}$.

The regularity condition also holds because

```math
49
\left(\frac{n}{25}\right)^{3/2}
\log\left(\frac{n}{25}\right)
```

is at most a constant strictly less than 1 times
$n^{3/2}\log n$ for sufficiently large $n$.

Therefore, the root work dominates and

```math
T(n)=\Theta(n^{3/2}\log n).
```

---

### g) T(n) = T(n-1) + 2

Expanding the recurrence,

```math
T(n)
=
T(n-1)+2
=
T(n-2)+4
=
\cdots
=
T(1)+2(n-1).
```

Therefore,

```math
T(n)=\Theta(n).
```

---

### h) T(n) = T(n-1) + n^c, with c >= 1

Expanding gives

```math
T(n)
=
T(1)
+
\sum_{k=2}^{n} k^c.
```

For constant $c\geq 1$,

```math
\sum_{k=1}^{n} k^c
=
\Theta(n^{c+1}).
```

Therefore,

```math
T(n)=\Theta(n^{c+1}).
```

---

### i) T(n) = T(sqrt(n)) + 1

Assume

```math
n=2^{2^k}.
```

After one recursive call, the input becomes

```math
\sqrt{n}=2^{2^{k-1}}.
```

After two calls it becomes

```math
2^{2^{k-2}},
```

and after $k$ calls the input becomes 2.

Thus, the recursion depth satisfies

```math
2^k=\log_2 n.
```

Taking another logarithm,

```math
k=\log_2\log_2 n.
```

Since each level contributes constant work,

```math
T(n)=\Theta(\log\log n).
```

---

## 2. Algorithms Comparison

### Algorithm A

Algorithm A creates five subproblems of half the input size and
performs linear combine work.

Its recurrence is

```math
T_A(n)=5T_A(n/2)+\Theta(n).
```

Since

```math
n^{\log_2 5}
```

grows faster than $n$, the recursive work dominates.

Therefore,

```math
T_A(n)
=
\Theta\left(n^{\log_2 5}\right).
```

Since

```math
\log_2 5\approx 2.322,
```

this is approximately

```math
\Theta(n^{2.322}).
```

### Algorithm B

Algorithm B creates two subproblems of size $n-1$ and performs
constant combine work.

Its recurrence is

```math
T_B(n)=2T_B(n-1)+\Theta(1).
```

Expanding the recurrence gives a binary recursion tree whose number
of nodes doubles at each level.

There are approximately $n$ levels, so

```math
T_B(n)=\Theta(2^n).
```

### Algorithm C

Algorithm C creates nine subproblems of size $n/3$ and performs
quadratic combine work.

Its recurrence is

```math
T_C(n)=9T_C(n/3)+\Theta(n^2).
```

Since

```math
n^{\log_3 9}=n^2,
```

this is the balanced case of the Master Method.

Therefore,

```math
T_C(n)=\Theta(n^2\log n).
```

### Choice

The three asymptotic running times are

```math
T_A(n)
=
\Theta\left(n^{\log_2 5}\right)
\approx
\Theta(n^{2.322}),
```

```math
T_B(n)=\Theta(2^n),
```

and

```math
T_C(n)=\Theta(n^2\log n).
```

For sufficiently large inputs,

```math
n^2\log n
```

grows more slowly than both $n^{2.322}$ and $2^n$.

Therefore, I would choose **Algorithm C**.

---

## 3. Integer Multiplication

The standard divide-and-conquer multiplication algorithm performs
four recursive multiplications on problems of half the bit length.

Its recurrence is

```math
T_Q(n)=4T_Q(n/2)+O(n).
```

Using the Master Method,

```math
T_Q(n)=\Theta(n^2).
```

The Karatsuba-Ofman algorithm reduces the number of recursive
multiplications from four to three.

Its recurrence is

```math
T_K(n)=3T_K(n/2)+O(n).
```

Therefore,

```math
T_K(n)
=
\Theta\left(n^{\log_2 3}\right)
\approx
\Theta(n^{1.585}).
```

The `compare_multiply` function measures both implementations on
increasing bit lengths. For sufficiently large inputs, the
Karatsuba implementation should scale more slowly than the
quadratic implementation, which is consistent with these
asymptotic bounds.