# import libraries
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
from bs4 import BeautifulSoup
import os


#------------------------------------------------

# To create DIR
def create_directory(directory):
    import os
    if not os.path.exists(directory):
        os.makedirs(directory)


#------------------------------------------------

# To download Files and save locally
def download_File(directory, url):
    # Open the url
    f = urllib2.urlopen(url)
    print("downloading " + url)

    # Open our local file for writing
    with open(directory+"/"+os.path.basename(url), "wb") as local_file:
        local_file.write(f.read())


#------------------------------------------------

# To extract link of all commit of a perticular REPO
def ExtractAllCommits(directory, quote_page):
    req = urllib2.Request(quote_page, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urllib2.urlopen(req)

    soup = BeautifulSoup(webpage, 'html.parser')


    for section in soup.findAll('a', attrs = {'class':'tooltipped-sw'}):
        repo_tree=section.get('href')
        print(repo_tree)
        zip_link = repo_tree.replace('/tree/','/archive/')
        link = "https://github.com" + zip_link + '.zip'
        print(link)
        download_File(directory, link)



#------------------------------------------------

#main
# specify the url
quote_page = 'https://github.com/search?l=Java&o=desc&p=1&q=Java+Maven&s=forks&type=Repositories'

# setting for accessing page
req = urllib2.Request(quote_page, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urllib2.urlopen(req)

soup = BeautifulSoup(webpage, 'html.parser')


# find all anchor tags
for section in soup.findAll('a', attrs = {'class':'v-align-middle'}):
    
    # find repo name
    repo_name=section.get_text(strip=True)

    # create folder with repo name
    create_directory(repo_name)

    print(repo_name)

    # Make link for all commits of master
    link = "https://github.com/" + repo_name + "/commits/master"
    print(link)

    ExtractAllCommits(repo_name, link)
    

