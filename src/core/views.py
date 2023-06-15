from django.core.cache import cache
from django.shortcuts import redirect, render

from core.forms import MessageForm


def index(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            cache.set('message', form.cleaned_data['message'], 5)

            return redirect('core:index')

    else:
        form = MessageForm()

    return render(request, 'core/index.html', {'message': cache.get('message'), 'form': form})
