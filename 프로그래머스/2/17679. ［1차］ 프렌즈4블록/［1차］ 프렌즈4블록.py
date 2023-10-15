# m = 가로, n = 세로
# 인덱스로 접근? 
# board[i][j], board[i][j+1], board[i+1][j], board[i+1][j+1] = > remove
# def solution(m, n, board):
#     answer = 0
#     filt = []
#     for i in board:
#         filt.append(list(i))
#     print(filt)

def solution(m, n, board):
    # cases : 네방향으로 나누어 삭제할 블록이 있는지 검사
    cases = [
        [(-1, -1), (-1, 0), (0, -1)], #왼쪽위
        [(-1, 1), (0, 1), (-1, 0)],   #오른쪽위
        [(0, -1), (1, -1), (1, 0)],   #왼쪽아래
        [(1, 0), (1, 1), (0, 1)]      #오른쪽아래
    ]
    board = [list(line) for line in board]
    score = 0
    while True:
        # 삭제할 위치 찾기 & 점수 계산
        delete = set([])
        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == '-': continue
                cur = board[i][j]
                for case in cases:
                    # 삭제 가능
                    if all(board[i+di][j+dj]==cur for (di,dj) in case):
                        delete.add((i,j))
                        delete.update(list(map(lambda x: (i+x[0], j+x[1]), case)))
        # 삭제할 블록 발견 못하면 리턴
        if len(delete)==0:
            return score
        score += len(delete)
        # 삭제 & 밀어넣기
        res_blocks = []
        for j in range(0, n):
            for i in range(m-1, -1, -1):
                if (i,j) in delete : continue
                res_blocks.append(board[i][j])
            while len(res_blocks)<m: res_blocks.append('-')
            for i in range(0, m):
                board[i][j] = res_blocks.pop()