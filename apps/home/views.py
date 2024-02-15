from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from os.path import join
from django.conf import settings


def home(request):
    template = loader.get_template("home/index.html")

    context = {
        "latest_question_list": datetime.now(),
    }

    return HttpResponse(template.render(context, request))
