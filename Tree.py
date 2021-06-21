class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class poon(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_poon(self, jalanan_type):
        if jalanan_type == "preorder":
            return self.kalo_preorder(tree.root, "")
        elif jalanan_type == "inorder":
            return self.kalo_inorder(tree.root, "")
        elif jalanan_type == "postorder":
            return self.kalo_postorder(tree.root, "")
        else:
            print("gagal bang")
            return False

    def kalo_preorder(self, start, jalanan):
        if start:
            jalanan += (str(start.value) + "-")
            jalanan = self.kalo_preorder(start.left, jalanan)  # ke kiri
            jalanan = self.kalo_preorder(start.right, jalanan)  # ke kanan
        return jalanan

    def kalo_inorder(self, start, jalanan):
        if start:
            jalanan = self.kalo_inorder(start.left, jalanan)  # ke kiri
            jalanan += (str(start.value) + "-")
            jalanan = self.kalo_inorder(start.right, jalanan)  # ke kanan
        return jalanan

    def kalo_postorder(self, start, jalanan):
        if start:
            jalanan = self.kalo_postorder(start.left, jalanan)  # ke kiri
            jalanan = self.kalo_postorder(start.right, jalanan)  # ke kanan
            jalanan += (str(start.value) + "-")
        return jalanan


#                 1
#               /   \
#              2     3
#            /  \   /  \
#           4    5  6   7

# 1-2-4-5-3-6-7-    urutan preorder
# 4-2-5-1-6-3-7-    urutan inorder
# 4-5-2-6-7-3-1-    urutan postorder
tree = poon(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node (5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)



print("Ini urutan Preorder : ", tree.print_poon("preorder"))
print("Ini urutan Preorder : ", tree.print_poon("inorder"))
print("Ini urutan Preorder : ", tree.print_poon("postorder"))




"""  def print_poon(self, jalanan_type):
        if jalanan_type == "preorder":
            return self.kalo_preorder(tree.root, "")
        else:
            print("gagal bang")
            return False


    def kalo_preorder(self, start, jalanan):
        if start:
            jalanan += (str(start.value) + "-")
            jalanan = self.kalo_preorder(start.left, jalanan) #ke kiri
            jalanan = self.kalo_preorder(start.right, jalanan) #ke kanan
            return jalanan
"""

"""tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node (5)
tree.right.left = Node(6)
tree.right.right = Node(7)
print(tree.value)
print(tree.left.value)
print(tree.right.value)
print(tree.left.left.value)
print(tree.left.right.value)
print(tree.right.left.value)
print(tree.right.right.value)"""