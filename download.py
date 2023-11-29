import os
from bs4 import BeautifulSoup
import urllib

def download_images_from_html(html_file, begin_id):
    i = begin_id
    save_directory = 'DonaldTrump600'
    os.makedirs(save_directory, exist_ok=True)
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    img_tags = soup.find_all('img')
    for img_tag in img_tags:
        img_url = img_tag['src']
        if img_url.startswith('https://media.gettyimages.com/id'):
            if i < 10:
                img_name = "00" + str(i) + ".png"
            elif i < 100:
                img_name = "0" + str(i) + ".png"
            else:
                img_name = str(i) + ".png"
            img_path = os.path.join(save_directory, img_name)
            # 下载图片
            try:
                urllib.request.urlretrieve(img_url, img_path)
                print(f"download:{img_name}")
                i = i + 1
            except:
                pass
    return i

begin_id = 0         
for html_id in range(0, 19, 1):
    print(f"download images from {html_id}.html")  
    html_file_path = 'html/{}.html'.format(html_id)
    begin_id = download_images_from_html(html_file_path, begin_id)