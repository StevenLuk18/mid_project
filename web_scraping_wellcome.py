#wellcome V3 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import pandas as pd
import time
from selenium.common.exceptions import NoSuchElementException
import re

driver = webdriver.Chrome()

url = "https://www.wellcome.com.hk/zh-hant/category/100001/1.html"
driver.get(url)

time.sleep(5)

#刪whatsapp pop-up,會阻擋禁入頁面
try:
    whatsapp =driver.find_element(By.XPATH,"//div[@class='easychat-chat-dismiss-button-mobile ']")
    whatsapp.click()
except NoSuchElementException:
    pass

posts = driver.find_elements(By.XPATH, "//a[@class='a-link router-link ware-wrapper']")

#貼文既連結<<<唔好刪,刪左直接唔洗寫
hrefs = [post.get_attribute("href") for post in posts]
base_url = "https://www.wellcome.com.hk"
product_urls = []
sold_out_status = []
wine_list = []
names = []
brands = []
pro_tags = []
current_prices = []
original_prices = []
volume= []
item_code = set()
#product_ids = set()


# 品牌名,加油後面慢慢加 
#BERNARD MAGREZ=海之藍 係同一款 佳樂事=CARLO  CH. D'ESCLANS=蝶之蘭酒莊   Chateau 梅鐸紅酒=CHATEAU HOLDEN  FRENCH CELLARS=法國酒窖 
#PAPE CLEMENT=Chateau Fombrauge PARTICULAR=杜卡斯=杜哈米陸  TIERRA D CUBAS=富巴斯                
brand_pattern = re.compile(r'(生力|蠔灣蘇維翁|朝日|布萊特|奔富冠蘭山系列|奔富|好卡頓|青島|史丹尼|藍妹|菲臘羅富齊|瑪特堡蘇維翁|獅威|K1664|詩莊堡|夏廸|\
                           |19 Crimes|19 CRIMES|絕對伏特加|Antinori|艾普羅|Ars Collecta|Artelatino|Auld Family|百加得|百利|百齡壇|加州赤足|八龍閣|必富達|\
                           |Beefsteak Club|Beefsteakclub|BERNARD MAGREZ|海之藍|藍冰|龐貝藍鑽石|寶尚父子|博嵐歌酒莊|BROWN BROTHERS|布萊特|百威|Pauillac|\
                           |金巴利|帝國田園|摩根船長|佳樂事|CARLO|嘉士伯|Carnivor|法國貝爾丹酒莊|奧希耶古堡|蝶之蘭酒莊|Ch. D\'Esclans|CH DE FIEUZA|羅拔世|幻之龍|\
                           |法國娜嘉麗酒莊|法國雲尼臣酒莊|CH.D\'ESCLANS|CH.LASCOMBES|CH.LES VALLEES|來福酒莊|CHANDON|香桐|尚德嘉莊園|Chateau 波爾多|\
                           |梅鐸紅酒|Chateau 優等波爾多紅酒|芝華士|蝶矢|雙劍蘇格蘭威士忌|雲霧之灣|康德努酒莊|Pepperjack|可樂娜|博多歌酒莊|BAREFOOT|\
                           |君度|智利干露紅魔鬼|Coopers|COOPERSS|拿破崙|法國拉菲|智利拉菲|Dewars|添普蘭尼諾|E.Guigal|艾丁格|智利武當|Fernando De Ca|FOUR PILLARS|Four Pillars|\
                           |FRENCH CELLARS|法國酒窖|月桂冠|GEORG JENSEN|雲咸|合同酒精|金星|Goose Island|哥頓|馬爾貝紅酒|GRAINSHAKER|法國小龍船波爾多紅酒|\
                           |格蘭堡|健力士|古越龍山|鬼佬|白鶴|夏迪|Havana|健樂園|喜力|軒尼詩|英雄啤酒|Higherthan|海特他拿|海特|紅星牌|傑卡斯|德國野格|Jean Bouchard|\
                           |濟州漢拏山|占邊|真露|尊美醇|尊尼獲加|樂怡仙地|豪帥|金利來|Jack Daniel\'s|K BRANDS|K VINTNERS|K Vintners|菊正宗|羅拔二世|金威|麒麟|國士無雙|越乃寒梅|\
                           |久保田|嘉芙麗酒莊|La Gioiosa|LA MARCA|La Marca|里奧哈|李錦記|Leffe|巴頓酒莊|酒花精靈|LITTLE GIANT|瀘州老窖|M.Cellars|M.CELLARS|M.GOLD|M.Gold|\
                           |幻之瀧|馬利保|馬爹利|馬天爾|瑪天露|Medoc|MG|Mg Spirit|Modelo|酩悅|森永|MOUNT PEAK|Mount Peak|瑪特堡|舞鶴|瑪姆|麥菲士|無名氏|日本盛|蠔灣|Orion|ORION|塔牌|\
                           |Pape Clement|Chateau Fombrauge|Particular|杜卡斯|杜哈米陸酒莊|倍事佳|拉菲酒莊 |Paul Blanck|保羅蘭|PEPPERJACK|PERONI|Peroni|巴黎之花|葡萄之路黃標系列|\
                           |保吉士拿|R By Clinet|羅遜氏|人頭馬|美國加州蒙大菲|Roche Bellene|意大利羅芬諾|雜賀|寶嘉龍酒副牌|三生牌|森美亞頓|愛士圖爾莊園|斯托堡|\
                           |薩摩|施務露|白雪|順昌源|泰國勝獅|皇冠|雪花|Somersby|SOMERSBY|Squealing Pig|SQUEALING PIG|聖哈利|史丹尼|Stella Artois|STERLING|Sticks|紅牌|STONE&WOOD|Stone&Wood|\
                           |三得利|太平山|台灣啤酒|寶酒造|添加利|Taylor\'s|智利美麗地|格蘭利威|倉吉蒸餾所|麥卡倫|蘇格登|THEHONEYMAN|THREE OAKS|TIERRA D CUBAS|富巴斯|\
                           |Trivento|梅乃宿|Vessier Brut|凱歌|波瑪酒莊|VODKA SODA &|WARNER\'S|Warner\'s|WHISTLER|Whistler|白馬|威廉費爾莊園|禾富巴斯|拉菲爾古堡莊園|\
                           |醞思酒莊|咸亨|洋河|燕京|雅拉堡|黃尾袋鼠|Yomeishu|少爺|越州|利達民|千代壽|御湖鶴|獺祭|茅台|JACK DANIEL\'S|雄獅酒莊副牌|杏花村)') 

