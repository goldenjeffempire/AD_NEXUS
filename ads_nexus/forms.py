from django import forms
from .models import AdCampaign, AdTargeting, SocialMediaAccount, ScheduledPost

class AdCampaignForm(forms.ModelForm):
    class Meta:
        model = AdCampaign
        fields = ['name', 'budget', 'start_date', 'end_date']


class AdTargetingForm(formis.ModelForm):
    class Meta:
        model = AdTargeting
        fields = ['age_range', 'location', 'interests']

class PerformanceSimulationForm(forms.Form):
    impressions = forms.IntegerField()
    clicks = forms.IntegerField()
    ad_spend = forms.DecimalField(max_digits=10, decimal_places=2)
    revenue = forms.DecimalField(max_digits=10, decimal_places=2)

class AdContentForm(forms.Form):
    campaign_description = forms.CharField(widget=forms.Textarea, label="Campaign Description", required=True)

from django import forms

class SchedulePostForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
    schedule_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

class SocialMediaAccountForm(forms.ModelForm):
    class Meta:
        model = SocialMediaAccount
        fields = ['platform_name', 'account_name', 'access_token', 'is_active']

class ScheduledPostForm(forms.ModelForm):
    class Meta:
        model = ScheduledPost
        fields = ['social_media_account', 'post_content', 'scheduled_time', 'status']
