import re
count = 0
Match_String = "ab1aa@34baaa8ba9"
Matcher = re.finditer('\W', Match_String)      # Any Spacial Character accept word (Spacial character).
print("\W Any Spacial characters match in string accept word")
for Match in Matcher:
    count +=1
    #print("\W Accept Space Characters")
    print("Start : {} , End : {} , Group : {}".format(Match.start(),Match.end(),Match.group()))
print('Number of occurencess: ',count)