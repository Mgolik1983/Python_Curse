class Numbers:
    def __init__(self, *args):
        self.numbers = args
    def average(self):
        return sum(self.numbers) / len(self.numbers)
    def max_count(self):
        from collections import Counter
        counter = Counter(self.numbers)
        max_common = counter.most_common(1)[0][1]
        numbers = [*filter(lambda x: self.numbers.count(x) == max_common, self.numbers)]
        return sum(numbers) / len(numbers)


n = Numbers(2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 2, 2, 3, 3)
print(n.average())