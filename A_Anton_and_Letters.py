import sys
input = sys.stdin.readline

def solve():
    letters = set(input())
    n = len(letters)
    print(n)
    seen = set()
    for letter in letters:
        if letter not in seen:
            seen.add(letter)
            n -= 1
    print(n)

if __name__ == "__main__":
    solve()