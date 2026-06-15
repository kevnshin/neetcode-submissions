class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # approaches:
            # 1. bfs, go through everything, check if it's part of an island
            # 2. dfs, explore a node, if it's 0, do nothing, if it's 1, check if already explored, if not, go all the way until no more 1's while marking explored one, return the furthest row, col combo already explored to start at
        already_explored:Set[Tuple[int, int]] = set()
        island_count: int = 0

        for r, row_list in enumerate(grid):
            for c, value in enumerate(row_list):
                island_count += self.dfs(grid, r, c, already_explored)
        
        return island_count
                

    def dfs(self, grid: List[List[str]], r: int, c: int, already_explored:Set[Tuple[int, int]]):
        if (r, c) in already_explored:
            return 0
        
        current_value: int = grid[r][c]

        if current_value == "0":

            already_explored.add((r, c))
            return 0
        else:
            already_explored.add((r, c))
            
            # explore above
            if r > 0:
                self.dfs(grid, r - 1, c, already_explored)
            # explore below
            if r < len(grid) - 1:
                self.dfs(grid, r + 1, c, already_explored)
            # explore left
            if c > 0:
                self.dfs(grid, r, c - 1, already_explored)
            # explore right
            if c < len(grid[r]) - 1:
                self.dfs(grid, r, c + 1, already_explored)
            return 1



        