import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import streamlit as st

init = np.array([0,1,2,3,4,5,6,7])
i1 = np.array([4,0,2,3,5,1,6,7])
i2 = np.array([1,5,2,3,0,4,6,7])
i5 = np.array([0,1,6,2,4,5,7,3])
i6 = np.array([0,1,3,7,4,5,2,6])
a = np.array([1,0,2])

i3 = np.array([4,1,0,3,6,5,2,7])
i4 = np.array([2,1,6,3,0,5,4,7])
i7 = np.array([0,5,2,1,4,7,6,3])
i8 = np.array([0,3,2,7,4,1,6,5])
b = np.array([2,1,0])

i9 = np.array([0,1,2,3,6,4,7,5])
i10 = np.array([0,1,2,3,5,7,4,6])
i11 = np.array([2,0,3,1,4,5,6,7])
i12 = np.array([1,3,0,2,4,5,6,7])
c = np.array([0,2,1])
d = np.array([0,1,2])

col1, col2, col3 = st.columns(3)

with col1:

    st.image('Capture3.jpg', caption = 'truc')

with col2:

    st.write('Inscrivez le rang du mouvement que vous sélectionnez comme mouvement n° X: 0=i1, 1=i2, 2=i3, 3=i4, 4=i5, 5=i6, 6=i7, 7=i8, 8=i9, 9=i10, 10=i11, 11=i12, NOTA : i9 et i10 sont face arrière')

    Index_Mouvement_1 = st.selectbox(
        'Sélectionnez le rang du mouvement n° 1',
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    Index_Mouvement_2 = st.selectbox(
        'Sélectionnez le rang du mouvement n° 2',
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])  

    Index_Mouvement_3 = st.selectbox(
        'Sélectionnez le rang du mouvement n° 3',
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    Index_Mouvement_4 = st.selectbox(
        'Sélectionnez le rang du mouvement n° 4',
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    Index_Mouvement_5 = st.selectbox(
        'Sélectionnez le rang du mouvement n° 5',
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    Index_Mouvement_6 = st.selectbox(
        'Sélectionnez le rang du mouvement n° 6',
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])  

    Index_Mouvement_7 = st.selectbox(
        'Sélectionnez le rang du mouvement n° 7',
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    Index_Mouvement_8 = st.selectbox(
        'Sélectionnez le rang du mouvement n° 8',
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    Index_Mouvement_9 = st.selectbox(
        'Sélectionnez le rang du mouvement n° 9',
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    Index_Mouvement_10 = st.selectbox(
        'Sélectionnez le rang du mouvement n° 10',
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])  

    Index_Mouvement_11 = st.selectbox(
        'Sélectionnez le rang du mouvement n° 11',
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    Index_Mouvement_12 = st.selectbox(
        'Sélectionnez le rang du mouvement n° 12',
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

liste = [[i1,a], [i2,a], [i3,b],[i4,b], [i5,a], [i6,a], [i7,b], [i8,b], [i9,c], [i10,c], [i11,c], [i12,c]]

Mv1 = liste[Index_Mouvement_1][0]
Mv2 = liste[Index_Mouvement_2][0]
Mv3 = liste[Index_Mouvement_3][0]
Mv4 = liste[Index_Mouvement_4][0]
Mv5 = liste[Index_Mouvement_5][0]
Mv6 = liste[Index_Mouvement_6][0]
Mv7 = liste[Index_Mouvement_7][0]
Mv8 = liste[Index_Mouvement_8][0]
Mv9 = liste[Index_Mouvement_9][0]
Mv10 = liste[Index_Mouvement_10][0]
Mv11 = liste[Index_Mouvement_11][0]
Mv12 = liste[Index_Mouvement_12][0]

cpl1 = liste[Index_Mouvement_1][1]
cpl2 = liste[Index_Mouvement_2][1]
cpl3 = liste[Index_Mouvement_3][1]
cpl4 = liste[Index_Mouvement_4][1]
cpl5 = liste[Index_Mouvement_5][1]
cpl6 = liste[Index_Mouvement_6][1]
cpl7 = liste[Index_Mouvement_7][1]
cpl8 = liste[Index_Mouvement_8][1]
cpl9 = liste[Index_Mouvement_9][1]
cpl10 = liste[Index_Mouvement_10][1]
cpl11 = liste[Index_Mouvement_11][1]
cpl12 = liste[Index_Mouvement_12][1]

def moving_the_cube(e,f,g,h,i,j,k,l,m,n,o,p):
    lista = [init]
    lista.append(e)
    lista.append(e[f])
    lista.append(e[f[g]])
    lista.append(e[f[g[h]]])
    lista.append(e[f[g[h[i]]]])
    lista.append(e[f[g[h[i[j]]]]])
    lista.append(e[f[g[h[i[j[k]]]]]])
    lista.append(e[f[g[h[i[j[k[l]]]]]]])
    lista.append(e[f[g[h[i[j[k[l[m]]]]]]]])
    lista.append(e[f[g[h[i[j[k[l[m[n]]]]]]]]])
    lista.append(e[f[g[h[i[j[k[l[m[n[o]]]]]]]]]])
    lista.append(e[f[g[h[i[j[k[l[m[n[o[p]]]]]]]]]]])
    return pd.DataFrame(lista, columns=['0', '1', '2', '3', '4', '5', '6', '7'])

df = moving_the_cube(Mv1,Mv2,Mv3,Mv4,Mv5,Mv6,Mv7,Mv8,Mv9,Mv10,Mv11,Mv12)

pas_1 = df.loc[0].compare(df.loc[1])
pas_2 = df.loc[1].compare(df.loc[2])
pas_3 = df.loc[2].compare(df.loc[3])
pas_4 = df.loc[3].compare(df.loc[4])
pas_5 = df.loc[4].compare(df.loc[5])
pas_6 = df.loc[5].compare(df.loc[6])
pas_7 = df.loc[6].compare(df.loc[7])
pas_8 = df.loc[7].compare(df.loc[8])
pas_9 = df.loc[8].compare(df.loc[9])
pas_10 = df.loc[9].compare(df.loc[10])
pas_11 = df.loc[10].compare(df.loc[11])
pas_12 = df.loc[11].compare(df.loc[12])

pas_1 = pas_1.loc[:,[False, True]]
pas_2 = pas_2.loc[:,[False, True]]
pas_3 = pas_3.loc[:,[False, True]]
pas_4 = pas_4.loc[:,[False, True]]
pas_5 = pas_5.loc[:,[False, True]]
pas_6 = pas_6.loc[:,[False, True]]
pas_7 = pas_7.loc[:,[False, True]]
pas_8 = pas_8.loc[:,[False, True]]
pas_9 = pas_9.loc[:,[False, True]]
pas_10 = pas_10.loc[:,[False, True]]
pas_11 = pas_11.loc[:,[False, True]]
pas_12 = pas_12.loc[:,[False, True]]
pd.concat([pas_1, pas_2,pas_3, pas_4,pas_5, pas_6,pas_7, pas_8,pas_9, pas_10,pas_11, pas_12])
tableau_de_comparaison_mini_cubes = pd.concat([pas_1, pas_2,pas_3, pas_4,pas_5, pas_6,pas_7, pas_8,pas_9, pas_10,pas_11, pas_12]).to_numpy()
tcmc = tableau_de_comparaison_mini_cubes.reshape(12,4)

def path_minicub(x,y,z,t,u,v,w,s):
    list_test_1 = []
    list_test_2 = []
    list_test_3 = []
    list_test_4 = []
    list_test_5 = []
    list_test_6 = []
    list_test_7 = []
    list_test_8 = []
    if x in tcmc[0]:
        list_test_1.append(cpl1)
    else : list_test_1.append(d)
    if x in tcmc[1]:
        list_test_1.append(cpl2)
    else : list_test_1.append(d)
    if x in tcmc[2]:
        list_test_1.append(cpl3)
    else : list_test_1.append(d)
    if x in tcmc[3]:
        list_test_1.append(cpl4)
    else : list_test_1.append(d)
    if x in tcmc[4]:
        list_test_1.append(cpl5)
    else : list_test_1.append(d)
    if x in tcmc[5]:
        list_test_1.append(cpl6)
    else : list_test_1.append(d)
    if x in tcmc[6]:
        list_test_1.append(cpl7)
    else : list_test_1.append(d)
    if x in tcmc[7]:
        list_test_1.append(cpl8)
    else : list_test_1.append(d)
    if x in tcmc[8]:
        list_test_1.append(cpl9)
    else : list_test_1.append(d)
    if x in tcmc[9]:
        list_test_1.append(cpl10)
    else : list_test_1.append(d)
    if x in tcmc[10]:
        list_test_1.append(cpl11)
    else : list_test_1.append(d)
    if x in tcmc[11]:
        list_test_1.append(cpl12)
    else : list_test_1.append(d)
    if y in tcmc[0]:
        list_test_2.append(cpl1)
    else : list_test_2.append(d)
    if y in tcmc[1]:
        list_test_2.append(cpl2)
    else : list_test_2.append(d)
    if y in tcmc[2]:
        list_test_2.append(cpl3)
    else : list_test_2.append(d)
    if y in tcmc[3]:
        list_test_2.append(cpl4)
    else : list_test_2.append(d)
    if y in tcmc[4]:
        list_test_2.append(cpl5)
    else : list_test_2.append(d)
    if y in tcmc[5]:
        list_test_2.append(cpl6)
    else : list_test_2.append(d)
    if y in tcmc[6]:
        list_test_2.append(cpl7)
    else : list_test_2.append(d)
    if y in tcmc[7]:
        list_test_2.append(cpl8)
    else : list_test_2.append(d)
    if y in tcmc[8]:
        list_test_2.append(cpl9)
    else : list_test_2.append(d)
    if y in tcmc[9]:
        list_test_2.append(cpl10)
    else : list_test_2.append(d)
    if y in tcmc[10]:
        list_test_2.append(cpl11)
    else : list_test_2.append(d)
    if y in tcmc[11]:
        list_test_2.append(cpl12)
    else : list_test_2.append(d)
    if z in tcmc[0]:
        list_test_3.append(cpl1)
    else : list_test_3.append(d)
    if z in tcmc[1]:
        list_test_3.append(cpl2)
    else : list_test_3.append(d)
    if z in tcmc[2]:
        list_test_3.append(cpl3)
    else : list_test_3.append(d)
    if z in tcmc[3]:
        list_test_3.append(cpl4)
    else : list_test_3.append(d)
    if z in tcmc[4]:
        list_test_3.append(cpl5)
    else : list_test_3.append(d)
    if z in tcmc[5]:
        list_test_3.append(cpl6)
    else : list_test_3.append(d)
    if z in tcmc[6]:
        list_test_3.append(cpl7)
    else : list_test_3.append(d)
    if z in tcmc[7]:
        list_test_3.append(cpl8)
    else : list_test_3.append(d)
    if z in tcmc[8]:
        list_test_3.append(cpl9)
    else : list_test_3.append(d)
    if z in tcmc[9]:
        list_test_3.append(cpl10)
    else : list_test_3.append(d)
    if z in tcmc[10]:
        list_test_3.append(cpl11)
    else : list_test_3.append(d)
    if z in tcmc[11]:
        list_test_3.append(cpl12)
    else : list_test_3.append(d)
    if t in tcmc[0]:
        list_test_4.append(cpl1)
    else : list_test_4.append(d)
    if t in tcmc[1]:
        list_test_4.append(cpl2)
    else : list_test_4.append(d)
    if t in tcmc[2]:
        list_test_4.append(cpl3)
    else : list_test_4.append(d)
    if t in tcmc[3]:
        list_test_4.append(cpl4)
    else : list_test_4.append(d)
    if t in tcmc[4]:
        list_test_4.append(cpl5)
    else : list_test_4.append(d)
    if t in tcmc[5]:
        list_test_4.append(cpl6)
    else : list_test_4.append(d)
    if t in tcmc[6]:
        list_test_4.append(cpl7)
    else : list_test_4.append(d)
    if t in tcmc[7]:
        list_test_4.append(cpl8)
    else : list_test_4.append(d)
    if t in tcmc[8]:
        list_test_4.append(cpl9)
    else : list_test_4.append(d)
    if t in tcmc[9]:
        list_test_4.append(cpl10)
    else : list_test_4.append(d)
    if t in tcmc[10]:
        list_test_4.append(cpl11)
    else : list_test_4.append(d)
    if t in tcmc[11]:
        list_test_4.append(cpl12)
    else : list_test_4.append(d)
    if u in tcmc[0]:
        list_test_5.append(cpl1)
    else : list_test_5.append(d)
    if u in tcmc[1]:
        list_test_5.append(cpl2)
    else : list_test_5.append(d)
    if u in tcmc[2]:
        list_test_5.append(cpl3)
    else : list_test_5.append(d)
    if u in tcmc[3]:
        list_test_5.append(cpl4)
    else : list_test_5.append(d)
    if u in tcmc[4]:
        list_test_5.append(cpl5)
    else : list_test_5.append(d)
    if u in tcmc[5]:
        list_test_5.append(cpl6)
    else : list_test_5.append(d)
    if u in tcmc[6]:
        list_test_5.append(cpl7)
    else : list_test_5.append(d)
    if u in tcmc[7]:
        list_test_5.append(cpl8)
    else : list_test_5.append(d)
    if u in tcmc[8]:
        list_test_5.append(cpl9)
    else : list_test_5.append(d)
    if u in tcmc[9]:
        list_test_5.append(cpl10)
    else : list_test_5.append(d)
    if u in tcmc[10]:
        list_test_5.append(cpl11)
    else : list_test_5.append(d)
    if u in tcmc[11]:
        list_test_5.append(cpl12)
    else : list_test_5.append(d) 
    if v in tcmc[0]:
        list_test_6.append(cpl1)
    else : list_test_6.append(d)
    if v in tcmc[1]:
        list_test_6.append(cpl2)
    else : list_test_6.append(d)
    if v in tcmc[2]:
        list_test_6.append(cpl3)
    else : list_test_6.append(d)
    if v in tcmc[3]:
        list_test_6.append(cpl4)
    else : list_test_6.append(d)
    if v in tcmc[4]:
        list_test_6.append(cpl5)
    else : list_test_6.append(d)
    if v in tcmc[5]:
        list_test_6.append(cpl6)
    else : list_test_6.append(d)
    if v in tcmc[6]:
        list_test_6.append(cpl7)
    else : list_test_6.append(d)
    if v in tcmc[7]:
        list_test_6.append(cpl8)
    else : list_test_6.append(d)
    if v in tcmc[8]:
        list_test_6.append(cpl9)
    else : list_test_6.append(d)
    if v in tcmc[9]:
        list_test_6.append(cpl10)
    else : list_test_6.append(d)
    if v in tcmc[10]:
        list_test_6.append(cpl11)
    else : list_test_6.append(d)
    if v in tcmc[11]:
        list_test_6.append(cpl12)
    else : list_test_6.append(d)    
    if w in tcmc[0]:
        list_test_7.append(cpl1)
    else : list_test_7.append(d)
    if w in tcmc[1]:
        list_test_7.append(cpl2)
    else : list_test_7.append(d)
    if w in tcmc[2]:
        list_test_7.append(cpl3)
    else : list_test_7.append(d)
    if w in tcmc[3]:
        list_test_7.append(cpl4)
    else : list_test_7.append(d)
    if w in tcmc[4]:
        list_test_7.append(cpl5)
    else : list_test_7.append(d)
    if w in tcmc[5]:
        list_test_7.append(cpl6)
    else : list_test_7.append(d)
    if w in tcmc[6]:
        list_test_7.append(cpl7)
    else : list_test_7.append(d)
    if w in tcmc[7]:
        list_test_7.append(cpl8)
    else : list_test_7.append(d)
    if w in tcmc[8]:
        list_test_7.append(cpl9)
    else : list_test_7.append(d)
    if w in tcmc[9]:
        list_test_7.append(cpl10)
    else : list_test_7.append(d)
    if w in tcmc[10]:
        list_test_7.append(cpl11)
    else : list_test_7.append(d)
    if w in tcmc[11]:
        list_test_7.append(cpl12)
    else : list_test_7.append(d)
    if s in tcmc[0]:
        list_test_8.append(cpl1)
    else : list_test_8.append(d)
    if s in tcmc[1]:
        list_test_8.append(cpl2)
    else : list_test_8.append(d)
    if s in tcmc[2]:
        list_test_8.append(cpl3)
    else : list_test_8.append(d)
    if s in tcmc[3]:
        list_test_8.append(cpl4)
    else : list_test_8.append(d)
    if s in tcmc[4]:
        list_test_8.append(cpl5)
    else : list_test_8.append(d)
    if s in tcmc[5]:
        list_test_8.append(cpl6)
    else : list_test_8.append(d)
    if s in tcmc[6]:
        list_test_8.append(cpl7)
    else : list_test_8.append(d)
    if s in tcmc[7]:
        list_test_8.append(cpl8)
    else : list_test_8.append(d)
    if s in tcmc[8]:
        list_test_8.append(cpl9)
    else : list_test_8.append(d)
    if s in tcmc[9]:
        list_test_8.append(cpl10)
    else : list_test_8.append(d)
    if s in tcmc[10]:
        list_test_8.append(cpl11)
    else : list_test_8.append(d)
    if s in tcmc[11]:
        list_test_8.append(cpl12)
    else : list_test_8.append(d)
    return list_test_1,list_test_2,list_test_3,list_test_4,list_test_5,list_test_6,list_test_7,list_test_8

result = path_minicub(0,1,2,3,4,5,6,7)

aa1 = result[0][0]
aa2 = result[0][1]
aa3 = result[0][2]
aa4 = result[0][3]
aa5 = result[0][4]
aa6 = result[0][5]
aa7 = result[0][6]
aa8 = result[0][7]
aa9 = result[0][8]
aa10 = result[0][9]
aa11 = result[0][10]
aa12 = result[0][11]

bb1 = result[1][0]
bb2 = result[1][1]
bb3 = result[1][2]
bb4 = result[1][3]
bb5 = result[1][4]
bb6 = result[1][5]
bb7 = result[1][6]
bb8 = result[1][7]
bb9 = result[1][8]
bb10 = result[1][9]
bb11 = result[1][10]
bb12 = result[1][11]

cc1 = result[2][0]
cc2 = result[2][1]
cc3 = result[2][2]
cc4 = result[2][3]
cc5 = result[2][4]
cc6 = result[2][5]
cc7 = result[2][6]
cc8 = result[2][7]
cc9 = result[2][8]
cc10 = result[2][9]
cc11 = result[2][10]
cc12 = result[2][11]

dd1 = result[3][0]
dd2 = result[3][1]
dd3 = result[3][2]
dd4 = result[3][3]
dd5 = result[3][4]
dd6 = result[3][5]
dd7 = result[3][6]
dd8 = result[3][7]
dd9 = result[3][8]
dd10 = result[3][9]
dd11 = result[3][10]
dd12 = result[3][11]

ee1 = result[4][0]
ee2 = result[4][1]
ee3 = result[4][2]
ee4 = result[4][3]
ee5 = result[4][4]
ee6 = result[4][5]
ee7 = result[4][6]
ee8 = result[4][7]
ee9 = result[4][8]
ee10 = result[4][9]
ee11 = result[4][10]
ee12 = result[4][11]

ff1 = result[5][0]
ff2 = result[5][1]
ff3 = result[5][2]
ff4 = result[5][3]
ff5 = result[5][4]
ff6 = result[5][5]
ff7 = result[5][6]
ff8 = result[5][7]
ff9 = result[5][8]
ff10 = result[5][9]
ff11 = result[5][10]
ff12 = result[5][11]

gg1 = result[6][0]
gg2 = result[6][1]
gg3 = result[6][2]
gg4 = result[6][3]
gg5 = result[6][4]
gg6 = result[6][5]
gg7 = result[6][6]
gg8 = result[6][7]
gg9 = result[6][8]
gg10 = result[6][9]
gg11 = result[6][10]
gg12 = result[6][11]

hh1 = result[7][0]
hh2 = result[7][1]
hh3 = result[7][2]
hh4 = result[7][3]
hh5 = result[7][4]
hh6 = result[7][5]
hh7 = result[7][6]
hh8 = result[7][7]
hh9 = result[7][8]
hh10 = result[7][9]
hh11 = result[7][10]
hh12 = result[7][11]

K1 = aa1[aa2[aa3[aa4[aa5[aa6[aa7[aa8[aa9[aa10[aa11[aa12]]]]]]]]]]]
K2 = bb1[bb2[bb3[bb4[bb5[bb6[bb7[bb8[bb9[bb10[bb11[bb12]]]]]]]]]]]
K3 = cc1[cc2[cc3[cc4[cc5[cc6[cc7[cc8[cc9[cc10[cc11[cc12]]]]]]]]]]]
K4 = dd1[dd2[dd3[dd4[dd5[dd6[dd7[dd8[dd9[dd10[dd11[dd12]]]]]]]]]]]
K5 = ee1[ee2[ee3[ee4[ee5[ee6[ee7[ee8[ee9[ee10[ee11[ee12]]]]]]]]]]]
K6 = ff1[ff2[ff3[ff4[ff5[ff6[ff7[ff8[ff9[ff10[ff11[ff12]]]]]]]]]]]
K7 = gg1[gg2[gg3[gg4[gg5[gg6[gg7[gg8[gg9[gg10[gg11[gg12]]]]]]]]]]]
K8 = hh1[hh2[hh3[hh4[hh5[hh6[hh7[hh8[hh9[hh10[hh11[hh12]]]]]]]]]]]

data_colori = { 'Face' :['r','r','r','r','m','m','m','m'], 'Côté':['b', 'g', 'b', 'g', 'b', 'g', 'b', 'g'], 'Top':['y', 'y', 'w', 'w', 'y', 'y', 'w', 'w'] }
 
tableau = pd.DataFrame(data_colori)

def foo(x,y,z,t,u,v,w,s):
    cub_init_0 = tableau.loc[0]
    cub_init_1 = tableau.loc[1]
    cub_init_2 = tableau.loc[2]
    cub_init_3 = tableau.loc[3]
    cub_init_4 = tableau.loc[4]
    cub_init_5 = tableau.loc[5]
    cub_init_6 = tableau.loc[6]
    cub_init_7 = tableau.loc[7]
    return cub_init_0[x[0]],cub_init_0[x[1]],cub_init_0[x[2]], cub_init_1[y[0]],cub_init_1[y[1]],cub_init_1[y[2]],cub_init_2[z[0]],cub_init_2[z[1]],cub_init_2[z[2]],cub_init_3[t[0]],cub_init_3[t[1]],cub_init_3[t[2]],cub_init_4[u[0]],cub_init_4[u[1]],cub_init_4[u[2]],cub_init_5[v[0]],cub_init_5[v[1]],cub_init_5[v[2]],cub_init_6[w[0]],cub_init_6[w[1]],cub_init_6[w[2]],cub_init_7[s[0]],cub_init_7[s[1]],cub_init_7[s[2]]

result2 = foo(K1,K2,K3,K4,K5,K6,K7,K8)
fii = pd.DataFrame(result2)
gii = fii.to_numpy

aaa = np.array([fii[0][0],fii[0][1],fii[0][2],fii[0][3],fii[0][4],fii[0][5],fii[0][6],fii[0][7],fii[0][8],fii[0][9],fii[0][10],fii[0][11],fii[0][12],fii[0][13],fii[0][14],fii[0][15],fii[0][16],fii[0][17],fii[0][18],fii[0][19],fii[0][20],fii[0][21],fii[0][22],fii[0][23]])
aaa.reshape(8,3)

def goo(fii):
    aaa = np.array([fii[0][0],fii[0][1],fii[0][2],fii[0][3],fii[0][4],fii[0][5],fii[0][6],fii[0][7],fii[0][8],fii[0][9],fii[0][10],fii[0][11],fii[0][12],fii[0][13],fii[0][14],fii[0][15],fii[0][16],fii[0][17],fii[0][18],fii[0][19],fii[0][20],fii[0][21],fii[0][22],fii[0][23]])
    return aaa.reshape(8,3)

result3 = goo(fii)
googoo = pd.DataFrame(result3)

def coloriage(R):
    if R == 'b':
        return 'background-color: blue'
    elif R == 'g':
        return 'background-color: green'
    elif R == 'w':
        return 'background-color: white'
    elif R == 'y':
        return 'background-color: yellow'
    elif R == 'r':
        return 'background-color: red'
    elif R == 'm':
        return 'background-color: orange'

mvk = Mv1[Mv2[Mv3[Mv4[Mv5[Mv6[Mv7[Mv8[Mv9[Mv10[Mv11[Mv12]]]]]]]]]]]
result4 = result3[mvk[0]],result3[mvk[1]],result3[mvk[2]],result3[mvk[3]],result3[mvk[4]],result3[mvk[5]],result3[mvk[6]],result3[mvk[7]]
tabl = pd.DataFrame(result4)

foofoo = tabl.set_axis(['Face','Côté','Top'], axis=1)
garb = foofoo.style.applymap(coloriage)

tableaus = tableau.style.applymap(coloriage)

someX, someY = 0.80, 0.50
plt.style.use('dark_background')
fig = plt.figure()
currentAxis = plt.gca()

hei = [tabl.loc[7][1], tabl.loc[3][1],tabl.loc[1][1], tabl.loc[5][1],tabl.loc[2][1], tabl.loc[6][1],tabl.loc[0][1],
       tabl.loc[4][1],tabl.loc[6][0], tabl.loc[4][0], tabl.loc[5][0],tabl.loc[7][0], tabl.loc[3][0],tabl.loc[2][0],
       tabl.loc[0][0],tabl.loc[1][0], tabl.loc[3][2],tabl.loc[7][2],tabl.loc[6][2],tabl.loc[2][2], tabl.loc[5][2],
       tabl.loc[1][2], tabl.loc[0][2],tabl.loc[4][2]]

currentAxis.add_patch(Rectangle((someX - .2, someY - .1), 0.1, 0.1, color = hei[0], alpha=0.9))
currentAxis.add_patch(Rectangle((someX - .3, someY - .1), 0.1, 0.1, color = hei[1], alpha=0.9))
currentAxis.add_patch(Rectangle((someX - .3, someY - .0), 0.1, 0.1, color = hei[2], alpha=0.9))
currentAxis.add_patch(Rectangle((someX - .2, someY - .0), 0.1, 0.1, color = hei[3], alpha=0.9))
currentAxis.add_patch(Rectangle((someX - .6, someY - .1), 0.1, 0.1, color = hei[4], alpha=0.9))
currentAxis.add_patch(Rectangle((someX - .7, someY - .1), 0.1, 0.1, color = hei[5], alpha=0.9))
currentAxis.add_patch(Rectangle((someX - .6, someY - .0), 0.1, 0.1, color = hei[6], alpha=0.9))
currentAxis.add_patch(Rectangle((someX - .7, someY - .0), 0.1, 0.1, color = hei[7], alpha=0.9))
currentAxis.add_patch(Rectangle((someX + .0, someY - .1), 0.1, 0.1, color = hei[8], alpha=0.9))
currentAxis.add_patch(Rectangle((someX - .0, someY - .0), 0.1, 0.1, color = hei[9], alpha=0.9))
currentAxis.add_patch(Rectangle((someX - .1, someY - .0), 0.1, 0.1, color = hei[10], alpha=0.9))
currentAxis.add_patch(Rectangle((someX - .1, someY - .1), 0.1, 0.1, color = hei[11], alpha=0.9))
currentAxis.add_patch(Rectangle((someX - .4, someY - .1), 0.1, 0.1, color = hei[12], alpha=0.9))
currentAxis.add_patch(Rectangle((someX - .5, someY - .1), 0.1, 0.1, color = hei[13], alpha=0.9))
currentAxis.add_patch(Rectangle((someX - .5, someY - .0), 0.1, 0.1, color = hei[14], alpha=0.9))
currentAxis.add_patch(Rectangle((someX - .4, someY - .0), 0.1, 0.1, color = hei[15], alpha=0.9))
currentAxis.add_patch(Rectangle((someX - .3, someY - .2), 0.1, 0.1, color = hei[16], alpha=0.9))
currentAxis.add_patch(Rectangle((someX - .2, someY - .2), 0.1, 0.1, color = hei[17], alpha=0.9))
currentAxis.add_patch(Rectangle((someX - .2, someY - .3), 0.1, 0.1, color = hei[18], alpha=0.9))
currentAxis.add_patch(Rectangle((someX - .3, someY - .3), 0.1, 0.1, color = hei[19], alpha=0.9))
currentAxis.add_patch(Rectangle((someX - .2, someY + .1), 0.1, 0.1, color = hei[20], alpha=0.9))
currentAxis.add_patch(Rectangle((someX - .3, someY + .1), 0.1, 0.1, color = hei[21], alpha=0.9))
currentAxis.add_patch(Rectangle((someX - .3, someY + .2), 0.1, 0.1, color = hei[22], alpha=0.9))
currentAxis.add_patch(Rectangle((someX - .2, someY + .2), 0.1, 0.1, color = hei[23], alpha=0.9))

plt.grid()
plt.show()

with col3:

    st.write('le cube de départ est:', tableaus)
    st.write('le cube d arrivée est:')
    st.pyplot(fig)
    
    if tableau.equals(foofoo) == True:
        st.balloons()