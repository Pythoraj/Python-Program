import re
count = 0
Match_String = "Hey! I am a Python Developer."
# Matcher = re.finditer(r'\s', Match_String)   # It will count only spaces from string
Matcher = re.finditer(r'[^I]\s', Match_String)  # It will only symbole alongwith space
for Match in Matcher:
    count += 1
    print('Start : {} , End : {} , Group : {} '.format(Match.start(), Match.end(), Match.group()))
print('Number of Occurences: ', count)