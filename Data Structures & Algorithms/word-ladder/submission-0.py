class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        q = deque([(beginWord, 1)])
        visited = {beginWord}
        while q:
            word, length = q.popleft()
            if word == endWord:
                return length
            word_list = list(word)
            for i in range(len(word_list)):
                tmp = word_list[i]
                for char in "abcdefghijklmnopqrstuvwxyz":
                    if char == tmp:
                        continue
                    word_list[i] = char
                    next_word = "".join(word_list)
                    if next_word in word_set and next_word not in visited:
                        q.append((next_word, length+1))
                        visited.add(next_word)
                word_list[i] = tmp
        return 0
