# Missile-Launcher-System

## Introduction
One of the important policies in military is assuring the consensus among the same level lieutenants regarding a command that results in catastrophic consequences or make innocent people at risk. Therefore, in the military, the generals use many different approaches to achieve this consensus. This report will show how a mathematical approach can be used to achieve consensus.

## Problem description
A general knows the key password 𝑵 to launch a missile (only him).
This general is commanding 𝒏 lieutenant generals and he want to share the knowledge of the key (without revealing it) with the 𝒏 lieutenant generals with consensus of at least 𝒌 of them to launch the missile. 

## Chinese Remainder Theorem ( CRT )
This project will use the Chinese Remainder Theorem (CRT) to achieve the specified requirement stated in the problem description. 
This section will explain the Chinese Remainder Theorem.
Chinese Remainder theorem states that it is possible to reconstruct integers in a
certain range from their residues modulo a set of pairwise relatively prime moduli.
Let 𝒎𝟏, 𝒎𝟐, . . . , 𝒎𝒏 be pairwise relatively prime positive integers greater than
one and 𝒂𝟏, 𝒂𝟐, . . . , 𝒂𝒏 arbitrary integers.
𝑵 ≡ 𝒂𝟏 (𝒎𝒐𝒅 𝒎𝟏,),
𝑵 ≡ 𝒂𝟐 (𝒎𝒐𝒅 𝒎𝟐),
… 
𝑵 ≡ 𝒂𝒏 (𝒎𝒐𝒅 𝒎𝒏)
 
Then the system has a unique solution modulo m = m1 • m2 • … • mn
Thus, there is a solution N with 0 ≤ N <m, and all other solutions are congruent
modulo m to this solution.


## Application of CRT
This section will explain how CRT will utilized to solve the consensus problem
in two sections: key generation, and key testing.
### - A. Key Generation
This part of the project will use the values 𝒏, 𝒌, and 𝑵 to generate the keys.
First, the system will check whether it is possible to get 𝒏 distinct coprime numbers
(𝑚1, … , 𝑚𝑛) knowing that the range of the coprime values that will be used are
satisfying the following:

⌈𝑘√𝑁⌉ ≤ 𝑚1, … , 𝑚𝑛 ≤ ⌊𝑘−1√𝑁⌋

This condition is critical to assure that the system will satisfy the condition that
says if at least 𝒌 of the 𝒏 keys are provided and to make sure that the multiplication of
the supplied 𝑚0, … , 𝑚𝑘 will be more than 𝑵. However, if this condition is not satisfied,
the system will refuse to generate keys and terminated.
Second, 𝒏 coprime numbers will be generated and sent to the third step. Third,
the system will calculate:

𝑵 𝒎𝒐𝒅 𝒎𝟏 = 𝒂𝟏
𝑵 𝒎𝒐𝒅 𝒎𝟐 = 𝒂𝟐
…
𝑵 𝒎𝒐𝒅 𝒎𝒏 = 𝒂𝒏

Then, it will return the values (𝑎1, 𝑚1), … , (𝑎𝑛, 𝑚𝑛) which is the list of the keys.
The system is demonstrated in Figure1 .

![image](https://user-images.githubusercontent.com/47674591/126030944-ef67f3a2-580b-4ed0-b33c-ba7d5ef9332b.png)

### - B. Key Testing

This part simply will use CRT to calculate 𝑵 using the supplied keys as
shown in Figure 2

![image](https://user-images.githubusercontent.com/47674591/126030981-5cfe934e-c029-427e-b786-da64d8276a98.png)

## References
Almuhammadi, S. “Lecture 05-Number Theory”. p11. King Fahd
University of Petroleum & Minerals.

