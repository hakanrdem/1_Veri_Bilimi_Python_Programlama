# Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama

import pandas as pd
df = pd.read_csv("/Users/hakanerdem/PycharmProjects/pythonProject/dsmlbc_9_abdulkadir"
                 "/Homeworks/hakan_erdem/Bitirme Projesi/persona.csv")
df
# Görev 1
# Aşağıdaki Soruları Yanıtlayınız

# Soru 1
# persona.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.

df.shape
df.dtypes

# Soru 2
# Kaç unique SOURCE vardır? Frekansları nedir?
df["SOURCE"].nunique()
df["SOURCE"].value_counts()

# Soru 3
# Kaç unique PRICE vardır?
df["PRICE"].nunique()

# Soru 4
# Hangi PRICE'dan kaçar tane satış gerçekleşmiş?
df["PRICE"].value_counts()

# Soru 5
# Hangi ülkeden kaçar tane satış olmuş?
df["COUNTRY"].value_counts()
df.groupby("COUNTRY")["PRICE"].count()

# Soru 6
# Ülkelere göre satışlardan toplam ne kadar kazanılmış?
df.groupby("COUNTRY")["PRICE"].sum()
df.groupby(['COUNTRY'])[['PRICE']].agg('sum')

# Soru 7
# SOURCE türlerine göre satış sayıları nedir?
df.groupby("SOURCE")["PRICE"].count()
df.groupby(["SOURCE"])[["PRICE"]].agg("count")

# Soru 8
# Ülkelere göre PRICE ortalamaları nedir?
df.groupby("COUNTRY")["PRICE"].mean()
df.groupby(['COUNTRY'])[['PRICE']].agg('mean')

# Soru 9
# SOURCE'lara göre PRICE ortalamaları nedir?
df.groupby("SOURCE")["PRICE"].mean()
df.groupby(['SOURCE'])[['PRICE']].agg('mean')

# Soru 10
# COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?
df.groupby(["COUNTRY","SOURCE"])["PRICE"].mean()
df.groupby(["COUNTRY","SOURCE"])[["PRICE"]].mean()
df.groupby(["COUNTRY","SOURCE"])[["PRICE"]].mean().unstack()

# Görev 2
# COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?
df.groupby(["COUNTRY","SOURCE","SEX","AGE"])["PRICE"].mean()
df.groupby(["COUNTRY","SOURCE","SEX","AGE"])[["PRICE"]].agg("mean")
agg_df = df.groupby([x for x in df.columns[df.columns != 'PRICE']]).mean()

# Görev 3
# Çıktıyı PRICE’a göre sıralayınız
agg_df = df.sort_values(by=['PRICE'], ascending=False)
agg_df

# Görev 4
# Indekste yer alan isimleri değişken ismine çeviriniz.
agg_df.reset_index(inplace = True)
agg_df

# Görev 5
# Age değişkenini kategorik değişkene çeviriniz ve agg_df’e ekleyiniz.
agg_df["AGE"] = agg_df["AGE"].astype("category")
agg_df["AGE"].dtypes

agg_df["AGE_CAT"] = pd.cut(agg_df["AGE"], bins=[0, 18, 23, 30, 40, 70],
                           labels=['0_18', '19_23', '24_30', '31_40','41_70'])
agg_df

# bins: defines the bin edges for the segmentation.
# labels: (array or bool, optional)
# Specifies the labels for the returned bins.Must be the same length as the resulting bins.
# If False, returns only integer indicators of the bins.

# Görev 6
# Yeni seviye tabanlı müşterileri (persona) tanımlayınız.
agg_df['CUSTOMERS_LEVEL_BASED'] = ['_'.join(i).upper() for i in agg_df[['COUNTRY', 'SOURCE', "SEX", "AGE_CAT"]].values]
agg_df

agg_df = agg_df.groupby(["CUSTOMERS_LEVEL_BASED"])[['PRICE']].agg('mean')
agg_df
agg_df.reset_index(inplace = True)
agg_df

# Görev 7
# Yeni müşterileri (personaları) segmentlere ayırınız.
agg_df["SEGMENT"] =  pd.qcut(agg_df["PRICE"], 4 , labels =["D","C","B","A"])
agg_df

agg_df.groupby(["SEGMENT"])[["PRICE"]].agg(["mean", "max", "sum"])

# Görev 8
# Yeni gelen müşterileri sınıflandırıp, ne kadar gelir getirebileceklerini tahmin ediniz

new_user = "TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df["CUSTOMERS_LEVEL_BASED"] == new_user]


new_user_2 = 'FRA_IOS_FEMALE_31_40'
agg_df[agg_df['CUSTOMERS_LEVEL_BASED'] == new_user_2]











