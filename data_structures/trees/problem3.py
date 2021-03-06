"""
Suppose an arithmetic expression is given as a binary tree.
Each leaf is an integer and each internal node is one of
+,-,* or /.

Given the root to such a tree, write a function to evaluate it.
For example, given the following tree:
	 *
   /   \
  +     +
 / \   / \
3   2 4	  5
You should return 45, as it is (3 + 2) * (4 + 5)
"""

PLUS  = "+"
MINUS = "-"
MUL   = "*"
DIV   = "/"

def evaluate(root):
	if root.data == PLUS:
		return evaluate(root.left) + evaluate(root.right)
	elif root.data == MINUS:
		return evaluate(root.left) - evaluate(root.right)
	elif root.data == MUL:
		return evaluate(root.left) * evaluate(root.right)
	elif root.data == DIV:
		return evaluate(root.left) / evaluate(root.right)
	else:
		return root.data


##### Test Code #####
class Node():
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


def decode_tree(root):
	result = []

	if root:
		result.append(root.data)
		result += decode_tree(root.left)
		result += decode_tree(root.right)

	return result


def main():
	tree = Node('*', Node('+', Node(3), Node(2)), Node('+', Node(4), Node(5)))
	tree_two = Node('/', 
		Node('*', Node('+', Node(1), Node(2)), Node('+', Node(3), Node(4))), 
		Node('*', Node('-', Node(5), Node(6)), Node('-', Node(7), Node(8))))

	print('First Tree; result:', evaluate(tree))
	print(decode_tree(tree))
	assert evaluate(tree) == 45

	print('\nSecond Tree; result:', evaluate(tree_two))
	print(decode_tree(tree_two))
	assert evaluate(tree_two) == 21.0


if __name__ == '__main__':
	main()
