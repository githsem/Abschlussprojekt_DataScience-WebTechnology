# Importing necessary libraries and tools
# -------------------------------------

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd


NameKlinik = []
Titel = []
DatumBewertung = []
Fachbereich = []
Erfahrungsbericht = []
Gesamtzufriedenheit = []
QualitaetBeratung = []
MedizBehandlung = []
VerwaltungAblaeufe = []


def scrape(url):

#chromedriver
    driver = webdriver.Chrome('/Users/yigit/Github/chromedriver')


    driver.get(url +'/bewertungen?allbew#more')

    driver.find_element_by_id("ez-accept-naecesary").click()

    
# Locating the xpaths and finding elements on the website
# -------------------------------------


    name = driver.find_element_by_xpath('//*[@id="content"]/header/h1')
    titels = driver.find_elements_by_xpath('//article[@class="bewertung" or @class="bewertung ignorieren"]/header')
    daten = driver.find_elements_by_xpath('//article[@class="bewertung" or @class="bewertung ignorieren"]/div/time')
    fachbereiche = driver.find_elements_by_xpath('//article[@class="bewertung" or @class="bewertung ignorieren"]/span')
    berichte = driver.find_elements_by_xpath("//p[@itemprop='reviewBody']")
    gesamtListe = driver.find_elements_by_xpath('//article[@class="bewertung" or @class="bewertung ignorieren"]/section/dl/dd[1]/img')
    qBeratung = driver.find_elements_by_xpath('//article[@class="bewertung" or @class="bewertung ignorieren"]/section/dl/dd[2]/img')
    medBehandlung = driver.find_elements_by_xpath('//article[@class="bewertung" or @class="bewertung ignorieren"]/section/dl/dd[3]/img')
    verwaltAbl = driver.find_elements_by_xpath('//article[@class="bewertung" or @class="bewertung ignorieren"]/section/dl/dd[4]/img')
    # ausGestaltung = driver.find_elements_by_xpath('//article[@class="bewertung" or @class="bewertung ignorieren"]/section/dl/dd[5]/img')


    # berichte = driver.find_elements_by_xpath('//section[@class="report"]/dl/dd/p')



# Scraping texts
# -------------------------------------

    clinicName = [name.text for a in titels]
    titel = [a.text for a in titels]
    dateOfReview = [a.text for a in daten]
    department = [a.text for a in fachbereiche]
    experience = [a.text for a in berichte]

# Scraping attributes for review stars
# -------------------------------------

    overall = [a.get_attribute("class") for a in gesamtListe]
    consultingQuality = [a.get_attribute("class") for a in qBeratung]
    medTreatment = [a.get_attribute("class") for a in medBehandlung]
    mgmt_process = [a.get_attribute("class") for a in verwaltAbl]
    # AusstattungGestaltung = [a.get_attribute("class") for a in ausGestaltung]


    # print(len(QualitaetBeratung))
    time.sleep(3)
    driver.quit()


    for i in clinicName:
        NameKlinik.append(i)
    for i in titel:
        Titel.append(i)
    for i in dateOfReview:
        DatumBewertung.append(i)
    for i in department:
        Fachbereich.append(i)
    for i in experience:
        Erfahrungsbericht.append(i)
    for i in overall:
        Gesamtzufriedenheit.append(i)
    for i in consultingQuality:
        QualitaetBeratung.append(i)
    for i in medTreatment:
        MedizBehandlung.append(i)
    for i in mgmt_process:
        VerwaltungAblaeufe.append(i)
    

df_url = pd.read_excel(r'Klinikliste.xlsx')[:24]["Link Klinikbewertungen"]
for url in df_url:
    scrape(url)

# Define dataframe
# -------------------------------------

df = pd.DataFrame(zip(NameKlinik, Titel, DatumBewertung, Fachbereich, Erfahrungsbericht, Gesamtzufriedenheit, QualitaetBeratung, MedizBehandlung, VerwaltungAblaeufe), columns=["NameKlinik", "Titel", "DatumBewertung", "Fachbereich", "Erfahrungsbericht", "Gesamtzufriedenheit", "QualitätBeratung", "MedizBehandlung", "VerwaltungAblaeufe"])


# Create the csv
# -------------------------------------
df.to_csv('klinikbew.csv', index=False, encoding="utf-8")




    


















# df2 = pd.DataFrame([bewertungen],columns=['bewertungen'])
    # df = df.append(df2,ignore_index=True)
    # df.to_csv("aaa.csv",index=False)



    # bewCount = 1

    # with open("bewertungen.txt","w",encoding = "UTF-8") as file:
    #     for bewertung in bewertungen:
    #         file.write(str(bewCount) + ".\n" + bewertung + "\n")
    #         file.write("**************************\n")
    #         bewCount += 1
                    

    # elements = driver.find_elements_by_xpath('//article[@class="bewertung"]/span')
    # liste = []
    # for element in elements:
    #     liste.append(element.text)
    # print(liste)