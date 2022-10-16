import re
count = 0
Match_String = "Hey! this is Reguler Expresion Program"
Matcher = re.finditer('\S', Match_String)      # It will return matched string accept white space
print("\S Accept Space Characters")
for Match in Matcher:
    count +=1
    #print("\S Accept Space Characters")
    print("Start : {} , End : {} , Group : {}".format(Match.start(),Match.end(),Match.group()))
print('Number of occurencess: ',count)