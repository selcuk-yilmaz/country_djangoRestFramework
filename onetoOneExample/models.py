from django.db import models

class Profil(models.Model):
    """Kullanıcı profili modeli."""
    kullanici_adi = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    telefon_numarasi = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.kullanici_adi


class Kullanici(models.Model):
    """Kullanıcı modeli."""
    isim = models.CharField(max_length=255)
    soyisim = models.CharField(max_length=255)
    profil = models.OneToOneField(Profil, on_delete=models.CASCADE)

    def __str__(self):
        return self.isim
