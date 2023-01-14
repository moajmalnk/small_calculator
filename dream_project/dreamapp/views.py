from django.shortcuts import render


def display_form(request):
    return render(request, "form.html")


def display_result(request):
    x = int(request.GET['number_one'])
    y = int(request.GET['number_two'])
    add = x + y
    sub = x - y
    mtp = x * y
    div = x / y
    return render(request, 'results.html',
                  {"display_one": add,
                   "display_two": sub,
                   "display_three": mtp,
                   "display_four": div})
