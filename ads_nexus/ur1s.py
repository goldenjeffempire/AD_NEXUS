from django.urls import path
from .views import ad_recommendations, ad_simulation, ai_creativity_booster, social_media_dashboard, connect_social_media_account, create_ad_campaign, set_ad_targeting

urlpatterns = [
    path('recommendations/', ad_recommendations, name='ad_recommendations'),
    path('simulate/<int:ad_id>/', ad_simulation, name='ad_simulation'),
    path('creativity-booster/', ai_creativity_booster, name='ai_creativity_booster'),
    path('social-media/', social_media_dashboard, name='social_media_dashboard'),
    path('social-media/connect/<int:platform_id>/', connect_social_media_account, name='connect_social_media_account'),
    path('campaigns/create/', create_ad_campaign, name='create_ad_campaign'),
    path('campaigns/<int:campaign_id>/targeting/', set_ad_targeting, name='set_ad_targeting'),
]
