#make sure chrome driver's executable path is correct
#make sure gecko driver's executable path is correct(optional)
#fix sys path if you want to run this seperately
import time
import sys

from selenium.common.exceptions import WebDriverException

from os.path import dirname as up
three_up = up(up(up(__file__)))
sys.path.insert(0, three_up)


#Requests Users


# print(result)
import requests
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
from bs4.element import Tag
# from fake_useragent import UserAgent
from random import choice

def proxy_generator():
    response = requests.get("https://sslproxies.org/")
    soup = BeautifulSoup(response.content, 'html5lib')
    proxy = {'https': choice(list(map(lambda x:x[0]+':'+x[1], list(zip(map(lambda x:x.text,
	   soup.findAll('td')[::8]), map(lambda x:x.text, soup.findAll('td')[1::8]))))))}
    return proxy

def use_chrome():
    # ua = UserAgent()
    # userAgent = ua.random #get a random user agent
    options = webdriver.ChromeOptions()  # use headless version of chrome to avoid getting blocked
    options.add_argument('headless')
    # options.add_argument(f'user-agent={userAgent}')
    options.add_argument('--no-sandbox')
    # options.add_argument("start-maximized")# // open Browser in maximized mode
    # options.add_argument("disable-infobars")# // disabling infobars
    # options.add_argument("--disable-extensions")# // disabling extensions
    # options.add_argument("--disable-gpu")# // applicable to windows os only
    # options.add_argument("--disable-dev-shm-usage")# // overcome limited resource problems

    browser = webdriver.Chrome(chrome_options=options,  # give the path to selenium executable
                               # executable_path='F://Armitage_lead_generation_project//chromedriver.exe'
                               executable_path=three_up+'//utilities//chromedriver.exe',
                               )
    return browser

def use_firefox():
    profile = webdriver.FirefoxProfile()
    # profile.set_preference("browser.privatebrowsing.autostart", True)
    proxies = ['54.213.66.208', "43.250.242.251", "192.248.15.153"
               ]
    prx = choice(proxies)
    print(prx)
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.http", prx)
    profile.set_preference("network.proxy.http_port", 80)
    options = Options()
    options.headless = True

    profile.update_preferences()
    browser = webdriver.Firefox(firefox_options=options, firefox_profile=profile,
                                executable_path=three_up+'utilities/geckodriver')
    return browser

def getGoogleLinksForSearchText(searchText,number_of_results,mode):#given a search query get first n results from google
    """

    :param searchText: query text of searching
    :param number_of_results: how many results required
    :return: save resulted links to csv along with title and description
    """
    print("searching on google",searchText)

    #buildingsearch query
    searchGoogle = URL = f"https://google.com/search?q={searchText}"+"&num=" + str(number_of_results)+"&cr=countryAU"

    try:

        #our scraper
        browser = use_chrome()#get a chrome instance
        browser.get(searchGoogle)
        time.sleep(5)
        pageSource = browser.page_source
        # print(pageSource)
        browser.quit()

        soup = BeautifulSoup(pageSource, 'html.parser')#bs4
        is_captcha_on_page = soup.find("div", id="recaptcha") is not None

        # if(is_captcha_on_page):#a captcha triggered
        #     return 'captcha'
        count = 0
        while (is_captcha_on_page):
            count = count + 1
            print("captch is detected " + str(count) + " times")
            print("waiting more time", count * 120)
            time.sleep(count * 120)
            browser = use_chrome()#get a chrome instance
            browser.get(searchGoogle)

            pageSource = browser.page_source
            time.sleep(5)
            browser.quit()
            soup = BeautifulSoup(pageSource, 'html.parser')#bs4
            is_captcha_on_page = soup.find("div", id="recaptcha") is not None


        #scraper_API
        # from scraper_api import ScraperAPIClient
        # client = ScraperAPIClient('e2bae63a5eb1be4d95ef7d341f5a58cb')
        # # client = ScraperAPIClient('8dc0cf0ed602333134489444b9ea19cd')
        # pageSource = client.get(url=searchGoogle, render=True).text
        # soup = BeautifulSoup(pageSource, 'html.parser')  # bs4






        results = []
        result_div = soup.find_all('div', attrs={'class': 'g'})
        print('len_res',len(result_div))
        # print(result_div)
        for r in result_div:
            # print('vvv',r)
            # Checks if each element is present, else, raise exception
            try:
                link = r.find('a', href=True)['href']#extracting the link
                print('link',link)
                title = None
                title = r.find('h3')

                if isinstance(title,Tag):#extracting the title of the link
                    title = title.get_text()
                print('title', title)
                description = None
                description = r.find('div', attrs={'class': 'VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf'})#extracting the description
                if(description==None):#VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf
                    description = r.find('div', attrs={'class' :'LGOjhe'})
                # print('ddd',description)
                if isinstance(description, Tag):
                    description = description.get_text()
                print('des',description)
                # Check to make sure everything is present before appending
                if (True):  # remove links if information is not available
                # if (link not in ['',None]) and (title not in ['',None]) and (description not in ['',None]):#remove links if information is not available
                    rich_description = []
                    if(mode=='initial'):
                        print("initial")

                        #our system
                        # browser = use_chrome()
                        # browser.get(link)
                        # time.sleep(5)
                        # pageSource = browser.page_source
                        # browser.quit()
                        # # browser.close()
                        # soup = BeautifulSoup(pageSource, 'html.parser')


                        #scraperAPI
                        pageSource = client.get(url=link, render=True).text
                        soup = BeautifulSoup(pageSource, 'html.parser')  # bs4






                        metas = soup.find_all('meta')
                        # print(metas)
                        meta_description = [meta.attrs['content'] for meta in metas if
                                            'name' in meta.attrs and meta.attrs['name'] == 'description']
                        og_description = [meta.attrs['content'] for meta in metas if
                                          'property' in meta.attrs and meta.attrs['property'] == 'og:description']
                        # twitter_description =  [meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == 'twitter:description']
                        if (meta_description != og_description):
                            rich_description = meta_description + og_description
                        else:
                            rich_description = meta_description

                        rich_description = '_'.join(rich_description)
                        rich_description = rich_description.replace(',',' ')
                        print('***',rich_description)

                    item = {
                        "search_text":searchText,
                        "title": title.replace(',','_'),
                        "link": link,
                        "description": description.replace(',',' '),
                        "rich_description":rich_description
                    }

                    # rich_descriptions = list(set(rich_descriptions))
                    # print(rich_descriptions)
                    # print(item)


                    # print("*************************************************")
                    results.append(item)



            # Next loop if one element is not present
            except Exception as e:
                print(e)
                continue

        # with open('first_n_results.csv', mode='w', encoding='utf8') as results_file:#store search results in to a csv file
        #     results_writer = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        #
        #     for each_item in results:
        #         results_writer.writerow([each_item['title'], each_item['link'], each_item['description']])
        #     results_file.close()
        print("got "+str(len(results))+" results")
        return results


    except WebDriverException as e:
        print("Browser Issue Occured!",e)
        return 'error'
    except Exception as e:
        print("Exception Occured!", e)
        return 'error'

