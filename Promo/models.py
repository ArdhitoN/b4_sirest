from decimal import Decimal
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]
# class Model_PromoMT(models.Model) :
#     # Model untuk pendaftaran relawan vaksin
#     # Pilihan_jenis_promo = [('Special Day Promo','Special Day Promo'),
#     # ('Minimum Transaksi Promo','Minimum Transaksi Promo'),
#     # ]
#     Nama = models.CharField('Nama Promo', max_length= 40)
#     # umur = models.IntegerField('Umur',)
#     Jenis_promo = 'Minimum Transaksi Promo'
#     Diskon = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0), validators=PERCENTAGE_VALIDATOR) 
#     Minimum_transaksi  = models.IntegerField('Minimum Transaksi',validators=[
#             # MaxValueValidator(100),
#             MinValueValidator(1)
#         ])

#     def __str__(self):
#         return str(self.pk)

class Model_Promo2(models.Model) :
    # Model untuk pendaftaran relawan vaksin
    Nama = models.CharField('Nama Promo', max_length=40)
    # umur = models.IntegerField('Umur',)
    Pilihan_Promo = [('Special Day Promo','Special Day Promo'),
    ('Minimum Transaksi Promo','Minimum Transaksi Promo'),
    ]

    Jenis_promo = models.CharField('Jenis Promo :',choices= Pilihan_Promo, max_length=40)
    Diskon = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0), validators=PERCENTAGE_VALIDATOR) 
    Tanggal_berlangsung = models.DateField(blank=True, null=True,)
    Minimum_transaksi  = models.IntegerField('Minimum Transaksi',validators=[
            # MaxValueValidator(100),
            MinValueValidator(1)
        ], blank=True, default=0)

    def __str__(self):
        return str(self.pk)
