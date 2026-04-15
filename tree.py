class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Binarytree:
    def __init__(self):
        self.root = None

    def _build_tree_recursive(self, prompt):
        value = input(prompt).strip()
        if value == "" or value.lower() in {"none", "null", "n", "-1"}:
            return None

        node = Node(value)
        node.left = self._build_tree_recursive(
            f"{value} ke left bete ka naam dalo (skip ke liye blank): "
        )
        node.right = self._build_tree_recursive(
            f"{value} ke right bete ka naam dalo (skip ke liye blank): "
        )
        return node

    def TreeBnaKarDo(self):
        if self.root is not None:
            overwrite = input(
                "Tree pehle se bana hua hai. Naya tree banana hai? (y/n): "
            ).strip().lower()
            if overwrite != "y":
                return self.root

        self.root = self._build_tree_recursive(
            "root ka naam dalo (skip ke liye blank): "
        )
        return self.root

    def _preorder(self, node, result):
        if node is None:
            return
        result.append(node.data)
        self._preorder(node.left, result)
        self._preorder(node.right, result)

    def preorder(self):
        result = []
        self._preorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node is None:
            return
        self._inorder(node.left, result)
        result.append(node.data)
        self._inorder(node.right, result)

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _postorder(self, node, result):
        if node is None:
            return
        self._postorder(node.left, result)
        self._postorder(node.right, result)
        result.append(node.data)

    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result