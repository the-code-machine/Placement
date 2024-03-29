class Solution(object):
    def findMatrix(self, nums):
        count= defaultdict(int)
        res=[]
        for n in nums:
            row=count[n]
            if len(res)==row:
                res.append([])
            res[row].append(n)
            count[n]+=1
        return res
