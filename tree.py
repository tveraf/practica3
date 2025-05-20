class Node:
    def __init__(self, value):
        self.value = value
        self.left = None   # Blanca
        self.right = None  # Negra

    def __str__(self):
        return str(self.value)

class GameTree:
    def __init__(self):
        self.root = Node("Partida")

    def build(self, turns):
        current = self.root
        for turn in turns:
            white_node = Node(turn.white)
            black_node = Node(turn.black) if turn.black else None

            current.left = white_node  # blanca va a la izquierda
            white_node.right = black_node  # negra va a la derecha de la blanca

            current = white_node  # siguiente turno continúa desde la blanca

    def print_tree(self, node=None, depth=1, side=""):
        if node is None:
            node = self.root
            depth = 0  # Asegura que la raíz tenga indentación cero

        prefix = "  " * depth
        branch = f"({side}) " if side else ""
        print(f"{prefix}{branch}{node.value}")

        if node.left:
            self.print_tree(node.left, depth + 1, "W")
        if node.right:
         self.print_tree(node.right, depth + 1, "B")




