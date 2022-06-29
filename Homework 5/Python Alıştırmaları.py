# Görev 1
# Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
import seaborn as sns
df = sns.load_dataset("titanic")
df

# Görev 2
# Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
df["sex"].value_counts()

# Görev 3
# Her bir sutuna ait unique değerlerin sayısını bulunuz.
df.nunique()

# Görev 4
# pclass değişkeninin unique değerlerinin sayısını bulunuz.
df["pclass"].nunique()

# Görev 5
# pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
df[["pclass", "parch"]].nunique()

# Görev 6
# embarked değişkeninin tipini kontrol ediniz.
# Tipini category olarak değiştiriniz ve tekrar kontrol ediniz.
df["embarked"].dtype
df["embarked"]= df["embarked"].astype("category")
df["embarked"].dtype

# Görev 7
# embarked değeri C olanların tüm bilgelerini gösteriniz.
df[df["embarked"] == "C"]

# Görev 8
# embarked değeri S olmayanların tüm bilgelerini gösteriniz.
df[df["embarked"] != "S"]

# Görev 9
# Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
df[(df["age"] < 30) & (df["sex"] == "female")]

# Görev 10
# Fare'i 500'den büyük veya yaşı 70’den büyük yolcuların bilgilerini gösteriniz.
df[(df["fare"] > 500) | (df["age"] > 70 )]

# Görev 11
# Her bir değişkendeki boş değerlerin toplamını bulunuz.
df.isnull().sum()

# Görev 12
# who değişkenini dataframe’den çıkarınız.
df.drop("who", axis=1)

#Görev 13
# deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.
df["deck"] = df["deck"].fillna(df["deck"].mode()[0])
df["deck"]

#Görev 14
# age değişkenindeki boş değerleri age değişkenin medyanı ile doldurunuz.
df["age"] = df["age"].fillna(df["age"].median())

# Görev 15
# survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.
df.groupby(["pclass","sex"]).agg({"survived": ["sum" , "count" , "mean"]})

# Görev 16
# 30 yaşın altında olanlar 1, 30 a eşit ve üstünde olanlara 0 verecek bir fonksiyon yazın.
# Yazdığınız fonksiyonu kullanarak titanik veri setinde age_flag adında bir değişken oluşturunuz oluşturunuz.
# (apply ve lambda yapılarını kullanınız)
df["age_flag"] = df.apply(lambda x: (1 if x['age'] < 30 else 0), axis=1)
df
# Görev 17
# Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.
df = sns.load_dataset("tips")

# Görev 18
# Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill değerinin sum,min, max ve mean değerlerini bulunuz.
df.groupby("time").agg({"total_bill" : ["sum" , "min" , "max", "mean"]})

# Görev 19
# Day ve time’a göre total_bill değerlerinin sum, min, max ve mean değerlerini bulunuz.
df.groupby(["time","day"]).agg({ "total_bill": ["sum", "min", "max", "mean"]})

# Görev 20
# Lunch zamanına ve kadın müşterilere ait total_bill ve tip değerlerinin daye göre
# sum, min, max ve mean değerlerini bulunuz.
df[(df["sex"] == "Female") & (df["time"] == "Lunch")].groupby("day")["total_bill", "tip"].sum()
df[(df["sex"] == "Female") & (df["time"] == "Lunch")].groupby("day")["total_bill", "tip"].min()
df[(df["sex"] == "Female") & (df["time"] == "Lunch")].groupby("day")["total_bill", "tip"].max()
df[(df["sex"] == "Female") & (df["time"] == "Lunch")].groupby("day")["total_bill", "tip"].mean()

# Görev 21
# size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)
df.loc[(df["size"] < 3) & (df["total_bill"] > 10)].median()
df.loc[(df["size"] < 3) & (df["total_bill"] > 10), ["total_bill"]].median()

# Görev 22
# total_bill_tip_sum adında yeni bir değişken oluşturunuz. Her bir müşterinin ödediğiCtotalbill ve tip in toplamını versin.
df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]
df
# Görev 23
# Total_bill değişkeninin kadın ve erkek için ayrı ayrı ortalamasını bulunuz.
# Bulduğunuz ortalamaların altında olanlara 0, üstünde ve eşit olanlara 1 verildiği yeni bir total_bill_flag değişkeni oluşturunuz.
# Kadınlar için Female olanlarının ortalamaları, erkekler için ise Male olanların ortalamaları dikkate alınacAktır.
# Parametre olarak cinsiyet ve total_bill alan bir fonksiyon yazarak başlayınız. (If-else koşulları içerecek)

male_total_bill = df[df["sex"] == "Male"]["total_bill"].mean()
female_total_bill = df[df["sex"] == "Female"]["total_bill"].mean()
df["total_bill_flag"] = df.apply(lambda x: (0 if x['total_bill'] < (male_total_bill if x['sex'] == "Male" else female_total_bill) else 1), axis=1)
df["total_bill_flag"]

# Görev 24
# total_bill_flag değişkenini kullanarak cinsiyetlere göre ortalamanın altında ve üstünde olanların sayısını gözlemleyiniz.
df.groupby("sex")["total_bill_flag"].value_counts()

# Görev 25
# Veriyi total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.
import pandas as pd
df_new = df.sort_values(by=['total_bill_tip_sum'], ascending=False).head(30)
df_new_dataframe = pd.DataFrame(df_new)
df_new_dataframe



