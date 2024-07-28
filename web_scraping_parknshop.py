#PNS

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import time
import pandas as pd
import re

driver = webdriver.Chrome()
#chrome_options = Options()
#chrome_options.add_argument("--headless=new")
#driver = webdriver.Chrome(options=chrome_options)
#url = "https://www.pns.hk/zh-hk/%E9%A3%9F%E5%93%81%E5%8F%8A%E9%A3%B2%E5%93%81/%E9%85%92%E7%B2%BE%E9%A3%B2%E5%93%81/c/04012000"
url = "https://www.pns.hk/zh-hk/search?text=%E9%85%92&useDefaultSearch=false&brandRedirect=true&q=%E9%85%92:mostRelevant:categoryNameLevel2:04012000"
try:
    driver.get(url)
except:
    print('url not found')
    exit

time.sleep(5)
brand_pattern = re.compile(r'人頭馬|青島|白鶴|獅威|月桂冠|ABSOLUT|瑞典伏特加|嘉士伯|ABTEI HIMMEROD|ALLEES CANTE|ANTU|APOTHIC|ARBOR MIST|AZAHARA|BALVENIE|BARON DE RICHEMONT|BARONS ROTHSCHILD|\
                           |BELLA TAVOLA|BELVEDERE|BITTER TRUTH|BODDINGTONS|BODEGA NORTON|BORGO SALCETINO|BORN ROSE|BRANCOTT EST|CALVET|CAMPARI|CAPE MENTELLE|CASILLERO DEL DIABLO|CASTILLO ALBAI|\
                           |CELLIER DES PRINCES|CH BEL AIR|CH CARCANIEUX|CH FERRANDE|CH HAUT PEYRUGUET|CH LIEUJEAN|CH SIRAN|CH STE MICHELLE|CH TOUR PRIGNAC|CH. BELLES EAUX|CH. DE COMBES|CH.LAVILLE BERTROU|\
                           |CHANDON|CHAP MOINES|CHAPEL HILL|CHARMES G CORBIN|CHATEAU D ESCLANS|CHUM CHURUM|CLARENDELLE|CON DE ORIZA|CORONA EXTRA|COURVOISIER|D\'ESCLANS|DARK HORSE|DBR LAFITE|\
                           |DOM D\'AUSSIERES|DOM MOUTARD|DOMAINES OTT|DULUC DUCRU|ENVOL DE MARTINET|ERNEST RAPENEAU|ESTRELLA|FAM LAPALU|FRANCOIS MARTENOT|G.H. MUMM|GABBIANO|GENESTRAS|GERARD BERTRAND|\
                           |GRANT BURGE|GS RETAIL YOUUS|GS25 X NETFLIX|H FAUGERES|HIGHERTHAN|HITE|JALOUSIE BEAULIEU|JEAN VALESTREL|JING|JJ馬克威廉|JUSTBE|K1664|KENDALL JACKSON|KING|KIZAKURA|KOKUSHIMUSHO|\
                           |KOSHINO HAKUCHO|KOSHINOKANBAI|KOYLE|KOYLE ROYALE|KSK|KUNIMARE|L. RAUZAN GASSIES|LA MARCA|LA VIEILLE FERME|LEFFE|LES FIEFS LAGRANGE|LEYDET VALEN|LIBERTY CREEK|LUC BELAIRE|\
                           |MABOROSHINOTAKI|MAISON CASTEL|MARJOSSE|MATUA|MCCORMICK|MCGUIGAN|MG SPIRIT|MICHEL LYNCH|MICHIZAKURA|MINUTY|MONKEY47|MOSELLAND|MOULIN BARRAIL|MUDHOUSE|ONLY VODKA SODA|\
                           |ORION BEER|OYSTER BAY|PALOUMEY|PAPE CLEMENT|PARTARRIEU|PAULANER|PENSEES TOUR CARNET|PERONI|PERRIER JOUET|PETIT VALLON|RAIMAT|RAVENSWOOD|RAWSON\'S RETREAT|SANTA HELENA|\
                           |SAVANNA|SAWAHIME|SECOND CAMENSAC|SHENG LONG|SHENG LONG|SNOW|SOMERSBY|ST HUGO|STELLA ARTOIS|TAIHEIZAN|TAKARA|TAMANO-HIKARI|TENRYOU|TERR BAUMET ST PAUL|TERRAZAS|TESSELLAE|\
                           |THE SHY PIG|THE STAG|THREE OAKS|TSUKUSU|VEUVE CLICQUOT|VILLA MURA|WAITROSE|WARRES|WOLFBERGER|WOLMAE|WYNNS|YALUMBA|YEBISU|YELLOWGLEN|YOSHIMURA|ZHENG DA BRAND|ZHIZHONGHE|\
                           |澳洲 JAMSHED|三得利|三生牌|五糧液|健力士|劍威|加利奧|加州佳樂事|加州百靈爵|加州赤足|勝獅|南非尼德堡|博蒙德斯克雷若斯|古越龍山|台灣啤酒|司特加|君度|哥頓|喜力|塔牌|夏迪|太陽|奇偉|好卡頓|\
                           |富樂|尊尼獲加|尊美|巴比斯|布根地古拉尼|帝皇|常陸野貓頭廌啤酒|德國金得樂|必富達|意大利湯馬斯|意大利瑞可薩|愛情故事|摩根船長|日本盛|智利加西亞|智利康樂斯|智利聖達麗泰|智利華詩歌|智利蒙加斯|\
                           |智利蒙迪斯|會稽山|朝日|札幌|杜威|杰克丹尼|格蘭摩連治|格蘭費迪|梅乃宿|森堡|樂天|樂怡仙地|武當波爾多|法國亞瑟梅斯|法國卡斯特莫爾酒莊|法國多芬斯|法國托卡|法國托卡酒莊|法國拉赫司酒莊|法國武當庄園紅|\
                           |法國法蘭索拉貝|法國美安酒莊|法國聖呂茲|法國蒙澳尼|法國酩悅|法國雅蕾堡|法國香奈|波士|波爾多力卡巴頓|波爾多迪雅詩酒莊|泰象啤|派柏司|添加利|澳洲傑卡斯|澳洲利達民|澳洲奔富|澳洲奔樂克|澳洲禾富巴斯|\
                           |澳洲雲咸|澳洲麥威廉|澳洲黃尾袋鼠|濟州漢拏山|瀘州老窖|灰鵝|熊野|珠江橋牌|瑞典|生力|白雪|白馬|白鶴|百利|百威|百家得|百齡壇|皇冠|真露|石灣|紅星|紅萬壽|紐西蘭明聖酒莊|紐西蘭聖克萊|舞鶴|艾立加|\
                           |芝華士|芳絲亞|萬寶來|萬歲樂|藍冰|藍妹|蘇格登|蘇聯|蜜桃紅|蝶矢|西班牙帝國田園|西班牙桃樂丝|西班牙菲斯奈特|貴州|軒尼詩|邦比|金威|金崙堡|金御膳|金星牌|金飛馬|阿佩羅|阿根廷仙塔茱莉亞|阿根廷堤麗雅|\
                           |阿根廷戴雲路|阿根廷野雁|雲霧之灣|順昌源|養命|馬天利|馬爹利|騎士|鬼佬|麒麟|麥卡倫|麥格根零系|麥菲士')

