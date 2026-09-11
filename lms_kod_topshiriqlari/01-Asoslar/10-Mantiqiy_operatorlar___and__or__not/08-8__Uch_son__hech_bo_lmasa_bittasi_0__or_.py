# a, b, c (bitta qatorda)
# Hech bo'lmasa bittasi 0 bo'lsa True, aks holda False.
# (a==0 or b==0 or c==0)
a, b, c = map(int, input().split())
print(a == 0 or b == 0 or c == 0)