#To run this scrpit individually use following line and run the script
# searchResults = getGoogleLinksForSearchText(text_to_search,number_of_results_required)
# for searchResult in searchResults:
#     print(searchResult)
keywords_ethics = ['Stakeholder engagement','Grievance mechanism','Independent monitoring','Covenants','Tax transparency','Barriers for entry to the sector' ,'actions that prevent competition','Customer privacy','data security','Quality management-customers and products','Abstain from improper involvement in local political activities','Incorporate governance considerations','Preventing environmental damage','Working with suppliers to improve environmental performance','Environmental assessment of suppliers','Environmentally sound technologies','Addressing climate change and transition to low-carbon economy','Adapting to climate change',',Operational eco-efficiency','Biodiversity','Environmental reporting','Incorporate environmental considerations','ethics','sustainability','sustainable']+['Human rights','Freedom of association','Human capital development','Occupational health and safety','Anti-forced labour exploitation','Anti-child labour exploitation','Social assessment of suppliers','Rights of Indigenous people','Anti-discrimination','Social reporting','Supply chain labour standards','Procurement practices disclosure','Encourage suppliers to apply principles of responsible business conduct','Increasing positive impacts to people','Creating shared prosperity for customers and clients','Incorporate social considerations into investment decisions, processes, policies, and practices','Anti-corruption','Anti-money laundering','Prompt payment of suppliers','Risk management','Supply chain management','Stakeholder engagement','Grievance mechanism','Independent monitoring','Covenants','Tax transparency','Barriers for entry to the sector and actions that prevent competition','Customer privacy','Information and data security','Quality management-customers products','Abstain from improper involvement in local political activities','Incorporate governance considerations into investment decisions, processes, policies, and practices','Preventing environmental damage','Working with suppliers to improve environmental performance','Environmental assessment of suppliers','Environmentally sound technologies','Addressing climate change and transition to low-carbon economy','Adapting to climate change','Operational eco-efficiency','Biodiversity','Environmental reporting','Incorporate environmental considerations into investment decisions, processes, policies, and practices']
keywords_ethics = list(set(keywords_ethics))
#example

comp_list = ['George Weston Foods',
             'BlueScope Steel',
             'Caltex',
             'Nestle',
             'Heinz',
             'Thales Australia',
             'Airbus',

             'Unilever Australia',
             'PepsiCo Australia and New Zealand',
             'Johnson and Johnson',]
import pandas as pd

# for c in comp_list[9:]:
#     dict_set = []
#     for k in keywords_ethics:
#         searchResults = getGoogleLinksForSearchText("%s australia %s"%(c,k),10,'normal')
#         # print(searchResults)
#         if(searchResults!='error'):
#             for searchResult in searchResults:
#                 print(searchResult)
#                 # print(type(searchResult))
#                 dict_set.append(searchResult)
#
#
#     try:
#         t = open(r"C:\ethics_project\armitage_worker_v2\crawl_n_depth\Simplified_System\Deep_Crawling\\"+str(c)+"_results.txt",'w+', encoding="utf-8")
#         t.write(str(dict_set))
#         t.close()
#         df = pd.DataFrame(dict_set)
#         df = df[['search_text','link','title','description']]
#         df.to_csv(r"C:\ethics_project\armitage_worker_v2\crawl_n_depth\Simplified_System\Deep_Crawling\\"+str(c)+"_results.csv")
#
#     except SyntaxError:
#         print('jhghjgj hfy yfhgj')
