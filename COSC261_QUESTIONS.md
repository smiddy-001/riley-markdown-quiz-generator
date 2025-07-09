# COSC261 Quiz: Foundations of Logic and Formal Languages

1. A tautology is a compound proposition that is always true, regardless of the truth values of its component propositions.
    - (x) True
    - ( ) False

2. Which of the following correctly represents DeMorgan's Law for propositional logic?
    - (x) ¬(p ∧ q) ≡ (¬p) ∨ (¬q)
    - ( ) ¬(p ∧ q) ≡ (¬p) ∧ (¬q)
    - ( ) ¬(p ∨ q) ≡ (¬p) ∧ (¬q) only
    - ( ) ¬(p → q) ≡ p ∧ ¬q

3. In a proof by contradiction for showing √2 is irrational, what do we assume at the start?
    - ( ) √2 is irrational
    - (x) √2 is rational
    - ( ) √2 = p/q where p and q are odd
    - ( ) √2 is a natural number

4. Which of the following statements about Russell's Paradox are correct?
    - [x] It shows there is no set of all sets
    - [x] It derives a contradiction from naive set theory
    - [ ] It proves that all sets are finite
    - [ ] It only applies to empty sets

5. If A ⊆ B, then P(A) ⊆ P(B), where P denotes the power set.
    - (x) True
    - ( ) False

6. Using Boolean algebra laws, A ∪ (A ∩ B) simplifies to:
    - ( ) A ∩ B
    - (x) A
    - ( ) B
    - ( ) A ∪ B

7. The Kleene star operation A* includes which of the following?
    - [x] The empty string ε
    - [x] All strings in A
    - [x] All concatenations of strings from A
    - [ ] Only strings of length 1

8. How many strings of length 2 or less are there over the alphabet Σ = {a, b, c}?
    - ( ) 6
    - ( ) 9
    - (x) 13
    - ( ) 12

9. The language L = {w | w ends with 'ab'} over Σ = {a, b} is regular.
    - (x) True
    - ( ) False

10. The regular expression a*b* over Σ = {a, b} generates which language?
    - ( ) All strings containing both a's and b's
    - (x) All strings of zero or more a's followed by zero or more b's
    - ( ) All strings with equal numbers of a's and b's
    - ( ) All strings ending in b

11. Which of the following are true about NFAs compared to DFAs?
    - [x] NFAs can have ε-transitions
    - [x] NFAs can have multiple transitions for the same symbol from one state
    - [ ] NFAs are more powerful than DFAs in terms of language recognition
    - [x] Every NFA can be converted to an equivalent DFA

12. A DFA that accepts strings over {0,1} where the third symbol is 1 requires at least how many states?
    - ( ) 3
    - (x) 4
    - ( ) 5
    - ( ) 6

13. The Pumping Lemma for regular languages states that for any regular language L, there exists a pumping length p such that any string w in L with |w| ≥ p can be divided into three parts xyz where:
    - [x] |xy| ≤ p
    - [x] |y| > 0
    - [x] xy^i z ∈ L for all i ≥ 0
    - [ ] |z| > 0

14. Regular languages are closed under which operations?
    - [x] Union
    - [x] Intersection
    - [x] Complementation
    - [x] Concatenation

15. The language L = {a^n b^n | n ≥ 0} is regular.
    - ( ) True
    - (x) False

16. Which production rule correctly generates palindromes over {a, b}?
    - ( ) S → aSa | bSb
    - (x) S → aSa | bSb | a | b | ε
    - ( ) S → aS | bS | ε
    - ( ) S → Sa | Sb | ε

17. A context-free grammar is ambiguous if:
    - ( ) It has left recursion
    - (x) There exists at least one string with two different parse trees
    - ( ) It cannot be parsed by any algorithm
    - ( ) It generates an infinite language

18. What is the name of the paradox that shows there cannot be a set of all sets?
    - R:= Russell's Paradox

19. What is the name of the algorithm used to convert an NFA to a DFA?
    - R:= Subset Construction

20. What is the minimum number of states needed for a DFA that accepts strings over {0,1} that contain the substring "101"?
    - R:= 4

21. A pushdown automaton (PDA) differs from a finite automaton by having:
   - ( ) Multiple input tapes
   - (x) A stack for memory
   - ( ) Bidirectional tape movement
   - ( ) Multiple start states

22. Which of the following languages can be recognized by a PDA but not by a DFA?
   - [x] {a^n b^n | n ≥ 0}
   - [x] {ww^R | w ∈ {a,b}*}
   - [ ] {a^n | n is even}
   - [x] {a^i b^j c^k | i = j or j = k}

23. The language {a^n b^n c^n | n ≥ 0} is context-free.
   - ( ) True
   - (x) False

24. A deterministic PDA is equivalent in power to a non-deterministic PDA.
   - ( ) True
   - (x) False

