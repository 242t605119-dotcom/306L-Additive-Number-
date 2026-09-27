class Solution:
    def isAdditiveNumber(self, num):
        n = len(num)

        def check(a, b, start):
            while start < n:
                total = a + b
                s = str(total)

                if not num.startswith(s, start):
                    return False

                start += len(s)
                a, b = b, total

            return True

        for i in range(1, n):
            if num[0] == '0' and i > 1:
                break

            a = int(num[:i])

            for j in range(i + 1, n):
                if num[i] == '0' and j - i > 1:
                    break

                b = int(num[i:j])

                if check(a, b, j):
                    return True

        return False
