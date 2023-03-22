from django.db import models




class User(models.Model):
    username = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=False)
    password = models.CharField(max_length=50)
    ifLogged = models.BooleanField(default=False)
    phonenumber= models.CharField(max_length=255, null=False)
    token = models.CharField(max_length=500, null=True, default="")
    

    def __str__(self):
        return "{} -{}".format(self.username, self.email)




class workshop (models.Model):
    marque = models.CharField(max_length=255, null=False)
    image_marque = models.CharField(max_length=255, null=False)
    modele = models.CharField(max_length=255, null=False)
    iftaken = models.BooleanField(default=False)
    acceleration= models.CharField(max_length=255, null=False)
    seat= models.IntegerField()
    x= models.FloatField()
    y= models.FloatField()
    pic= models.CharField(max_length=255, null=False)
    price= models.FloatField()
    Users = models.ManyToManyField(User, through='membre')

    def __str__(self):
        return "{} -{}".format(self.marque, self.modele)



class membre(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    car = models.ForeignKey(workshop,on_delete=models.CASCADE)
    DateDebute = models.CharField(max_length=255,default="")
    DateFin = models.CharField(max_length=255 ,default="")
    Pin = models.IntegerField(default=0)

    def __str__(self):
        return "{} -{}".format(self.DateDebute, self.Pin)        
    

class workshop1 (models.Model):
    domaine= models.CharField(max_length=255, null=False)
    image_marque = models.CharField(max_length=255, null=False)
    modele = models.CharField(max_length=255, null=False)
    iftaken = models.BooleanField(default=False)
    acceleration= models.CharField(max_length=255, null=False)
    seat= models.IntegerField()
    x= models.FloatField()
    y= models.FloatField()
    pic= models.CharField(max_length=255, null=False)
    price= models.FloatField()
    Users = models.ManyToManyField(User, through='membre1')

    def __str__(self):
        return "{} -{}".format(self.marque, self.modele)



class membre1(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    car = models.ForeignKey(workshop1,on_delete=models.CASCADE)
    DateDebute = models.CharField(max_length=255,default="")
    DateFin = models.CharField(max_length=255 ,default="")
    Pin = models.IntegerField(default=0)

    def __str__(self):
        return "{} -{}".format(self.DateDebute, self.Pin)     

class Work_Shop (models.Model):
    domaine= models.CharField(max_length=255, null=False)
    DateDebute = models.CharField(max_length=255,default="")
    DateFin = models.CharField(max_length=255 ,default="")
    Users = models.ManyToManyField(User, through='Membres')

    def __str__(self):
        return "{} -{}".format(self.domaine,self.DateDebute)



class Membres(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    Work_Shop = models.ForeignKey(Work_Shop ,on_delete=models.CASCADE)
    position_A = models.IntegerField(default=0)
    position_B = models.IntegerField(default=0)

    def __str__(self):
        return "{} -{}".format(self.User,self.Work_Shop)         




