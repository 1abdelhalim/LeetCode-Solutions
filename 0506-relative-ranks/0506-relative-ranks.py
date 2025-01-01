class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Sort the scores desciding 
        # We can use enumerate + 1 
        # (idx, score) (0,5)
        sorted_arr = sorted(enumerate(score),key=lambda x:x[1], reverse=True)
        n = len(score)
        answer = [""] * n  

        for rank, (i,val) in enumerate(sorted_arr):
            if rank == 0:
                answer[i] = "Gold Medal"

            elif rank == 1:
                answer[i] = "Silver Medal"
            
            elif rank == 2:
                answer[i] = "Bronze Medal"

            else:
                answer[i] = str(rank +1)


        return answer 
