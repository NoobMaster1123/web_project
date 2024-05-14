from re import search
from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

from categories.models import Movie

def q_search(query):
    
    if query.isdigit() and len(query) <= 5:
        return Movie.objects.filter(id=int(query))
    
    vector = SearchVector("name", "description")
    query = SearchQuery(query)
    return Movie.objects.annotate(rank=SearchRank(vector, query)).order_by("-rank")


    # keyword = [word for word in query.split() if len(word) > 2]
    
    # q_objects = Q()

    # for token in keyword:
    #     q_objects |= Q(description__icontains=token)
    #     q_objects |= Q(name__icontains=token)

    # return Movie.objects.filter(q_objects)