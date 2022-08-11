from dataclasses import field
from datetime import datetime
from email.generator import DecodedGenerator
import json
from unicodedata import decimal

from django import http
from django.core import management, serializers
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from locations.forms import LocationForm
from locations.models import Location

@method_decorator(csrf_exempt, name='dispatch')
class BaseView(View):
    def get_params(self):
        try:
            return json.loads(self.request.body.decode('utf-8'))
        except ValueError as e:
            return {'exception': e}

class Locations(BaseView):
    def put(self, *args, **kwargs):
        form = LocationForm(data = self.get_params())
        if form.is_valid():
            form.save()
            return http.HttpResponse('Position stored')
        return http.HttpResponseBadRequest('Not valid')

class Stops(BaseView):
    def dif_and_return(self, first, last):
        difference = last.timestamp - first.timestamp

        res = {}
        res['duration'] = difference.total_seconds()
        res['lat'] = first.lat
        res['lon'] = first.lon
        return res

    def post(self, *args, **kwargs):

        params = self.get_params()
        try:
            search_date = datetime.strptime(params.get('date'), '%d/%m/%Y').date()
        except:
            return http.HttpResponseBadRequest()
        locations = Location.objects.filter(timestamp__year = search_date.year,
                                            timestamp__month = search_date.month,
                                            timestamp__day = search_date.day).order_by('timestamp')
        last = None
        result = []
        for loc in locations:
            if (loc.speed == 0):
                if(last != None):
                    if(loc.lat != last.lat or loc.lon != last.lon):
                        result.append(self.dif_and_return(last, loc))
                        last = loc
                else:
                    last = loc
            else:
                if (last != None):
                    result.append(self.dif_and_return(last, loc))
                    last = None
        return http.JsonResponse(result, safe=False)
        


class OverSpeed(BaseView):
    def post(self, *args, **kwargs):
        params = self.get_params()
        try:
            search_date = datetime.strptime(params.get('date'), '%d/%m/%Y').date()
            speed = params.get('speed')
        except:
            return http.HttpResponseBadRequest()
        locations = Location.objects.filter(timestamp__year = search_date.year,
                                            timestamp__month = search_date.month,
                                            timestamp__day = search_date.day,
                                            speed__gte = speed).values('houmer_id', 'lat', 'lon', 'speed', 'timestamp')
        return http.JsonResponse(list(locations), safe=False)
 
@method_decorator(csrf_exempt, name='dispatch')
def migrate(request):
    management.call_command('migrate')
    return http.HttpResponse('done')