red_wine_pattern = re.compile(r'紅酒|红酒|奥堂|奔富|瑪特堡單一園系列431宣言灰皮諾|波爾多紅|Rhone Rouge|赤霞珠|切粒子|黑皮諾|優等波爾多|Dolce Rosso|紅葡萄酒|Manadero|\
                              |Dux Imperial|富巴斯皇家特級|Malbec|CH DE FIEUZAL|庫納瓦梅洛|431宣言灰皮諾|Chateau Haut|Cabernet Merlot|CHEVALIER|\
                              |紅莫斯卡托|Tempranillo|Bourgogne|Raymond Cyrot|Bordeaux|GOLDEN WEST|Wilberforce|Shiraz|Syrah|寶嘉龍酒|雄獅酒莊|\
                              |Haut-Peyraguey|杜卡斯酒莊|巴頓酒莊副牌|Pinot|愛士圖爾莊園副牌|Pichon Baro|原箱CARLO ROSSICALIFORNIA DARK|嘉芙麗酒莊副牌|\
                              |拉菲酒莊 2011|杜哈米陸酒莊 2020|混釀|仙粉黛|梅洛|MERLOT|COTEAUX|CASILLERO DEL DIABLO|LEOGNAN', re.IGNORECASE)

beer_pattern = re.compile(r'啤酒|嘉士伯|CRUSHED APPLE CIDER|樂怡仙地|黑啤|麥啤|一番搾|生啤|鬼佬|Coopers|少爺|Pacific Ale|GREEN COAST|CHU-HI', re.IGNORECASE)

