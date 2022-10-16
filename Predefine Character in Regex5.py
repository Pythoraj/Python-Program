import re
count = 0
Match_String = "ab1aa@34baaa8ba9"
Matcher = re.finditer('\w', Match_String)      # It will return matched CHARACTER (Alphanumeric Character like [a-z A-Z 0-9]).
print("\W Any word characters match in string")
for Match in Matcher:
    count +=1
    #print("\S Accept Space Characters")
    print("Start : {} , End : {} , Group : {}".format(Match.start(),Match.end(),Match.group()))
print('Number of occurencess: ',count)