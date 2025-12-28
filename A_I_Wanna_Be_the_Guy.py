import sys
input = sys.stdin.readline

def solve():
    n  = int(input())
    xlevel = list(map(int, input().split()))
    ylevel = list(map(int, input().split()))
    levels = xlevel[1:] + ylevel[1:]
    for i in range(1, n + 1):
        if i not in levels:
            print("Oh, my keyboard!")
            return
    print("I become the guy.")

if __name__ == "__main__":
    solve()