from django.shortcuts import render

from website.models.biography import Biography


def base(request):
    biography = Biography.objects.first()
    if biography is not None:
        return render(request, "base.html", {"biography": biography})
    
    return render(request, "base.html")
