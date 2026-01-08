board =[' ']*9
def game_board():
    print()
    print(f"{board[0]} | {board[1]} | {board[2]} ")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]} ")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]} ")
    print()
def check_winner():
    win_conditions =[[0,1,2],[3,4,5],[6,7,8], #row
                     [0,3,6],[1,4,7],[2,5,8], #column
                     [0,4,8],[2,4,6]   #diagonal 
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False
def is_draw():
    return ' ' not in board
player = 'X'
while True: 
    game_board()
    move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
    if board[move] != ' ':
        print("Invalid move. Try again.")
        continue
    board[move] = player
    if check_winner():
        game_board()
        print(f"🎉 Player {player} wins!")
    if is_draw():
        game_board()
        print("🤝 It's a draw!")
        break  
player = 'O' if player == 'X' else 'X'         