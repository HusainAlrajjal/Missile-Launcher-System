# Missile-Launcher-System

## Introduction
One of the important policies in military is assuring the consensus among the same level lieutenants regarding a command that results in catastrophic consequences or make innocent people at risk. Therefore, in the military, the generals use many different approaches to achieve this consensus. This report will show how a mathematical approach can be used to achieve consensus.

## Problem description
A general knows the key password 𝑵 to launch a missile (only him).
This general is commanding 𝒏 lieutenant generals and he want to share the knowledge of the key (without revealing it) with the 𝒏 lieutenant generals with consensus of at least 𝒌 of them to launch the missile. 

## Chinese Remainder Theorem
This project will use the Chinese Remainder Theorem (CRT) to achieve the specified requirement stated in the problem description. 
This section will explain the Chinese Remainder Theorem.
Chinese Remainder theorem states that it is possible to reconstruct integers in a
certain range from their residues modulo a set of pairwise relatively prime moduli.
Let m1, m2, . . . , mn be pairwise relatively prime positive integers greater than
one and a1, a2, . . . , an arbitrary integers.
N ≡ a1 (mod m1),
N ≡ a2 (mod m2),
… N
≡ an (mod mn)3
Then the system has a unique solution modulo m = m1 ・ m2 ・ … ・ mn .
Thus, there is a solution N with 0 ≤ N <m, and all other solutions are congruent
modulo m to this solution.[1]
