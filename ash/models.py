from django.db import models

# #Home Page
# class Home(models.Model):
#     name = models.CharField(max_length=25)
#     greetings_1 = models.CharField(max_length=10)
#     greetings_2 = models.CharField(max_length=10)
#     # picture = models.ImageField(upload_to='picture/')
#
#     updated = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.name
#
# #About
# class About(models.Model):
#     heading = models.CharField(max_length=25)
#     career = models.CharField(max_length=25)
#     description = models.TextField(blank=False)
#     # profile_image = models.ImageField(upload_to='profile/')
#
#     updated = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.career
#
# class Profile(models.Model):
#     about = models.ForeignKey(About,
#                               on_delete=models.CASCADE)
#     social_name = models.CharField(max_length=25)
#     link = models.URLField(max_length=250)
#
# #Skills
# class Category(models.Model):
#     name = models.CharField(max_length=25)
#
#     updated = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         verbose_name = 'Skill'
#         verbose_name_plural = 'Skills'
#
#     def __str__(self):
#         return self.name
# class Skills(models.Model):
#     category = models.ForeignKey(Category,
#                                  on_delete=models.CASCADE)
#     skill_name = models.CharField(max_length=25)
#
# #Portfolio
# class Portfolio(models.Model):
#     # image = models.ImageField(upload_to='portfolio/')
#     link = models.URLField(max_length=250)
#
#     def __str__(self):
#         return f'Portfolio {self.id}'