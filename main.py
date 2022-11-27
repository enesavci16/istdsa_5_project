

import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image
from sklearn.feature_extraction.text import TfidfVectorizer

df=pd.read_csv("jobs.csv")
df.drop(["Unnamed: 0"],axis=1,inplace=True)
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(stop_words='english') # TF-IDF yöntemini kullanalım

tfidf_matrix = tfidf.fit_transform(df['job_dscription'])
from sklearn.metrics.pairwise import cosine_similarity # Hesaplaması biraz zaman alabilir
cosine_sim = cosine_similarity(tfidf_matrix)


indices = pd.Series(df.index, index=df['job_name'])

image_ist = Image.open('akademi.jpeg')

image_2 = Image.open('jobs_header_1.png')
st.image(image_ist)
st.image(image_2)
st.title('BEST JOBS')



st.sidebar.header('INPUT')

a = st.text_input('First enry jobs:','Data Scientist')
b = st.text_input('Second enry jobs:','Physician')
c = st.text_input('Third enry jobs:','Medical and Health Services Manager')


def get_recommendations(job_name, cosine_sim=cosine_sim):
    idx = indices[str(job_name)]  # Her bir biraya karşılık gelen index değerleri

    sim_scores = list(enumerate(cosine_sim[idx]))  # Biralar arasındaki ikili benzerlik puanları

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)  # Benzerlik oranlarına göre sıralama

    sim_scores = sim_scores[1:11]  # En benzer 10 bira

    beer_indices = [i[0] for i in sim_scores]  # Bu biraların index değerleri

    set_ = df['job_name'].iloc[beer_indices]  # En benzer 10 birayı göster
    return set(set_)

try:
    a=get_recommendations(a)
except:
     st.write("Please jobs")


try :
    b=get_recommendations(b)
except:
     st.write("Please jobs")

try :
    c=get_recommendations(c)
except:
     st.write("Please jobs")







try:
    sonuc_1=a.intersection(b)
except:
    print("please enter the jobs in the list If you do not know the professions to choose you can look 'https://money.usnews.com/careers/best-jobs/rankings/the-100-best-jobs' ")
try:
    sonuc_2=a.intersection(c)
except:
    print("please enter the jobs in the list If you do not know the professions to choose you can look 'https://money.usnews.com/careers/best-jobs/rankings/the-100-best-jobs'  ")
try:

    sonuc_3=b.intersection(c)
except:
    print("please enter the jobs in the list If you do not know the professions to choose you can look 'https://money.usnews.com/careers/best-jobs/rankings/the-100-best-jobs'  ")
try:
    sonuc_4=a.intersection(b).intersection(c)
except:
    print("please enter the jobs in the list If you do not know the professions to choose you can look 'https://money.usnews.com/careers/best-jobs/rankings/the-100-best-jobs'  ")
try:
    sonuc=sonuc_1.union(sonuc_2).union(sonuc_3).union(sonuc_4)
except:
    print("please enter the jobs in the list If you do not know the professions to choose you can look 'https://money.usnews.com/careers/best-jobs/rankings/the-100-best-jobs'  ")


print(sonuc)
sonuc=list(sonuc)
sonuc_last=pd.DataFrame(sonuc, columns =['Jobs'])
url=list()
url_google=[]
for job in sonuc:
    if "/" in job:
        job=job.split("/")[0]
    else:
        job=job.replace(" ","-")
    url.append("https://money.usnews.com/careers/best-jobs/"+str(job))
    job_2=job.replace("-","+")
    url_google.append("https://www.google.com/search?q=" + str (job_2))


sonuc_last["You can look at google"]=url_google
sonuc_last["You can look at jobs"]=url
df_boyut=(len(sonuc_last))
df_boyut=range(df_boyut)
print(df_boyut)
sonuc_list=list(sonuc)
def pred():
        #st.write(sonuc_last.iloc[:,:1])
        df[df["job_name"].isin(sonuc_list)].iloc[:,:-1]


predict=st.button("Predict")
if predict:
    pred()
    st.write("Top three occupations")
    st.write(sonuc_last["You can look at google"][df_boyut][0])
    st.write(sonuc_last["You can look at jobs"][df_boyut][0])

    st.write(sonuc_last["You can look at google"][df_boyut][1])
    st.write(sonuc_last["You can look at jobs"][df_boyut][1])

    st.write(sonuc_last["You can look at google"][df_boyut][2])
    st.write(sonuc_last["You can look at jobs"][df_boyut][2])




















