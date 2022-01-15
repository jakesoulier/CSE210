def main():
    grid = ['1','2','3','4','5','6','7','8','9']
    printgrid(grid)
    symbol = 'x'
    isxturn = True
    while not (gameover(grid) or isdraw(grid)):
        if isxturn:
            symbol = 'x'
        else:
            symbol = 'o'
        # while not is_pos_taken(grid):
        xuser = int(input(f"{symbol}'s turn to choose a square: "))
        if xuser not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print('That input is not possible, try again')
            xuser = int(input(f"{symbol}'s turn to choose a square: "))
        grid = updategrid(grid, xuser, symbol)
        printgrid(grid)
        if isxturn:
            isxturn = False
        else:
            isxturn = True
    print()
    print('game over!!')
    
def printgrid(grid):
    print(f'{grid[0]}|{grid[1]}|{grid[2]}\n{grid[3]}|{grid[4]}|{grid[5]}\n{grid[6]}|{grid[7]}|{grid[8]}')
    
def updategrid(grid, xuser, symbol):
    xuser -= 1
    grid[xuser] = symbol
    return grid

def gameover(grid):
    return (grid[0] == grid[1] == grid[2] or
            grid[3] == grid[4] == grid[5] or
            grid[6] == grid[7] == grid[8] or
            grid[0] == grid[3] == grid[6] or
            grid[1] == grid[4] == grid[7] or
            grid[2] == grid[5] == grid[8] or
            grid[0] == grid[4] == grid[8] or
            grid[2] == grid[4] == grid[6])

def isdraw(grid):
    for x in range(9):
        if grid[x] != 'x' and grid[x] != 'o':
            return False
    print('It was a draw!')
    return True

def is_pos_taken(grid):
    for x in range(9):
        if grid[x] == 'x' or 'o':
            print('That position is already taken, try again')
            return False
    return True
    
if __name__ == "__main__":
    main()