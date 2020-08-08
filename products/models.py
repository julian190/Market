from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Product(models.Model):
    PDRName= models.CharField(max_length=100, verbose_name="Product Name")
    #category
    PDRDesc = models.TextField(verbose_name="Product Description")
    PDRPrice = models.DecimalField(max_digits=5,decimal_places=2, verbose_name= "Product Price")
    PDRCost = models.DecimalField(max_digits=5,decimal_places=2, verbose_name= "Product Cost")
    PDRCreated =models.DateTimeField(auto_created=True, verbose_name= "Product created at ")

    def __str__(self):
        return self.PDRName
#images
class ProductImage(models.Model):
    PRDID = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name="Product")
    PRDImage = models.ImageField(upload_to="products/",verbose_name="Product Images")

    def __str__(self):
        return str(self.PRDID)
#category
class Category(models.Model):
    CATName = models.CharField(max_length=50,verbose_name="category name")
    CATParent = models.ForeignKey('self',limit_choices_to={"CATParent__isnull":True} ,on_delete=models.CASCADE,blank=True,null=True,verbose_name="category parent")
    CATDescription = models.TextField(verbose_name="Category description")
    CATImage = models.ImageField(upload_to='Category/', verbose_name="category Images")

    def __str__(self):
        return self.CATName

#altrantives
class Product_Altrnative(models.Model):
    PALNProduct = models.ForeignKey(Product,on_delete=models.CASCADE)
    PALNAltrnative = models.ManyToManyField(Product,related_name='Alternative_Products')
    class Meta:
        verbose_name = _("Product Alternative")
        verbose_name_plural = _('Product Alternatives')
    def __str__(self):
        return str(self.PALNProduct)

class Product_Accessories(models.Model):
    PACCProduct = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='mainAccessories_product')
    PACCAltrantives = models.ManyToManyField(Product,related_name='accessories_products')
    class Meta:
        verbose_name = _("Product Accessory")
        verbose_name_plural = _('Product Accessories')
    def __str__(self):
        return str(self.PACCProduct)

    #accessory