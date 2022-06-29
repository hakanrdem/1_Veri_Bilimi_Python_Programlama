# Virtual Environment (Sanal Ortam) ve (Package Management) Paket Yönetimi

# conda env list komutunu kullandım.Baseden çalıştırdım.
# conda env list komutu ile varolan sanal ortamları listeledim.

# > base                  *  /opt/anaconda3
# > myenv                    /opt/anaconda3/envs/myenv

# GÖREV 1
# Kendi adımla sanal ortam Oluşturma: base den çalıştırdım.
# conda create -n hakan python-3

# GÖREV 2
# Sanal ortamı Aktif etme/ içine girme artık env sanal ortamındayız.
# conda activate hakan

# GÖREV 3
# Yüklü paketleri listeledim.
# conda list

# Hiç paket olmadığı için aşağıdaki gibi bir çıktı aldım.

#
# Name                    Version                   Build  Channel

# GÖREV 4
# Paket Yükleme - Numpy Guncel versiyon  ve pandas 1.2.1 paketlerini aynı anda yükledim.
# conda install numpy pandas=1.2.1

# GÖREV 5
# İndirilen numpy versiyonunu öğrenmek için conda list komutunu çalıştırdım.

# numpy versiyonu = numpy                     1.22.3           py39h2e5f0a9_0

# GÖREV 6
# Pandas upgrade edildi ve yeni versiyon belirlendi.
# conda upgrade pandas
# Yeni pandans versiyonu -pandas                    1.4.2            py39he9d5cce_0

# GÖREV 7
# Numpy silidi.
# conda remove numpy

# GÖREV 8
# Seaborn ve matplotlib kütüphanesinin güncel versiyonları aynı anda indirildi.
# conda install seaborn matplotlib

# GÖREV 9
# Virtual environment içindeki kütüphaneleri versiyon bilgisi ile
# beraber export edildi ve yaml dosyası incelendi.
# conda env export > enviroment.yaml

# GÖREV 10
# Sanal ortamı deactive etme /base envirormenta geri dönme işlemi yapıldı.
# conda deactivate

# GÖREV 11
# İşletim sistemi üzerinde kurduğumuz sanal ortamı silmim :baseden çalıştırdım.
# conda env remove -n myenv

# conda environments:
#
#base                  *  /opt/anaconda3
#myenv                    /opt/anaconda3/envs/myenv
