from pybbcode import *


tag_set = default_set()
tag_set.add_tag(*extras['css'])

print(tag_set.parse_with_ignore('''
[i][b][u]Hello?[/u][/b][/i]
[css="[i][/i]"][/css]
[ignore]
    [i]This would be italic.[/i]
[/ignore]
[url="http://www.google.com"]Google[/url]
[big][url]http://www.python.org[/url][/bigg]
[size=50][css="elaborate"]Power of PyBBCode[/css][/size]'''))