25. A Turing machine consists of which components?
   - [x] A finite state control
   - [x] An infinite tape
   - [x] A read/write head
   - [ ] A stack

26. The Church-Turing thesis states that:
   - ( ) All problems are computable
   - (x) Any effectively computable function can be computed by a Turing machine
   - ( ) Turing machines are faster than other computation models
   - ( ) All languages are decidable

27. Which of the following problems is undecidable?
   - ( ) Whether a DFA accepts a given string
   - ( ) Whether two DFAs are equivalent
   - (x) Whether a Turing machine halts on a given input
   - ( ) Whether a context-free grammar is ambiguous

28. A language is recursively enumerable if:
   - ( ) It can be decided by a Turing machine that always halts
   - (x) It can be accepted by a Turing machine (may not halt on rejection)
   - ( ) It is finite
   - ( ) It is context-free

29. Which grammar type allows productions of the form αAβ → αγβ where α, β, γ are strings and A is a non-terminal?
   - ( ) Regular grammar
   - (x) Context-sensitive grammar
   - ( ) Context-free grammar
   - ( ) Unrestricted grammar

30. In the Chomsky hierarchy, which inclusion relationship is correct?
   - ( ) Regular ⊃ Context-Free ⊃ Context-Sensitive ⊃ Recursively Enumerable
   - (x) Regular ⊂ Context-Free ⊂ Context-Sensitive ⊂ Recursively Enumerable
   - ( ) All language classes are equal
   - ( ) Context-Free ⊂ Regular ⊂ Context-Sensitive

31. The CYK algorithm is used for:
   - ( ) Converting NFAs to DFAs
   - ( ) Minimizing DFAs
   - (x) Parsing with context-free grammars in Chomsky Normal Form
   - ( ) Deciding if a language is regular

32. LL(1) parsing is:
   - [x] A top-down parsing method
   - [x] Requires one symbol of lookahead
   - [ ] More powerful than LR(1) parsing
   - [x] Cannot handle left-recursive grammars

33. An LR(1) grammar can handle left recursion while an LL(1) grammar cannot.
   - (x) True
   - ( ) False

34. What is the name of the construction method used to convert a regular expression to an NFA?
   - R:= Thompson's Construction

35. What is the name of the lemma used to prove that certain languages are not context-free?
   - R:= Pumping Lemma for Context-Free Languages

36. In the subset construction algorithm, what do the states of the resulting DFA represent?
   - R:= Sets of NFA states

37. What is the name of the famous undecidable problem concerning whether a program terminates?
   - R:= Halting Problem

38. What normal form requires all productions to be of the form A → BC or A → a?
   - R:= Chomsky Normal Form

39. What type of automaton is needed to recognize the language {a^n b^n | n ≥ 0}?
   - R:= Pushdown Automaton

40. What is the name of the operation that creates a new language containing all possible concatenations of strings from the original language?
   - R:= Kleene Star

41. Which complexity class contains problems that can be solved in polynomial time?
   - ( ) NP
   - (x) P
   - ( ) PSPACE
   - ( ) EXPTIME

42. The Universal Turing Machine is significant because:
   - [x] It can simulate any other Turing machine
   - [x] It demonstrates the concept of stored-program computation
   - [ ] It solves the Halting Problem
   - [x] It shows that computation can be described by data

43. Rice's Theorem states that:
   - ( ) All languages are decidable
   - (x) Any non-trivial property of recursively enumerable languages is undecidable
   - ( ) Context-free languages are closed under intersection
   - ( ) Regular languages have finite descriptions

44. What is the cardinality of the set of all languages over a finite alphabet?
   - R:= Uncountable

45. Name one closure property that regular languages have but context-free languages do not.
   - R:= Complementation

46. What is the minimum number of tape symbols needed for a universal Turing machine (including blank)?
   - R:= 2

47. In formal language theory, what does ε represent?
   - R:= Empty String

48. What is the name of the algorithm used to minimize a DFA by identifying equivalent states?
   - R:= Table Filling Algorithm

49. Which of the following strings are in the language generated by the regular expression (a|b)*abb?
   - [x] abb
   - [x] aabb
   - [x] babb
   - [ ] abab

50. For the grammar S → aSb | SS | ε, which strings can be generated?
   - [x] ε (empty string)
   - [x] ab
   - [x] aabb
   - [x] abab

51. A context-free grammar in Greibach Normal Form has all productions of the form:
   - ( ) A → a
   - ( ) A → BC
   - (x) A → aα where a is terminal and α is a string of non-terminals
   - ( ) A → αBβ

52. The complement of a context-free language is always context-free.
   - ( ) True
   - (x) False

53. Which of the following problems are decidable?
   - [x] Whether a DFA accepts the empty language
   - [x] Whether two DFAs accept the same language
   - [ ] Whether a context-free grammar is ambiguous
   - [x] Whether a regular expression matches a given string

