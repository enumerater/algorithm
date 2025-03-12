class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        self.build(data)

    def build(self, data):
        # Initialize leaves
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        # Build the tree by calculating parents
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, index, value):
        # Update the leaf node
        pos = index + self.n
        self.tree[pos] = value
        # Update the internal nodes
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]
                                                                                                              
    def query(self, left, right):
        # Query the sum in the range [left, right)
        result = 0
        left += self.n
        right += self.n
        while left < right:
            if left % 2:
                result += self.tree[left]
                left += 1
            if right % 2:
                right -= 1
                result += self.tree[right]
            left //= 2
            right //= 2
        return result

# Example usage:
data = [1, 2, 3, 4, 5, 6, 7, 8]
seg_tree = SegmentTree(data)
print(seg_tree.query(0, 4))  # Output: 10 (1+2+3+4)
seg_tree.update(3, 10)
print(seg_tree.query(0, 4))  # Output: 16 (1+2+3+10)