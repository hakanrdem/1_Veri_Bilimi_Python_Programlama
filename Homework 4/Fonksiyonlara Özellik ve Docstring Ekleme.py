# Fonksiyonlara Özellik ve Docstring Ekleme

# GÖREV
# cat_summary() fonksiyonuna 1 özellik ekleyiniz. Bu özellik argümanla biçimlendirilebilir olsun.
#  ...Var olan özelliği de argümanla kontrol edilebilir hale getirebilirsiniz.
# Fonksiyonlara Özellik Eklemek

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]
num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int", "float"]]
cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]

cat_cols = cat_cols + num_but_cat
cat_cols = [col for col in cat_cols if col not in cat_but_car]
df[cat_cols].nunique()


df["survived"].value_counts()
100 * df["survived"].value_counts() / len(df)

####################################
def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)

cat_summary(df, "sex", plot=True)

# Docstring Yazımı
# Görev:
# check_df(), cat_summary() fonksiyonlarına 4 bilgi (uygunsa) barındıran numpy tarzı docstring yazınız.
# (task, params, return, example)

def check_df(dataframe, head=5):

    """
    Veri setine ait betimleyici istatistikleri getirir.

    Parameters
    ----------
    dataframe: dataframe
        değişken isimleri alınmak istenen dataframe'dir.
    head : Sorgu sonucu getirilmek istenen ilk 5 satır sayısını ifade eder. Default 5 değeri belirlenmiştir.

    Returns
    -------
    shape:
        dataframe boyut bilgisini verir.
    dtypes:
        Değişkenlerin veri tipi bilgisini verir.
    head:
        Sorgu sonucu getirilmek istenen ilk 5 satır sayısını ifade eder. Default 5 değeri belirlenmiştir.
    tail:
        Sorgu sonucu getirilmek istenen son 5 satır sayısını ifade eder.
    isnull().sum():
        Değişken bazında NaN sayısını ifade eder.
    describe:
        Datafame de yer alan değişkenlerin betimleyici istatistiklerine ait bilgileri verir.

    Example
    ------
        def check_df(dataframe, head=5)

    """

    print("##################### Shape #####################")
    print(dataframe.shape)
    print("##################### Types #####################")
    print(dataframe.dtypes)
    print("##################### Head #####################")
    print(dataframe.head(head))
    print("##################### Tail #####################")
    print(dataframe.tail(head))
    print("##################### NA #####################")
    print(dataframe.isnull().sum())
    print("##################### Quantiles #####################")
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T)


check_df(df)

def cat_summary(dataframe, col_name, plot=False):

    """
    Veri setine ait değişkenlerin sınıf sayılarını ve herbir sınıfın kendi içinde oranlarını verir.

    Parameters
    ----------
    dataframe: dataframe
        değişken isimleri alınmak istenen dataframe'dir.
    col_name : Sorgu sırasında kullanılan değişkendir. Cat, int, float
    plot:False
        Default değerdir.

    Returns
    -------
    value_counts:
        dataframe içerisinde yer alan değişkenlerin sınıf sayılarını getirir.

    Example
    ------
    def cat_summary(dataframe, col_name, plot=False)

    """
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)












