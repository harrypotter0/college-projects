import bs4
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(),"html.parser")
elems = exampleSoup.select('a')

print(elems)
