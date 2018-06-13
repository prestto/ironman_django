from django.http import HttpResponse
from . import urls

def home_page(request):
    
    resp = """
        This is the home page of the ironbase website. <br>
        Not very interesting for the moment<br><br>
        but I hope that this will change.<br><br>
        Perhaps you'd like to visit the 
        <a href="{% url 'racehome' %}">Racespage</a> 
        to view all races for which we hold information.
        """

    return HttpResponse(resp)
