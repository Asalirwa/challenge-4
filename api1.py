
import click
import requests

# the apikey btained from newsapi.org/account
API_KEY = '5a7053e4e1ed494995f5605158a7eaa1'

@click.group()
def main():
        """
        API1  is a news app that returns/echos top 10 trending headlines from  any 4 newssources
        The news headline has a title, description and a url in case the user needs to follow up
        The user also needs to have a valid news api created from http://www.newsapi.org
        """
        pass

@main.command()

def listsources():
	""" Lists 4 sources from the API """
	main_url = " https://newsapi.org/v2/sources?apiKey=5a7053e4e1ed494995f5605158a7eaa1"

	# fetch data in json format 
	open_source = requests.get(main_url).json() 

	# get all articles in a string sources
	source = open_source["sources"] 

	# empty list which will 
	# contain all trending newssources 
	news_sources = [] 
	
	for s in source: 
                news_sources.append(s["id"])
            
   	
	for i in results[0:4]:
            print(i)	


@main.command()
def topheadlines():
          """ Please enter your choice from the listsources """
          newsSource = click.prompt("Please enter your choice from listsources")
    
          main_url = "https://newsapi.org/v2/top-headlines?apiKey=5a7053e4e1ed494995f5605158a7eaa1&sources="+newsSource

	# fetching data in json format 
          open_headline = requests.get(main_url).json() 

	# getting all headlines in a string articles 
          headline = open_headline["articles"] 

	# empty list which will 
	# contain all trending newssources 
          output = [] 
	
          for h in headline: 
                click.echo('\n')
                click.secho('TITLE: ' + h['title'], fg='red')
                click.secho((h['description']))
                click.secho('DOMAIN: ' + h['url'], fg='blue')
           
           	
          for i in output[:11]:
                print(i)


if __name__ == '__main__':
	main()