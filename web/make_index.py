import re
from collections import Counter
def reveal():
    with open('index_template.html') as it:
        s = Counter()
        for l in it.readlines():
            x = re.findall(r'#.{1,20}#',l)
            for a in x:
                s.update([a])

        print(s)

reveal()