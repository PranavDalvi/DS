# Write s program(s) to implement sets and sets operations.

# Declaraction of set
s1 = set({1,2,3})
s2 = set({1,4,5,6,7})

# Set Operation: add
s2.add(8)
print(s2)

# Set Operation: len
print(f"Length of the s1: {len(s1)}")
print(f"Length of the s2: {len(s2)}")

# Set Operation: remove
s2.remove(6)
print(s2)

# Set Operation: Copy
s3 = set()
s3 = s2.copy()
print(s3)

# Set Operation: Intersection (&)
print(s1 & s2)

# Set Operation: Union(|)
print(s1 | s2)

# Set Operation: <= (subset)
print(s1 <= s2)

# Set Operation: >= (superset)
print(s1 >= s2)