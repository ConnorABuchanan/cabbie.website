from django.shortcuts import render
from . import models

# Create your views here.

project_info = [["https://gx.games/games/2gz94d/outofsight/tracks/91f267ee-2ca9-4943-9cf1-e8513b38fdf9/", "out of sight", "outofsightthumb.webp"],
                ["https://github.com/ConnorABuchanan/DinoPrototype", "dinostd prototype", "dinosprototypethumb.png"],
                ["/naughty-or-nice", "naughty or nice", "present.png"]
                ]

def index(request):
    return render(request, "index.html", {"project_info": project_info})

def nice(request):
    return render(request, "nice.html")