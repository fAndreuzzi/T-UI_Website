from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Theme

import datetime
import json

# Views

def index(request):
    template = loader.get_template('themes/index.html')

    now = datetime.datetime.now()
    dt = now.strftime("%Y-%m-%d")

    context = {
        "header" : get_header(request, './new_theme', 'New theme'),
        # default values from index.html
        "theme_list" : get_theme_list(request, 0, 3, 0),
        "dt_string" : dt
    }

    return HttpResponse(template.render(context, request))

def new_theme(request):
    template = loader.get_template('themes/new_theme.html')
    theme_preview_template = loader.get_template('themes/theme_preview.html')

    now = datetime.datetime.now()
    dt = now.strftime("%Y-%m-%d")

    def_theme = Theme.objects.filter(author='tui-launcher').values()[0]
    adjust_colors(def_theme)

    theme_preview_context = {
        "dt_string" : dt,
        'theme' : def_theme
    }

    context = {
        "header" : get_header(request, './index', 'View themes'),
        "default_theme_preview" : theme_preview_template.render(theme_preview_context, request),
        "default_theme" : def_theme
    }

    return HttpResponse(template.render(context, request))


# ajax

def more_themes(request, n, order_by, order_type):
    return HttpResponse(get_theme_list(request, n, order_by, order_type))

def publish_theme(request):
    theme = json.loads(request.POST['theme'])
    theme['name'] = request.POST['name']
    theme['author'] = request.POST['author']

    theme_entry = Theme.objects.create(**theme)

    response = JsonResponse({'id' : theme_entry.id})
    return response

# nested templates

def get_theme_list(request, last, order_by, order_type):
    list_template = loader.get_template('themes/theme_list.html')
    theme_template = loader.get_template('themes/theme.html')
    theme_preview_template = loader.get_template('themes/theme_preview.html')

    now = datetime.datetime.now()
    dt = now.strftime("%Y-%m-%d")

    theme_preview_context = {
        "dt_string" : dt,
        'theme' : None
    }

    theme_context = {
        'theme' : None,
        'theme_preview' : None
    }

    list_context = {
        'themes' : []
    }

    themes = get_themes(last, last + 20, order_by, order_type);

    for theme in themes:
        theme_preview_context['theme'] = theme

        theme_context['theme_preview'] = theme_preview_template.render(theme_preview_context, request)
        theme_context['theme'] = theme

        list_context['themes'].append(theme_template.render(theme_context, request))

    return list_template.render(list_context, request)

def get_header(request, nav_link, nav_label):
    template = loader.get_template('themes/header.html')

    context = {
        "nav_link" : nav_link,
        "nav_label" : nav_label
    }

    return template.render(context, request)

# utility functions

def adjust_colors(theme):
    for k,v in theme.items():
        if type(v) == str and v.startswith('#') and len(v) == 9:
            theme[k] = v[1:7]

    return theme

order_by_columns = ['name', 'author', 'downloads', 'id']
def get_themes(from_index, to_index, order_by, order_type):
    # '-' -> desc
    if order_type:
        prefix = ''
    else:
        prefix = '-'

    return Theme.objects.order_by(prefix + order_by_columns[order_by])[min(from_index,Theme.objects.count()):min(to_index,Theme.objects.count())]
