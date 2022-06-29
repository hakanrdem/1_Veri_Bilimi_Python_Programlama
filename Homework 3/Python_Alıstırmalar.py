# GÖREV 1
# Verilen değerlerin veri yapılarını inceleyiniz.
x = 8
type(x)

y = 3.2
type(3.2)

z = 8j + 18
type(z)

a = "Hello World"
type(a)

c = 23 < 22
type(c)

l = [1,2,3,4]
type(l)

d = {"Name": "Jake",
     "Age": 27,
     "Adress": "Downtown"}
type(d)

t = ("Machine Learning", "Data Science")
type(t)

s = {"Python", "Machine Learning", "Data Science"}
type(s)

# GÖREV 2
# Verilen string ifadenin tüm harflerini büyük harfe çeviriniz.
# Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız

# 1.method
text = "The goal is to turn data information, and information into insight"

a = text.upper()
b = a.replace("."," ")
c = b.replace(","," ")
c.split()

# 2.method
text = "The goal is to turn data information, and information into insight"

def textmodifying(text):
    new_text = ""
    for i in range(len(text)):
        if text[i] ==",":
            new_text += " "
        elif text[i] == ".":
            new_text +=" "
        else:
            new_text +=text[i].upper()

    dil= new_text.split()
    print(dil)

textmodifying(text)

# GÖREV 3
# Verilen listeye aşağıdaki adımları uygulayınız.
lst = ["D","A","T","A","S","C","I","E","N","C","E"]

# Adım 1
# Verilen listenin eleman sayısına bakınız.
len(lst)

# Adım 2
# Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
lst[0]
lst[10]

# Adım 3
# Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
lst[0:4]

# Adım 4
# Sekizinci indeksteki elemanı siliniz.
lst.pop(8)
lst

# Adım 5
# Yeni bir eleman ekleyiniz.
lst.append("H")
lst

# Adım 6
# Sekizinci indekse "N" elemanını tekrar ekleyiniz.
lst.insert(8,"N")
lst

# GÖREV 4
# Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
dict = {"Christian": ["America",18],
        "Daisy": ["England",12],
        "Antonio": ["Spain",22],
        "Dante": ["Italy", 23]}

# Adım 1
# Key değerlerine erişiniz.
dict.keys()

# Adım 2
# Value'lara erişiniz.
dict.values()

# Adım 3
# Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
dict["Daisy"][1]=13
dict

# Adım 4
# Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
dict["Ahmet"] = ["Turkey",24]
dict

# Adım 5
# Antonio'yu dictionary'den siliniz.
dir(dict)

dict.pop("Antonio")
dict

# Görev 5
# Argüman olarak bir liste alan, listenin içerisindeki
# tek ve çift sayıları ayrı listelere atayan ve bu listeleri return eden fonksiyon yazınız.

# 1.method

l = [2,13,18,93,22]
odd_list = []
even_list = []

def func(x):
    for i in l:
        if i % 2 == 0:
            odd_list.append(i)
        else:
            even_list.append(i)

    return odd_list , even_list

odd_list , even_list = func(l)

# GÖREV 6
# List Comprehension yapısı kullanarak
# car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

num_col = [col for col in df.columns if df[col].dtypes != "O"]
df_columns = ["NUM_" + col.upper() if col in num_col else col.upper() for col in df.columns]
df_columns

# GÖREV 7
# List Comprehension yapısı kullanarak car_crashes verisinde isminde
# "no" barındırmayan değişkenlerin isimlerinin sonuna "FLAG" yazınız.

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

[col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]

# GÖREV 8:
# List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden
# FARKLI olan değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns
og_list = ["abbrev","no_previous"]
new_cols = []
new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
new_df.head()













