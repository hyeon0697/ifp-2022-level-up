# 별 찍기 - 12

n = int(input()) # n 값 입력

# 첫째 줄부터 2×N-1번째 줄까지 규칙에 맞춰 차례대로 별을 출력
for i in range(1,2*n):
    if(i <= n):
        print(" " * (n-i) + "*" * i)
    else:
        print(" " * (i-n) + "*" * (2*n-i))