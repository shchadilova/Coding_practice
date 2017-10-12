import urllib.request
import urllib.parse

def read_text():
    quotes= open("/Users/yes/Documents/Learning/Programming/movie_quotes.txt")
    contents = quotes.read()
    #print(contents)
    profanity_check(contents)
    quotes.close()
    
def profanity_check(text_to_check):
    url_quote = urllib.parse.quote(text_to_check)
    response = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+url_quote)
    output = response.read()
    print(output)
    response.close()
    if output == b'true':
        print("This text is profanity checked.")
    elif output == b'false':
        print("This text contains curse words!")
    else:
        print("Couldn't read the document properly")

read_text()

#profanity_check("i have troubles")
