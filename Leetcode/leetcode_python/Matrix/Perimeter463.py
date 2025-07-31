
def islandPerimeter(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    result=0
    for i in range(0,len(grid)):
        for j in range(len(grid[i])):
            count=0
            if grid[i][j]==1:
                if (j-1>=0 and grid[i][j-1]==0) or (j-1<0):
                    count+=1
                if (j+1<len(grid[i]) and grid[i][j+1]==0) or (j+1>=len(grid[i])):
                    count+=1
                if (i-1>=0 and grid[i-1][j]==0) or (i-1<0):
                    count+=1
                if (i+1<len(grid) and grid[i+1][j]==0) or (i+1>=len(grid)):
                    count+=1
            result+=count
    return result

test=[[1,0]]
print(islandPerimeter(test))