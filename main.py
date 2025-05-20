from parser_san import ChessGameParser
from tree import GameTree

def main():
    parser = ChessGameParser()
    try:
        turns = parser.parse_file("partida.txt")
        tree = GameTree()
        tree.build(turns)
        tree.print_tree()
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
