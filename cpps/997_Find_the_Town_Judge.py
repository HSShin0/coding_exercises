'''
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
'''

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        source_count = [0] * N
        target_count = [0] * N
        # 각 i에 대해서, trust[i] = [a, b] 일 때, a를 source, b를 target으로 count한다.
        for arrow in trust:
            a = arrow[0]
            b = arrow[1]
            source_count[a - 1] += 1
            target_count[b - 1] += 1
            
        if target_count.count(N-1) == 1:
            judge_candidate = target_count.index(N-1) + 1
            # 위의 판사후보가 아무도 믿지 않는지 확인한다.
            if source_count[judge_candidate - 1] == 0:
                return judge_candidate
            else:
                return -1
        else:
            return -1
