class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counts number of appearance for each n
        counts = {}
        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
        
        # convert counts to a list of tuple to sort later
        my_list = []
        for num, count in counts.items():
            my_list.append((num, count))
        
        #sort based on number of count, highest ones go in front
        my_list.sort(key = lambda x : x[1], reverse = True)

        result = []
        for i in range(k):
            result.append(my_list[i][0])
        
        return result
