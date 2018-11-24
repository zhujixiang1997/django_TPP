from django.shortcuts import render

from movies.models import Film, Cata


def index(request):
    film_movies1 = Film.objects.filter(cata_log_name='电影').order_by('-update_time')[0:12]
    film_movies2 = Film.objects.filter(cata_log_name='电影').order_by('-update_time')[0:13]
    film_teleplays1 = Film.objects.filter(cata_log_name='电视剧').order_by('-update_time')[0:12]
    film_teleplays2 = Film.objects.filter(cata_log_name='电视剧').order_by('-update_time')[0:13]
    film_animations1 = Film.objects.filter(cata_log_name='动漫').order_by('-update_time')[0:12]
    film_animations2 = Film.objects.filter(cata_log_name='动漫').order_by('-update_time')[0:13]
    catas = Cata.objects.all()
    return render(request,'index.html',context={'catas':catas,
                                                'film_movies1':film_movies1,
                                                'film_movies2':film_movies2,
                                                'film_teleplays1':film_teleplays1,
                                                'film_teleplays2':film_teleplays2,
                                                'film_animations1':film_animations1,
                                                'film_animations2':film_animations2,
                                                }
                  )