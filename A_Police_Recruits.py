import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    events = list(map(int, input().split()))
    police, crimes = 0, 0
    for event in events:
        if event < 0:
            if police > 0:
                police -= 1
            else:
                crimes += 1
        else:
            police += event
    print(crimes)

if __name__ == "__main__":
    solve()