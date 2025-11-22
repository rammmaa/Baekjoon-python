# [Gold V] Give-a-Gnocchi - 25862 

[문제 링크](https://www.acmicpc.net/problem/25862) 

### 성능 요약

메모리: 111036 KB, 시간: 96 ms

### 분류

수학, 정수론, 소수 판정, 에라토스테네스의 체

### 제출 일자

2025년 11월 22일 22:46:12

### 문제 설명

<p>Your favorite Italian restaurant is having a promotion. The restaurant is giving away “free” gnocchi soups. The only cost is to provide them with a prime number. But the restaurant does not want to go out of business; they will only accept a prime number if it is not already in their database. Once a prime number is accepted, they add it to their database. As it turns out, every time you have tried to give them a prime number, no matter how large, they already have it in their database, so you end up having to pay for your meal.</p>

<p>Your friend, Euler, noticed something odd about the verification program. Euler gave the restaurant the number 24,990,001, and they accepted it. Euler realized this value was not prime after he checked it at home, so he did some analysis to determine what happened. It turns out the restaurant’s database accepts any number (even a composite number!) that is not divisible by a prime lower than or equal to some value n; which means you can easily get your gnocchi soup (albeit a little dishonestly) by finding a number (even a composite) the restaurant will accept. Basically, on the first day, you could give the first composite number that is not divisible by a prime lower than or equal to n; on the second day, you would give the next composite number that is not divisible by a prime lower than or equal to n, etc.</p>

<p>Since the restaurant keeps track of the numbers given to them, it is difficult to find what number to give to the restaurant next. Your other friend, Fermat, suggests that you write a program that will take in a value n and a day k, and it will output the k<sup>th</sup> (1-indexed) composite number that is not divisible by a prime less than n.</p>

### 입력 

 <p>The input consists of a single line providing two positive integers: n (n ≤ 1000), representing the highest possible value for checking for primality, and k (k ≤ 1000), indicating the index of the desired composite number.</p>

### 출력 

 <p>Print the k<sup>th</sup> (1-indexed) composite number satisfying the given constraints.</p>

