import sys
input = sys.stdin.readline

def solve():
    distance = list(map(int, input().split()))
    distance.sort()
    print(distance[1] - distance[0] + abs(distance[1] - distance[-1]))

if __name__ == "__main__":
    solve()