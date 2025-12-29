import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        s = input().strip()
        print("YES" if s.lower() == "yes" else "NO")

if __name__ == "__main__":
    solve()