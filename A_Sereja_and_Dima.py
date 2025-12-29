import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    cards = list(map(int, input().split()))
    sereja_score , dima_score = 0, 0
    turn_sereja = True
    while cards:
        if cards[0] >= cards[-1]:
            chosen_card = cards.pop(0)
        else:
            chosen_card = cards.pop()
        
        if turn_sereja:
            sereja_score += chosen_card
        else:
            dima_score += chosen_card
        
        turn_sereja = not turn_sereja
    print(sereja_score, dima_score)

if __name__ == "__main__":
    solve()