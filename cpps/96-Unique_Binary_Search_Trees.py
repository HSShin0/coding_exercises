class Solution:
    def __init__(self):
        self.memory = [1, 1] 
        # n = 0 은 numTrees 구현 시 편리함을 위해 1 로 설정.
        # n = 1 인 경우, 1 개의 binary search tree 존재.
    
    def numTrees(self, n: int) -> int:
        if n < len(self.memory):
            return self.memory[n]
        
        num_trees = 0
        
        # 1부터 n사이의 정수 k를 기준으로 가능한 left subtree와
        # right subtree들의 조합의 개수를 세어 num_trees에 더해준다.
        if n % 2 == 0:  # n 이 even number일 때
            for k in range(1, n//2 + 1):
                num_trees += 2 * self.numTrees(k-1) * self.numTrees(n - k)
        else:
            for k in range(1, n + 1):  
                num_trees += self.numTrees(k - 1) * self.numTrees(n - k)

        if n == len(self.memory):
            self.memory.append(num_trees)            
        
        return num_trees
