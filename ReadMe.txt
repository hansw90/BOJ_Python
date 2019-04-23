-------------------------------------- Day01 -------------------------------------------------- 

Big O Complecxity
//복잡도 순

O(N!)     : factorial 
// travelling salesman problem with brute force search
O(2^N)    : exponential
// travellling salesman problem with dynamic programming
O(N^2)    : quadratic
// bubble sort
O(N*logN) : linearithmic
// mergesort, quicksort, heapsort
O(N)      : linear
//search for a maximum element in an unsorted array
O(logN)   : logarithmic
//swap two numbers


-Polinomial (P) 다항식
//One of the most fundamental complexity classes  가장 근본적인 복잡도 클래스 중 하나
//Contains all decision problems that can be solved by a deterministic Turing machine
결정론적 튜링 기계로 해결할 수 있는 모든 의사결정 문제 포함???
//P is the class of computational problems that are "efficiently solvable"
P는 "효율적으로 해결 가능"한 계산 문제 클래스 입니다.
//For example : sorting algorithms


-Nondeterministic Polynomial (NP) 비결정성 다항식 //다항식으로 표현불가,,
//IF we have a solution to a problem, we can verify this solution in polynomial time (by a deterministic Turing machine)
//For instance where the answer is "Yes -> have efficiently verifiable proofs of the fact that the answer is indeed "yes..
//The complexity class P is contained in NP
//MOST IMPORTANT QUESTION : N = NP is it true?
//For example : integer factorization, travelling salesman problem


-NP-complete problems
//A decision problem is NP-complete when it is both in NP and NP-hard
//Although any given solution to an NP-complete problem ca be verified in polynomial time , there is no Known efficient way to locate a solution in the first place
//We usually just look for an approximate solution
//Heuristics 발견적 교수법??
//For example : chiness postman problem, graph coloring, Hamiltonian cycle

-NP-hard problems
//This is a class of problems that are at least as hard as the hardest problems in NP
//A problem H is NP-hard when every problem L in NP can be reduced in polynomial time to H
NP의 모든 문제 L이 다항식 시간에서 H로 감소 될 수있을 때 문제 H가 NP 하드 임
//As a consequence, finding a polynomial algorithm to solve any NP-hard problem would give polynomial algorithms for all the problems in NP
//For example : halting problem
정지문제(Halting Problem) : 입력을 통해 실행되는 프로그램 P가 있다고 가정하자. P에 어떤 입력값 A를 넣었을 때
P(A) 가 어떤 연산을 통해 프로그램이 종료가 되는지, 아니면 계속 연산을 진행하여 프로그램이 종료되지 않는지 확인하는 P가 있는가? 에대한 문제

