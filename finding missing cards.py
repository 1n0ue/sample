all_cards = [(s,n) for s in ["S","H","C","D"] for n in range(1,14)]
#for_inで配列代入
n = int(input())
hold_cards = [] #空のリスト
for i in range(n):
    suit,num = input().split()
    num = int(num) #キャスト
    hold_cards.append((suit,num)) #タプル
for cards in all_cards:
    if cards not in set(hold_cards): #not_inで含まれない場合実行
        print(*cards)