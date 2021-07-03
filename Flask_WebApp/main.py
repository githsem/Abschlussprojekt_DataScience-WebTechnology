from flask import Flask, render_template, request
import pandas as pd
import TeamITea

app = Flask(__name__)

# klinikbewertungen.de 
df=pd.read_csv("kbClean.csv")
kb_stars = df[['NameKlinik', 'Gesamt', 'Zufriedenheit']]
kb_means = kb_stars.groupby(['NameKlinik'], as_index=False)['Gesamt'].mean()
kb_means = kb_means.sort_values('Gesamt',ascending=False, ignore_index=True)
vergleich_list = kb_means['Gesamt'].to_list()
nameKlinik = kb_means['NameKlinik'].to_list()
# KB Sterne Dict
df2 = df.groupby(['NameKlinik', 'Gesamt']).size().unstack().reset_index()
sterneDict = df2.set_index('NameKlinik').T.to_dict('list')


# Google Maps
dfgm=pd.read_csv("GM_Clean.csv")
gm_stars = dfgm[['Name der Klinik', 'Sternebewertung', 'Zufriedenheit']]
gm_means = gm_stars.groupby(['Name der Klinik'], as_index=False)['Sternebewertung'].mean()
gb_means = gm_means.sort_values('Sternebewertung',ascending=False, ignore_index=True)
gm_vergleich_list = gm_means['Sternebewertung'].to_list()
gmnameKlinik = gm_means['Name der Klinik'].to_list()
# GM Sterne Dict
df3 = dfgm.groupby(['Name der Klinik', 'Sternebewertung']).size().unstack().reset_index()
df3 = df3.fillna(0)
gmsterneDict = df3.set_index('Name der Klinik').T.to_dict('list')

adressen = {
'Herzogin Elisabeth Hospital' : 'Leipziger Str. 24, 38124 Braunschweig',
'Klinik am Zuckerberg' : 'Zuckerbergweg 2, 38124 Braunschweig',
'Klinikum Wolfsburg' : 'Sauerbruchstraße 7, 38440 Wolfsburg',
'Klinikum Peine' : 'Virchowstraße 8 h, 31226 Peine',
'St. Martini Krankenhaus' : 'Göttinger Str. 34, 37115 Duderstadt',
'DIAKOVERE Henriettenstift' : 'Marienstraße 72-90, 30171 Hannover',
'Eilenriede Klinik Hannover' : 'Uhlemeyerstraße 16, 30175 Hannover',
'Sophienklinik' : 'Bischofsholer Damm 160, 30173 Hannover',
'KRH Klinikum Agness Karll Laatzen' : 'Hildesheimer Str. 158, 30880 Laatzen',
'Klinikum Wahrendorff' : 'Rudolf-Wahrendorff-Straße 23, 31319 Sehnde',
'AMEOS Klinikum Hildesheim' : 'Goslarsche Landstraße 60, 31135 Hildesheim',
'Helios Kliniken Mittelweser' : 'Ziegelkampstraße 39, 31582 Nienburg/Weser',
'HELIOS Klinik Cuxhaven' : 'Altenwalder Chaussee 10, 27474 Cuxhaven',
'AMEOS Klinikum Seepark Geestland' : 'Langener Str. 66, 27607 Geestland',
'Krankenhaus Buchholz' : 'Steinbecker Str. 44, 21244 Buchholz in der Nordheide',
'Krankenhaus Winsen' : 'Friedrich-Lichtenauer-Allee 1, 21423 Winsen (Luhe)',
'Psychiatrische Klinik Lüneburg' : 'Am Wienebütteler Weg 1, 21339 Lüneburg',
'Agaplesion - Diakonieklinikum Rotenburg' : 'Elise-Averdieck-Straße 17, 27356 Rotenburg (Wümme)',
'Kreiskrankenhaus Osterholz' : 'Am Krankenhaus 4, 27711 Osterholz-Scharmbeck',
'Klinik Fallingbostel' : 'Kolkweg 1, 29683 Bad Fallingbostel',
'MediClin Klinikum Soltau' : 'Oeninger Weg 59, 29614 Soltau',
'Krankenhaus Walsrode' : 'Robert-Koch-Straße 4, 29664 Walsrode',
'Elbe Klinikum Buxtehude' : 'Am Krankenhaus 1, 21614 Buxtehude',
'Diana Kliniken' : 'Dahlenburger Str. 2A, 29549 Bad Bevensen'}

@app.route("/")
def index():
    return render_template("index.html",serie=vergleich_list)

@app.route('/vorhersage')
def my_form():
    return render_template('vorhersage.html')

@app.route('/vorhersage', methods=['POST'])
def my_form_post():
    text = request.form['text']
    result = TeamITea.vorhersage(text)
    if text =='':
        result = ['Bitte ein Text eingeben!']
    if result[0]=='Positiv':
        thumb ='up text-success'
    elif  result[0]=='Negativ': 
        thumb ='down text-danger' 
    else:
        thumb =''
    return render_template('vorhersage.html',result=result[0],text1=text,thumb=thumb)

@app.route("/bewertungen")
def bewertungen():
    dizi = df.groupby(['NameKlinik']).mean().get('Gesamt')
    dummy = [1,2,3,4]
    return render_template("bewertungen.html",dizi=dizi,nameKlinik=nameKlinik,display='none',dummy=dummy)   

@app.route("/bewertungen", methods=['POST'])
def bewertungen_post():
    kname = request.form['options']
    adresse = adressen[kname]

    # KB Bewertungen
    df2 = df.where(df["NameKlinik"]==kname)
    df2.dropna(inplace=True)
    kb_bewertungen = df2['Erfahrungsbericht']
    # KB Sterne
    kb_sterne = df2['Gesamt']
    kb_sterne =[int(i) for i in kb_sterne]
    # KB poz_neg result
    kb_result = df2['Polarity Stimmung']
    kb = zip(kb_bewertungen,kb_sterne,kb_result)
    data = sterneDict[kname]

    # GM Bewertungen
    df3 = dfgm.where(dfgm["Name der Klinik"]==kname)
    df3.dropna(inplace=True)
    gm_bewertungen = df3['Bewertung']
    # GM Sterne
    gm_sterne = df3['Sternebewertung']
    gm_sterne =[int(i) for i in gm_sterne]
    # GM poz_neg result

    gm_result = df3['Polarity Stimmung']
    gm = zip(gm_bewertungen,gm_sterne,gm_result)
    gmdata = gmsterneDict[kname]
    
    # print(gmdata)
  
    return render_template("bewertungen.html",kname=kname,display='block',display2='none',nameKlinik=nameKlinik,gmnameKlinik=gmnameKlinik,kb=kb,gm=gm,data=data,gmdata=gmdata,adresse=adresse)      
  

if __name__ == "__main__":
    app.run(debug=True)