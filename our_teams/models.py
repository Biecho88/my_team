from django.db import models


class My_Team(models.Model):
    team_name = models.CharField(max_length=50)
    team_category = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.team_name

    def get_team_category(self):
        return self.team_category


class Team(models.Model):
    team_name = models.ForeignKey('My_Team', null=True, blank=True, on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    second_position = models.CharField(max_length=50)
    health_conditions = models.CharField(max_length=50)
    comments = models.CharField(max_length=100)


    def __str__(self):
        return self.team_name