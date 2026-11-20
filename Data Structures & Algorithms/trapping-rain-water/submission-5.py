class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxi_l, maxi_r = [0], [0]
        m_l, m_r = 0, 0
        for i in range(0,n) :
            left, right = height[i], height[n-1-i]
            m_l, m_r = max(m_l, left), max(m_r, right)
            maxi_l.append(m_l)
            maxi_r.append(m_r)
        maxi_r = [maxi_r[i] for i in range(n-1,-1,-1)]
        total = 0
        for i in range(n) :
            left, right, h = maxi_l[i], maxi_r[i], height[i]
            mini = min(left, right)
            if mini > h :
                total = total+mini-h
        return total
# maxi_r = [0, 0,2]                         left = 0,2, 1
# m_l = 0, 0,2                              right = 1,2, 0
# m_r = 0, 1,2
# maxi_l = [0, 1,2]


                

