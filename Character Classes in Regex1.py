import re
count = 0
Match = re.finditer('[^abc]','ab7aab@2aaa9ba0')
for match in Match:
    count+=1
    print("Start : {}  and  End : {}  and  Group : {}".format(match.start(),match.end(),match.group()))
print("The Number of Occurences: ", count)