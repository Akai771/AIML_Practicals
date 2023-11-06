player, opponent = 'x', 'o'

def evaluate(b):
    lines = [b[0], b[1], b[2], [b[i][j] for i in range(3) for j in range(3) if i==j], [b[i][2-i] for i in range(3)]]
    for line in lines:
        if line.count(line[0]) == len(line) and line[0] != '_':
            return 10 if line[0] == player else -10
    return 0

def minimax(board, depth, isMax):
    score = evaluate(board)
    if score in [10, -10] or not any('_' in row for row in board):
        return score
    best = -1000 if isMax else 1000
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = player if isMax else opponent
                best = max(best, minimax(board, depth + 1, not isMax)) if isMax else min(best, minimax(board, depth + 1, not isMax))
                board[i][j] = '_'
    return best

def findBestMove(board):
    bestVal, bestMove = -1000, (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = player
                moveVal = minimax(board, 0, False)
                board[i][j] = '_'
                if moveVal > bestVal:
                    bestMove = (i, j)
                    bestVal = moveVal
    return bestMove

board = [
    [ 'x', 'o', 'x' ],
    [ 'o', '_', 'x' ],
    [ '_', 'o', '_' ]
]

bestMove = findBestMove(board)
print(f"The Optimal Move is : ROW: {bestMove[0]} COL: {bestMove[1]}")