@echo off
chcp 65001
echo ===================================================
echo   Brand Forge AI - Windows Kurulum Scripti
echo ===================================================
echo.

REM Python kontrolu
echo [1/6] Python kontrol ediliyor...
python --version >nul 2>&1
if errorlevel 1 (
    echo HATA: Python yuklu degil!
    echo Lutfen https://www.python.org/downloads/ adresinden Python indirin
    echo KURULUM SIRASINDA "Add Python to PATH" KUTUSUNU ISARETLEYIN!
    pause
    exit /b 1
)
echo Python bulundu!
echo.

REM Sanal ortam olustur
echo [2/6] Sanal ortam olusturuluyor...
python -m venv venv
if errorlevel 1 (
    echo HATA: Sanal ortam olusturulamadi!
    pause
    exit /b 1
)
echo Sanal ortam basariyla olusturuldu!
echo.

REM Sanal ortami aktiflestir
echo [3/6] Sanal ortam aktiflestiriliyor...
call venv\Scripts\activate
echo Sanal ortam aktif!
echo.

REM Bagimliliklari yukle
echo [4/6] Bagimliliklar yukleniyor...
pip install -r requirements.txt
if errorlevel 1 (
    echo HATA: Bagimliliklar yuklenemedi!
    pause
    exit /b 1
)
echo Bagimliliklar basariyla yuklendi!
echo.

REM Veritabanini baslat
echo [5/6] Veritabani baslatiliyor...
python -c "from app import init_db; init_db()"
echo Veritabani basariyla baslatildi!
echo.

REM Uygulamayi calistir
echo [6/6] Uygulama baslatiliyor...
echo.
echo ===================================================
echo   KURULUM TAMAMLANDI!
echo ===================================================
echo.
echo Tarayicinizda su adrese gidin:
echo http://localhost:5000
echo.
echo Uygulama calisirken bu pencereyi kapatmayin!
echo Kapatmak icin CTRL+C tuslarina basin.
echo.
python app.py
pause
