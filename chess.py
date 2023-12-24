
class Move:
    def __init__(self, start: int, end: int, board) -> None:
        self.start = start
        self.end = end
        self.board = board
        self.rating = 0

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
        return f'{self.start} => {self.end}(Rating:{self.rating})'

    def calculate_rating(self) -> None:
        start_piece = self.board.board[self.start]
        end_piece = self.board.board[self.end]
        square_table_start_index = self.start
        square_table_end_index = self.end
        start_piece_val = self.piece_value_map[start_piece.lower()]
        end_piece_val = self.piece_value_map[end_piece.lower()]

        if start_piece.islower():
            square_table = list(reversed(self.piece_square_table[start_piece]))
        else:
            square_table = self.piece_square_table[start_piece.lower()]

        print(square_table_start_index)

        if end_piece_val > start_piece_val:
            self.rating += end_piece_val
        else:
            self.rating += (start_piece_val + end_piece_val) // 2

        if square_table[square_table_end_index] > square_table[square_table_start_index]:
            self.rating += square_table[square_table_end_index] - \
                square_table[square_table_start_index]
        elif square_table[square_table_end_index] < square_table[square_table_start_index]:
            self.rating += square_table[square_table_start_index] - \
                square_table[square_table_end_index]
        else:
            self.rating += 0


class Board:
    def __init__(self) -> None:
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
        print(len(self.board))
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
        return possible_moves

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

    def search(self) -> (int, int):
        depth = 2

        def find() -> (int, int):
            nonlocal depth

            if depth == 0:
                return

            moves = self.generate_possible_moves()
            flattened = [i for x in moves for i in x]
            filtered = sorted(flattened, key=lambda x: x.rating)
            print(filtered)

            depth -= 1
            find()

        find()


if __name__ == '__main__':
    b = Board()
    print(b)
    b.search()
