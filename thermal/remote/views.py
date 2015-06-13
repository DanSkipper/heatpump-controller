from django.shortcuts import render 
from django.views.decorators.csrf import ensure_csrf_cookie

import json
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

#import pigpio
#from ir.ir_tx import tx
#from ir.control import *

from remote.models import HeatPumpState

def run(temperature, fan, mode, power):
   return 5
   if mode == '0':
      mode = MODE_HEAT
   elif mode == '1':
      mode = MODE_COOL
   elif mode == '2':
      mode = MODE_AUTO
   elif mode == '3':
      mode = MODE_DEHU

   if fan == '0':
      fan = FAN_0
   elif fan == '1':
      fan = FAN_1
   elif fan == '2':
      fan = FAN_2
   elif fan == '3':
      fan = FAN_3
   elif fan == '4':
      fan = FAN_A

   if power:
      power = POWER_ON
   else:
      power = POWER_OFF

   pi = pigpio.pi()

   transmitter = tx(pi, 25, 38000)

   transmitter.clear_code()
   print mode, fan, power
   #  recorder code
   transmitter.add_to_code(128, 61)
   for bit in build_command(17, mode, fan, power):
      if bit == '1':
         transmitter.add_to_code(16, 18)
      else:
         transmitter.add_to_code(16, 47)
   transmitter.go()

   pi.stop()



@ensure_csrf_cookie
def index(request):
    return render(request, 'remote/index.html' )

@ensure_csrf_cookie
def state(request):
    if HeatPumpState.objects.count() == 0:
        saved_state = HeatPumpState()
    else:
        saved_state = HeatPumpState.objects.all()[0]

    print saved_state.temperature, saved_state.mode, saved_state.fan, saved_state.power

    if request.method == "POST":
        tmp = request.read()
        print tmp
        status = json.loads(tmp)
        run(status["temperature"], status["fan"], status["mode"], status["power"])
        saved_state.temperature = int(status['temperature'])
        saved_state.fan = int(status['fan'])
        saved_state.mode = int(status['mode'])
        saved_state.power = status['power']
        saved_state.save()

    else:
        status = {"power": saved_state.power,
                  "temperature": str(saved_state.temperature),
                  "mode": str(saved_state.mode),
                  "fan": str(saved_state.fan)}

    sendable_data = json.dumps(status, cls=DjangoJSONEncoder)
    return HttpResponse(sendable_data, content_type='application/json')
