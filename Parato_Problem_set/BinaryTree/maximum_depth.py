class Solution(object):
    def maxDepth(self, root):
        node=[None,root]
        for i in node:
            if i:
                if i.left:
                    node.append(i.left)
                else:
                    node.append(None)
                if i.right:    
                    node.append(i.right)
                else:    
                    node.append(None)
        depth=0 
        skip=2  
        j=1   
        while j<len(node):
            if node[j]:
                depth+=1
                j=skip
                skip=skip*2
            else:
                j+=1         
        return depth