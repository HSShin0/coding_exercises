'''
In this problem, a tree is an undirected graph that is connected and has no cycles.
The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added.
The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.
The resulting graph is given as a 2D-array of edges.
Each element of edges is a pair [u, v] with u < v, that represents an undirected edge connecting nodes u and v.

Return an edge that can be removed so that the resulting graph is a tree of N nodes.
If there are multiple answers, return the answer that occurs last in the given 2D-array.
The answer edge [u, v] should be in the same format, with u < v.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given undirected graph will be like this:
  1
 / \
2 - 3

Example 2:
Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
Output: [1,4]
Explanation: The given undirected graph will be like this:
5 - 1 - 2
    |   |
    4 - 3

Note:
The size of the input 2D-array will be between 3 and 1000.
Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.

Update (2017-09-26):
We have overhauled the problem description + test cases and specified clearly the graph is an undirected graph.
For the directed graph follow up please see Redundant Connection II). We apologize for any inconvenience caused.
'''

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ''' time/space complexity : O(ND?))/O(N**2) where D: "diameter" of graph '''
        # 각 node 가 edges 안에서 나오는 index 와 그 짝이 되는 node의 값을 기록한다.
        v_count = {v : [] for v in range(1, len(edges) + 1)}
        for idx, edge in enumerate(edges):
            v0, v1 = edge
            v_count[v0].append((idx, v1))
            v_count[v1].append((idx, v0))
            
        # leaf와 연결된 edge들을 반복해서 제거한다.
        while True:
            count = 0
            
            for v0, i_v_list  in v_count.items():
                # v0가 leaf인 경우
                if i_v_list and len(i_v_list) == 1:
                    idx, v1 = i_v_list[0]
                    # v0와 연결되어있는 v1과 연결된 node들의 리스트에서 (idx, v0)를 제거한다.
                    v_count[v1].remove((idx, v0))
                    # v0와 연결된 node들의 list를 비운다.
                    v_count[v0] = None
                    count += 1
                    
            if count == 0:
                break
        
        # 남은 edge 중 원래 edges 안에서 가장 뒤에 나오는 원소를 찾아서 반환한다.
        last_idx = -1
        for _, i_v_list in v_count.items():
            if i_v_list:
                for idx, _ in i_v_list:
                    last_idx = max(last_idx, idx)
        
        return edges[last_idx]
