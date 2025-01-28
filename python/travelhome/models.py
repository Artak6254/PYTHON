from django.db import models
from django.core.validators import FileExtensionValidator

class Travel_banner(models.Model):
    id = models.AutoField(primary_key=True)
    banner_text = models.CharField(max_length=255, default="Default Banner Text")
    banner_sub_text = models.CharField(max_length=255)
    video = models.FileField(upload_to='videos_uploaded', null=True,
                             validators=[FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    banner_image = models.ImageField(upload_to='images_uploaded', null=True, blank=True, default="svg") 
    def __str__(self):
        return f"{self.banner_text} {self.banner_sub_text}, {self.banner_image}"


class Travel_gallery(models.Model):
    id = models.AutoField(primary_key=True)
    gallery_image = models.ImageField(upload_to="image", default="jpg", blank=True)
    gallery_title = models.CharField(max_length=100,default="Armenia")  # Removed the comma
    gallery_text = models.TextField()
    gallery_price = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.gallery_image} {self.gallery_title}, {self.gallery_text} {self.gallery_price}"

class Travel_services(models.Model):
    id = models.AutoField(primary_key=True)
    icon_class = models.CharField(max_length=150)
    services_title = models.CharField(max_length=200)
    services_text = models.TextField()
    
    def __str__(self):
        return f"{self.icon_class} {self.services_title} {self.services_text}"


class Travel_packages_gallery(models.Model):
    id = models.AutoField(primary_key=True)
    gallery_image = models.ImageField(upload_to="image", default="jpg", blank=True)
    gallery_title = models.CharField(max_length=100,default="Armenia")  # Removed the comma
    gallery_text = models.TextField()

    def __str__(self):
        return f"{self.gallery_image} {self.gallery_title}, {self.gallery_text}"



class Travel_Review(models.Model):
    id = models.AutoField(primary_key=True)
    review_image = models.ImageField(upload_to="image", default="jpg", blank=True)
    review_fullname = models.CharField(max_length=30)
    review_decr = models.CharField(max_length=200)
    review_icons = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.review_fullname} {self.review_decr} {self.review_icons}"


class Travel_Brand(models.Model):
    id = models.AutoField(primary_key=True)
    brand_img = models.ImageField(upload_to="image", default="jpg", blank=True)



class Booking(models.Model):
    place_name = models.TextField()
    guest_num = models.IntegerField(default=0)
    arrive_date = models.DateField()
    leave_date = models.DateField()
    
    def __str__(self):
        return f"{self.place_name}"
    



class Contact(models.Model):
    contact_svg = models.FileField(upload_to='svgs/', default="svg")
    email_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True)
    people_num = models.IntegerField(default=0)
    subject = models.CharField(max_length=255, blank=True)
    message = models.TextField()
    

    def __str__(self):
        return self.email 