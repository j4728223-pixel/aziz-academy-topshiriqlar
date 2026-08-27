# a, b, c, d (bitta qatorda)
# result = (a + b*2) - (c//2) + (d%3)
# "Result: <result>" chiqarilsin.
a, b, c, d = map(int, input().split())
result = (a + b *2) - (c // 2) + (d % 3)
print(f"Result: {result}")