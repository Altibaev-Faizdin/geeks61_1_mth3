from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms
from django.core.paginator import Paginator
from django.db.models import F #
from django.views import generic


class SeachView(generic.ListView):
    template_name = 'prog_languages.html'
    context_object_name = 'prog_lang'
    model = models.ProgLang

    def get_queryset(self):
        return models.ProgLang.objects.filter(title__icontains=self.request.GET.get('s', ''))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = self.request.GET.get('s', '')
        return context


# def search_view(request):
#         quary = request.GET.get('s', '')
#         if quary:
#             prog_lang = models.ProgLang.objects.filter(title__icontains=quary)
#         else:
#             prog_lang = models.ProgLang.objects.none
#         return render(
#             request,
#                 'prog_languages.html',
#                     {
#                     'prog_lang': prog_lang
#                        })
        


class UpdateProgLangView(generic.UpdateView):
    template_name = 'update_prog_lang.html'
    form_class = forms.ProgLangForm
    model = models.ProgLang
    success_url = '/prog_lang/'

    def get_object(self, **kwargs):
        prog_lang_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=prog_lang_id)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateProgLangView, self).form_valid(form=form)

# def update_prog_lang_view(request, id):
#     prog_lang_id = get_object_or_404(models.ProgLang, id=id)
#     if request.method == 'POST':
#         form = forms.ProgLangForm(
#             request.POST,
#             request.FILES,
#             instance=prog_lang_id
#         )
#         if form.is_valid():
#             form.save()
#             return redirect('/prog_lang/')
#     else:
#         form = forms.ProgLangForm(instance=prog_lang_id)

#     return render(request, 'update_prog_lang.html', {
#         'form': form,
#         'prog_lang': prog_lang_id
#     })




class DeleteProgLangView(generic.DeleteView):
    template_name = 'confirm_delete.html'
    success_url = '/prog_lang/'
    content_object_name = 'prog_lang'
    model = models.ProgLang

    def get_object(self, **kwargs):
        prog_lang_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=prog_lang_id)


# def delete_prog_lang_view(request, id):
#     prog_lang_id = get_object_or_404(models.ProgLang, id=id)
#     prog_lang_id.delete()
#     return redirect('/prog_lang/')







class CreateProgLangView(generic.CreateView):
    template_name = 'create_prog_lang.html'
    form_class = forms.ProgLangForm
    success_url = '/prog_lang/'
    model = models.ProgLang

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateProgLangView, self).form_valid(form=form)
    



# def create_prog_lang_view(request):
#     if request.method == 'POST':
#         form = forms.ProgLangForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('/prog_lang/')
#     else:
#         form = forms.ProgLangForm()
#     return render(request, 'create_prog_lang.html', {'form': form}) 




   










class ProgLangDetailView(generic.DetailView):
    template_name = 'prog_lang_detail.html'
    context_object_name = 'prog_id'
    model = models.ProgLang
    pk_url_kwarg = 'id'

    def get_object(self, qweryset=None):
        obj = super().get_object(qweryset)
        request = self.request

        views_lang = request.session.get('viewed_lang', [])
        if obj.pk not in views_lang:
            models.ProgLang.objects.filter(pk=obj.pk).update(views=F('views') + 1)
            views_lang.append(obj.pk)
            request.session['viewed_lang'] = views_lang

            obj.refresh_from_db()
        return obj


# def prog_lang_detail_view(request, id):
#     if request.method == 'GET':
#         prog_lang_id = get_object_or_404(models.ProgLang, id=id)
#         views_lang = request.session.get('viewed_lang', [])

#         if id not in views_lang:
#             prog_lang_id.views = F('views') + 1
#             prog_lang_id.save()
#             prog_lang_id.refresh_from_db()

#             views_lang.append(id)
#             request.session['viewed_lang'] = views_lang

            

#         return render(
#             request, 
#             'prog_lang_detail.html',
#             {
#                 'prog_id': prog_lang_id
#                 }
#             )







class ProgLangListView(generic.ListView):
    template_name = 'prog_languages.html'
    context_object_name = 'prog_lang'
    model = models.ProgLang
    paginate_by = 2


    def get_queryset(self):
        return models.ProgLang.objects.all().order_by('-id')
    


# def prog_lang_list_view(request):
#     if request.method == 'GET':
#         prog_lang = models.ProgLang.objects.all()
#         paginator = Paginator(prog_lang, 2)
#         page = request.GET.get('page')
#         page_obj = paginator.get_page(page)
#         return render(
#             request, 
#             'prog_languages.html',
#             {'prog_lang': page_obj}
#             )
