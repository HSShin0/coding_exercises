'''
N couples sit in 2N seats arranged in a row and want to hold hands. We want to know the minimum number of swaps so that every couple is sitting side by side. A swap consists of choosing any two people, then they stand up and switch seats.

The people and seats are represented by an integer from 0 to 2N-1, the couples are numbered in order, the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2N-2, 2N-1).

The couples' initial seating is given by row[i] being the value of the person who is initially sitting in the i-th seat.

Example 1:

Input: row = [0, 2, 1, 3]
Output: 1
Explanation: We only need to swap the second (row[1]) and third (row[2]) person.
Example 2:

Input: row = [3, 2, 0, 1]
Output: 0
Explanation: All couples are already seated side by side.
Note:

len(row) is even and in the range of [4, 60].
row is guaranteed to be a permutation of 0...len(row)-1.
'''


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        ''' time/space complexity : O(N?)/O(N) '''
        elt2idx = {x: idx for idx, x in enumerate(row)}
        
        def partner(x):
            '''
            row의 원소 x와 couple인 partner를 반환한다.
            '''
            if x % 2 == 0:
                partner = x + 1
            else:
                partner = x - 1
            return partner
        
        
        def idx_next_to(x):
            '''
            row의 원소 x와 현재 같이 앉은 사람의 index를 반환한다.
            '''
            x_idx = elt2idx[x]
            if x_idx % 2 == 0:
                idx = x_idx + 1
            else:
                idx = x_idx - 1
            return idx
        
        swaps = 0
        unvisited = set(range(len(row)))
        
        for x in row:        
            if x in unvisited:
                unvisited.remove(x)
                idx = idx_next_to(x)  # x "옆자리"의 index
                x_length = 0
                y = partner(x)
                while True:
                    unvisited.remove(y)
                    if idx == elt2idx[y]:
                        break
                    x_length += 1
                    next_to_y = row[idx_next_to(y)]
                    unvisited.remove(next_to_y)
                    y = partner(next_to_y)
                swaps += x_length
        
        return swaps
