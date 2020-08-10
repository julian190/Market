from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Product(models.Model):
    PDRName= models.CharField(max_length=100, verbose_name="Product Name")
    PDRcategory = models.ForeignKey("Category",on_delete=models.CASCADE,null=True,blank=True,verbose_name="Product Category")
    PDRBrand = models.ForeignKey("settings.Brand",on_delete=models.CASCADE,null=True,blank=True,verbose_name="Product Brand")
    PDRDesc = models.TextField(verbose_name="Product Description")
    PDRPrice = models.DecimalField(max_digits=5,decimal_places=2, verbose_name= "Product Price")
    PDRCost = models.DecimalField(max_digits=5,decimal_places=2, verbose_name= "Product Cost")
    PDRCreated =models.DateTimeField(auto_created=True, verbose_name= "Product created at ")

    def __str__(self):
        return self.PDRName
    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _('Products')
#images
class ProductImage(models.Model):
    PRDID = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name="Product")
    PRDImage = models.ImageField(upload_to="products/",verbose_name="Product Images")

    def __str__(self):
        return str(self.PRDID)
    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _('Product Images')
#category
class Category(models.Model):
    CATName = models.CharField(max_length=50,verbose_name="category name")
    CATParent = models.ForeignKey('self',limit_choices_to={"CATParent__isnull":True} ,on_delete=models.CASCADE,blank=True,null=True,verbose_name="category parent")
    CATDescription = models.TextField(verbose_name="Category description")
    CATImage = models.ImageField(upload_to='Category/', verbose_name="category Images")

    def __str__(self):
        return self.CATName
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _('Categories')

#altrantives
class Product_Altrnative(models.Model):
    PALNProduct = models.ForeignKey(Product,on_delete=models.CASCADE, verbose_name="the orginal product")
    PALNAltrnative = models.ManyToManyField(Product,related_name='Alternative_Products',verbose_name="the alternative ")
    class Meta:
        verbose_name = _("Product Alternative")
        verbose_name_plural = _('Product Alternatives')
    def __str__(self):
        return str(self.PALNProduct)
#accessory
class Product_Accessories(models.Model):
    PACCProduct = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='mainAccessories_product',verbose_name="Product")
    PACCAltrantives = models.ManyToManyField(Product,related_name='accessories_products',verbose_name="the altrnatives")
    class Meta:
        verbose_name = _("Product Accessory")
        verbose_name_plural = _('Product Accessories')
    def __str__(self):
        return str(self.PACCProduct)

