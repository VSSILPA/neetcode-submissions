class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for op in operations:
            if op == '+':
                last = record.pop()
                last_last = record.pop()
                record.append(last_last)
                record.append(last)
                record.append(last_last + last)
            elif op == 'C':
                record.pop()
            elif op == 'D':
                prev_score = record.pop()
                record.append(prev_score)
                record.append(2*prev_score)
            else:
                record.append(int(op))
        print(record)
        return sum(record)
        