from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.forms.models import model_to_dict


class Project(models.Model):
    # TODO: Use these as choices for category
    CATEGORIES = (("recurring", "Recurring"),
                  ("building", "Major Building"),
                  ("planning", "Planning"),
                  ("parks", "Parks and Playgrounds"),
                  ("infrastructure", "Infrastructure"),
                  ("onetime", "One-Time"))

    name = models.CharField(max_length=128,
                            unique=True)
    department = models.CharField(max_length=128,
                                  db_index=True,)
    category = models.CharField(max_length=20,
                                db_index=True)
    region_name = models.CharField(max_length=128,
                                   default="Somerville, MA")
    address = models.CharField(default="", max_length=256)
    location = models.PointField(null=True)
    shape = models.MultiPolygonField(null=True)
    description = models.TextField(default="")
    justification = models.TextField(default="")
    website = models.URLField(null=True)
    approved = models.BooleanField(db_index=True)

    def to_dict(self, include_budget=True):
        d = model_to_dict(self)

        if include_budget:
            d["budget"] = {bi.year: bi.to_dict() for bi in
                           self.budgetitem_set.all()}

        return d

    @classmethod
    def create_from_dict(kls, d):
        project = kls(name=d["name"],
                      department=d["department"],
                      category=d["category"],
                      region_name=d["region_name"],
                      description=d["description"],
                      justification=d["justification"],
                      approved=d["approved"])

        project.save()

        for year, amount in d["budget"].items():
            project.budgetitem_set.create(year=year,
                                          budget=amount,
                                          funding_source=d["funding_source"])

        if d["address"]:
            project.address = d["address"]
            project.location = Point(d["long"], d["lat"])

        return project


class BudgetItem(models.Model):
    project = models.ForeignKey(Project)
    year = models.IntegerField()
    budget = models.DecimalField(max_digits=11, decimal_places=2)
    funding_source = models.CharField(max_length=64)
    comment = models.TextField()

    def to_dict(self):
        return model_to_dict(self)
