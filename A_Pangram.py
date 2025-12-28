import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    s = input().strip()
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    s_set = set(s.lower())
    if alphabet.issubset(s_set):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()