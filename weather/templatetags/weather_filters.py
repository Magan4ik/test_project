from django import template
from django.contrib.auth import get_user_model

from weather.models import City

User = get_user_model()

register = template.Library()

@register.filter
def follow_city(user: User, city_name: str) -> bool:
    return user.cities.filter(city_name=city_name).exists()
