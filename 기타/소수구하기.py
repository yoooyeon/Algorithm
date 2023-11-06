n, m = map(int, input().split())
dp = [1 for _ in range(m + 1)]
dp[0] = dp[1] = 0
for num in range(n, m + 1):
    if dp[num] == 0:
        continue
    for i in range(2, int(num**0.5)+1): ## 소수 대칭성
        if num % i == 0:
            dp[num] = 0
            tmp = num
            while True:
                tmp += i
                if tmp >= m:
                    break
                dp[tmp] = 0
for i in range(n, m + 1):
    if dp[i] and i >= 2:
        print(i)


###### 효율성 높인 코드 ######

n, m = map(int, input().split())
is_prime = [True] * (m + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(m**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, m + 1, i): # i*i보다 작은 수는 이미 작은 소수에 의해 걸러졌다
            is_prime[j] = False

for i in range(max(2, n), m + 1):
    if is_prime[i]:
        print(i)