54. The Post Correspondence Problem (PCP) is:
   - ( ) Decidable for all instances
   - (x) Undecidable in general
   - ( ) Only defined for binary alphabets
   - ( ) Equivalent to the Halting Problem

55. Two context-free grammars are equivalent if they generate the same language.
   - (x) True
   - ( ) False

56. When converting an NFA with ε-transitions to a DFA, the ε-closure of a state includes:
   - [x] The state itself
   - [x] All states reachable via ε-transitions
   - [x] States reachable through chains of ε-transitions
   - [ ] Only directly connected ε-transition states

57. In DFA minimization, two states are equivalent if:
   - [x] They have the same acceptance status (both final or both non-final)
   - [x] For every input symbol, they transition to equivalent states
   - [ ] They have the same number of outgoing transitions
   - [ ] They are both reachable from the start state

58. A right-linear grammar has productions of the form:
   - ( ) A → αB where α is any string
   - (x) A → aB or A → a or A → ε
   - ( ) A → Ba or A → a or A → ε
   - ( ) A → BC where B and C are non-terminals

59. Which machine model is needed to recognize each language class?
   Match the language class with its corresponding machine:
   - Context-Sensitive Languages: ( ) Finite Automaton, ( ) Pushdown Automaton, (x) Linear Bounded Automaton, ( ) Turing Machine
   - Regular Languages: (x) Finite Automaton, ( ) Pushdown Automaton, ( ) Linear Bounded Automaton, ( ) Turing Machine
   - Context-Free Languages: ( ) Finite Automaton, (x) Pushdown Automaton, ( ) Linear Bounded Automaton, ( ) Turing Machine

60. The language {a^i b^j c^k | 0 ≤ i ≤ j ≤ k} is:
   - ( ) Regular
   - (x) Context-free
   - ( ) Context-sensitive but not context-free
   - ( ) Not recursively enumerable

61. Which problems are in NP-Complete?
   - [x] Boolean Satisfiability (SAT)
   - [x] Hamiltonian Path Problem
   - [x] Vertex Cover Problem
   - [ ] Shortest Path Problem

62. If P = NP, then:
   - [x] Every problem in NP has a polynomial-time algorithm
   - [x] NP-Complete problems can be solved efficiently
   - [ ] The Halting Problem becomes decidable
   - [x] Cryptography based on computational hardness would be compromised

63. What is the name of the technique used to prove that certain context-free languages are not regular?
   - R:= Pumping Lemma for Regular Languages

64. In the context of Turing machines, what does it mean for a language to be co-recursively enumerable?
   - R:= Its complement is recursively enumerable

65. What is the name of the property that allows us to say "if a problem A reduces to problem B and B is decidable, then A is decidable"?
   - R:= Reducibility

66. Name the type of reduction commonly used to prove undecidability results.
   - R:= Many-one reduction

67. What is the technical term for a Turing machine that can simulate any other Turing machine?
   - R:= Universal Turing Machine

68. In parsing theory, what does "shift-reduce conflict" indicate?
   - R:= Grammar ambiguity in LR parsing

69. Regular expressions are commonly used in:
   - [x] Text processing and search
   - [x] Lexical analysis in compilers
   - [x] Input validation
   - [x] Pattern matching in programming languages

70. Context-free grammars are essential for:
   - [x] Programming language syntax definition
   - [x] Compiler design and parsing
   - [x] XML and markup language validation
   - [ ] Regular expression implementation

71. The undecidability of the Halting Problem has practical implications for:
   - [x] Static program analysis
   - [x] Automated debugging tools
   - [x] Program verification systems
   - [ ] Sorting algorithm efficiency

72. Consider the language L = {w#w | w ∈ {a,b}*}. This language is:
   - ( ) Regular
   - ( ) Context-free
   - (x) Context-sensitive
   - ( ) Not recursively enumerable

73. The intersection of two context-free languages is:
   - ( ) Always context-free
   - (x) Not necessarily context-free
   - ( ) Always regular
   - ( ) Always context-sensitive

74. A linear bounded automaton is a Turing machine where:
   - ( ) The tape is infinite in both directions
   - (x) The tape is bounded by the input length
   - ( ) Multiple tapes are used
   - ( ) The machine is deterministic

75. What is the name of the famous conjecture that P ≠ NP?
   - R:= P versus NP problem

76. In automata theory, what does the term "acceptance by final state" mean for a PDA?
   - R:= String accepted when PDA reaches final state regardless of stack

77. What is the name of the algorithm that determines if a context-free grammar generates any strings?
   - R:= Emptiness Algorithm

78. Name the property that states context-free languages are closed under union and concatenation but not intersection.
   - R:= Partial closure properties

79. What is the minimum number of colors needed to color any planar graph (this connects to computational complexity)?
   - R:= 4

80. In the context of formal language theory, what does "generative capacity" refer to?
   - R:= The set of languages a grammar type can generate