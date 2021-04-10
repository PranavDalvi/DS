class Bintree():
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None
    
  def insert(self,x):
	  if self.left == x:
	  	return None

	  elif x < self.data:
	  	if self.left is not None:
	  		self.left.insert(x)
	  		return x

	  	self.left=Bintree(x)
	  	return  x

	  elif x > self.data:
	  	if self.right is not None:
	  		self.right.insert(x)
	  		return x

	  	self.right=Bintree(x)
	  	return  x

#Inorder(LDR)
def inorder(root):
  if root is not None:
    inorder(root.left)
    print(str(root.data))
    inorder(root.right)
    return root

#Preorder (DLR) 
def preorder(root):
  if root is not None:
    print(str(root.data))
    preorder(root.left)
    preorder(root.right)
    return root

#Postorder(LRD) 
def postorder(root):
  if root is not None:
    postorder(root.left)
    postorder(root.right)
    print(str(root.data))
    return root
  
#driver code
root = Bintree(1)
root.left=Bintree(2)
root.right=Bintree(3)
root.left.left=Bintree(4)
root.left.right=Bintree(5)

root.insert(10)

print("Inorder traversal ")
a=inorder(root)

print("\nPreorder traversal ")
b=preorder(root)

print("\nPostorder traversal ")
c=postorder(root)

# output
# Inorder traversal 
# 4
# 2
# 5
# 1
# 3
# 10
# 
# Preorder traversal
# 1
# 2
# 4
# 5
# 3
# 10
# 
# Postorder traversal
# 4
# 5
# 2
# 10
# 3
# 1