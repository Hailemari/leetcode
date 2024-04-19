# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequency = Counter(words)
        heap = []
        heapify(heap)

        def word_to_num(word):
            word = list(word)
            word += ["a"] * (10 - len(word))

            total = 0
            j = 1
            for i in range(len(word) - 1, -1, -1):
                total += j * (26 ** j) * (ord(word[i]) - 97)
                j += 1
            
            return total
        

        
        for key, val in frequency.items():
            heappush(heap, (val, -word_to_num(key), -len(key), key))
            if len(heap) > k:
                heappop(heap)
        
        ans = []
        while heap:
            ans.append(heappop(heap)[3])
    
        return ans[::-1]
