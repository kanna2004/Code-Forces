import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    heights = list(map(int, input().split()))
    max_hieght = max(heights)
    min_height = min(heights)
    max_indices = [i for i, h in enumerate(heights) if h == max_hieght]
    min_indices = [i for i, h in enumerate(heights) if h == min_height]
    first_min_max_index = min(max_indices)
    firs_max_min_index = max(min_indices)
    moves = first_min_max_index + (n - 1 - firs_max_min_index)
    if first_min_max_index > firs_max_min_index:
        moves -= 1
    print(moves)

if __name__ == "__main__":
    solve()