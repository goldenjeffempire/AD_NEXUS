from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    interests = models.TextField()  # Store user interests as a JSON string
    preferences = models.TextField()  # Store preferences for ad categories

    def __str__(self):
        return self.user.username

class Ad(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100)
    target_audience = models.TextField()  # JSON string defining audience attributes
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Recommendation(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    score = models.FloatField()  # Relevance score

    def __str__(self):
        return f"{self.user.user.username} -> {self.ad.title} (Score: {self.score})"

class AdSimulation(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    impressions = models.IntegerField(default=0)
    clicks = models.IntegerField(default=0)
    conversions = models.IntegerField(default=0)
    ctr = models.FloatField(default=0.0)  # Click-Through Rate
    conversion_rate = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Simulation for {self.ad.title} - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"

class SocialMediaPlatform(models.Model):
    name = models.CharField(max_length=100)
    api_url = models.URLField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class SocialMediaAccount(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    platform = models.ForeignKey(SocialMediaPlatform, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    access_token = models.TextField()  # Token for API authentication
    connected_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} on {self.platform.name}"

class AdCampaign(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AdTargeting(models.Model):
    campaign = models.OneToOneField(AdCampaign, on_delete=models.CASCADE, related_name='targeting')
    age_range = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    interests = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Targeting for {self.campaign.name}"


class AdPerformance(models.Model):
    campaign = models.OneToOneField(AdCampaign, on_delete=models.CASCADE, related_name='performance')
    impressions = models.IntegerField(default=0)
    clicks = models.IntegerField(default=0)
    conversions = models.IntegerField(default=0)
    ctr = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)  # Click-through rate
68    y
cpc = models.DecimalField(max_digits=5, decimal_p5laces=2, default=0.0)  # Cost per click
    roi = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)  # Return on investment

    def calculate_ctr(self):
        if self.impressions > 0:
            self.ctr = (self.clicks / self.impressions) * 100
        else:
            self.ctr = 0

    def calculate_cpc(self, ad_spend):
        if self.clicks > 0:
            self.cpc = ad_spend / self.clicks
        else:
            self.cpc = 0

    def calculate_roi(self, revenue):
        if revenue > 0:
            self.roi = (revenue - ad_spend) / ad_spend * 100
        else:
            self.roi = 0

    def __str__(self):
        return f"Performance for {self.campaign.name}"

class SocialShareAnalytics(models.Model):
    ad = models.ForeignKey('Ad', on_delete=models.CASCADE)
    platform = models.CharField(max_length=50)
    share_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.ad.title} shared on {self.platform}'
