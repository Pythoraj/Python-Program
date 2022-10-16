import re
s = 'Open the command prompt "terminal" and type git version to verify Git was installed.'
Match = re.search(r'installed',s)
print('start index', Match.start())
print('End Index',Match.end())