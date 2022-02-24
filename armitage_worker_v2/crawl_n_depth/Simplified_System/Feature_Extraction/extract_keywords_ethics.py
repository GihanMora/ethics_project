import os
import pandas as pd
import json

from armitage_worker_v2.crawl_n_depth.key_phrase_extractors.wordnet import get_wc_results

# root = r"C:\ethics_project\armitage_worker_v2\crawl_n_depth\Simplified_System\Deep_Crawling\deep_crawls\\"
# dir_list = os.listdir(root)
#
# print(dir_list)
#
# for ff in dir_list[1:]:
#     full_path = os.path.join(root,ff)
#     json_list = os.listdir(full_path)
#     res = {}
#     k=0
#     file_names = []
#     bi_grams = []
#     tri_grams = []
#     for s in json_list:
#         k=k+1
#         if(s[-5:]=='.json'):
#             with open(os.path.join(full_path,s), 'r') as f:
#                 data = json.load(f)
#                 print(data.keys())
#                 para = (' ').join(data['paragraph_text'])
#                 # text_all+=para
#                 file_names.append(s)
#                 bi_grams.append(get_wc_results([para],'bi')[:50])
#                 tri_grams.append(get_wc_results([para],'tri')[:50])
#         # if(k==5):break
#
#     res['file_names'] = file_names
#     res['bi_grams'] = bi_grams
#     res['tri_grams'] = tri_grams
#
#     out_path_dir = r"C:\ethics_project\armitage_worker_v2\crawl_n_depth\Simplified_System\Deep_Crawling\keywords\\"+str(ff)+"\\"
#     if not os.path.exists(out_path_dir):
#         os.makedirs(out_path_dir)
#     df = pd.DataFrame(res)
#     df.to_csv(os.path.join(out_path_dir,"web_results.csv"))
#
#     print(res)

root = r"C:\ethics_project\armitage_worker_v2\crawl_n_depth\Simplified_System\Deep_Crawling\deep_crawls\\"
dir_list = os.listdir(root)

print(dir_list)

for ff in dir_list:
    full_path = os.path.join(root,ff)
    full_path = os.path.join(full_path, 'pdfs')
    json_list = os.listdir(full_path)
    res = {}
    k=0
    file_names = []
    bi_grams = []
    tri_grams = []
    for s in json_list:
        k=k+1
        if(s[-5:]=='.json'):
            with open(os.path.join(full_path,s), 'r') as f:
                data = json.load(f)
                all_text = []
                print(data.keys())
                for dk in data.keys():
                    all_text.append(data[dk])
                print(all_text)
                para = (' ').join(all_text)
                # print(all_text)

    #             para = (' ').join(data['paragraph_text'])
    #             # text_all+=para
                file_names.append(s)
                bi_grams.append(get_wc_results([para],'bi')[:50])
                tri_grams.append(get_wc_results([para],'tri')[:50])
        # if(k==5):break
    #
    res['file_names'] = file_names
    res['bi_grams'] = bi_grams
    res['tri_grams'] = tri_grams

    out_path_dir = r"C:\ethics_project\armitage_worker_v2\crawl_n_depth\Simplified_System\Deep_Crawling\keywords\\"+str(ff)+"\\"
    if not os.path.exists(out_path_dir):
        os.makedirs(out_path_dir)
    df = pd.DataFrame(res)
    df.to_csv(os.path.join(out_path_dir,"pdf_results.csv"))

    print(res)

    # break