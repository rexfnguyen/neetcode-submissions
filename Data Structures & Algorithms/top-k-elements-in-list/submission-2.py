class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
        ##counts = {1:1, 2:2, 3:3}

        #convert this to a list of tuple to sort data
        counts_tuple = []
        for x, y in counts.items():
            counts_tuple.append((x,y))
        ##counts_tuple = [(1:1), (2:2), (3:3)]

        #sort the tuple list based on frequency
        counts_tuple.sort(key = lambda x : x[1], reverse = True)
        ##counts_tuple = [(3:3), (2:2), (1:1)]

        result = []
        for i in range(k):
            result.append(counts_tuple[i][0])

        return result
