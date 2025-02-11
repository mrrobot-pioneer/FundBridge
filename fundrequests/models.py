from django.db import models
from django.contrib.auth.models import User

class Fundraiser(models.Model):
    CATEGORY_CHOICES = [
        ("academic", "Academic"),
        ("talent", "Talent"),
    ]

    title = models.CharField(max_length=255, help_text="Title of the fundraiser")
    description = models.TextField(help_text="Brief description of the fundraiser")
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default="academic")
    image = models.ImageField(upload_to="fundraiser_images/", default="default.jpg")
    target_amount = models.DecimalField(max_digits=10, decimal_places=2, help_text="Target amount to be raised")
    raised_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, help_text="Amount already raised")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, help_text="User who created the fundraiser")
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False, help_text="Admin approval status")

    def progress_percentage(self):
        """Calculate the fundraising progress in percentage"""
        if self.target_amount > 0:
            return (self.raised_amount / self.target_amount) * 100
        return 0

    def __str__(self):
        return self.title
