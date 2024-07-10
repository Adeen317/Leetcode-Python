class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count=0
        for i in range(len(logs)):
            if logs[i]=="../":
                if count>0:
                    count-=1
            elif logs[i]!="./":
                count+=1
        return count



        