#分類紅白啤清啤,如果沒有我先SETUP(NULL),後面會回來SETUP
red_wine_pattern = re.compile(r'紅酒|奔富|瑪特堡單一園系列431宣言灰皮諾|波爾多紅|Rhone Rouge|赤霞珠|切粒子|黑皮諾|優等波爾多|Dolce Rosso|紅葡萄酒|Manadero|\
                              |Dux Imperial|富巴斯皇家特級|Malbec|CH DE FIEUZAL|庫納瓦梅洛|431宣言灰皮諾|Chateau Haut|Cabernet Merlot|CHEVALIER|\
                              |紅莫斯卡托|Tempranillo|Bourgogne|Raymond Cyrot|Bordeaux|GOLDEN WEST|Wilberforce|Shiraz|Syrah|寶嘉龍酒|雄獅酒莊|\
                              |Haut-Peyraguey|杜卡斯酒莊|巴頓酒莊副牌|Pinot|愛士圖爾莊園副牌|Pichon Baro|原箱CARLO ROSSICALIFORNIA DARK|嘉芙麗酒莊副牌|\
                              |拉菲酒莊 2011|杜哈米陸酒莊 2020|混釀|仙粉黛|梅洛|Cab Sauv|California Dark', re.IGNORECASE)

beer_pattern = re.compile(r'啤酒|嘉士伯|CRUSHED APPLE CIDER|樂怡仙地|黑啤|麥啤|一番搾|生啤|鬼佬|Coopers|少爺|Pacific Ale|GREEN COAST|CHU-HI', re.IGNORECASE)

