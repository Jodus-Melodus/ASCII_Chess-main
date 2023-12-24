class Board:
    def __init__(self) -> None:
        self.board = '''\
         
 rnbqkbnr
 pppppppp
 ........
 ........
 ........
 ........
 ........
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
        self.piece_score_map = {
            'p': 1,
            'n': 3,
            'b': 3,
            'r': 5,
            'q': 9,
            'k': 999999999
        }
        self.turn = 'w'

    def __repr__(self) -> str:
        t = self.board.split('\n')
        scores = f'{self.white_score} : {self.black_score}'
        out = f'  {scores:^{18}}\n  ----------------\n'
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
                if (piece.isupper() != new_pos_piece.isupper()) or (new_pos_piece == '.'):
                    possible_moves.append(new_pos)
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

                if (new_pos_piece == '.') and (direction_offset not in (-11, -9)):
                    possible_moves.append(new_pos)

                elif (piece.isupper() == new_pos_piece.islower()) and (direction_offset in (-11, -9)):
                    possible_moves.append(new_pos)
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
                        possible_moves.append(new_pos)
                        break
                    elif new_pos_piece == '.':
                        possible_moves.append(new_pos)
                    else:
                        break
                else:
                    break
        return possible_moves


if __name__ == '__main__':
    b = Board()
    # while True:
    print(b)
    print(b.generate_possible_moves())
