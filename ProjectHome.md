pygoogle is a **very basic** Google search module for Python.
It has a limitation of only 64 results. If you want more results, see [xgoogle](http://www.catonmat.net/blog/python-library-for-google-translate/)

## Pages ##
Google's Search API returns 4 or 8 results per 'page'. So, if you want 40 results, you will need to request 4x10pages or 8x5pages.
pygoogle uses 8 results per page (default, use rsz to change this to 4).

## Examples ##

### Get URLs from the first 5 result pages ###
```
from pygoogle import pygoogle
g = pygoogle('quake 3 arena')
g.pages = 5
print '*Found %s results*'%(g.get_result_count())
g.get_urls()
```

### Use at command line ###
you can use pygoogle at command line:
```
python pygoogle.py quake 3 arena
```

will show about 10 results (truncated):
```
*Found 4540000 results*
[id Software: Quake III Arena]
Welcome to the Arena, where high-ranking warriors are transformed into spineless   mush. Abandoning every ounce of common sense and any trace of doubt,
http://www.idsoftware.com/games/quake/quake3-arena/

[id Software]
the PLAYSTATION®3 computer entertainment system and PC. ... DOOM, QUAKE and   Enemy Territory have become staples of popular culture for generations of
http://www.idsoftware.com/

[Quake III Arena - Wikipedia, the free encyclopedia]
Quake III Arena (also known as Quake 3; abbreviated as Q3A or Q3), is a   multiplayer first-person shooter computer and video game released on December 2,
http://en.wikipedia.org/wiki/Quake_III_Arena
```

### Notes ###
| **method** | **return** |
|:-----------|:-----------|
| search()   | returns a dict of Title/URLs |
| get\_urls() |returns list of result URLs |
| get\_result\_count() | returns the number of results |
| display\_results()|  prints results (for command line) |

## Installation ##
  * svn checkout http://pygoogle.googlecode.com/svn/trunk/ pygoogle-read-only
  * python setup.py build
  * sudo python setup.py install