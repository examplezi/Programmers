from collections import Counter
def solution(players, callings):
    # callings에 이름이 몇 번 나오는지 counter
    # players를 순회해서 counter의 키랑 같으면, 인덱스에서 값만큼 빼줌  
#     count = dict(Counter(callings))
#     for i in range(len(players)):
#         if players[i] in count:
#             temp = players[i - count[players[i]]] # soe, poe
#             players[i - count[players[i]]] = players[i]
#             players[i] = temp 
 
#     return players

          # list to map
      maps = {player: idx for idx, player in enumerate(players)}
  
      # for loop callings list
      for player in callings:
          # 현재 호출된 유저의 순위(인덱스) curPlayer에 할당
          curPlayer = maps[player]
          # maps에 저장된 현재 호출된 유저 순위 -1
          maps[player] -= 1
          # maps에 저장된 호출된 유저의 앞에 있던 유저 순위 +1
          maps[players[curPlayer-1]] += 1
          # players list에 저장된 두 유저의 위치 교체
          players[curPlayer-1], players[curPlayer] = players[curPlayer], players[curPlayer-1]
          # 위 코드가 어렵다면, 아래처럼 작성하셔도 괜찮습니다.
          # temp = players[curPlayer]
          # players[curPlayer] = players[curPlayer - 1]
          # players[curPlayer - 1] = temp
  
      return players
