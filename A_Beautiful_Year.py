import sys
input = sys.stdin.readline

def solve():
    n = int(input().strip())
    digits = set(str(n))
    
    for year in range(n + 1, 9013):
        if len(set(str(year))) == 4:
            print(year)
            break

if __name__ == "__main__":
    solve()