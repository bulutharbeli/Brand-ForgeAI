# 🪟 Windows İçin Brand Forge AI Kurulum Rehberi

## ❌ Karşılaştığınız Hatalar

Siz şu hataları aldınız:
```
❌ 'bash' is not recognized
❌ 'python3' is not recognized  
❌ 'source' is not recognized
❌ # işareti komut olarak tanınmıyor
❌ requirements.txt bulunamadı
❌ ModuleNotFoundError: No module named 'app'
```

**Çözüm:** Windows için özel komutlar kullanmalısınız!

---

## ✅ Windows İçin Adım Adım Kurulum

### **Yöntem 1: Otomatik Kurulum (En Kolay!)**

#### **Adım 1: Python'ın Yüklü Olduğunu Kontrol Edin**
```powershell
# PowerShell veya Command Prompt açın
python --version
```

**Eğer hata alırsanız:**
1. https://www.python.org/downloads/ adresinden Python indirin
2. Kurulum sırasında ✅ **"Add Python to PATH"** kutusunu işaretleyin!
3. Kurulum bittikten sonra PowerShell'i yeniden başlatın

---

#### **Adım 2: Projeyi İndirin**

**Seçenek A: Git ile (Önerilen)**
```powershell
cd C:\Users\bulut.harbeli\Downloads
git clone https://github.com/bulutharbeli/Brand-ForgeAI.git
cd Brand-ForgeAI
```

**Seçenek B: ZIP olarak indirin**
1. https://github.com/bulutharbeli/Brand-ForgeAI adresine gidin
2. Yeşil "Code" butonuna tıklayın
3. "Download ZIP" seçin
4. ZIP dosyasını açın

---

#### **Adım 3: Windows Kurulum Scriptini Çalıştırın**
```powershell
setup_windows.bat
```

**Bu script otomatik olarak:**
- ✅ Sanal ortam oluşturur
- ✅ Tüm bağımlılıkları yükler
- ✅ Veritabanını başlatır
- ✅ Uygulamayı başlatır

**Kurulum bittikten sonra:**
```
Tarayıcınızda şu adrese gidin: http://localhost:5000
```

---

### **Yöntem 2: Manuel Kurulum (Kontrollü Yöntem)**

#### **Adım 1: PowerShell Açın**
```
Windows Key → "powershell" yazın → Enter'a basın
```

---

#### **Adım 2: Proje Klasörüne Gidin**
```powershell
cd C:\Users\bulut.harbeli\Downloads\Brand-ForgeAI
```

*(Eğer başka bir yere indirdiyseniz, o yolu yazın!)*

---

#### **Adım 3: Sanal Ortam Oluşturun**
```powershell
# Windows'ta doğru komut budur:
python -m venv venv
```

**Başarılı mesajı:**
```
Yükleme gerekiyor... tamamlandı.
```

---

#### **Adım 4: Sanal Ortamı Aktifleştirin**
```powershell
venv\Scripts\activate
```

**Önemli:** Satır başında `(venv)` yazısını görmelisiniz!
```
(venv) C:\Users\bulut.harbeli\Downloads\Brand-ForgeAI>
```

*(Eğer görmüyorsanız, sanat ortam aktif değil demektir!)*

---

#### **Adım 5: Bağımlılıkları Yükleyin**
```powershell
pip install -r requirements.txt
```

**Bekleyin:** 50-100 MB dosya indirilecek, 2-5 dakika sürebilir.

**Karşılaşabileceğiniz hatalar:**
```
ERROR: Could not open requirements file
```
**Çözüm:** Doğru klasörde olduğunuzu kontrol edin:
```powershell
dir requirements.txt
```
*(Eğer dosya görünmüyorsa, yanlış klasördesiniz!)*

---

#### **Adım 6: Veritabanını Başlatın**
```powershell
python -c "from app import init_db; init_db()"
```

**Başarılı mesajı:** (Hiçbir hata vermemeli, sadece yeni satıra geçmeli)

**Kontrol edin:**
```powershell
dir brand_forge.db
```
*(Bu dosyayı görmelisiniz!)*

---

#### **Adım 7: Uygulamayı Başlatın**
```powershell
python app.py
```

