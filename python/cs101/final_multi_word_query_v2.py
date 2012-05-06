#Multi-word Queries

#Triple Gold Star

#For this question, your goal is to modify the search engine to be able to
#handle multi-word queries.  To do this, we need to make two main changes:

#    1. Modify the index to keep track of not only the URL, but the position
#    within that page where a word appears.

#    2. Make a version of the lookup procedure that takes a list of target
#    words, and only counts a URL as a match if it contains all of the target
#    words, adjacent to each other, in the order they are given in the input.

#For example, if the search input is "Monty Python", it should match a page that
#contains, "Monty Python is funny!", but should not match a page containing
#"Monty likes the Python programming language."  The words must appear in the
#same order, and the next word must start right after the end of the previous
#word.

#Modify the search engine code to support multi-word queries. Your modified code
#should define these two procedures:

#    crawl_web(seed) => index, graph
#        A modified version of crawl_web that produces an index that includes
#        positional information.  It is up to you to figure out how to represent
#        positions in your index and you can do this any way you want.  Whatever
#        index you produce is the one we will pass into your multi_lookup(index,
#        keyword) procedure.

#    multi_lookup(index, list of keywords) => list of URLs
#        A URL should be included in the output list, only if it contains all of
#        the keywords in the input list, next to each other.

#def adj(idx_list):
#    for i in range(1, len(idx_list)):
#        if idx_list[i] - idx_list[i-1] != 1:
#            return False
#    return True

def sect(list1, list2):
    sect = []
    for e in list1:
        if e in list2:
            sect.append(e)
    return sect
    
def find(needle, haystack):
    for hay in haystack:
        if needle == hay[0]: # only look into the url field
            return hay

def combine(res1, res2, urls):
    combo_res = []
    for u in urls:
        r1 = find(u, res1)
        r2 = find(u, res2)
        pos1 = r1[1]
        pos2 = r2[1]
        for p1 in pos1:
            if p1+1 in pos2:
                if u not in [col[0] for col in combo_res]:
                    combo_res.append([u, [p1]])
                else:
                    find(u, combo_res)[1] += [p1] # add the pos of the word in front, for recursive compares
    return combo_res
            

# aggregate common urls
# check if among the urls, there are correctly ordered keywords
def aggregate(res1, res2):
    is_adj = False
    url1 = [col[0] for col in res1]
    url2 = [col[0] for col in res2]
    
    common_urls = sect(url1, url2)
    combo_res = combine(res1, res2, common_urls)
    return combo_res

        
def chain_lookup(index, query):
    res = []
    if len(query) == 1:
        return lookup(index, query[0])
    else:
        q = query.pop(0)
        res = lookup(index, q)
        next_res = chain_lookup(index, query)
        aggr_res = aggregate(res, next_res)
        return [col[0] for col in aggr_res]
        
            
def multi_lookup(index, query):
    res = []
    res_m = {}
    if len(query) == 1:
        res = lookup(index, query[0])
        return [col[0] for col in res] # strip away the index
    else:
        res = chain_lookup(index, query)
    return res
   


def crawl_web(seed): # returns index, graph of inlinks
    tocrawl = [seed]
    crawled = []
    graph = {}  # <url>, [list of pages it links to]
    index = {} 
    while tocrawl: 
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            outlinks = get_all_links(content)
            graph[page] = outlinks
            union(tocrawl, outlinks)
            crawled.append(page)
    return index, graph


def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)

def add_page_to_index(index, url, content):
    words = content.split() # the split can be improved
    words_idx = {}
    for i in range(len(words)):
        if words[i] not in words_idx:
            words_idx[words[i]] = [i]
        else:
            words_idx[words[i]].append(i)
    for word in words:
        add_to_index(index, word, [url, words_idx[word]])
        
def add_to_index(index, keyword, url):
    if keyword in index:
        if url not in index[keyword]:
            index[keyword].append(url)
    else:
        index[keyword] = [url]

def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return []
    



cache = {
   'http://www.udacity.com/cs101x/final/multi.html': """<html>
<body>

<a href="http://www.udacity.com/cs101x/final/a.html">A</a><br>
<a href="http://www.udacity.com/cs101x/final/b.html">B</a><br>

</body>
""", 
   'http://www.udacity.com/cs101x/final/b.html': """<html>
<body>

Monty likes the Python programming language
Thomas Jefferson founded the University of Virginia
When Mandela was in London, he visited Nelson's Column.

</body>
</html>
""", 
   'http://www.udacity.com/cs101x/final/a.html': """<html>
<body>

Monty Python is not about a programming language
Udacity was not founded by Thomas Jefferson
Nelson Mandela said "Education is the most powerful weapon which you can
use to change the world."
</body>
</html>
""", 
}

def get_page(url):
    if url in cache:
        return cache[url]
    else:
        print "Page not in cache: " + url
        return None

#Here are a few examples from the test site:

index, graph = crawl_web('http://www.udacity.com/cs101x/final/multi.html')
#print index
#print multi_lookup(index, ['Python'])
#>>> ['http://www.udacity.com/cs101x/final/b.html', 'http://www.udacity.com/cs101x/final/a.html']

print multi_lookup(index, ['Monty', 'Python'])
#>>> ['http://www.udacity.com/cs101x/final/a.html']

#print multi_lookup(index, ['Python', 'programming', 'language'])
#>>> ['http://www.udacity.com/cs101x/final/b.html']

#print multi_lookup(index, ['Thomas', 'Jefferson'])
#>>> ['http://www.udacity.com/cs101x/final/b.html', 'http://www.udacity.com/cs101x/final/a.html']

#print multi_lookup(index, ['most', 'powerful', 'weapon'])
#>>> ['http://www.udacity.com/cs101x/final/a.html']

#print multi_lookup(index, ['the'])