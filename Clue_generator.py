# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 00:32:42 2019

@author: faisal jamali


"""

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import datetime
import tkinter
from selenium.common.exceptions import NoSuchElementException
import random


today1 = datetime.date.today()
today1 = str(today1)

#accessing the nyt website to get the clues and solutions from the puzzle grid
driver = webdriver.Firefox()
url = 'https://www.nytimes.com/crosswords/game/mini'
driver.get(url)
driver.find_element_by_class_name("buttons-modalButton--1REsR").click()

#clicking the necessary buttons to reveal the clues in the grid, which is necessary to attain the clues from the webpage
buttons = driver.find_elements_by_class_name("Toolbar-expandedMenu--2s4M4")

for button in buttons:
    button.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/main/div[2]/div/div/ul/div[2]/li[2]/button").click()
    button.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/main/div[2]/div/div/ul/div[2]/li[2]/ul/li[3]/a").click()
    button.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/article/div[2]/button[2]/div/span").click()
    button.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/span").click()
    
#extract puzzle from from nyt website
print('extract puzzle and clues from from nyt website...')    
dict_letters = {'r1' : {'c1':'', 'c2':'', 'c3':'', 'c4':'', 'c5':'','n1':'','n2':'','n3':'','n4':'','n5':''},
                'r2' : {'c1':'', 'c2':'', 'c3':'', 'c4':'', 'c5':'','n1':'','n2':'','n3':'','n4':'','n5':''},
                'r3' : {'c1':'', 'c2':'', 'c3':'', 'c4':'', 'c5':'','n1':'','n2':'','n3':'','n4':'','n5':''},
                'r4' : {'c1':'', 'c2':'', 'c3':'', 'c4':'', 'c5':'','n1':'','n2':'','n3':'','n4':'','n5':''},
                'r5' : {'c1':'', 'c2':'', 'c3':'', 'c4':'', 'c5':'','n1':'','n2':'','n3':'','n4':'','n5':''},}




for i in range (1,26):
    el = driver.find_element_by_css_selector("#xwd-board > g:nth-child(5) > g:nth-child("+ str(i) +")")
    r = el.find_elements_by_tag_name('text')
    if i<=5:
        h=i
        if len(r) == 0:
            dict_letters['r1']['c'+str(h)] ='-'
    
            
        if len(r)==4:
            dict_letters['r1']['c'+str(h)] =r[2].text
            dict_letters['r1']['n'+str(h)] = r[0].text

#    
        if len(r)==2:
            dict_letters['r1']['c'+str(h)] =r[0].text
    if i>5 and i<=10:
        h=i%5
        if i==10:
            h=5
        if len(r) == 0:
            dict_letters['r2']['c'+str(h)] ='-'

            
        if len(r)==4:
            dict_letters['r2']['c'+str(h)] =r[2].text
            dict_letters['r2']['n'+str(h)] = r[0].text

        if len(r)==2:
            dict_letters['r2']['c'+str(h)] =r[0].text        
    if i>10 and i<=15:
        h=i%10
        
        if len(r) == 0:
            dict_letters['r3']['c'+str(h)] ='-'

    
        if len(r)==4:
            dict_letters['r3']['c'+str(h)] =r[2].text
            dict_letters['r3']['n'+str(h)] = r[0].text


        if len(r)==2:
            dict_letters['r3']['c'+str(h)] =r[0].text
    if i>15 and i<=20:
        h=i%15
        if len(r) == 0:
            dict_letters['r4']['c'+str(h)] ='-'

            
        if len(r)==4:
            dict_letters['r4']['c'+str(h)] =r[2].text
            dict_letters['r4']['n'+str(h)] = r[0].text

        if len(r)==2:
            dict_letters['r4']['c'+str(h)] =r[0].text
            
    if i>20:
        h=i%20
        if len(r) == 0:
            dict_letters['r5']['c'+str(h)] ='-'

    
        if len(r)==4:
            dict_letters['r5']['c'+str(h)] =r[2].text
            dict_letters['r5']['n'+str(h)] = r[0].text

    
        if len(r)==2:
            dict_letters['r5']['c'+str(h)] =r[0].text 
            

    
#to get the original clues from the nyt website    
r = requests.get('https://www.nytimes.com/crosswords/game/mini')
driver2 = BeautifulSoup(r.content, 'lxml')


clues = driver2.find("section",attrs={"class":"Layout-clueLists--10_Xl"})
date = driver2.find("div",attrs={"class":"PuzzleDetails-date--1HNzj"})
date=str(date)
date = date.split(">")  
date=date[3].replace('</div','')
a= str(clues)

clueA =[] # a list of all the Across clues
clueD =[] # a list of all the Down clues
[b1,b2] = a.split('Across')
if len(b2.split('Down'))==2:
    [A,D]= b2.split('Down')
if len(b2.split('Down')) == 4:
    A = (b2.split('Down'))[0]
    D =  b2.split('Down')[1]+b2.split('Down')[2]+b2.split('Down')[3]

[A1,A2,A3,A4,A5,A6]= A.split('<span class="Clue-text--3lZl7">') #n+1 elements where the puzzle is nxn
[D1,D2,D3,D4,D5,D6]= D.split('<span class="Clue-text--3lZl7">')  #n+1 elements where the puzzle is nxn

AA1=A2.split('</span>')
AAA1=AA1[0]
clueA.append(str(AAA1))

AA2=A3.split('</span>')
AAA2=AA2[0]
clueA.append(str(AAA2))

AA3=A4.split('</span>')
AAA3=AA3[0]
clueA.append(str(AAA3))

AA4=A5.split('</span>')
AAA4=AA4[0]
clueA.append(str(AAA4))

AA5=A6.split('</span>')
AAA5=AA5[0]
clueA.append(str(AAA5))

DD1=D2.split('</span>')
DDD1=DD1[0]
clueD.append(str(DDD1))

DD2=D3.split('</span>')
DDD2=DD2[0]
clueD.append(str(DDD2))

DD3=D4.split('</span>')
DDD3=DD3[0]
clueD.append(str(DDD3))

DD4=D5.split('</span>')
DDD4=DD4[0]
clueD.append(str(DDD4))

DD5=D6.split('</span>')
DDD5=DD5[0]
clueD.append(str(DDD5))

#preparing the clues so they are in same form shown on the website
for i in range(len(clueA)):
    if '<' in clueA[i]:
        clueA[i]=clueA[i].replace('<','')
    if '>' in clueA[i]:
        clueA[i]=clueA[i].replace('>','')
    if '\ ' in clueA[i]:
        clueA[i]=clueA[i].replace('\ ','')
        
for i in range(len(clueD)):
    if '<' in clueD[i]:
        clueD[i] = clueD[i].replace('<','')
    if '>' in clueD[i]:
        clueD[i]=clueD[i].replace('>','')
    if '\ ' in clueD[i]:
        clueD[i]=clueD[i].replace('\ ','')
    
     
      
original_clues = []        
                                                                                                        
for i in range(len(clueA)):
    original_clues.append(clueA[i])
for i in range(len(clueD)):
    original_clues.append(clueD[i])

#constructioning solutions/ans of the puzzle form the puzzle grid
#across
sol = ['']*10
sol[0] = dict_letters['r1']['c1'] + dict_letters['r1']['c2'] + dict_letters['r1']['c3']+ dict_letters['r1']['c4']+ dict_letters['r1']['c5']
sol[1] = dict_letters['r2']['c1'] + dict_letters['r2']['c2'] + dict_letters['r2']['c3']+ dict_letters['r2']['c4']+ dict_letters['r2']['c5']
sol[2] = dict_letters['r3']['c1'] + dict_letters['r3']['c2'] + dict_letters['r3']['c3']+ dict_letters['r3']['c4']+ dict_letters['r3']['c5']
sol[3] = dict_letters['r4']['c1'] + dict_letters['r4']['c2'] + dict_letters['r4']['c3']+ dict_letters['r4']['c4']+ dict_letters['r4']['c5']
sol[4] = dict_letters['r5']['c1'] + dict_letters['r5']['c2'] + dict_letters['r5']['c3']+ dict_letters['r5']['c4']+ dict_letters['r5']['c5']
#down
sol[5] = dict_letters['r1']['c1'] + dict_letters['r2']['c1'] + dict_letters['r3']['c1']+ dict_letters['r4']['c1']+ dict_letters['r5']['c1']
sol[6] = dict_letters['r1']['c2'] + dict_letters['r2']['c2'] + dict_letters['r3']['c2']+ dict_letters['r4']['c2']+ dict_letters['r5']['c2']
sol[7] = dict_letters['r1']['c3'] + dict_letters['r2']['c3'] + dict_letters['r3']['c3']+ dict_letters['r4']['c3']+ dict_letters['r5']['c3']
sol[8] = dict_letters['r1']['c4'] + dict_letters['r2']['c4'] + dict_letters['r3']['c4']+ dict_letters['r4']['c4']+ dict_letters['r5']['c4']
sol[9] = dict_letters['r1']['c5'] + dict_letters['r2']['c5'] + dict_letters['r3']['c5']+ dict_letters['r4']['c5']+ dict_letters['r5']['c5']

     
for i in range(len(sol)):
    sol[i] = sol[i].replace('-','')
 
    
#getting across and down 'keys': numbers for the across and down clues
dict_keys = {'a1' : '','a2' : '','a3' : '','a4' : '','a5' : '','d1' : '','d2' : '','d3' : '','d4' : '','d5' : ''}    
key_across=['']*5
key_down=['']*5
for j in range(1,6):
    for i in range(1,6):
        if dict_letters['r'+str(j)]['n'+str(i)] !='' and key_across[j-1] =='': 
            key_across[j-1]=dict_letters['r'+str(j)]['n'+str(i)]
            dict_keys['a'+str(j)] = dict_letters['r'+str(j)]['n'+str(i)]


for i in range(1,5):
    for j in range(1,6):
        if dict_letters['r'+str(i)]['n'+str(j)] !='' and key_down[j-1] =='': 
            key_down[j-1]=dict_letters['r'+str(i)]['n'+str(j)]
            dict_keys['d'+str(j)] = dict_letters['r'+str(i)]['n'+str(j)]


                     

for g in range(1,5):
    if dict_keys['d'+str(g)] > dict_keys['d'+str(g+1)]:
        a = dict_keys['d'+str(g)]
        b= dict_keys['d'+str(g+1)]
        c = sol[g+4]
        d = sol[g+5]
        dict_keys['d'+str(g+1)] = a
        dict_keys['d'+str(g)] = b
        sol[g+4] = d
        sol[g+5] = c


       
#extracting new clues from cambridge dictionary website  
print('extracting new clues from cambridge dictionary website...')
cam_new_clues=['-']*10
a = 0
while a < 10:
    word = (sol[a])
    a+=1
    url = 'https://dictionary.cambridge.org/dictionary/english/'+word
    driver.get(url)
    try:     
        el = driver.find_element_by_xpath('//*[@id="page-content"]/div[2]/div/div[1]/div[2]/div/div[3]/div/div/div[1]/div[3]/div/div[2]/div[1]/div[2]/div')
        cam_new_clues[a-1]=el.text
    except:
        NoSuchElementException
        cam_new_clues[a-1]='-'
    
    
    if '\n' in cam_new_clues[a-1]:      
        cam_new_clues[a-1] = cam_new_clues[a-1].split('\n')[1]
    if ':' in cam_new_clues[a-1]:    
        cam_new_clues[a-1]=cam_new_clues[a-1].replace(':','')

#preparing the clues from cambridge dictionary       
for i in range(len(cam_new_clues)):
    g = cam_new_clues[i]
    if "(" in g:
        g_list= g.split("(")
        cam_new_clues[i] = g_list[0].replace(')','')

for i in range(len(cam_new_clues)):
    g = cam_new_clues[i]
    if ';' in g:
        g_list = g.split(';')
        cam_new_clues[i] = g_list[0]
        
for i in range(len(cam_new_clues)):
    g = cam_new_clues[i]
    if '"' in g:
        g_list = g.split('"')
        cam_new_clues[i] = g_list[0]

for i in range(len(cam_new_clues)):
    g = cam_new_clues[i]
    if ':' in g:
        g_list = g.split(':')
        cam_new_clues[i] = g_list[0]    
        
#extracting new clues from lexico.com    
print('extracting new clues from lexico.com...')
lex_new_clues=['-']*10
a = 0
while a < 10:
    word = sol[a]
    a+=1

    driver = webdriver.Firefox()
    driver.get('https://www.lexico.com/en/definition/'+word)
    try:          
        el = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div/div/div/div/section[1]/ul/li[1]/div/p/span[3]')
        lex_new_clues[a-1] =el.text
    except:
        NoSuchElementException
        lex_new_clues[a-1] ='-'
        
    if lex_new_clues[a-1] =='-':
        try:
            el = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div/div/div/div/section[1]/ul/li[1]/div/p/span[2]')
            lex_new_clues[a-1] =el.text

                
        except:
            NoSuchElementException
            lex_new_clues[a-1] ='-'
       
       
#preparing the clues from the Lexico.com

for i in range(len(lex_new_clues)):
    g = lex_new_clues[i]
    if "(" in g:
        g_list= g.split("(")
        lex_new_clues[i] = g_list[1].replace(')','')

for i in range(len(lex_new_clues)):
    g = lex_new_clues[i]
    if ';' in g:
        g_list = g.split(';')
        lex_new_clues[i] = g_list[0]
        
for i in range(len(lex_new_clues)):
    g = lex_new_clues[i]
    if '"' in g:
        g_list = g.split('"')
        lex_new_clues[i] = g_list[0]

for i in range(len(lex_new_clues)):
    g = lex_new_clues[i]
    if ':' in g:
        g_list = g.split(':')
        lex_new_clues[i] = g_list[0]
        
        
#extracting new clues from wordnet website
print('extracting new clues from wordnet website...')
wn_new_clues = ['-']*10

a = 0
while a < 10:
    word = (sol[a])
    a+=1

    url = "http://wordnetweb.princeton.edu/perl/webwn?s="+word+"&sub=Search+WordNet&o2=&o0=1&o8=1&o1=1&o7=&o5=&o9=&o6=&o3=&o4=&h=000000"
    r = requests.get(url)
    soup = BeautifulSoup(r.content,"lxml")
    try:
        li = soup.select("li")[0]
        wn_new_clues[a-1]=(li.text)
    except IndexError:
        wn_new_clues[a-1]='-'
        
#preparing the clues from wordnet
    
for i in range(len(wn_new_clues)):
    if i != 7:
        g = wn_new_clues[i]
        if "(" in g:
            g_list= g.split("(")
            wn_new_clues[i] = g_list[1].replace(')','')
    if i == 7:
        g = wn_new_clues[i]
        if "(" in g:
            g_list= g.split("(")
            wn_new_clues[i] = g_list[2].replace(')','')

for i in range(len(wn_new_clues)):
    g = wn_new_clues[i]
    if ';' in g:
        g_list = g.split(';')
        wn_new_clues[i] = g_list[0]
        
for i in range(len(wn_new_clues)):
    g = wn_new_clues[i]
    if '"' in g:
        g_list = g.split('"')
        wn_new_clues[i] = g_list[0]

for i in range(len(wn_new_clues)):
    g = wn_new_clues[i]
    if ':' in g:
        g_list = g.split(':')
        wn_new_clues[i] = g_list[0]
        
        
#extracting new clues from dictionary.com
print('extracting new clues from dictionary.com...')
dict_new_clues = ['-']*10
a = 0
while a < 10:
    word = (sol[a])
    a+=1

    url = "https://www.dictionary.com/browse/"+word
    r = requests.get(url)
    soup = BeautifulSoup(r.content,"lxml")
    try:
        definitions = soup.find_all("span",{"class" : "one-click-content"})
        dict_new_clues[a-1]=(definitions[0].text)
    except IndexError:
        dict_new_clues[a-1]='-'
        
    
#preparing the clues from the dictionary.com 
for i in range(len(dict_new_clues)):
    g = dict_new_clues[i]
    if "(" in g:
        g_list= g.split("(")
        dict_new_clues[i] = g_list[1].replace(')','')

for i in range(len(dict_new_clues)):
    g = dict_new_clues[i]
    if ';' in g:
        g_list = g.split(';')
        dict_new_clues[i] = g_list[0]
        
for i in range(len(dict_new_clues)):
    g = dict_new_clues[i]
    if '"' in g:
        g_list = g.split('"')
        dict_new_clues[i] = g_list[0]
        
for i in range(len(dict_new_clues)):
    g = dict_new_clues[i]
    if ':' in g:
        g_list = g.split(':')
        dict_new_clues[i] = g_list[0]      
        
for i in range(len(dict_new_clues)):
    g = dict_new_clues[i]
    if ';' in g:
        g_list = g.split(';')
        dict_new_clues[i] = g_list[0]     
        
#extracting clues from merriam webbster website
print('extracting clues from merriam webbster website...')
mw_new_clues=['-']*10
 
a = 0
while a < 10:
    word = (sol[a])
    a+=1

    url = "https://www.merriam-webster.com/dictionary/"+word
    r = requests.get(url)
    soup = BeautifulSoup(r.content,"lxml")
    # print(soup.select_one('.mw_t_bc').next_sibling.strip())
    definitions = soup.find("span", {"class" : "dt"})    
    
    try:
        tag = definitions.findChild()
        mw_new_clues[a-1]=(tag.find("strong").next_sibling.strip())
    except AttributeError:    
        mw_new_clues[a-1] = '-'
    except TypeError:
        mw_new_clues[a-1] = '-'
        
#preparing the clues from the merriam webster        
for i in range(len(mw_new_clues)):
    g = mw_new_clues[i]
    if "(" in g:
        g_list= g.split("(")
        mw_new_clues[i] = g_list[1].replace(')','')

for i in range(len(mw_new_clues)):
    g = mw_new_clues[i]
    if ';' in g:
        g_list = g.split(';')
        mw_new_clues[i] = g_list[0]
        
for i in range(len(mw_new_clues)):
    g = mw_new_clues[i]
    if '"' in g:
        g_list = g.split('"')
        mw_new_clues[i] = g_list[0]
        
for i in range(len(mw_new_clues)):
    g = mw_new_clues[i]
    if ':' in g:
        g_list = g.split(':')
        mw_new_clues[i] = g_list[0]      
        
for i in range(len(mw_new_clues)):
    g = mw_new_clues[i]
    if ';' in g:
        g_list = g.split(';')
        mw_new_clues[i] = g_list[0]        


#filtering algorithm to select clues, I will use a rule based system        
new_Across = ['no result']*5
new_Down = ['no result']*5

'''
We have three fundamental rules to decide whether each new clue generated from each website meets 
the requirements for a new clue:
1)rule that the clue is not the same as the clue on the nyt website
2)rule if 'no result' for clue      
3)rule for length of new clue 

'''
print('filtering through clues to look for best clue...')

for i in range(5):
    if (cam_new_clues[i]).lower() != (clueA[i]).lower() and cam_new_clues[i] != '-' and ((len(cam_new_clues[i]))<=150 and (len(cam_new_clues[i]))>=20):
        new_Across[i] = cam_new_clues[i]
         
    elif (mw_new_clues[i]).lower() != (clueA[i]).lower() and mw_new_clues[i] != '-' and ((len(mw_new_clues[i]))<=150 and (len(mw_new_clues[i]))>=20):
        new_Across[i] = mw_new_clues[i]
    elif (dict_new_clues[i]).lower() != (clueA[i]).lower() and dict_new_clues[i] != '-' and ((len(dict_new_clues[i]))<=150 and (len(dict_new_clues[i]))>=20):
        new_Across[i] = dict_new_clues[i]
    elif (lex_new_clues[i]).lower() != (clueA[i]).lower() and lex_new_clues[i] != '-' and ((len(lex_new_clues[i]))<=150 and (len(lex_new_clues[i]))>=20):
        new_Across[i] = lex_new_clues[i]
    elif (wn_new_clues[i]).lower() !=(clueA[i]).lower() and wn_new_clues[i] != '-' and ((len(wn_new_clues[i]))<=150 and (len(wn_new_clues[i]))>=20):
        new_Across[i] = wn_new_clues[i]
        
    if (cam_new_clues[i+5]).lower() !=(clueD[i]).lower() and cam_new_clues[i+5] != '-' and ((len(cam_new_clues[i+5]))<=150 and (len(cam_new_clues[i+5]))>=20):
        new_Down[i] = cam_new_clues[i+5]     
    elif (mw_new_clues[i+5]).lower()!=(clueD[i]).lower() and mw_new_clues[i+5] != '-' and ((len(mw_new_clues[i+5]))<=150 and (len(mw_new_clues[i+5]))>=20):
        new_Down[i] = mw_new_clues[i+5]
    elif (dict_new_clues[i+5]).lower() != (clueD[i]).lower() and dict_new_clues[i+5] != '-' and ((len(dict_new_clues[i+5]))<=150 and (len(dict_new_clues[i+5]))>=20):
        new_Down[i] = dict_new_clues[i+5]
    elif (lex_new_clues[i+5]).lower() != (clueD[i]).lower() and lex_new_clues[i+5] != '-' and ((len(lex_new_clues[i+5]))<=150 and (len(lex_new_clues[i+5]))>=20):
        new_Down[i] = lex_new_clues[i+5]
    elif (wn_new_clues[i+5]).lower() != (clueD[i]).lower() and wn_new_clues[i+5] != '-' and ((len(wn_new_clues[i+5]))<=150 and (len(wn_new_clues[i+5]))>=20):
        new_Down[i] = wn_new_clues[i+5]
        




#we account for two special cases, one for when the clue is an abbreviation and the second case is when there is no generated clues
   
        
#we paraphrase the original clue when the answer to the clue is an abbreviation
for i in range(len(new_Across)):
    if 'Abbr.' in clueA[i]:
        abb = clueA[i].replace('Abbr.','')
        abb = abb.replace(':','')
        new_Across[i] = 'Abbreviation of: ' + abb
        
for i in range(len(new_Down)):
    if 'Abbr.' in clueD[i]:
        abb = clueD[i].replace('Abbr.','')
        abb = abb.replace(':','')
        new_Down[i] = 'Abbreviation of: ' + abb 

        
#if the answer is within the new clue it will be blanked out, this is another kind of clue
for i in range(len(new_Across)):
    if sol[i].lower() in (new_Across[i]).lower() and 'Abbr.' not in new_Across[i]:
        l = len(sol[i])
        u = '_'*l
        new_Across[i]=(new_Across[i].lower()).replace(sol[i].lower(),u)
        new_Across[i]=new_Across[i].lower()
        
    if sol[i+5].lower() in new_Down[i].lower() and 'Abbr.' not in new_Down[i]:
        l = len(sol[i+5])
        u = '_'*l
        new_Down[i]=(new_Down[i].lower()).replace((sol[i+5]).lower(),u)
        new_Down[i] = new_Down[i].lower()
        
#if there is no result' (no new clue generated) after all the rules have been applied to the clues from each website, then the original clue will be displayed
for i in range(len(new_Across)):
    if new_Across[i]=='no result':
        new_Across[i] = clueA[i]
    if new_Down[i]=='no result':
        new_Down[i] = clueD[i] 
        
        
#making the first letter of each new clue a capital letter
new_across =['']*5
new_down = ['']*5        
for i in range(len(new_Across)):
    a = new_Across[i][0].upper()
    c = new_Down[i][0].upper()  
    for j in range(len(new_Across[i])):
        b = a + new_Across[i][1:]
        d = c + new_Down[i][1:]
        
        new_across[i] = b
        new_down[i] = d
    
    
    
#Code for GUI

#initializing window
window = tkinter.Tk()
    
#small numbers for 'small' numbers in the puzzle grid
keys = {1: u"\u00B9",2: u"\u00B2",3: u"\u00B3",4: u"\u2074",5: u"\u2075",6: u"\u2076",7: u"\u2077",8: u"\u2078",9: u"\u2079",10: u"\u2080"}

window.title("New York Times Mini CrossWord new clues generator")
window.geometry("1366x768")

#headers of Across and Down cluelist
tkinter.Label(window, text="Across",font='Helvetica 20 bold').grid(row=0, column=9)
tkinter.Label(window, text="Down",font='Helvetica 20 bold').grid(row=0, column=11)

#headers of new Across and Down cluelist
tkinter.Label(window, text="New Across",font='Helvetica 20 bold').grid(row=6, column=9,pady=(20, 20)) 
tkinter.Label(window, text="New Down",font='Helvetica 20 bold').grid(row=6, column=11,pady=(20, 20))


#to make grid in the GUI
for r in range(1,6):
    for c in range(1,6):
                        
        if dict_letters['r'+str(r)]['c'+str(c)] != '-' and dict_letters['r'+str(r)]['n'+str(c)]=='':
            tkinter.Label(window,text= " "+ dict_letters['r'+str(r)]['c'+str(c)],font=("Helvetica", 15), foreground="Black", borderwidth="4", relief="groove", height=2, width=4).grid(row=r,column=c)
        
        if dict_letters['r'+str(r)]['c'+str(c)] == '-':
            tkinter.Label(window,bg='Black',font=("Helvetica", 15), foreground="Black", borderwidth="4", height=2, width=4).grid(row=r,column=c)  
        if dict_letters['r'+str(r)]['c'+str(c)] != '-' and dict_letters['r'+str(r)]['n'+str(c)]!='':
            tkinter.Label(window, text=keys[int(dict_letters['r'+str(r)]['n'+str(c)])] + " " + dict_letters['r'+str(r)]['c'+str(c)],font=("Helvetica", 15), foreground="Black", borderwidth="4", relief="groove", height=2, width=4).grid(row=r, column=c)
   


for x in range(1, len(new_across) + 1):
    if len(new_across[x-1])>1:
        tkinter.Label(window, text=' ', borderwidth="3").grid(row=len(new_across) + 1+ x, column=7,padx=(10, 0), pady =(5,5))

#across original
for x in range(1, len(clueA) + 1):
    if len(clueA[x-1])>1:
        tkinter.Label(window, text=clueA[x - 1],anchor='w', borderwidth="3", bg="White", height = 2, width=55, wraplength =395).grid(row=x, column=9)
           
for y in range(len(key_across)):
    tkinter.Label(window, text=dict_keys['a'+str(y+1)], borderwidth="3", height = 2, width=1).grid(row=y+1, column=8)    
#down original
for x in range(1, len(clueD) + 1):
    if len(clueD[x-1])>1:
        tkinter.Label(window, text=clueD[x - 1], anchor='w', borderwidth="3", bg="White", width=55,height = 2, wraplength =395).grid(row=x,column=11)
for y in range(len(key_down)):
    tkinter.Label(window, text=dict_keys['d'+str(y+1)], borderwidth="3", width=1,height = 2).grid(row=y+1, column=10)            
        
#displaying generated across clues
for x in range(1, len(new_across) + 1):
    if len(new_Across[x-1])>1:
        tkinter.Label(window, text=new_across[x-1], anchor='w',borderwidth="3", bg="White", height=2, width=55, wraplength =395).grid(row=len(new_Across) + 1+ x, column=9,padx=(10, 0), pady =(5,5))
#displaying the small numbers in the list for the generated across clues
for y in range(len(key_across)):
    tkinter.Label(window, text=dict_keys['a'+str(y+1)], borderwidth="3",height=2, width=1).grid(row=y+7, column=8)    
    
#displaying generated down clues
for x in range(1, len(new_down) + 1):
    if len(new_down[x-1])>1:
        tkinter.Label(window, text=new_down[x-1], anchor='w',borderwidth="3", bg="White", height=2, width=55, wraplength=395).grid(row=len(new_Down) + 1 + x, column=11,padx=(10, 0), pady =(5,5))
#displaying the small numbers in the list for the generated down clues
for y in range(len(key_down)):
    tkinter.Label(window, text=dict_keys['d'+str(y+1)], borderwidth="3", width=1,height=2).grid(row=y+7, column=10)    

#Date = upload_file[-4]
name = 'WATSON'

tkinter.Label(window, text="Date:").grid(row=7, column=1)
tkinter.Label(window, text=today1).grid(row=7, column=2)
tkinter.Label(window, text='Group').grid(row=8, column=1)
tkinter.Label(window, text='name:').grid(row=8, column=2)
tkinter.Label(window, text=name).grid(row=8, column=3)

window.mainloop()

