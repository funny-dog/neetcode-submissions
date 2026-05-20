class CountSquares:

    def __init__(self):
        self.point_cnt = Counter()

    def add(self, point: List[int]) -> None:
        self.point_cnt[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        x, y = point[0], point[1]
        for px, py in self.point_cnt:
            if px == x or py == y or abs(x-px) != abs(y-py):
                continue
            res += self.point_cnt[(px, py)] * self.point_cnt[(x, py)] * self.point_cnt[(px, y)]
        return res