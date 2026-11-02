# Copyright 2021 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd
"""
Different models used for testing django-spanner code.
"""

from django.db import models


# Register transformations for model fields.
class UpperCase(models.Transform):
    lookup_name = "upper"
    function = "UPPER"
    bilateral = True


models.CharField.register_lookup(UpperCase)
models.TextField.register_lookup(UpperCase)


# Models
class ModelDecimalField(models.Model):
    field = models.DecimalField()


class ModelCharField(models.Model):
    field = models.CharField()


class Item(models.Model):
    item_id = models.IntegerField()
    name = models.CharField(max_length=10)
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ["name"]


class Number(models.Model):
    num = models.IntegerField()
    decimal_num = models.DecimalField(max_digits=5, decimal_places=2)
    item = models.ForeignKey(Item, models.CASCADE)


class Author(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    num = models.IntegerField(unique=True)
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)


class Report(models.Model):
    name = models.CharField(max_length=10)
    creator = models.ForeignKey(Author, models.CASCADE, null=True)

    class Meta:
        ordering = ["name"]
