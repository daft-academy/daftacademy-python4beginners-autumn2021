# daftacademy-python_4beginners-autumn2021

## Ważne linki
Materiały z zajęć:
[https://github.com/daftcode/daftacademy-python4beginners-autumn2021](https://github.com/daftcode/daftacademy-python4beginners-autumn2021)

## Kontakt
[python@daftacademy.pl](python@daftacademy.pl)
## Przygotowanie środowiska pracy przed zajęciami
### Instalacja Python 3.8
Żeby nie tracić czasu w trakcie warsztatu, zależałoby nam żebyście przyszli na zajęcia z zainstalowaną odpowiednią wersją Pythona. Poniżej opisana jest krótka instrukcja instalacji dla najpopularniejszych systemów operacyjnych. 

Prosimy o nie używanie menadżera pakietów takich jak Conda czy Anaconda itp.
#### Windows
Wejdź na stronę [https://www.python.org/downloads/release/python-3810/](https://www.python.org/downloads/release/python-3810/) i pobierz odpowiedni instalator z sekcji `Files` - `Windows installer (64-bit)` dla systemu 64-bitowego lub `Windows installer (32-bit)` dla systemu 32-bitowego.

Uruchom pobrany instalator. Zaznacz opcję `Add Python 3.10 to PATH`, a następnie kliknij `Install Now`.
#### macOS
Wejdź na stronę [https://www.python.org/downloads/release/python-3810/](https://www.python.org/downloads/release/python-3810/) i pobierz odpowiedni instalator z sekcji `Files` - `macOS 64-bit Intel installer`. Uruchom pobrany plik i dokończ instalację.
#### macOS @ Apple Silicone M1 & Big Sur
Potrzebny będzie nowszy Python 3.9.1. Nie ma to większego wpływu na działanie aplikacji. Wejdź na stronę [https://www.python.org/downloads/release/python-397/](https://www.python.org/downloads/release/python-397/) i pobierz odpowiedni instalator z sekcji `Files` - `macOS 64-bit universal2 installer`. Uruchom pobrany plik i dokończ instalację. Python dla Apple Silicone M1 jest w fazie eksperymentalnej sam python oraz my nie bierzemy za jego stabile działanie odpowiedzialności.
#### Linux
Istnieje duża szansa, że masz już zainstalowanego pythona na swoim komputerze. W celu sprawdzenia jaka wersja jest zainstalowana, wpisz w terminalu:
```
python3 --version
```
Jeżeli uzyskasz wynik `Python 3.8.x` - jesteś gotowy na zajęcia. W przypadku, gdy nie zostanie odnaleziona komenda `python3` lub zainstalowana będzie niższa wersja niż `Python 3.8`, należy podążać za kolejnymi krokami, zależnymi od systemu, który posiadasz.
##### Debian lub Ubuntu
Użyj w terminalu następującej komendy:
```
sudo apt install python3.8
```
Dla wersji Ubuntu starszych niż 16.10 powyższa komenda może nie zadziałać. W takiej sytuacji należy skorzystać z deadsnakes PPA:
```
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.8
sudo apt install python3.8-distutils python3.8-dev python3.8-venv wget
sudo wget https://bootstrap.pypa.io/get-pip.py
python3.8 get-pip.py
```
##### Fedora (29+)

```
sudo dnf -y install python38 python3-pip python3-virtualenv
```
Dla starszych wersji Fedory powyższa komenda może nie zadziałać. W takiej sytuacji należy wykonać następującej komendy:
```
sudo dnf -y install gcc gcc-c++ zlib zlib-devel libffi-devel openssl-devel openssl-static wget tar make
cd /tmp/;
wget https://www.python.org/ftp/python/3.8.10/Python-3.8.10.tgz;
tar xzf Python-3.8.10.tgz;
cd Python-3.8.10;
sudo ./configure --prefix=/opt/python38 --enable-optimizations --with-lto --with-system-ffi --with-computed-gotos --enable-loadable-sqlite-extensions;
sudo make -j $(nproc);
sudo make altinstall;
sudo rm /tmp/Python-3.8.10.tgz;
sudo ln -s /opt/python38/bin/python3.8 /opt/python38/bin/python3;
sudo ln -s /opt/python38/bin/python3.8 /opt/python38/bin/python;
sudo ln -s /opt/python38/bin/python3.8-config /opt/python38/bin/python-config;
sudo ln -s /opt/python38/bin/pydoc3.8 /opt/python38/bin/pydoc;
sudo ln -s /opt/python38/bin/idle3.8 /opt/python38/bin/idle;
sudo ln -s /opt/python38/bin/python3.8 /usr/bin/python38;
sudo ln -s /opt/python38/bin/pip3.8 /opt/python38/bin/pip3;
sudo ln -s /opt/python38/bin/pip3.8 /opt/python38/bin/pip;
```
Dla starszych wersji Fedory możesz dostać błąd mówiący o tym, że komenda `dnf` nie została znaleziona. W takiej sytuacji należy skorzystać z komendy `yum`.
##### openSUSE
Użyj w terminalu następujące komendy:
```
sudo zypper in python3 python3-pip python3-virtualenv
```
Dla starszych wersji openSUSE powyższa komenda może nie zadziałać. W takiej sytuacji należy wykonać następującej komendy:
```
sudo zypper in gcc gcc-c++ zlib-devel bzip2 libbz2-devel libffi-devel libopenssl-devel readline-devel sqlite3 sqlite3-devel xz xz-devel wget tar make;
cd /tmp/;
sudo wget https://www.python.org/ftp/python/3.8.10/Python-3.8.10.tar.xz;
tar xf Python-3.8.10.tar.xz;
cd Python-3.8.10;
sudo ./configure --prefix=/opt/python38 --enable-optimizations --with-lto --with-system-ffi --with-computed-gotos --enable-loadable-sqlite-extensions;
sudo make -j $(nproc);
sudo make altinstall;
sudo rm /tmp/Python-3.8.10.tgz;
sudo ln -s /opt/python38/bin/python3.8 /opt/python38/bin/python3;
sudo ln -s /opt/python38/bin/python3.8 /opt/python38/bin/python;
sudo ln -s /opt/python38/bin/python3.8-config /opt/python38/bin/python-config;
sudo ln -s /opt/python38/bin/pydoc3.8 /opt/python38/bin/pydoc;
sudo ln -s /opt/python38/bin/idle3.8 /opt/python38/bin/idle;
sudo ln -s /opt/python38/bin/python3.8 /usr/bin/python38;
sudo ln -s /opt/python38/bin/pip3.8 /opt/python38/bin/pip3;
sudo ln -s /opt/python38/bin/pip3.8 /opt/python38/bin/pip;
```
### Sprawdzenie, czy Python 3.8 jest zainstalowany
Wpisz w terminalu następującą komendę:
```
python3.8 --version
```
Jeżeli powyższa komenda zwróci wynik `Python 3.8.x` oznacza to, że masz zainstalowaną odpowiednią wersję Pythona.

Na Windowsie powyższa komenda może nie zadziałać. Wtedy należy użyć w `Wierszu polecenia`:
```
python --version
```
Powinno ono zwrócić wynik `Python 3.8.x`.
### Wybór edytora tekstu
Programowanie w Pythonie nie wymaga żadnych specjalistycznych narzędzi - wystarczy korzystać z edytora tekstu. Na zajęciach możesz korzystać z dowolnego edytora. Jeżeli nie wiesz co wybrać, polecamy Sublime Text [https://www.sublimetext.com/](https://www.sublimetext.com/).
