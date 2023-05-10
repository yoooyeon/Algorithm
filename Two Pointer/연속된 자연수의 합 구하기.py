N = int(input())
s, e = 0, 0
sum_ = 0
cnt = 1  # 자기 자신을 뽑는 경우

while e < N: # e의 범위: 1 ~ N - 1
    if sum_ == N:
        cnt += 1
        e += 1
        sum_ += e

    if sum_ > N: # 현재값이 목표값보다 크면 s 포인터를 한 칸 뒤로 옮긴다.
        s += 1
        sum_ -= s

    if sum_ < N: # 현재값이 목표값보다 작으면 e 포인터를 한 칸 뒤로 옮긴다.
        e += 1
        sum_ += e

print(cnt) # N = 15 , cnt = 4
