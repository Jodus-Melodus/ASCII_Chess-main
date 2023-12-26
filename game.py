import random, time
import chessboard

class Move:
    def __init__(self, start: int, end: int, board) -> None:
        self.start = start
        self.end = end
        self.board = board
        self.rating = 0.0
        self.start_piece = self.board.board[self.start]
        self.end_piece = self.board.board[self.end]

        self.piece_square_table = {
            'p': map(lambda x: x*10, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1, 1, -2, -2, 1, 1, 5, 0, 0, 5, -5, -1, 0, 0, -1, -5, 5, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 5, 5, 1, 2.5, 2.5, 1, 5, 5, 0, 0, 1, 1, 2, 3, 3, 2, 1, 1, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
            'n': map(lambda x: x*10, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -5, -4, -3, -3, -3, -3, -4, -5, 0, 0, -4, -2, 0, 5, 5, 0, -2, -4, 0, 0, -3, 5, 1, 1.5, 1.5, 1, 5, -3, 0, 0, -3, 0, 1.5, 2, 2, 1.5, 0, -3, 0, 0, -3, 5, 1.5, 2, 2, 1.5, 5, -3, 0, 0, -3, 0, 1, 1.5, 1.5, 1, 0, -3, 0, 0, -4, -2, 0, 0, 0, 0, -2, -4, 0, 0, -5, -4, -3, -3, -3, -3, -4, -5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
            'b': map(lambda x: x*10, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2, -1, -1, -1, -1, -1, -1, -2, 0, 0, -1, 5, 0, 0, 0, 0, 5, -1, 0, 0, -1, 1, 1, 1, 1, 1, 1, -1, 0, 0, -1, 0, 1, 1, 1, 1, 0, -1, 0, 0, -1, 5, 5, 1, 1, 5, 5, -1, 0, 0, -1, 0, 5, 1, 1, 5, 0, -1, 0, 0, -1, 0, 0, 0, 0, 0, 0, -1, 0, 0, -2, -1, -1, -1, -1, -1, -1, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
            'r': map(lambda x: x*10, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, -5, 0, 0, 0, 0, 0, 0, -5, 0, 0, -5, 0, 0, 0, 0, 0, 0, -5, 0, 0, -5, 0, 0, 0, 0, 0, 0, -5, 0, 0, -5, 0, 0, 0, 0, 0, 0, -5, 0, 0, -5, 0, 0, 0, 0, 0, 0, -5, 0, 0, 5, 1, 1, 1, 1, 1, 1, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
            'q': map(lambda x: x*10, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2, -1, -1, -5, -5, -1, -1, -2, 0, 0, -1, 0, 5, 0, 0, 0, 0, -1, 0, 0, -1, 5, 5, 5, 5, 5, 0, -1, 0, 0, -5, 0, 5, 5, 5, 5, 0, -5, 0, 0, 0, 0, 5, 5, 5, 5, 0, -5, 0, 0, -1, 0, 5, 5, 5, 5, 0, -1, 0, 0, -1, 0, 0, 0, 0, 0, 0, -1, 0, 0, -2, -1, -1, -5, -5, -1, -1, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
            'k': map(lambda x: x*10, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -3, -4, -4, -5, -5, -4, -4, -3, 0, 0, -3, -4, -4, -5, -5, -4, -4, -3, 0, 0, -3, -4, -4, -5, -5, -4, -4, -3, 0, 0, -3, -4, -4, -5, -5, -4, -4, -3, 0, 0, -2, -3, -3, -4, -4, -3, -3, -2, 0, 0, -1, -2, -2, -2, -2, -2, -2, -1, 0, 0, 2, 2, 0, 0, 0, 0, 2, 2, 0, 0, 2, 3, 1, 0, 0, 1, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        }
        self.piece_value_map = {
            'p': 10,
            'n': 30,
            'b': 30,
            'r': 50,
            'q': 90,
            'k': 999999999,
            '.': 0,
            ' ': 0
        }
        self.idx_to_algebraic = lambda idx: f'{chr(idx%10 + 96)}{9 - idx//10}'
        self.calculate_rating()

    def __repr__(self) -> str:
        return f'{self.idx_to_algebraic(self.start)}[{self.start_piece}] => {self.idx_to_algebraic(self.end)}[{self.end_piece}](Rating:{self.rating})'

    def calculate_rating(self) -> None:
        square_table_start_index = self.start
        square_table_end_index = self.end
        start_piece_val = self.piece_value_map[self.start_piece.lower()]
        end_piece_val = self.piece_value_map[self.end_piece.lower()]

        if self.start_piece.islower():
            square_table = list(
                reversed(list(self.piece_square_table[self.start_piece])))
        else:
            square_table = list(
                self.piece_square_table[self.start_piece.lower()])

        if end_piece_val > start_piece_val:
            self.rating += end_piece_val * 2
        else:
            self.rating += end_piece_val

        if (
            square_table[square_table_end_index]
            > square_table[square_table_start_index]
            or square_table[square_table_end_index]
            < square_table[square_table_start_index]
        ):
            self.rating += square_table[square_table_end_index]


class Board:
    def __init__(self, string: str = '') -> None:
        if string:
            self.board = string
        else:
            self.board = '''\
         
 rnbqkbnr
 pppppppp
 ........
 ........
 ........
 ........
 PPPPPPPP
 RNBQKBNR
         
'''
        self.invalid_indexes = list(filter(
            lambda x: x is not None, [i if n in '\n ' else None for i, n in enumerate(self.board)]))
        self.move_offsets = {
            'p': ((10, 11, 9, 20), 1),
            'n': ((-19, -21, -12, -8, 19, 21, 12, 8), 1),
            'b': ((11, 9, -9, -11), 7),
            'r': ((-10, 10, -1, 1), 7),
            'q': ((-11, -9, 9, 11, -10, 10, -1, 1), 7),
            'k': ((-11, -9, 9, 11, -10, 10, -1, 1), 1),
            'P': ((-10, -11, -9, -20), 1),
            'N': ((-19, -21, -12, -8, 19, 21, 12, 8), 1),
            'B': ((-11, -9, 9, 11), 7),
            'R': ((-10, 10, -1, 1), 7),
            'Q': ((-11, -9, 9, 11, -10, 10, -1, 1), 7),
            'K': ((-11, -9, 9, 11, -10, 10, -1, 1), 1)
        }
        self.white_score = 0
        self.black_score = 0
        self.turn = 'w'
        self.piece_value_map = {
            'p': 1,
            'n': 3,
            'b': 3,
            'r': 5,
            'q': 9,
            'k': 999999999,
            '.': 0
        }
        self.algebraic_to_idx = lambda AN: -10 * int(AN[1]) + ord(AN[0]) - 6
        self.idx_to_algebraic = lambda idx: f'{chr(idx%10 + 96)}{9 - idx//10}'

    def __repr__(self) -> str:
        t = self.board.split('\n')
        out = ''
        k = 8
        for i in t:
            if j := i.strip(' ').split():
                x = list(j[0])
                out += f'{str(k)}| ' + ' '.join(x) + ' |\n'
                k -= 1

        return out + '  ----------------\n   a b c d e f g h\n--------------------------------------------------------------'
    
    def is_white(self, piece:str) -> bool:
        if piece in 'KQRBNP':
            return True
        elif piece in 'kqrbnp':
            return False
        else:
            return None
        
    def is_black(self, piece: str) -> bool:
        if piece in 'kqrbnp':
            return True
        elif piece in 'KQRBNP':
            return False
        else:
            return None

    def toggle_turn(self) -> None:
        self.turn = 'b' if self.turn == 'w' else 'w'

    def calculate_score(self) -> None:
        score = 0
        for char in self.board:
            if char.lower() in self.piece_value_map:
                if self.turn == 'w' and self.is_white(char):
                    score += self.piece_value_map[char.lower()]
                elif self.turn == 'b' and self.is_black(char):
                    score += self.piece_value_map[char.lower()]
                else:
                    score -= self.piece_value_map[char.lower()]
        return score

    def generate_possible_moves(self) -> list[Move]:
        possible_moves = []
        for piece_idx in range(len(self.board)):
            piece = self.board[piece_idx]
            if (self.is_white(piece) and self.turn == 'w') or (self.is_black(piece) and self.turn == 'b'):
                match piece:
                    case 'p' | 'P':
                        possible_moves.append(self.pawn_moves(piece_idx))
                    case 'n' | 'N':
                        possible_moves.append(self.knight_moves(piece_idx))
                    case _:
                        possible_moves.append(self.sliding_moves(piece_idx))

        flattened = [i for x in possible_moves for i in x]
        return sorted(flattened, key=lambda x: x.rating, reverse=True)

    def knight_moves(self, piece_idx: int) -> list:
        piece = self.board[piece_idx]
        possible_moves = []

        for direction_offset in self.move_offsets[piece][0]:
            new_pos = piece_idx + direction_offset
            if (new_pos not in self.invalid_indexes) and (0 < new_pos < len(self.board)):
                new_pos_piece = self.board[new_pos]
                if new_pos_piece == '.':
                    possible_moves.append(Move(piece_idx, new_pos, self))
                elif self.is_white(piece) == self.is_black(new_pos_piece):
                    possible_moves.append(
                        Move(piece_idx, new_pos, self))               
    
        return possible_moves

    def pawn_moves(self, piece_idx: int) -> list:
        piece = self.board[piece_idx]
        possible_moves = []

        if self.is_black(piece) and piece_idx > 30:
            self.move_offsets[piece] = self.move_offsets[piece][0][:-1], self.move_offsets[piece][1]
        elif self.is_white(piece) and piece_idx < 70:
            self.move_offsets[piece] = self.move_offsets[piece][0][:-1], self.move_offsets[piece][1]

        for direction_offset in self.move_offsets[piece][0]:
            new_pos = piece_idx + direction_offset

            if (new_pos not in self.invalid_indexes) and (0 < new_pos < len(self.board)):
                new_pos_piece = self.board[new_pos]
                if (new_pos_piece == '.') and (direction_offset not in (11, 9, -11, -9)):
                    possible_moves.append(Move(piece_idx, new_pos, self))
                elif (self.is_white(piece) == self.is_black(new_pos_piece)) and (direction_offset in (11, 9, -11, -9)):
                    possible_moves.append(Move(piece_idx, new_pos, self))
                        
        return possible_moves

    def sliding_moves(self, piece_idx: int) -> list:
        piece = self.board[piece_idx]
        possible_moves = []

        for direction_offset in self.move_offsets[piece][0]:
            for offset_multiplier in range(1, self.move_offsets[piece][1] + 1):
                new_pos = piece_idx + direction_offset * offset_multiplier
                if (new_pos not in self.invalid_indexes) and (0 < new_pos < len(self.board)):
                    new_pos_piece = self.board[new_pos]
                    if self.is_white(piece) == self.is_black(new_pos_piece):
                        possible_moves.append(
                            Move(piece_idx, new_pos, self))
                        break
                    elif new_pos_piece == '.':
                        possible_moves.append(Move(piece_idx, new_pos, self))
                    else:
                        break
                else:
                    break
        return possible_moves

    def move(self, move: Move | str) -> None:
        if isinstance(move, Move):
            self.board = self.board[:move.start] + \
                '.' + self.board[move.start + 1:]
            self.board = self.board[:move.end] + \
                move.start_piece + self.board[move.end + 1:]

            self.toggle_turn()

        elif isinstance(move, str):
            start_idx = self.algebraic_to_idx(move)
            if start_idx < len(self.board):
                self.get_des_move_piece(start_idx)
        else:
            raise ValueError("Invalid argument")
            

    def unmake_move(self, move: Move | str) -> None:
        if isinstance(move, Move):
            self.board = self.board[:move.end] + \
                '.' + self.board[move.end + 1:]
            self.board = self.board[:move.start] + \
                move.start_piece + self.board[move.start + 1:]

            self.toggle_turn()

    def get_des_move_piece(self, start_idx):
        p = filter(lambda x: x.start == start_idx,
                   self.generate_possible_moves())
        print(list(p))
        end = input('> ')
        end_idx = self.algebraic_to_idx(end)
        m = Move(start_idx, end_idx, self)
        self.move(m)

    def search(self) -> Move:
        duplicate_board = Board(self.board)
        duplicate_board.turn = self.turn
        depth = 3

        def find(depth: int, move: Move = None) -> Move:
            if depth == 0:
                return move

            moves = duplicate_board.generate_possible_moves()
            best_move = None
            best_score = float('-inf')

            for move in moves:
                duplicate_board.move(move)
                score = duplicate_board.calculate_score()

                if score > best_score:
                    best_score = score
                    best_move = move

                duplicate_board.unmake_move(move)

            return best_move

        best_move = find(depth)
        return best_move



if __name__ == '__main__':
    b = Board()
    cb = chessboard.Chessboard()

    while True:
        cb.paint(b.board)
        b.move(b.search())