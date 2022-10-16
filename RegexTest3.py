import re
count = 0
Pattern = re.compile('ab')
Matcher = Pattern.finditer('abaababa')

for match in Matcher:
    count+=1
    print('Start Index: {} and End Index: {} and Group: {}'.format(match.start(),match.end(),match.group()))

print("The Number of occurences : ", count)