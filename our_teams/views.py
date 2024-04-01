from django.shortcuts import render
from .models import Team


def our_teams(request):

    """ A view to show all products, including sorting and search queries """

    teams = Team.objects.all()

    context = {
        'teams': teams,
    }

    return render(request, 'our_teams.html', context)