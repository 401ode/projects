from functools import reduce
from operator import or_
from datetime import datetime


from django.db import models
from django.db.models import Q


class ModelBase(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Client(models.Model):
    department = models.CharField(
        help_text='Department is the highest organizational level.',
        max_length=255,
        blank=True
    )
    agency = models.CharField(
        help_text='Agency is the level below the Department.',
        max_length=255,
        blank=True
    )
    omb_agency_code = models.CharField(
        help_text='OMB Agency Code is the code id for the agency described here.',
        max_length=255,
        blank=True,
        verbose_name='OMB Agency Code'
    )

    class Meta:
        ordering = ['department', 'agency']

    def __str__(self):
        return '{} - {}'.format(self.department, self.agency)


class BusinessUnit(models.Model):
    name = models.CharField(max_length=100)
    class Meta: 
        verbose_name_plural = "Business Units"
    
    def __str__(self):
        return self.name

class FiscalYear(models.Model):
    name = models.CharField(max_length=10)
    start_date = models.DateField()
    end_date = models.DateField()
    class Meta:
        verbose_name_plural = "Fiscal Years"
    

class Category(models.Model):
    name = models.CharField(max_length=100)
    category_type = models.PositiveIntegerField(
        choices = [
            (0,"Project"), (1,"Funding Source")
            ],
        default=0)
    
    class Meta: 
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name


class FundingSourceCategory(Category):
    class Meta: 
        verbose_name_plural = "Funding Source Categories"
    
    def __str__(self):
        return self.name


class ProjectManager(models.Manager):
    def search(self, terms):
        qs = self.get_queryset()
        terms = [term.strip() for term in terms.split()]

        if not terms:
            return qs

        q_objs = []
        for term in terms:
            q_objs.append(Q(name__icontains=term))
            q_objs.append(Q(tagline__icontains=term))

        return qs.filter(reduce(or_, q_objs))


class Project(ModelBase):
    name = models.CharField(
        max_length=100,
        help_text='The full name of the project (e.g., "UHIP")'
    )
    slug = models.SlugField(
        max_length=100,
        help_text='The slug of the project (e.g., "uhip")',
        blank=True
    )
    tagline = models.CharField(
        max_length=300,
        help_text='The tagline of the project; short and concise.',
        blank=True
    )
    client = models.ForeignKey(
        Client,
        help_text='The client of the project, if any.',
        blank=True,
        null=True
    )
    project_lead = models.CharField(
        help_text='Name of ETSS/ODE employee who is responsible for this'
        ' project.',
        max_length=255,
        verbose_name='Project Lead',
        blank=True
    )
    description = models.TextField(
        help_text='The description of the project. Markdown is allowed.'
    )
    impact = models.TextField(
        help_text='The impact of the project. Markdown is allowed.',
        blank=True
    )
    status = models.IntegerField(
        help_text='Current status of the project.',
        choices=[
            (0, 'Tentative'), (1, 'Active'), (2, 'Paused'), (3, 'Complete')
        ],
        default=1
    )
    priority = models.IntegerField(
        help_text='Official designated priority of the project.',
        choices=[
            (0, 'Designated Strategic Imperative'), (1, 'Critical'), (2, 'High'), (3, 'Medium'), (4, 'Low')
        ],
        default=3
    )
    # Level of Effort Section 
    tech_effort = models.PositiveIntegerField(
        help_text = "Estimate of technical staff necessary for the project.",
        verbose_name = "Tech Staff Level of Effort",
        default=0
    )
    agency_effort = models.PositiveIntegerField(
        help_text = "Estimate of Agency staff necessary for the project.",
        verbose_name = "Agency Staff Level of Effort",
        default=0
    )
    contractor_effort = models.PositiveIntegerField(
        help_text = "Estimate of contractor staff necessary for the project.",
        verbose_name = "Contractor Staff Level of Effort",
        default=0
    )
    # End Level of Effort Section
    # Timeline Section
    start_date = models.DateField(
        help_text = "The estimated or actual project start date.",
        verbose_name = "Project Start Date",
        blank=True,
        null=True
    )
    go_live_date = models.DateField(
        help_text = "The estimated or actual project go-live date.",
        verbose_name = "Project Go-Live Date",
        blank=True,
        null=True
    )
    # End Timeline Section
    blockers = models.TextField(
        help_text='What stands in the way of this project? Markdown is allowed.',
        blank=True
    )
    live_site_url = models.URLField(
        help_text='A URL to the site where the project is deployed, '
                  'if one exists.',
        blank=True,
        verbose_name='Live URL'
    )
    github_url = models.URLField(
        help_text='The GitHub URL of the project, e.g. '
                  'https://github.com/401ode/analytics-reporter',
        blank=True,
        verbose_name='GitHub URL'
    )
    
    is_billable = models.BooleanField(
        help_text='Whether or not the project is chargeable to a'
        ' non-ODE/ETSS client.',
        default=False
    )
    cloud_dot_gov = models.BooleanField(
        help_text='Whether or not the project includes cloud.gov '
        'platform support.',
        default=False,
        verbose_name='Cloud.gov Project'
    )
    rifans_number = models.CharField(
        help_text='The unique identifier for the project in'
        'the RIFANS financial system.',
        max_length=100,
        blank=True,
        null=True,
        # unique=True,
        verbose_name='RIFANS Account Number'
    )
    business_unit = models.ForeignKey(
        BusinessUnit,
        help_text='The Business Unit that owns the project.',
        default=None,
        blank=True,
        null=True,
        verbose_name='Business Unit'
    )
    categories = models.ManyToManyField(
        Category,
        help_text = "Which categories does this project fall into?"
    )
    is_visible = models.BooleanField(
        help_text='Projects with a primary private repos should'
        'be listed as false. All other projects should be '
        'listed as true.',
        default=False,
        verbose_name='Is visible (in dashboard)?'
    )

    objects = ProjectManager()

    class Meta:
        ordering = ['priority','client','name']
        

    def __str__(self):
        return self.name

class FundingSource(models.Model):
    project = models.OneToOneField(
        Project,
        on_delete = models.CASCADE)
    
    funding_source_category = models.ForeignKey(
        FundingSourceCategory,
        on_delete = models.CASCADE,
        help_text = "The category (ITIF, Operational Budget, etc. of this funding source.")
        
    dollar_amount = models.PositiveIntegerField(
        help_text = "The amount budgeted for this funding source.",
        default=0)
        
    fiscal_year = models.ForeignKey(
        FiscalYear,
        on_delete = models.CASCADE,
        null=True)
        
    funding_status = models.PositiveIntegerField(
        help_text = "Overall approval status for this funding source.",
        choices = [
            (0,"Proposed"), (1, "Approved"), (2, "Denied")
            ],
        default = 0,
        )
    
    def dollar_amount_display(self):
        """
        Format the integer field `dollar_amount` as `$NN`.
        """
        return "${}".format(self.dollar_amount)
    
    class Meta:
        unique_together = ('project', 'funding_source_category','fiscal_year')
        verbose_name_plural = "Funding Sources"
        
    def __str__(self):
        return "{} - {} - {}".format(self.project, self.funding_source_category, self.dollar_amount)