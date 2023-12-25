import random


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
            'p': 1,
            'n': 3,
            'b': 3,
            'r': 5,
            'q': 9,
            'k': 999999999,
            '.': 0
        }
        self.calculate_rating()

    def __repr__(self) -> str:
        return f'{self.start}[{self.start_piece}] => {self.end}[{self.end_piece}](Rating:{self.rating})'

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
            self.rating += end_piece_val

        if square_table[square_table_end_index] > square_table[square_table_start_index]:
            self.rating += square_table[square_table_end_index] - \
                square_table[square_table_start_index]
        elif square_table[square_table_end_index] < square_table[square_table_start_index]:
            self.rating += square_table[square_table_start_index] - \
                square_table[square_table_end_index]
        else:
            self.rating += 0


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
            'p': ((-10, -11, -9, -20), 1),
            'n': ((-19, -21, -12, -8, 19, 21, 12, 8), 1),
            'b': ((-11, -9, 9, 11), 7),
            'r': ((-10, 10, -1, 1), 7),
            'q': ((-11, -9, 9, 11, -10, 10, -1, 1), 7),
            'k': ((-11, -9, 9, 11, -10, 10, -1, 1), 1)
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
            j = i.strip(' ').split()
            if j:
                x = [n for n in j[0]]
                out += str(k) + '| ' + ' '.join(x) + ' |\n'
                k -= 1

        return out + '  ----------------\n   a b c d e f g h'

    def calculate_score(self) -> None:
        score = 0
        for char in self.board:
            if char.lower() in self.piece_value_map:
                if (char.isupper()) and (self.turn == 'w'):
                    score += self.piece_value_map[char.lower()]
                elif (char.islower()) and (self.turn == 'b'):
                    score += self.piece_value_map[char]
                else:
                    score -= self.piece_value_map[char]

        return score

    def generate_possible_moves(self) -> list:
        possible_moves = []
        for piece_idx in range(len(self.board)):
            piece = self.board[piece_idx]
            if (piece.isupper() and self.turn == 'w') or (piece.islower() and self.turn == 'b'):
                match piece:
                    case 'p' | 'P':
                        possible_moves.append(self.pawn_moves(piece_idx))
                    case 'n' | 'N':
                        possible_moves.append(self.knight_moves(piece_idx))
                    case _:
                        possible_moves.append(self.sliding_moves(piece_idx))

        flattened = [i for x in possible_moves for i in x]
        filtered = sorted(flattened, key=lambda x: x.rating, reverse=True)
        return filtered

    def knight_moves(self, piece_idx: int) -> list:
        piece = self.board[piece_idx]
        possible_moves = []
        for direction_offset in self.move_offsets[piece.lower()][0]:
            new_pos = piece_idx + direction_offset
            if (new_pos not in self.invalid_indexes) and (new_pos < len(self.board)):
                new_pos_piece = self.board[new_pos]
                if new_pos_piece == '.':
                    possible_moves.append(Move(piece_idx, new_pos, self))
                elif piece.isupper() == new_pos_piece.islower():
                    possible_moves.append(
                        Move(piece_idx, new_pos, self))
        return possible_moves

    def pawn_moves(self, piece_idx: int) -> list:
        piece = self.board[piece_idx]
        possible_moves = []
        if piece.islower() and piece_idx > 30:
            self.move_offsets[piece.lower()] = self.move_offsets[piece.lower(
            )][0][:-1], self.move_offsets[piece.lower()][1]
        if piece.isupper() and piece_idx < 70:
            self.move_offsets[piece.lower()] = self.move_offsets[piece.lower(
            )][0][:-1], self.move_offsets[piece.lower()][1]
        for direction_offset in self.move_offsets[piece.lower()][0]:
            new_pos = piece_idx + direction_offset
            if (new_pos not in self.invalid_indexes) and (new_pos < len(self.board)):
                new_pos_piece = self.board[new_pos]
                # One or Two moves straight
                if (new_pos_piece == '.') and (direction_offset not in (-11, -9)):
                    possible_moves.append(Move(piece_idx, new_pos, self))
                # Capture left or right
                elif (piece.isupper() == new_pos_piece.islower()) and (direction_offset in (-11, -9)):
                    possible_moves.append(
                        Move(piece_idx, new_pos, self))
        return possible_moves

    def sliding_moves(self, piece_idx: int) -> list:
        piece = self.board[piece_idx]
        possible_moves = []
        for direction_offset in self.move_offsets[piece.lower()][0]:
            for offset_multiplier in range(1, self.move_offsets[piece.lower()][1] + 1):
                new_pos = piece_idx + direction_offset * offset_multiplier
                if (new_pos not in self.invalid_indexes) and (new_pos < len(self.board)):
                    new_pos_piece = self.board[new_pos]
                    if piece.isupper() == new_pos_piece.islower():
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
        elif isinstance(move, str):
            start_idx = self.algebraic_to_idx(move)
            if start_idx < len(self.board):
                p = filter(lambda x: x.start == start_idx,
                           self.generate_possible_moves())
                print(list(p))
                end = input('> ')
                end_idx = self.algebraic_to_idx(end)
                m = Move(start_idx, end_idx, self)
                self.move(m)

        self.turn = 'w' if self.turn == 'b' else 'w'

    def search(self) -> (int, int):
        duplicate_board = Board(self.board)
        duplicate_board.turn = self.turn
        depth = 1
        move = None

        def find() -> (int, int):
            nonlocal depth, move

            if depth == 0:
                d = duplicate_board.calculate_score()
                return d

            moves = duplicate_board.generate_possible_moves()
            weights = [x.rating for x in moves]
            choise = random.choices(moves, weights=weights, k=1)[0]

            if move is None:
                move = choise

            duplicate_board.move(choise)

            depth -= 1
            return find()

        x = find()
        return move


if __name__ == '__main__':
    b = Board()

    while True:
        print(b)
        b.move(input('> '))
        b.move(b.search())
