## YouTube Video İndirici

Bu proje, Python ve Flask kullanarak basit bir YouTube video indirici uygulamasıdır. Kullanıcıların YouTube videolarını MP4 veya MP3 formatlarında indirmelerine olanak tanır. Ayrıca, MP4 formatı için çözünürlük ve FPS değerlerini seçme imkanı sağlar.

### Özellikler

- **Video İndirme**: YouTube videolarını MP4 (video) veya MP3 (ses) formatlarında indirin.
- **Çözünürlük ve FPS Seçimi**: MP4 formatı için çeşitli çözünürlük ve FPS seçeneklerini görüntüleyin ve seçin.
- **İndirme İlerlemesi**: İndirmenin ilerlemesini gerçek zamanlı olarak takip edin.
- **Basit Kullanıcı Arayüzü**: Flask ve HTML kullanılarak oluşturulmuş kullanıcı dostu bir arayüz.

### Kurulum

1. **Depoyu Klonlayın**:

   ```bash
   git clone https://github.com/kullanici_adiniz/yt-downloader.git
   cd yt-downloader
   ```

2. **Gerekli Paketleri Yükleyin**:

   Sanal bir ortam oluşturun ve gerekli Python paketlerini yükleyin.

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows kullanıcıları için: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Uygulamayı Çalıştırın**:

   Flask uygulamasını başlatın.

   ```bash
   python app.py
   ```

   Ardından tarayıcınızda `http://127.0.0.1:5000` adresine giderek uygulamayı kullanabilirsiniz.

### Kullanım

- Uygulama açıldığında YouTube video URL'sini girin.
- İndirme formatını (MP4 veya MP3) seçin.
- MP4 formatı için uygun çözünürlük ve FPS seçeneklerini belirleyin.
- "İndir" düğmesine tıklayarak videoyu indirmeye başlayın.
- İndirme ilerlemesini takip edin ve tamamlandığında dosyayı indirin.

### Katkıda Bulunma

Katkıda bulunmak isterseniz, lütfen bir pull request gönderin veya mevcut sorunları rapor edin. Herhangi bir öneri veya hata raporu için [issues](https://github.com/kullanici_adiniz/yt-downloader/issues) sayfasını kullanabilirsiniz.

### Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için [LICENSE](LICENSE) dosyasına bakabilirsiniz.
