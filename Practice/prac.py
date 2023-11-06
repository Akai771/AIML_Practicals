import math

def minMax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    if(curDepth == targetDepth):
        return scores[nodeIndex]
    
    if (maxTurn):
        return max (minMax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),
                    minMax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth))
    else:
        return min (minMax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth),
                    minMax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth))
    
scores = [3,5,2,9,12,5,23,23]
treeDepth = math.log(len(scores), 2)

print("optimal score : ", end="")
print(minMax(0,0,True,scores, treeDepth))