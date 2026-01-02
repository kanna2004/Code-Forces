import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    
    common = None
    for _ in range(n):
        route = list(map(int, input().split()))
        stations = set(route[1:])  # ignore first element
        
        if common is None:
            common = stations
        else:
            common &= stations   # intersection
    
    print(*sorted(common))

if __name__ == "__main__":
    solve()
