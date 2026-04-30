class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for op in operations:
            if op == '+':
                if len(record) >= 2:
                    new = int(record[- 1]) + int(record[-2])
                    record.append(new)
            elif op == 'C':
                if len(record) >= 1:
                    record.pop()
            elif op == 'D':
                if len(record) >= 1:
                    new = 2 * int(record[-1])
                    record.append(new)
            else:
                record.append(int(op))
        return sum(record)

        