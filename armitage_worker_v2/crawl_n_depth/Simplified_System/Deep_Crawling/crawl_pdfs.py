import json

import requests, PyPDF2


# url = 'https://www.atsb.gov.au/media/29959/b20050205.pdf'
# response = requests.get(url)
# my_raw_data = response.content
#
# with open("my_pdf.pdf", 'wb') as my_data:
#     my_data.write(my_raw_data)
#
# pdfFileObject = open('my_pdf.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
# count = pdfReader.numPages
# for i in range(count):
#     page = pdfReader.getPage(i)
#     print(page.extractText())

import os
import pandas as pd
root_path = r"C:\ethics_project\armitage_worker_v2\crawl_n_depth\Simplified_System\Deep_Crawling\links\\"
files_list = os.listdir(root_path)
for f in files_list[2:]:
    inpu_path = os.path.join(root_path,f)
    out_path_dir = os.path.join(r"C:\ethics_project\armitage_worker_v2\crawl_n_depth\Simplified_System\Deep_Crawling\deep_crawls\\",f[:-4])
    out_path_dir = os.path.join( out_path_dir, 'pdfs')
    if not os.path.exists(out_path_dir):
        os.makedirs(out_path_dir)
    df = pd.read_csv(inpu_path)
    # links_list_a = []
    # out_names_list = []
    for kk,row in df.iterrows():
        # print(row['title'])
        s = row['title']
        import string


        for char in string.punctuation:
            s = s.replace(char, ' ')
        out_name = os.path.join(out_path_dir, "no_"+str(kk)+"_"+s)
        link_name = row['link']
        print(link_name)
        if(link_name[-4:]=='.pdf'):
            try:
                url = link_name
                response = requests.get(url)
                my_raw_data = response.content

                with open("my_pdf.pdf", 'wb') as my_data:
                    my_data.write(my_raw_data)

                pdfFileObject = open('my_pdf.pdf', 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFileObject)

                count = pdfReader.numPages
                pdf_text_dict = {}
                for i in range(count):
                    page = pdfReader.getPage(i)
                    # print(page.extractText())
                    pdf_text_dict[i] = page.extractText()
                print(pdf_text_dict)
                with open(out_name+'_data.json', 'w') as fp:
                    json.dump(pdf_text_dict, fp)

            except Exception:
                continue