**Başarılı mesajı:**
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://169.254.0.21:5000
 ```

**Önemli:** Bu pencereyi kapatmayın! Uygulama çalışmaya devam ediyor.

---

#### **Adım 8: Tarayıcıda Açın**
```
Tarayıcınızı açın (Chrome, Edge, Firefox...)
Şu adrese gidin: http://localhost:5000
```

**Görmeniz gereken:**
- ✅ "🔥 Brand Forge AI" başlığı
- ✅ "Forge Your Brand Identity with AI" yazısı
- ✅ "Start Building Your Brand" butonu

---

## 🔧 Sorun Giderme (Troubleshooting)

### **Sorun 1: 'python' is not recognized**
**Çözüm:** Python yüklü değil veya PATH'e eklenmemiş.

**Kontrol edin:**
```powershell
where python
```

**Eğer boş sonuç alırsanız:**
1. Python'ı https://www.python.org/downloads/ adresinden indirin
2. Kurulum sırasında ✅ **"Add Python to PATH"** kutusunu işaretleyin!
3. PowerShell'i yeniden başlatın

---

### **Sorun 2: 'pip' is not recognized**
**Çözüm:** Python kurulumu bozuk.

**Düzeltin:**
```powershell
python -m pip --version
```

**Eğer hata alırsanız, Python'ı yeniden kurun.**

---

### **Sorun 3: 'requirements.txt' not found**
**Çözüm:** Yanlış klasördesiniz!

**Kontrol edin:**
```powershell
dir
```

**Görmeniz gereken:**
```
app.py
requirements.txt  ← Bu dosya burada olmalı!
setup.sh
static/
templates/
utils/
```

**Eğer görmüyorsanız:**
```powershell
# Doğru klasöre gidin
cd C:\Users\bulut.harbeli\Downloads\Brand-ForgeAI
dir
```

---

### **Sorun 4: 'ModuleNotFoundError: No module named app'**
**Çözüm:** Sanal ortam aktif değil veya yanlış klasördesiniz.

**Kontrol edin:**
1. Satır başında `(venv)` var mı? (Yoksa `venv\Scripts\activate` yazın!)
2. `app.py` dosyası bu klasörde mi? (`dir` yazarak kontrol edin!)

---

### **Sorun 5: 'Port 5000 is already in use'**
**Çözüm:** Başka bir uygulama 5000 portunu kullanıyor.

**Kontrol edin:**
```powershell
netstat -ano | findstr :5000
```

**Öldürün (PID numarasını yazın):**
```powershell
taskkill /PID <PID_NUMARASI> /F
```

**VEYA portu değiştirin (app.py içinde):**
```python
# app.py'nin en alt satırını değiştirin:
app.run(debug=True, host='0.0.0.0', port=5001)  # 5001 olarak değiştirin
```

---

### **Sorun 6: Sayfa Yüklenmiyor (http://localhost:5000 açılmıyor)**
**Çözüm:** Uygulama çalışmıyor.

**Kontrol edin:**
1. `python app.py` çalıştırdığınız pencerede hata var mı?
2. Şu komutu çalıştırın:
```powershell
curl http://localhost:5000/health
```
**Başarılı cevap:**
```json
{"status": "healthy", "timestamp": "...", "version": "1.0.0"}
```

---

## ✅ Kontrol Listesi (Checklist)

Kurulum başarılı mı? Şunları kontrol edin:

- [ ] `python --version` çalışıyor ✅
- [ ] `venv` klasörü oluştu ✅
- [ ] `(venv)` satır başında görünüyor ✅
- [ ] `pip install -r requirements.txt` hata vermedi ✅
- [ ] `brand_forge.db` dosyası oluştu ✅
- [ ] `python app.py` başarıyla başladı ✅
- [ ] http://localhost:5000 yüklendi ✅

**Hepsi işaretli mı? ✅ O zaman hazırsınız!**

---

## 🌐 Uygulamayı Kullanma

### **Adım 1: Ana Sayfayı Açın**
```
http://localhost:5000
```

### **Adım 2: Marka İsmi Oluşturun**
1. Sayfayı aşağı kaydırın → "TRY IT YOURSELF" bölümüne gidin
2. "🔤 Brand Names" butonuna tıklayın
3. Endüstri: "Technology" seçin
4. Keywords: `innovative, cloud, smart` yazın
5. Style: "Modern" seçin
6. **"Generate Brand Names"** butonuna tıklayın
7. 2 saniye bekleyin → 10 isim görünecek!

### **Adım 3: Devam Edin**
Aynı şekilde:
- 🎨 Colors → Renk paleti oluşturun
- ✏️ Logos → Logo kavramları oluşturun
- 💬 Slogans → Sloganlar oluşturun
- 📋 Guidelines → Marka kılavuzu oluşturun

---

## 📖 Daha Fazla Bilgi İçin

### **Türkçe Dokümanlar:**
- `QUICKSTART.md` - Hızlı başlangıç
- `USER_GUIDE.md` - Kullanım kılavuzu
- `VISUAL_GUIDE.md` - Görsel rehber

### **İngilizce Dokümanlar:**
- `README.md` - Tam dokümantasyon
- `DEPLOYMENT.md` - Production kurulumu

---

## 🆘 Yardıma İhtiyacınız Varsa

### **Sorunuzu şu şekilde sorun:**
1. **Hata mesajını kopyalayın** (Tam metin!)
2. **Hangi adımda olduğunuzu söyleyin**
3. **PowerShell ekran görüntüsü gönderin** (VEYA metin olarak yapıştırın)

### **Örnek:**
```
Sorun: Adım 5'teyim, "pip install" yazdığımda şu hatayı alıyorum:
ERROR: Could not open requirements file: [Errno 2] No such file or directory
```

---

## 🎉 Tebrikler!

**Brand Forge AI artık Windows'ta çalışıyor!**

Şimdi:
1. ✅ http://localhost:5000 adresine gidin
2. ✅ Marka oluşturmaya başlayın
3. ✅ 10 dakikada tam bir marka kimliği oluşturun!

---

## 🔗 Önemli Linkler

- **GitHub:** https://github.com/bulutharbeli/Brand-ForgeAI
- **Yerel Uygulama:** http://localhost:5000
- **Sağlık Kontrolü:** http://localhost:5000/health

---

**İyi eğlenceler! Marka oluşturma işlemi 5-10 dakika sürüyor! 🚀**
