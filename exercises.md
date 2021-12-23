# Exercises

**Unless otherwise specified, write unit tests for everything!**

Additional resources:
* [Project Euler](https://projecteuler.net/)
* [Cryptopals](https://cryptopals.com/)

In vague order of difficulty,

* Propose your own exercise through a [Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) changing this file!
* Modular Arithmetic
  * Create functions which add, subtract, and multiply integers modulo some other integer
    * Make sure to deal with overflow
  * Create a class/type to represent integers modulo some integer
* Fibonacci
  * Write a function which, given a number, n, returns the nth [Fibonacci number](https://en.wikipedia.org/wiki/Fibonacci_number)
    * Make a function which is as short as possible
    * Make a function which is as fast as possible
    * Make a function which extends this to the real numbers
* Set Intersection (Join)
  * Write a function which takes two lists and returns their intersection
  * Write a version of this function which takes two functions from `Int -> T` and finds the intersection of the images of `{0, ..., n}`
* [Pi](https://en.wikipedia.org/wiki/Pi) Approximation
  * Implement a function that computes the first n digits of pi
  * How will you test this?
* [Mandlebot](https://en.wikipedia.org/wiki/Mandelbrot_set) and other Fractal Fun (no testing necessary, just fun)
  * Make a program which visualizes part of the mandlebrot set
  * What other cool things can you make by modifying your solution?
* Search
  * Write a function to search for the index of an element in a sorted list
* [Sort](https://en.wikipedia.org/wiki/Sorting_algorithm)
  * Write a function to sort a list of elements given some ordering function
    * Compare different sorting functions
  * Write an even better function which sorts a list of integers
* Change of Base
  * Write a function which takes in a number in one base and converts it to another
* Modular Exponentiation
  * Write a function which computes an input base raised to an input exponent modulo some integer
* [Euclid's Algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm)
  * Write a function which computes the gcd of two integers
  * Write a function which computes a number's inverse modulo some integer
* Big Integer
  * Implement a class/type representing arbitrarily large integers
  * Implement basic arithmetic operations for this class/type
  * Implement modular arithmetic for this class/type
* [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
  * Implement Conway's Game of Life
* [Polynomial Interpolation](https://en.wikipedia.org/wiki/Lagrange_polynomial)
  * Implement Lagrange Interpolation
    * Make sure to define all the necessary classes/types
* [Elliptic Curve](EllipticCurveExcerpt.pdf) Point Addition, Multiplication
  * Implement EC point addition over a finite field
  * Implement efficient EC point multiplication by a scalar over a finite field
* Counting Paths on [Graphs](https://en.wikipedia.org/wiki/Graph_theory)
  * Implement a class/type for directed graphs
  * Write a function which counts the number of distinct paths between two given vertices
* Normal Form of a Group Element given a Presentation
  * Implement a class/type for a presentation of a group consisting of generators, orders, and commutators
  * Write a function which computes the normal form of a given group element
* Voting Method Comparison
  * Implement a class/type for a person's (weighted) preferences between a set of options
  * Implement functions simulating election results under various voting methods
* [Markoff Chain](https://en.wikipedia.org/wiki/Markov_chain) Shenanigans
  * Do something fun with a Markoff chain
* [Wagner](https://www.iacr.org/archive/crypto2002/24420288/24420288.pdf) Collision Finding Implementation
  * Implement Wagner's algorithm for k=4
  * Implement Wagner's algorithm for when k is not bounded
  * Use your algorithm to find a sum-collision of SHA256
* [Convex Hull](https://en.wikipedia.org/wiki/Convex_hull) for a Finite Set
  * Given a finite set of points in R^n, write a function to find the smallest subset of points whose convex hull contains all others
    * Define all necessary classes/types
* Primality Testing
  * Write a function which determines whether a given integer is prime
  * Write a function which finds a prime number in a given large range
* Differential Equation Numerical Solving
  * Solve some differential equations numerically or something
* Graph Algorithms
  * Implement a class/type for graphs
    * Implement your favorite graph algorithm, or one you have or will teach in M106 (e.g. [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm))
  * Graph Coloring via [backtrack search](https://en.wikipedia.org/wiki/Backtracking)
    * Implement a function which computes a graph coloring by brute force using a backtrack search
* [Schnorr Signature](https://suredbits.com/introduction-to-schnorr-signatures/) Implementation
  * Implement Schnorr signatures for the [secp256k1 curve](https://en.bitcoin.it/wiki/Secp256k1)
  * Reused Nonce Key Derivation Implementation
    * Implement a function which computes the private keys of a signer who re-uses a nonce
  * Naive Signature Aggregation
    * Implement a key and signature aggregation protocol which simply adds directly the keys and signatures of participants
      * Implement a Rogue Key Attack on this protocol
  * Adaptor Variant
    * Implement [Schnorr single-signer adaptor signatures](https://suredbits.com/schnorr-applications-scriptless-scripts/)
  * Batch Verification
    * Implement the [Schnorr batch verification algorithm](https://suredbits.com/schnorr-applications-batch-verification/)
