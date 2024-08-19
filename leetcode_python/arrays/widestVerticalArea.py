class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        x_points=[]
        for i in range(len(points)):
            x_points.append(points[i][0])
        width=0
        x_points.sort()
        for j in range(len(x_points)-1):
            if width<abs(x_points[j]-x_points[j+1]):
                width=abs(x_points[j]-x_points[j+1])
        return width        
        