white_wine_pattern = re.compile(r'白酒|白葡萄酒|波爾多白|莎當尼|沙當妮|莎當妮|雷司令|長相思|Blanco|灰皮諾|BROWN BROTHERS|Chardonnay|Cervaro|Chabolle Musigny|\
                                |Gewurztraminer|Meursault|西班牙果酒|白葡萄甜酒|Y SERIES VIOGNIER|HARVEST', re.IGNORECASE)

clear_beer_pattern = re.compile(r'清啤', re.IGNORECASE)

champagne_pattern = re.compile(r'香檳|Cuvee Decouverte|SPRITZ|CHANDON|原箱佳樂事莫斯卡托|MARCAPROSECCO',re.IGNORECASE)

sparkling_wine_pattern = re.compile(r'汽酒|汽泡酒|有汽甜酒|氣泡酒|有氣酒|有汽葡萄酒|Grand Rose|普羅賽柯',re.IGNORECASE)

liquor_pattern = re.compile(r'威士忌|Whisky|干邑|Cognac|雞尾酒|氈酒|毡酒|Gin|拔蘭地|白蘭地|龍舌蘭|冧酒|蘭姆酒|Rum|忌廉甜酒|力嬌酒|VODKA|伏特加|尊尼獲加|特優香檳干邑|VSOP|V.S.O.P|\
                            |甜威末酒|香甜酒|秀訂金福|Dry Gin|十二年黃金三桶|金酒|朗姆酒|高球酒|百利甜酒',re.IGNORECASE) #烈酒

jap_alco_pattern = re.compile(r'養命酒|甘酒|清酒|上撰|佳撰|上撰清酒|菊正宗|梅原酒|梅酒|燒酎|燒酌|純米大吟釀|梅子酒|柚子酒|生貯造酒|柚子純米酒|純米梅酒|山田錦|柚子濁酒|辛口|生酛|吟釀灑|濁酒|梅子|香桃酒|\
                              |桃酒|原油酒|高梅|吟醸|大吟醸|本醸造|越の白鳥',re.IGNORECASE)

tonic_wine_pattern = re.compile(r'人參酒|骨痛酒|補酒|金雞鐵樹酒',re.IGNORECASE)

chin_alco_pattern = re.compile(r'花彫酒|花雕酒|花彫|紹興酒|紹興|瀘州老窖|花雕|糯米酒|加飯酒|茅台|甜酒釀|玫瑰露酒|黑標10年|二鍋頭酒|藍瓷|高糧酒|老媽甜酒|五糧液|佬米酒|廣東米酒|三蒸酒|雙蒸酒|特醇米酒|\
                               |勁酒',re.IGNORECASE)

kor_alco_pattern = re.compile(r'濟州漢拏山|真露|燒酒|WOLMAE',re.IGNORECASE)

fruit_pattern = re.compile(r'蘋果酒|接骨木花|SOMERSBY|葡萄橙汁酒|果酒',re.IGNORECASE)

rose_pattern = re.compile(r'玫瑰酒|玫瑰紅酒|Garnacha Rosado|玫瑰葡萄酒|玫瑰氣泡酒|Cavarose|Rose Wine|Rose Non Vintage|白仙芬黛酒|Bone Rose',re.IGNORECASE)

honey_wine_pattern = re.compile(r'蜂蜜酒|HONEY WINE',re.IGNORECASE)

fortified_Wine_pattern = re.compile(r'波特酒|缽酒|砵酒|雪利酒|Ruby Port|Oloroso',re.IGNORECASE)

no_alco_pattern = re.compile(r'無酒精',re.IGNORECASE)

peach_pattern = re.compile(r'白桃酒',re.IGNORECASE)


# 所有商品既都有既xpath<<應該改唔到
#product_containers = driver.find_elements(By.XPATH, "//div[@class='productContainer']")


WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='productContainer']")))

# 存ID 存商品用
processed_ids = set()
products = []
start_time = time.time()  
max_duration = 1800 #超過30分鐘就出結果

