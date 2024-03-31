from django.shortcuts import render

def our_teams(request):
    return render(request, 'our_teams.html', {})