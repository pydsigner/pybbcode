from pybbcode import *


tag_set = default_set()
tag_set.add_tag(*extras['css'])

print(tag_set.parse_with_ignore('''
[i][b][u]Hello?[/u][/b][/i]
[css="[i][/i]"]Stuff inside the tags themselves is not immune to parsing![/css]
[ignore]
    [i]This would be italic.[/i]
[/ignore]
[url="http://github.com/pydsigner/pybbcode"]PyBBCode[/url]
[big][url]http://www.python.org[/url][/bigg]
[size=50][css="elaborate"]Power of PyBBCode[/css][/size]
[list][*]Cool[/list]
[list=]
    [*]Cooler
    [*]Coolest
[/list]
[code]
import pybbcode
[/code]'''))
