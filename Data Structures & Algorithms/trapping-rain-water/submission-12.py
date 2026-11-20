class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []          # indices de barres de hauteur décroissante
        total = 0

        for i, h in enumerate(height):
            while stack and height[stack[-1]] < h:
                bottom = stack.pop()
                if not stack:
                    break           # pas de mur gauche, rien à piéger
                left = stack[-1]
                width = i - left - 1
                depth = min(height[left], h) - height[bottom]
                total += width * depth
            stack.append(i)

        return total