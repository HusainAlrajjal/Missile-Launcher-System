# Missile-Launcher-System

## Introduction
One of the important policies in military is assuring the consensus among the same level lieutenants regarding a command that results in catastrophic consequences or make innocent people at risk. Therefore, in the military, the generals use many different approaches to achieve this consensus. This project will show how a mathematical approach can be used to achieve consensus.

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
𝑵 ≡ 𝒂𝟏 (𝒎𝒐𝒅 𝒎𝟏),
𝑵 ≡ 𝒂𝟐 (𝒎𝒐𝒅 𝒎𝟐),
… ,
𝑵 ≡ 𝒂𝒏 (𝒎𝒐𝒅 𝒎𝒏)
 
Then the system has a unique solution modulo 𝒎 = 𝒎𝟏 • 𝒎𝟐 • … • 𝒎𝒏
Thus, there is a solution 𝑵 with 0 ≤ 𝑵 < 𝒎, and all other solutions are congruent
modulo 𝒎 to this solution.[1]

## Application of CRT
This section will explain how CRT will utilized to solve the consensus problem
in two sections: key generation, and key testing.
###  A. Key Generation
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

𝑵 𝒎𝒐𝒅 𝒎𝟏 = 𝒂𝟏, 
𝑵 𝒎𝒐𝒅 𝒎𝟐 = 𝒂𝟐, 
… ,
𝑵 𝒎𝒐𝒅 𝒎𝒏 = 𝒂𝒏, 

Then, it will return the values (𝑎1, 𝑚1), … , (𝑎𝑛, 𝑚𝑛) which is the list of the keys.
The system is demonstrated in Figure1 .

![image](https://user-images.githubusercontent.com/47674591/126030944-ef67f3a2-580b-4ed0-b33c-ba7d5ef9332b.png)

###  B. Key Testing

This part simply will use CRT to calculate 𝑵 using the supplied keys as
shown in Figure 2

![image](https://user-images.githubusercontent.com/47674591/126030981-5cfe934e-c029-427e-b786-da64d8276a98.png)

## How to run the project ?

Navigate to the project folder then run the main.py file

## Interaction with the system
1. you will be asked to provide simple information about the problem as a setup such as K and n where K is the minimum number of general consensus required to launch the missile and n is the number of all generals in the system
2. The keys will be stored in a txt file called keys.txt, this file include they keys for all the n generals and each row in the file represents a single key.

  **NOTE: Each single key is actually a pair of two numbers represented as single row in the keys.txt file**
  
3. To test a key you need to paste the two numbers first, then press ENTER to enter the next key, note that the key length doesn't matter and you may test wrong keys also, if you finished entering all the keys enter e then click on ENTER to check whether the keys are correct or not

![image](https://user-images.githubusercontent.com/47674591/126032104-37bc5aeb-9569-4b6a-a05c-7715054831cf.png)

## Sample run
 **NOTE: We are not allowed to launch the missile here because we provided only 2 valid keys and we should've provided 3 instead since k = 3**
![image](https://user-images.githubusercontent.com/47674591/126032123-bd827e03-1f96-489a-88ea-7079536439eb.png)
