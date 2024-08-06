from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .models import Review, Yarn
from .forms import SignUpForm, ReviewForm
from django.utils.timezone import now


class SignUpView(generic.CreateView):
    # import our adjusted form
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def list_yarn(request):
    """The view for our landing page processes our database for easy iteration
    in the list_yarn template using loops, and passes the processed database
    into context.

    :param request: a Django-generated HttpRequest instance
    :type request: Any
    :return: an HttpResponse that renders the given template with the given
    context
    :rtype: function
    """    
    
    # list of querysets to iterate over in the view
    list_yarns = [i for i in Yarn.objects.all()]
    
    # make a list of lists to use a nested for loop for a grid layout
    table_yarns = []
    while list_yarns:
        table_yarns.append([list_yarns.pop(0) for i in range(4) if list_yarns])
    
    context = {"table_yarns": table_yarns}
    return render(request, "store/list_yarn.html", context=context)


def display_yarn(request, yarn_id):
    yarn = get_object_or_404(Yarn, pk=yarn_id)
    reviews = Review.objects.filter(yarn=yarn_id).select_related("author")
    
    # pass qty into context for use in a dropdown menu
    context = {
        "yarn": yarn,
        "reviews": reviews,
        "qty": range(1, yarn.in_stock + 1)
    }
    
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            new_review = Review(
                author=request.user,
                yarn=yarn, 
                content=review_form.cleaned_data.get("review_content"),
                pub_date=now()
            )
            new_review.save()
    else:
        review_form = ReviewForm()
    
    context['form'] = review_form
    
    return render(request, "store/yarn.html", context=context)
