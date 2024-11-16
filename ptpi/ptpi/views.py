from django.http import JsonResponse

def home_page(request):
    print("home page requested")
    friends=[
        'Nidhi',
        'Kumkum',
        'Riya',
        'puja',
        'paras'
    ]
    return JsonResponse(home_page)