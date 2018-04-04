#!/usr/bin/python
import sys
from splinter import Browser
import json, requests
executable_path = {'executable_path':'/Users/priyanka/Downloads/geckodriver'}
inputFileStr = sys.argv[1]
outputFile = open('/Users/priyanka/Downloads/splinterOutput.tsv', 'a')

proxyIP = '9.81.19.27'// tochange it
proxyPort = 3128
proxy_settings = {
    'network.proxy.type': 1,
    'network.proxy.http': proxyIP,
    'network.proxy.http_port': proxyPort,
    'network.proxy.ssl': proxyIP,
    'network.proxy.ssl_port':proxyPort,
    'network.proxy.socks': proxyIP,
    'network.proxy.socks_port':proxyPort,
    'network.proxy.ftp': proxyIP,
    'network.proxy.ftp_port':proxyPort 
}

def getFromRedsky():
    try:
        r = requests.get('https://redsky.target.com/v1/pdp/tcin/'+tcin)
        jsonData = json.loads(r.content)
        return jsonData['product']['price']['offerPrice']['formattedPrice']
    except:
        return "NA"

def getAvail(avail1, avail2):
    try:
        r = requests.post('http://localhost:8080/example.web/service/availability/getavailabilitydata', data='')
        jsonData = json.loads(r.content)
        return jsonData
    except:
        return "INCONCLUSIVE"

def getTemplate(tmpl):
    templateFile = open('/Users/priyanka/Downloads/templates.json', 'r')
    templates = json.load(templateFile)
    templateFile.close()
    return templates[tmpl]

try:
    outputFile.write("TCIN\tDPCI\tTITLE\tAMZ_PRICE\tWMART_PRICE\tTGT_PRICE\tAMZ_AVAIL1\tAMZ_AVAIL2\tWMART_AVAIL1\tWMART_AVAIL2\tAMZ_BUYBOX_WINNER\tWMART_BUYBOX_WINNER\tAMZ_BUYBOX_FLFL_BY\tWMART_BUYBOX_FLFL_BY\tAMZ_PRICE_PROMO\tWMART_PRICE_PROMO\tAMZ_PROMO_MSG\tWMART_PROMO_MSG\n")
    with open(inputFileStr, 'r') as lines:
        with Browser('firefox', profile_preferences=proxy_settings) as browser:
            browser.visit("http://www.icanhazip.com")
            print(browser.find_by_css("body")).first.value
            for line in lines:
                vals = line.split("\t")
                tcin = vals[0]
                dpci = vals[1]
                title = vals[2]
                outputFile.write(tcin+"\t"+dpci+"\t"+title+"\t")
                amzPrice = ''
                amzAvailability1 = ''
                amzAvailability2 = ''
                wmartPrice = ''
                wmartAvailability1 = ''
                wmartAvailability2 = ''
                amzBuyboxWinner = ''
                wmartBuyboxWinner = ''
                amzBuyboxFlflBy = ''
                wmartBuyboxFlflBy = ''
                amzPricePromo = ''
                wmartPricePromo = ''
                amzPromoMsg = ''
                wmartPromoMsg = ''
                dummy = ''

                if (vals[3] is not None and vals[3] != ''):
                    amzUrl = vals[3]
                    browser.visit(amzUrl)
                    try:
                        amzPrice =  browser.find_by_css(getTemplate("price")).first.value.encode('utf-8').strip('\n').strip('\t').replace('\n','').replace('\t','')
                    except:
                        dummy = ''
                    try:
                        amzAvailability1 =  browser.find_by_css(getTemplate("avail1")).first.value.encode('utf-8').strip('\n').strip('\t').replace('\n','').replace('\t','')
                    except:
                        dummy = ''
                    try:
                        amzAvailability2 =  browser.find_by_css(getTemplate("avail2")).first.value.encode('utf-8').strip('\n').strip('\t').replace('\n','').replace('\t','')
                    except:
                        dummy = ''
                    
                    try:
                        amzBuyboxWinner =  browser.find_by_css(getTemplate("buyboxWinner")).first.value.encode('utf-8').strip('\n').strip('\t').replace('\n','').replace('\t','')
                    except:
                        dummy = ''
                    
                    try:
                        amzBuyboxFlflBy =  browser.find_by_css(getTemplate("buyboxFlflBy")).first.value.encode('utf-8').strip('\n').strip('\t').replace('\n','').replace('\t','')
                    except:
                        dummy = ''
                    
                    try:
                        amzPricePromo =  browser.find_by_css(getTemplate("pricePromo")).first.value.encode('utf-8').strip('\n').strip('\t').replace('\n','').replace('\t','')
                    except:
                        dummy = ''
                    
                    try:
                        amzPromoMsg =  browser.find_by_css(getTemplate("promoMsg")).first.value.encode('utf-8').strip('\n').strip('\t').replace('\n','').replace('\t','')
                    except:
                        dummy = ''

                if (vals[4] is not None and vals[4] != ''):
                    wmartUrl = vals[4]
                    browser.visit(wmartUrl)
                    try:
                        wmartPrice =  browser.find_by_css(getTemplate("price")).first.value.encode('utf-8').strip('\n').strip('\t').replace('\n','').replace('\t','')
                    except:
                        dummy = ''
                    
                    try:
                        wmartAvailability1 =  browser.find_by_css(getTemplate("avail1")).first.value.encode('utf-8'.strip('\n').strip('\t').replace('\n','').replace('\t',''))
                    except:
                        dummy = ''
                    
                    try:
                        wmartAvailability2 =  browser.find_by_css(getTemplate("avail2")).first.value.encode('utf-8').strip('\n').strip('\t').replace('\n','').replace('\t','')
                    except:
                        dummy = ''
                    
                    try:
                        wmartBuyboxWinner =  browser.find_by_css(getTemplate("buyboxWinner")).first.value.encode('utf-8').strip('\n').strip('\t').replace('\n','').replace('\t','')
                    except:
                        dummy = ''
                    
                    try:
                        wmartBuyboxFlflBy =  browser.find_by_css(getTemplate("buyboxFlflBy")).first.value.encode('utf-8').strip('\n').strip('\t').replace('\n','').replace('\t','')
                    except:
                        dummy = ''
                    
                    try:
                        wmartPricePromo =  browser.find_by_css(getTemplate("pricePromo")).first.value.encode('utf-8').strip('\n').strip('\t').replace('\n','').replace('\t','')
                    except:
                        dummy = ''
                    
                    try:
                        wmartPromoMsg =  browser.find_by_css(getTemplate("promoMsg")).first.value.encode('utf-8').strip('\n').strip('\t').replace('\n','').replace('\t','')
                    except:
                        dummy = ''
                
                tgtPrice = getFromRedsky()
                print (tgtPrice)
                tgtPricePrintable = tgtPrice.encode('utf-8')
                outputFile.write(amzPrice+"\t"+wmartPrice+"\t"+tgtPricePrintable+"\t"+amzAvailability1+"\t"+amzAvailability2+"\t"+wmartAvailability1+"\t"+wmartAvailability2+"\t"+amzBuyboxWinner+"\t"+wmartBuyboxWinner+"\t"+amzBuyboxFlflBy+"\t"+wmartBuyboxFlflBy+"\t"+amzPricePromo+"\t"+wmartPricePromo+"\t"+amzPromoMsg+"\t"+wmartPromoMsg+"\n")
                outputFile.flush()
except Exception as e:
    print("Error!" + str(e))
    exit(1)
finally:
    outputFile.close()
