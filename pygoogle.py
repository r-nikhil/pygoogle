#!/usr/bin/python
"""
Google AJAX Search Module
http://code.google.com/apis/ajaxsearch/documentation/reference.html
"""
try:
    import simplejson as json
except:
    import json
import urllib

__author__ = "Kiran Bandla"
__version__ = "0.1"
URL = 'http://ajax.googleapis.com/ajax/services/search/web?'

#Web Search Specific Arguments
#http://code.google.com/apis/ajaxsearch/documentation/reference.html#_fonje_web
#SAFE,FILTER
"""
SAFE
This optional argument supplies the search safety level which may be one of:
    * safe=active - enables the highest level of safe search filtering
    * safe=moderate - enables moderate safe search filtering (default)
    * safe=off - disables safe search filtering
"""
SAFE_ACTIVE     = "active"
SAFE_MODERATE   = "moderate"
SAFE_OFF        = "off"

"""
FILTER
This optional argument controls turning on or off the duplicate content filter:

    * filter=0 - Turns off the duplicate content filter
    * filter=1 - Turns on the duplicate content filter (default)

"""
FILTER_OFF  = 0
FILTER_ON   = 1

#Standard URL Arguments
#http://code.google.com/apis/ajaxsearch/documentation/reference.html#_fonje_args
"""
RSZ
This optional argument supplies the number of results that the application would like to recieve. 
A value of small indicates a small result set size or 4 results. 
A value of large indicates a large result set or 8 results. If this argument is not supplied, a value of small is assumed. 
"""
RSZ_SMALL = "small"
RSZ_LARGE = "large"


class pygoogle:
    
    def __init__(self,query,pages=10):
        self.pages = pages          #Number of pages. default 10
        self.query = query
        self.filter = 1             #Controls turning on or off the duplicate content filter. On = 1.
        self.rsz = 'large'          #Results per page. small = 4 /large = 8
        self.safe = 'off'           #SafeBrowsing -  active/moderate/off
        
    def __search__(self,print_results = False):
        results = []
        for page in range(0,self.pages):
            args = {'q' : self.query,
                    'v' : '1.0',
                    'start' : page,
                    'rsz': RSZ_LARGE,
                    'safe' : SAFE_OFF, 
                    'filter' : FILTER_ON,    
                    }
            q = urllib.urlencode(args)
            search_results = urllib.urlopen(URL+q)
            data = json.loads(search_results.read())
            if print_results:
                for result in  data['responseData']['results']:
                    #print result
                    if result:
                        print '[%s]'%(urllib.unquote(result['titleNoFormatting']))
                        print result['content'].strip("<b>...</b>").replace("<b>",'').replace("</b>",'').replace("&#39;","'").strip()
                        print urllib.unquote(result['unescapedUrl'])+'\n'                
            results.append(data)
        return results
    
    def search(self):
        """Returns a dict of Title/URLs"""
        results = {}
        for data in self.__search__():
            for result in  data['responseData']['results']:
                if result:
                    title = urllib.unquote(result['titleNoFormatting'])
                    results[title] = urllib.unquote(result['unescapedUrl'])
        return results
    
    def get_urls(self):
        """Returns list of result URLs"""
        results = []
        for data in self.__search__():
            for result in  data['responseData']['results']:
                if result:
                    results.append(urllib.unquote(result['unescapedUrl']))
        return results

    def get_result_count(self):
        """Returns the number of results"""
        temp = self.pages
        self.pages = 1
        return self.__search__()[0]['responseData']['cursor']['estimatedResultCount']
        self.pages = temp
        
    def display_results(self):
        """Prints results (for command line)"""
        self.__search__(True)

    
if __name__ == "__main__":
    import sys
    query = ' '.join(sys.argv[1:])
    #print pygoogle(' '.join(sys.argv[1:])).display_results()
    g = pygoogle(query)
    print '*Found %s results*'%(g.get_result_count())
    g.pages = 1
    g.display_results()
