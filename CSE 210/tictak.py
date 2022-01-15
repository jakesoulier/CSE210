def main():
    print()
    grid = create_grid()
    print(grid)
    player_turn(grid)
    # printgrid = grid('0')
    # x_turn = input("x's turn to choose a square (1-9): ")
    # secondgrid = grid(x_turn)
def create_grid():
    grid = []
    for x in range(9):
        grid.append(x + 1)
    return grid
# def grid(turn):
#     line = ('1|2|3|4|5|6|7|8|9')
#     brkline = line.split('|')
#     listline = list(brkline)
#     turn = int(turn)
#     listline[turn - 1] = 'X'
#     print(listline)
def player_turn(grid):
    turn = int(input("X's turn to choose a square (1-9): "))
    grid[turn - 1]
    print(grid)
# if __name__ == '__main__':
#     main()
    
grid = ['1','2','3','4','5','6','7','8','9']
print(f'{grid[0]}|{grid[1]}|{grid[2]}\n{grid[3]}|{grid[4]}|{grid[5]}\n{grid[6]}|{grid[7]}|{grid[8]}')
userinput = int(input("x's turn to choose a square: "))