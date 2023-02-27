class Numbers:
    def __init__(self, numbers):
        self.numbers = numbers
    def average(self):
        return sum(self.numbers) / len(self.numbers)
    def max_count(self):
        from collections import Counter
        counter = Counter(self.numbers)
        max_common = counter.most_common(1)[0][1]
        numbers = [*filter(lambda  x: self.numbers.count(x) == max_common, self.numbers)]
        return sum(numbers) / len(numbers)

n = numbers(2,5,8,9,7,8,9,8,9,5,8)
print(n.average())