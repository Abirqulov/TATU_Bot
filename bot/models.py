from django.db import models

# Create your models here.


class Teachers(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='static/images/', default='')
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.f_name


class Faculty(models.Model):
    fac_name = models.CharField(max_length=100)

    def __str__(self):
        return self.k


class Groups(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True, blank=True)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    gr_name = models.CharField(max_length=100)
    tal_soni = models.CharField(max_length=100)
    img = models.ImageField(upload_to='static/images/', default='')

    def __str__(self):
        return self.gr_name


class News(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='static/images/', default='')
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class DarsJadval(models.Model):
    img = models.ImageField(upload_to='static/images/', default='')
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)
    group_nomi = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.group.gr_name


class User(models.Model):
    chat_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)


