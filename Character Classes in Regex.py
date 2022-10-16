import re
count = 0
Pattern = re.compile('[abc]')
Matcher = Pattern.finditer('abaabaaaba')
for match in Matcher:
    count+=1
    print('Start : {}   and   End: {}   and   Group : {}'.format(match.start(),match.end(),match.group()))
print('Number of occurences: ', count)