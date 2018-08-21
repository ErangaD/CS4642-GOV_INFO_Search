from django.shortcuts import render
from . searchField import getSearchResults

def index(request):
    return render(request, 'current_datetime.html')

def get_search_field(request):
    search_term = request.POST.get('search_text', '')
    blog_entries = [{'text': "name", 'link': "calm"}]

    if request.method == 'POST':
        print(search_term)
        blog_entries = getSearchResults(search_term)

    return render(request, 'current_datetime.html', {'blog_entries': blog_entries})