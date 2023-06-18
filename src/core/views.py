from django.shortcuts import redirect, render

from core.forms import MessageForm


def index(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            request.session['message'] = form.cleaned_data['message']

            return redirect('core:index')

        else:
            message = '<failed to set>'

    else:
        form = MessageForm()

        message = request.session.get('message', '')

    return render(request, 'core/index.html', {'message': message, 'form': form})
