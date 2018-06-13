from django.shortcuts import render
from django.http import HttpResponse
from races.models import LinkPage


# Create your views here.

def race_home(request):
    # http://127.0.0.1:8000/races/racehome/
	# return HttpResponse("This is the races home page<br><br>Lets take a look at some of the most recent races...")
    return render(request, 'index.html', {})

def race_page(request, pg_no):
    # http://127.0.0.1:8000/races/racehome/1/
    start_result = (pg_no - 1) * 10
    end_result = start_result + 10

    pertinent_races = LinkPage.objects.values('event_name', 'datetime').order_by('id')[start_result:end_result]
    
    start_body = "This is a list of the top 10 most recent races: <br>"
    http_body = []
    for ind, race in enumerate(pertinent_races):
        http_body.append("{0}. {1} : {2}".format(start_result + (ind + 1), race['event_name'], race['datetime']))
    http_string = "<br>".join(http_body)

    end_body = "<br>Hope you enjoy!"
    return HttpResponse(start_body + http_string + end_body)
    # return HttpResponse(str(start_result) + " " + str(end_result))