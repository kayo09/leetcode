import heapq
from typing import List

class Solution:
    class Cell:
        def __init__(self, height, row, col):
            self.height = height
            self.row = row
            self.col = col
        def __lt__(self, other):
            return self.height < other.height

    def _is_valid_cell(self, row, col, num_of_rows, num_of_cols):
        return 0 <= row < num_of_rows and 0 <= col < num_of_cols

    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        d_row = [0, 0, -1, 1]
        d_col = [-1, 1, 0, 0]

        n_rows = len(heightMap)
        n_columns = len(heightMap[0])
        visited = [[False] * n_columns for _ in range(n_rows)]
        boundary = []

        # push left/right boundaries
        for i in range(n_rows):
            heapq.heappush(boundary, self.Cell(heightMap[i][0], i, 0))
            heapq.heappush(boundary, self.Cell(heightMap[i][n_columns-1], i, n_columns-1))
            visited[i][0] = visited[i][n_columns-1] = True

        # push top/bottom boundaries
        for j in range(n_columns):
            heapq.heappush(boundary, self.Cell(heightMap[0][j], 0, j))
            heapq.heappush(boundary, self.Cell(heightMap[n_rows-1][j], n_rows-1, j))
            visited[0][j] = visited[n_rows-1][j] = True

        total_water_volume = 0

        while boundary:
            current_cell = heapq.heappop(boundary)
            current_row, current_col = current_cell.row, current_cell.col
            min_boundary_height = current_cell.height

            for direction in range(4):
                neighbor_row = current_row + d_row[direction]
                neighbor_col = current_col + d_col[direction]

                if (self._is_valid_cell(neighbor_row, neighbor_col, n_rows, n_columns) 
                    and not visited[neighbor_row][neighbor_col]):

                    neighbor_height = heightMap[neighbor_row][neighbor_col]

                    if neighbor_height < min_boundary_height:
                        total_water_volume += (min_boundary_height - neighbor_height)

                    heapq.heappush(
                        boundary, 
                        self.Cell(max(neighbor_height, min_boundary_height), neighbor_row, neighbor_col)
                    )
                    visited[neighbor_row][neighbor_col] = True

        return total_water_volume


solution = Solution()
print(solution.trapRainWater([
    [1,4,3,1,3,2],
    [3,2,1,3,2,4],
    [2,3,3,2,3,1]
]))

