import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        even_mismatch = 0
        odd_mismatch = 0

        for i in range(n):
            if a[i] % 2 != i % 2:
                if i % 2 == 0:
                    even_mismatch += 1
                else:
                    odd_mismatch += 1

        if even_mismatch != odd_mismatch:
            print(-1)
        else:
            print(even_mismatch)

if __name__ == "__main__":
    solve()
