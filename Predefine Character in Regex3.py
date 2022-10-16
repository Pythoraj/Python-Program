import re
count = 0
Match_String = "ab1aa@34baaa8ba9"
Matcher = re.finditer('\d', Match_String)      # It will return matched digit only
print("\d [0-9] Any digit")
for Match in Matcher:
    count +=1
    #print("\S Accept Space Characters")
    print("Start : {} , End : {} , Group : {}".format(Match.start(),Match.end(),Match.group()))
print('Number of occurencess: ',count)