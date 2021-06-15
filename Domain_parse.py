'''
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
'''

# Test cases make this kata quite tricky. Had to use urlparse with a little addition of http:// to urls that start with something else, otherwise it has difficulty parsing.

def domain_name(url):
    from urllib.parse import urlparse

    if url[:4] != 'http':
        edit_domain = 'http://' + url   # See this if else statment. Adds the http(s):// if it isn't there which aids parsing. 
                                        # Then its a case of splitting on '.' and finding the root domain.
    else:
        edit_domain = url

    domain = urlparse(edit_domain).netloc
    domain_breakdown = domain.split('.')

    for element in domain_breakdown:
        if element != 'www':
            return element
