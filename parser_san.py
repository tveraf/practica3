import re

class Move:
    def __init__(self, notation):
        self.notation = notation

    def __str__(self):
        return str(self.notation) if self.notation else "-"


class Turn:
    def __init__(self, number, white, black=None):
        self.number = number
        self.white = white
        self.black = black

class ChessGameParser:
    # Reglas para validar jugadas según BNF
    MOVE_REGEX = re.compile(r'''
        (^O-O(-O)?$)                                     # Enroque
        | (^([KQRBN])?([a-h1-8]{0,2})?x?[a-h][1-8](=[QRBN])?[+#]?$)  # Movimiento de pieza o peón
    ''', re.VERBOSE)

    TURN_REGEX = re.compile(r'(\d+)\.\s*([^\s]+)(?:\s+([^\s]+))?')

    def parse_file(self, filename):
        with open(filename, 'r') as f:
            content = f.read().strip()
        return self.parse_game(content)

    def parse_game(self, text):
        turns = []
        for match in self.TURN_REGEX.finditer(text):
            num, white_move, black_move = match.groups()
            if not self.valid(white_move):
                raise ValueError(f"Jugada blanca inválida en turno {num}: {white_move}")
            if black_move and not self.valid(black_move):
                raise ValueError(f"Jugada negra inválida en turno {num}: {black_move}")
            turn = Turn(int(num), Move(white_move), Move(black_move))
            turns.append(turn)
        return turns

    def valid(self, move):
        return self.MOVE_REGEX.fullmatch(move) is not None
