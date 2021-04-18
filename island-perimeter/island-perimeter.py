class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0

  # check if only one row exists?
  # if len(grid) == 1:
    

  # Iterate over cells in grid 
        for i in range(len(grid)):
            for j in range(len(grid[0])):



      # land
                if grid[i][j] == 1:
          # check top in 3 checks
            # TOP
                    if i -1 < 0 or grid[i-1][j] == 0:
                        perimeter += 1
            # check if top is water 
            # elif grid[i-1][j] == 0:
            #   perimeter +=1
            # check if top is land

            # BOTTOM
                    if i +1 == len(grid) or grid[i+1][j]==0:
                        perimeter += 1
                    # elif grid[i+1][j] == 0:
                    #   perimeter +=1

                    # LEFT
                    if j - 1 < 0 or grid[i][j-1] == 0:
                        perimeter += 1


                # RIGHT 
                    if j + 1 == len(grid[0]) or grid[i][j+1] == 0:
                        perimeter += 1


        return perimeter