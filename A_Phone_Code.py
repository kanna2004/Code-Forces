import sys
input = sys.stdin.readline

def solve():
    def lcp(strings):
        if not strings:
            return ""
        
        first = strings[0]
        n = len(first)

        for s in strings[1:]:
            i = 0
            while i < n and i < len(s) and first[i] == s[i]:
                i += 1
            n = i
            if n == 0:
                break

        return len(first[:n])

    n = int(input())
    codes = [input().strip() for _ in range(n)]
    print(lcp(codes))

if __name__ == "__main__":
    solve()
