def merge(intervals):
    intervals.sort(key=lambda x:x[0])
    i=0
    while i<len(intervals)-1:
        if intervals[i][1]>=intervals[i+1][0]:
            intervals[i:i+2]=[[intervals[i][0],max(intervals[i+1][1],intervals[i][1])]]
            continue
        i+=1
    return intervals


intervals = [[1,4],[0,2],[3,5]]
print(merge(intervals))