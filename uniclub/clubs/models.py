from django.db import models
from django.utils.text import slugify
from django.conf import settings

class Club(models.Model):
    name = models.CharField(max_length=100)
    username = models.SlugField(unique=True)  
    slug = models.SlugField(unique=True, blank=True)
    
    description = models.TextField()
    
    wilaya = models.CharField(max_length=50)
    university = models.CharField(max_length=100)
    
    founded_at = models.DateField()
    is_active = models.BooleanField(default=True)
    
    category = models.CharField(max_length=100)
    
    logo = models.ImageField(upload_to="club_logos/")
    
    president = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="president_clubs",
        null=True,
        blank=True
    )
    
    vice_president = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="vice_president_clubs",
        null=True,
        blank=True
    )

    departments = models.TextField(blank=True) 

    custom_fields = models.JSONField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ClubRequest(models.Model):
    name = models.CharField(max_length=100)
    username = models.SlugField(unique=True)  
    slug = models.SlugField(unique=True, blank=True)
    
    description = models.TextField()
    wilaya = models.CharField(max_length=50)
    university = models.CharField(max_length=100)
    founded_at = models.DateField()
    
    category = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="club_logos/" ,blank=True, null=True)
    
    president = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="club_requests"
    )
    vice_president = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="vp_requests",
        null=True,
        blank=True
    )

    departments = models.TextField(blank=True) 
    custom_fields = models.JSONField(blank=True, null=True)

    is_approved = models.BooleanField(default=False)  # This is key!
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        old = None 

        if Club.objects.filter(username=self.username).exists():
            return #Already created 

        if self.pk:
            old = ClubRequest.objects.get(pk=self.pk)

        if not self.slug:
            self.slug = slugify(self.username)
        super().save(*args, **kwargs)

        if old and not old.is_approved and self.is_approved:
            Club.objects.create(
            name=self.name,
            username=self.username,
            slug=slugify(self.username),
            description=self.description,
            wilaya=self.wilaya,
            university=self.university,
            founded_at=self.founded_at,
            category=self.category,
            logo=self.logo,
            president=self.president,
            vice_president=self.vice_president,
            departments=self.departments,
            custom_fields=self.custom_fields
            )

    def __str__(self):
        return f"[REQUEST] {self.name}"
