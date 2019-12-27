'''
Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list A of strings.  Every string in A is an anagram of every other string in A.  How many groups are there?

 

Example 1:

Input: A = ["tars","rats","arts","star"]
Output: 2
 

Constraints:

1 <= A.length <= 2000
1 <= A[i].length <= 1000
A.length * A[i].length <= 20000
All words in A consist of lowercase letters only.
All words in A have the same length and are anagrams of each other.
The judging time limit has been increased for this question.
'''


class Solution:
    def numSimilarGroups(self, A: List[str]) -> int:
        '''
        time/space complexity : O(N^2*W)/O(N^2) where W is the (maximal) length of words in A
        '''
        unvisited = set(range(len(A)))
        
        # Construct a graph structure on A whose edges are difined by similarity relation.
        edges = {}
        
        for i in range(len(A)):
            
            # To remove repetitive words in A, we use the set unvisited. (****)
            if i not in unvisited:
                continue
                
            for j in range(i+1, len(A)):
                # Count the number of different (ordered) characters between A[i] and A[j].
                count = 0
                for ch_i, ch_j in zip(A[i], A[j]):
                    if ch_i != ch_j:
                        count += 1
                    if count > 2:
                        break
                        
                # If there are only two different charaters, they are similar.
                if count == 2:
                    # The similarity relation is symmetric.
                    edges.setdefault(i, list()).append(j)
                    edges.setdefault(j, list()).append(i)
                # If they are exactly same, remove the node j(>i) from the set unvisited. (****)   
                if count == 0:
                    unvisited.remove(j)
                    
        # Count connected components in the above graph.
        n_components = 0      
        ##############################################################################################
        def visit(i):
            '''
            Visit every nodes connected to i with updating the set unvisited.
            '''
            unvisited.remove(i)
            
            # Recursively visit nodes connected to i.
            if i in edges.keys():
                for j in edges[i]:
                    if j in unvisited:
                        visit(j)
            return
        #############################################################################################
        
        for i in range(len(A)):
            # If we never visited the node i, visit every nodes connected to the node i.
            if i in unvisited:
                visit(i)    
                n_components += 1
        
        
        return n_components
