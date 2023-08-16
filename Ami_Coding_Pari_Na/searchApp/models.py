from django.db import models
from django.core.validators import validate_comma_separated_integer_list
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class InputData(models.Model):
    input_values = models.CharField(validators=[validate_comma_separated_integer_list],
                                    max_length=200)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    input_time = models.DateTimeField(default=timezone.now)
