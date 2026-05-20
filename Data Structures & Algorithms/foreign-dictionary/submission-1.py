class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indegree = {c: 0 for c in set("".join(words))}
        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]
            min_size = min(len(word1), len(word2))
            for j in range(min_size):
                c1, c2 = word1[j], word2[j]
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        indegree[c2] += 1
                    break
            else:
                if len(word1) > len(word2):
                    return ""

        res = []
        q = deque([c for c in indegree if indegree[c] == 0])
        while q:
            c = q.popleft()
            res.append(c)
            for next_c in graph[c]:
                indegree[next_c] -= 1
                if indegree[next_c] == 0:
                    q.append(next_c)
        return "".join(res) if len(res) == len(indegree) else ""