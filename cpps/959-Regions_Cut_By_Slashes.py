'''
In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \, or blank space.
These characters divide the square into contiguous regions.
(Note that backslash characters are escaped, so a \ is represented as "\\".)
Return the number of regions.

Note:
1 <= grid.length == grid[0].length <= 30
grid[i][j] is either '/', '\', or ' '.
'''

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        ''' time/space complexity : O(N^2 ?)/ O(N^2) '''
        # List of all nodes
        nodes = []
        # List of edges
        graph = []
        
        # Construct graphs from grid        
        for i, row in enumerate(grid):
            prev_ch = None
            for j, ch in enumerate(row):
                # Append nodes.
                nodes.append((i,j,0))
                if ch in ['\\','/']:
                    nodes.append((i,j,1))
                # Append horizontal edges.
                if not prev_ch:
                    pass
                elif prev_ch in ['\\','/']:
                    graph.append({(i, j-1, 1), (i, j, 0)})
                else:
                    graph.append({(i, j-1, 0), (i, j, 0)})
                
                # Update prev_ch before going to the next column.
                prev_ch = ch
                # If i=0, go to the next column.
                if i == 0:
                    continue
                # If i > 0, construct vertical edges connecting elements in the previous row.
                if prev_row[j] == '/':
                    if ch == '\\':
                        graph.append({(i-1, j, 1), (i, j, 1)})
                    else:
                        graph.append({(i-1, j, 1), (i, j, 0)})
                else:
                    if ch == '\\':
                        graph.append({(i-1, j, 0), (i, j, 1)})
                    else:
                        graph.append({(i-1, j, 0), (i, j, 0)})
            # Update prev_row before going to the next row.
            prev_row = row
                    
        unvisited = set(nodes)
        
        def tra_del(v):
            '''
            Recursively traverses nodes connected to v, removing the node from the set "unvisited".
            '''
            if v not in unvisited:
                return
            unvisited.remove(v)
            for edge in graph:
                if v in edge:
                    while True:
                        w = edge.pop()
                        if w != v:
                            break
                    if w in unvisited:
                        tra_del(w)
            return
        
        # Count the number of connected components.
        n_comp = 0
        for v in nodes:
            if v in unvisited:
                tra_del(v)
                n_comp += 1
            # If we visit every nodes, escape from the loop.
            if not unvisited:
                break
                
        return n_comp
