# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AthleteMeta(models.Model):
    id = models.IntegerField(primary_key=True,blank=True, null=False)
    bib_id = models.TextField(blank=True, null=True)  
    name = models.TextField(blank=True, null=True)  
    country = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)  # This field type is a guess.
    division = models.TextField(blank=True, null=True)  # This field type is a guess.
    age = models.TextField(blank=True, null=True)  # This field type is a guess.
    profession = models.TextField(blank=True, null=True)  # This field type is a guess.
    meta_url = models.TextField(blank=True, null=True)  # This field type is a guess.
    scrape_date = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'athlete_meta'


class LinkPage(models.Model):
    """
    
    """
    id = models.IntegerField(primary_key=True,blank=True, null=False)
    link = models.TextField(blank=True, null=True)  # This field type is a guess.
    event_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    datetime = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)  # This field type is a guess.
    country = models.TextField(blank=True, null=True)  # This field type is a guess.
    year_table = models.IntegerField(blank=True, null=True)
    location_table = models.TextField(blank=True, null=True)  # This field type is a guess.
    distance = models.TextField(blank=True, null=True)  # This field type is a guess.
    format = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'link_page'


class RaceTimes(models.Model):
    id = models.IntegerField(primary_key=True,blank=True, null=False)
    name = models.TextField(blank=True, null=True)  # This field type is a guess.
    bib_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    country = models.TextField(blank=True, null=True)  # This field type is a guess.
    datetime = models.TextField(blank=True, null=True)
    swim = models.TextField(blank=True, null=True)
    bike = models.TextField(blank=True, null=True)
    run = models.TextField(blank=True, null=True)
    gen_rank = models.TextField(blank=True, null=True)  # This field type is a guess.
    ovr_rank = models.TextField(blank=True, null=True)  # This field type is a guess.
    div_rank = models.TextField(blank=True, null=True)  # This field type is a guess.
    total = models.TextField(blank=True, null=True)  # This field type is a guess.
    points = models.TextField(blank=True, null=True)  # This field type is a guess.
    parent_url = models.TextField(blank=True, null=True)  # This field type is a guess.
    meta_link = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'race_times'


class ScrapeDetails(models.Model):
    """
    
    """
    id = models.IntegerField(primary_key=True,blank=True, null=False)
    link = models.TextField(blank=True, null=True)
    datetime = models.TextField(blank=True, null=True)
    page_type = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'scrape_details'


class ScrapePage(models.Model):
    id = models.IntegerField(primary_key=True,  blank=True, null=False)
    link = models.TextField(blank=True, null=True)  # This field type is a guess.
    datetime = models.TextField(blank=True, null=True)
    page_type = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'scrape_page'
