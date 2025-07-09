# COSC261 Quiz: Foundations of Logic and Formal Languages

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
