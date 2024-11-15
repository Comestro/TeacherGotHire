from django.http import JsonResponse

def home_page(request):
    print("home page requested")
    friends=[
        'Nidhi',
        'Kumkum',
        'Riya'
    ]
    return JsonResponse(friends,safe=False)
