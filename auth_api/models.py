from django.db import models

# Create your models here.


class Aspnetusers(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=128)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    lastname = models.TextField(db_column='LastName', blank=True, null=True)  # Field name made lowercase.
    idcard = models.TextField(db_column='IDCard')  # Field name made lowercase.
    phonenumber = models.TextField(db_column='PhoneNumber', blank=True, null=True)  # Field name made lowercase.
    phonenumberconfirmed = models.BooleanField(db_column='PhoneNumberConfirmed')  # Field name made lowercase.
    enable = models.BooleanField(db_column='Enable')  # Field name made lowercase.
    forcechangepassword = models.BooleanField(db_column='ForceChangePassword')  # Field name made lowercase.
    lastlogindate = models.DateTimeField(db_column='LastLoginDate', blank=True, null=True)  # Field name made lowercase.
    passwordduedate = models.DateTimeField(db_column='PasswordDueDate', blank=True, null=True)  # Field name made lowercase.
    languageid = models.IntegerField(db_column='LanguageID')  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=100)  # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase.
    emailconfirmed = models.BooleanField(db_column='EmailConfirmed')  # Field name made lowercase.
    passwordhash = models.TextField(db_column='PasswordHash', blank=True, null=True)  # Field name made lowercase.
    twofactorenabled = models.BooleanField(db_column='TwoFactorEnabled')  # Field name made lowercase.
    accessfailedcount = models.IntegerField(db_column='AccessFailedCount')  # Field name made lowercase.
    lockoutenabled = models.BooleanField(db_column='LockoutEnabled')  # Field name made lowercase.
    lockoutenddateutc = models.DateTimeField(db_column='LockoutEndDateUtc', blank=True, null=True)  # Field name made lowercase.
    enableipfiltering = models.BooleanField(db_column='EnableIPFiltering')  # Field name made lowercase.
    securitystamp = models.TextField(db_column='SecurityStamp')  # Field name made lowercase.
    mobileuserapp = models.BooleanField(db_column='MobileUserApp')  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate')  # Field name made lowercase.
    creationuserid = models.CharField(db_column='CreationUserID', max_length=128)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='ModificationDate', blank=True, null=True)  # Field name made lowercase.
    modificationuserid = models.CharField(db_column='ModificationUserID', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AspNetUsers'
