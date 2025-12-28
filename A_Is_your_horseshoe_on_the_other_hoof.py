import sys
input = sys.stdin.readline

def solve():
    colors = list(map(int, input().split()))
    seen = set()
    for color in colors:
        if color not in seen:
            seen.add(color)
    #print(seen)
    print(4 - len(seen))

if __name__ == "__main__":
    solve()