white_wine_pattern = re.compile(r'白酒|白葡萄酒|波爾多白|莎當尼|沙當妮|莎當妮|雷司令|長相思|Blanco|灰皮諾|BROWN BROTHERS|Chardonnay|Cervaro|Chabolle Musigny|\
                                |Gewurztraminer|Meursault|西班牙果酒', re.IGNORECASE)

clear_beer_pattern = re.compile(r'清啤', re.IGNORECASE)

champagne_pattern = re.compile(r'香檳|Cuvee Decouverte|SPRITZ|CHANDON|原箱佳樂事莫斯卡托|MARCAPROSECCO',re.IGNORECASE)

sparkling_wine_pattern = re.compile(r'汽酒|汽泡酒|有汽甜酒|氣泡酒|有汽葡萄酒|Grand Rose|普羅賽柯',re.IGNORECASE)

liquor_pattern = re.compile(r'威士忌|Whisky|干邑|Cognac|雞尾酒|氈酒|毡酒|Gin|拔蘭地|白蘭地|龍舌蘭|冧酒|蘭姆酒|Rum|忌廉甜酒|力嬌酒|VODKA|伏特加|尊尼獲加|優質香檳區干邑|VSOP|\
                            |甜威末酒|香甜酒|秀訂金福|Dry Gin|十二年黃金三桶',re.IGNORECASE) #烈酒

jap_alco_pattern = re.compile(r'養命酒|甘酒|清酒|上撰|菊正宗|梅原酒|梅酒|燒酎|純米大吟釀|梅子酒|大吟釀|柚子酒|生貯造酒|柚子純米酒|純米梅酒|山田錦|柚子濁酒|辛口|生酛|吟釀灑',re.IGNORECASE)

tonic_wine_pattern = re.compile(r'人參酒|骨痛酒|補酒|金雞鐵樹酒')

chin_alco_pattern = re.compile(r'花彫酒|花雕酒|花彫|紹興酒|紹興|瀘州老窖|花雕|糯米酒|加飯酒|茅台|甜酒釀|玫瑰露酒|黑標10年|二鍋頭酒|藍瓷|高糧酒|汾酒',re.IGNORECASE)

kor_alco_pattern = re.compile(r'濟州漢拏山|真露|燒酒',re.IGNORECASE)

fruit_pattern = re.compile(r'蘋果酒|接骨木花|SOMERSBY',re.IGNORECASE)

rose_pattern = re.compile(r'玫瑰酒|玫瑰紅酒|Garnacha Rosado|玫瑰葡萄酒|玫瑰氣泡酒|Cavarose|Rose Wine|Rose Non Vintage|白仙芬黛酒|Bone Rose',re.IGNORECASE)

honey_wine_pattern = re.compile(r'蜂蜜酒|HONEY WINE',re.IGNORECASE)

fortified_Wine_pattern = re.compile(r'波特酒|缽酒|砵酒|雪利酒|Ruby Port|Oloroso',re.IGNORECASE)

no_alco_pattern = re.compile(r'無酒精',re.IGNORECASE)

peach_pattern = re.compile(r'白桃酒',re.IGNORECASE)


last_page = driver.find_element(By.XPATH,"//a[@class='last cursor num-box']").text
print(last_page)

