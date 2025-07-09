# COSC261 Quiz: Foundations of Logic and Formal Languages

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
