from django.db import models

class Profile(models.Model):

    user_name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    telephone_number = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.user_name


class Member(models.Model):

    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.job
    

# yukarıdaki durumda
# 1- oluşturulan profile silinirse, member da silinir.
# 2- oluşturulan member silinirse, member silinir profile kalır.
# 3- member oluştururken oluşturulan profile sadece 1 kere seçilebilir.one to one ilşki gereği.

# aşağısını netleştir
#member oluştururken end pointten profile nasıl belirlenecek?ilgili field'e yazılan string post işlemi sonrasında otomatik olarak profil oluşturacak mı dene?
#burda mantık şu mu:bir model belirliyorsun ve istediğin veya öne çıkan bilgileri bu tabloda yer veriyorsun ancak daha detaylı bilgileri one to one ilişki kurarak ikinci bir tabloda tutuyorsun.    
