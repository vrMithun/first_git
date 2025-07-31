def matrixReshape(mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        result=[]
        mat=flat(mat)
        if len(mat)==r*c:
            for _ in range(r):
                empty_list=[]
                for j in range(c):
                    val=mat.pop(0)
                    empty_list.append(val)
                result.append(empty_list)
            return result
        else:
            return mat
def flat(mat):
    result=[]
    if type(mat[0])==list:
        for i in mat:
             for j in i:
                  result.append(j)
    return result

mat=[[1,2],[3,4]]
print(matrixReshape(mat,2,2))
''' Alternate method
def matrixReshape(mat, r, c):
    flat = [num for row in mat for num in row]
    
    if len(flat) != r * c:
        return mat

    return [flat[i*c:(i+1)*c] for i in range(r)]

# Test
mat = [[1, 2], [3, 4]]
print(matrixReshape(mat, 2, 2))
'''