
class HrestyNoliki():

    def __init__(self, 
                 matrix: list | None = None, 
                 size  : int  | None = None):
        
        self.cross  = '+'
        self.zero   = '0'

        if matrix is not None:
            if not isinstance(matrix, list) or len(matrix) < 3:
                raise ValueError("Matrix must be list and have at least 3 elements")
            
            etalon = len(matrix[0])
            if len(matrix) != etalon:
                raise ValueError("Matrix must be nxn")

            if any(len(i) != etalon for i in matrix):
                raise ValueError("Rows must be identical")
                
            self.matrix = matrix
            self.size   = len(matrix)
        
        elif size is not None:
            if type(size) != int:
                raise ValueError("Size must be int")
            if size < 3:
                raise ValueError("Matrix must be at least 3x3")
            self.matrix = [["*"] * size for _ in range(size)]
            self.size   = size

        else:
            self.matrix = [['*', '*', '*'],
                           ['*', '*', '*'],
                           ['*', '*', '*']]
            self.size   = 3
            
    def display(self):
        for i in self.matrix:
            print(' | '.join(i))

    def check_winner(self):
        for row in self.matrix:
            if len(set(row)) == 1 and row[0] in (self.zero, self.cross):
                return row[0]
        
        check = [   
                    # cols
                    *[set(self.matrix[j][i] 
                           for j in range(self.size)) 
                                for i in range(self.size)],

                    # diag main 
                    set(self.matrix[i][i] 
                        for i in range(self.size)),

                    # diag other
                    set(self.matrix[i][self.size-1-i] 
                        for i in range(self.size))
                ]

        for s in check:
            if len(s) == 1 and '*' not in s:
                symbol = list(s)[0] 
                return symbol

        return None
    
    def player_move(self, symb):
        enter = '_' * 50
        
        print(  f'{enter}                         \n'
                f'                                \n'
                f'|----Make your gap "{symb}"----|\n')
        
        while True:
            try:
                try:
                    x = int(input("|----Input coordinat row: "))
                    if x < 0 or x > self.size - 1: 
                        raise IndexError
                except ValueError: 
                    print(f"!!! There must be int:) !!! \n")
                    continue  
                except IndexError:
                    print(f"!!! You can choose only 0-{self.size-1} !!! \n")
                    continue  
                    
                try:
                    y = int(input("|----Input coordinat col: "))
                    if y < 0 or y > self.size - 1: 
                        raise IndexError
                except ValueError: 
                    print(f"!!! There must be int:) !!! \n")
                    continue  
                except IndexError:
                    print(f"!!! You can choose only 0-{self.size-1} !!! \n")
                    continue  
                
                if self.matrix[x][y] != '*':
                    raise ValueError
                
                break

            except ValueError:
                print('!!! You can`t do this move (cell occupied) !!!\n')

        print(f'{enter} \n')

        self.matrix[x][y] = symb

    def game(self):
        first_move = self.cross
        while True:
            self.display()
            self.player_move(first_move)
            result = self.check_winner()
            if result:
                self.display()
                return result 
            
            if not any('*' in row for row in self.matrix):
                self.display()
                print("Game Over")
                return 'Loxi'
            
            first_move = '0' if first_move == '+' else '+'
            
    
if __name__ == '__main__':

    test = HrestyNoliki()

    print(f'{'_' * 50}                     \n'
          f'CONGRATULATIONS!!!             \n'
          f'OUR WINNER IS "{test.game()}"!!!')

