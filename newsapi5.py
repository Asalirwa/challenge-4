from newsapi import NewsApiClient

api = NewsApiClient(api_key='f8a01ffc38c9468281f52ab903905670')

headlines = api.get_top_headlines(sources='abc-news')["articles"][:10]
articles = ["title","description","url"]


#everything = api.get_everything(q='abc-news')

sources = api.get_sources()["sources"][:4]

print("Heads", headlines)
print ("art", articles)
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>1")
# print("every", everything)
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>2")
print("Soc", sources)
print("list" , sources) 

