class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def clone(node, memo):
            if not node:
                return None
            if node in memo:
                return memo[node]
            copy = Node(node.val)
            memo[node] = copy
            copy.next = clone(node.next, memo)
            copy.random = clone(node.random, memo)
            return copy

        return clone(head, {})