while True:
    time.sleep(5)
    if time.time() - start_time > max_duration:
        print("Reached the maximum duration. Ending the collection process...")
        break
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//div[@appear=''][@class='productContainer']")))
    product_containers = driver.find_elements(By.XPATH, "//div[@appear=''][@class='productContainer']")

    for container in product_containers:
        product_quantity = driver.find_element(By.XPATH,"//div[@class='product-quantity']").text.replace('件貨品','')

        # ID
        try:
            product_link_element = container.find_element(By.XPATH, ".//a[@class='productName']")
            product_link = product_link_element.get_attribute("href")
            product_id = product_link.split('/')[-1].split('.')[0]
            
        except NoSuchElementException:
            continue

        # 用商品ID去CHECK有冇重複
        if product_id in processed_ids:
            continue
        else:
            processed_ids.add(product_id)
        try:
            product_name = container.find_element(By.XPATH, ".//a[@class='productName']").text
        except NoSuchElementException:
            product_name = None

        #現價/原價
        
        current_price = None
        original_price = None
        try:
            
            current_price_element = container.find_element(By.XPATH, ".//span[contains(@class, 'currentPrice')]")
            current_price = current_price_element.text
            
            if "isDiscount" in current_price_element.get_attribute("class"):
                try:
                    original_price = container.find_element(By.XPATH, ".//span[@class='originalPrice']").text
                except NoSuchElementException:
                    original_price = current_price  
            else:
                original_price = current_price  
        except NoSuchElementException:
            continue
            

        # vol
        try:
            product_unit = container.find_element(By.XPATH, ".//div[@class='productUnit']").text
        except NoSuchElementException:
            product_unit = None

        # 折扣
        try:
            pro_tags = container.find_element(By.XPATH, ".//p[@class='ellipsis']").text
        except NoSuchElementException:
            pro_tags = None

        # sell,要獨位開LIST,因為佢係獨立一個xpath到,所以好難搵唔開list會erro
        sells = []
        try:
            sells_elements = container.find_elements(By.XPATH, ".//span[@class='sellQuantity']")
            for sell in sells_elements:
                sells.append(sell.text)
        except NoSuchElementException:
            sells = None
            # 品牌名
        
        brand_match = brand_pattern.search(product_name)
        brand = brand_match.group() if brand_match else None

        # 酒類型
        if red_wine_pattern.search(product_name):
            wine_type = "紅酒"
        elif white_wine_pattern.search(product_name):
            wine_type = "白酒"
        elif beer_pattern.search(product_name):
            wine_type = "啤酒"
        elif clear_beer_pattern.search(product_name):
            wine_type = "清啤"
        elif liquor_pattern.search(product_name):
            wine_type = '烈酒'
        elif champagne_pattern.search(product_name):
            wine_type = "香檳"
        elif sparkling_wine_pattern.search(product_name):
            wine_type = '汽酒'
        elif fruit_pattern.search(product_name):
            wine_type = '果酒'
        elif jap_alco_pattern.search(product_name):
            wine_type = '日本酒'
        elif chin_alco_pattern.search(product_name):
            wine_type = '中國酒'
        elif tonic_wine_pattern.search(product_name):
            wine_type = '滋補酒'
        elif kor_alco_pattern.search(product_name):
            wine_type = '韓國酒'
        elif rose_pattern.search(product_name):
            wine_type = '玫瑰酒'
        elif honey_wine_pattern.search(product_name):
            wine_type = '蜂蜜酒'
        elif fortified_Wine_pattern.search(product_name):
            wine_type = '加強葡萄酒'
        elif peach_pattern.search(product_name):
            wine_type = '白桃酒'
        elif no_alco_pattern.search(product_name):
            wine_type = '無酒精'
        else:
            wine_type = None  # 如果都不匹配則設為None

        try:
            container.find_element(By.XPATH, ".//div[@class='productHighlightOOS']")
            sold_out = 1  # 1=冇貨
        except NoSuchElementException:
            sold_out = 0  # 0=有貨

        # ... 构建产品信息字典的代码
        product_info = {
            'product_id': product_id,
            'product': product_name,
            'current_price': current_price,
            'original_price': original_price,
            'volume': product_unit,
            'discount': pro_tags,
            'sold_quantity': sells,
            'url': product_link,
            'sold_out': sold_out
        }
        product_info.update({
            'brand': brand,
            'type': wine_type
        })
        #我用左info加入去,我怕我唔小覆蓋左
        products.append(product_info)

        if len(products) >= int(product_quantity):
            break
#driver.quit()

df_pns = pd.DataFrame(products)

current_datetime = datetime.now()
formatted_date = current_datetime.strftime("%d-%m-%Y")
df_pns['date'] = formatted_date

df_pns.set_index('date', inplace=True)

df_pns = df_pns[['product_id','brand', 'product', 'volume', 'type', 'current_price','original_price','discount','sold_quantity','sold_out','url']]
df_pns['market_id'] = ['parknshop']*len(df_pns)


#df_pns.head()
print(f"Total products: {len(df_pns)}")

df_pns.to_csv('pns_data_{}.csv'.format(formatted_date))
