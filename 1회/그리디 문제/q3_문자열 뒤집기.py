# 답지 풀이
s = input()
cnt0, cnt1 = 0, 0

if s[0] == '0':
  cnt1 += 1
else:
  cnt0 += 1

for i in range(1, len(s)):
  if s[i-1] != s[i]:
    if s[i] == '1':
      cnt0 += 1
    else:
      cnt1 += 1
      
print(min(cnt0, cnt1))