for i in range(int(last_page)-1): #int(last_page)-1
    time.sleep(2)
    posts = driver.find_elements(By.XPATH, "//a[@class='a-link router-link ware-wrapper']")
    for i in range(len(posts)):
        posts = driver.find_elements(By.XPATH, "//a[@class='a-link router-link ware-wrapper']")
        post = posts[i]
        post.click()
        time.sleep(2)
        find_pcode = driver.find_element(By.CLASS_NAME,"item-code").text
        #print(find_pcode)
        pcode = find_pcode.split(': ')[1]
        #print(pcode)
        item_code.add(pcode)
        #back to main page
        driver.back()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0,50);")

    posts = driver.find_elements(By.XPATH, "//a[@class='a-link router-link ware-wrapper']")
    for post in posts:
        name = post.find_element(By.XPATH, ".//div[@class='name']").text
        names.append(name.strip())
        try:
            pro_tag = post.find_element(By.XPATH, ".//div[@class='pro tag']")
            pro_tag_text = pro_tag.text
        except NoSuchElementException:
            pro_tag_text = 'None'
    
        pro_tags.append(pro_tag_text)
        
        # 匹配品牌個名
        brand_match = brand_pattern.search(name)
        if brand_match:
            brand = brand_match.group()
        else:
            brand = None
        brands.append(brand)

        # 分類紅酒、白酒、啤酒和清啤
        if red_wine_pattern.search(name):
            wine_type = "紅酒"
        elif white_wine_pattern.search(name):
            wine_type = "白酒"
        elif beer_pattern.search(name):
            wine_type = "啤酒"
        elif clear_beer_pattern.search(name):
            wine_type = "清啤"
        elif liquor_pattern.search(name):
            wine_type = '烈酒'
        elif champagne_pattern.search(name):
            wine_type = "香檳"
        elif sparkling_wine_pattern.search(name):
            wine_type = '汽酒'
        elif fruit_pattern.search(name):
            wine_type = '果酒'
        elif jap_alco_pattern.search(name):
            wine_type = '日本酒'
        elif chin_alco_pattern.search(name):
            wine_type = '中國酒'
        elif tonic_wine_pattern.search(name):
            wine_type = '滋補酒'
        elif kor_alco_pattern.search(name):
            wine_type = '韓國酒'
        elif rose_pattern.search(name):
            wine_type = '玫瑰酒'
        elif honey_wine_pattern.search(name):
            wine_type = '蜂蜜酒'
        elif fortified_Wine_pattern.search(name):
            wine_type = '加強葡萄酒'
        elif peach_pattern.search(name):
            wine_type = '白桃酒'
        elif no_alco_pattern.search(name):
            wine_type = '無酒精'
        else:
            wine_type = None
            
        wine_list.append(wine_type)

        match = re.search(r'(\d+)\s*(ML|LT|CL|BT|PK|GM)', name, re.IGNORECASE) 
        if match:
            volume.append(match.group(1) + match.group(2))  
        else:
            volume.append(None)
        
        try:
            product_id_ar = post.get_attribute('href')
            full_url = base_url + product_id_ar.split(base_url)[-1]
            product_urls.append(full_url)
        except NoSuchElementException:
            full_url = None 
        

        
        price_box = post.find_element(By.XPATH, ".//div[@class='price-box']")
        try:
            
            price = price_box.find_element(By.XPATH, ".//span[@class='price']").text.replace('$','').replace('.00','').replace(',','')
        except NoSuchElementException:
            price = ""  

        line_price = price  
        try:
            
            line_price_element = price_box.find_element(By.XPATH, ".//span[@class='line-price']")
            line_price = line_price_element.text.replace('$','').replace('.00','').replace(',','') if line_price_element else price
        except NoSuchElementException:
            pass  

        current_prices.append(price.strip())
        original_prices.append(line_price.strip())

        try:
            post.find_element(By.XPATH, ".//div[contains(@class, 'sold tag')]")
            sold_out = 1  # 1=冇貨
        except NoSuchElementException:
            sold_out = 0  # 0=有貨

        sold_out_status.append(sold_out)
        
    next_page_element = post.find_element(By.XPATH, "//div[@class='text'][contains(text(),'下一頁')]")
    next_page_element.click()
    

#driver.quit()
#assert len(product_ids) == len(product_urls), "Mismatch in lengths of product_ids and product_urls"
# DF<<LEN
paired_data = list(zip(item_code, brands, names, volume, wine_list, current_prices, original_prices, pro_tags, sold_out_status,product_urls))

df_wc = pd.DataFrame(paired_data, columns=["product_id", "brand", "product", "volume", "type", "current_price", "original_price", "discount", "sold_out","url"])
current_datetime = datetime.now()
formatted_date = current_datetime.strftime("%d-%m-%Y")
df_wc['date'] = formatted_date

df_wc.set_index('date', inplace=True)

df_wc.insert(8, "sold_quantity", ['None']*len(df_wc), True)
df_wc.insert(11, "market_id", ['wellcome'] * len(df_wc), True)



df_wc.tail()

df_wc.to_csv('wc_data_{}.csv'.format(formatted_date))