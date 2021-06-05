from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.loader import render_to_string
from django.core.files.storage import FileSystemStorage
import datetime
# messages framework
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
# class-based generic views
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
# third party imports
from taggit.models import Tag
from weasyprint import HTML
# import models
from django.contrib.auth.models import User
from .models import Summary



# display summary list
class SummaryList(ListView): 
    model = Summary
    template_name = 'summaries/summary/summary_list.html'
    context_object_name = 'summary_list'
    paginate_by = 5

    def get_queryset(self):
        # filter summary list by tags
        if 'tag_id' in self.kwargs:
            tag = get_object_or_404(Tag, pk=self.kwargs['tag_id']) # get the tag instance
            summary_list =  super().get_queryset().filter(tags__in=[tag]) # filter summary list
            return summary_list
        # filter summary list by category
        elif 'category_id' in self.kwargs:
            category = get_object_or_404(Category, pk=self.kwargs['category_id']) # get the category instance
            summary_list =  super().get_queryset().filter(category=category) # filter summary list
            return summary_list
        else:
            return super().get_queryset()


# display summary details
class SummaryDetail(DetailView):
    model = Summary
    template_name = 'summaries/summary/summary_detail.html'
    context_object_name = 'summary'


# create summary 
class SummaryCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView): 
    model = Summary
    template_name = 'summaries/summary/summary_form_create.html' 
    fields = ['title', 'category', 'body', 'tags']
    success_message = "your summary has been added successfully"

    def form_valid(self, form):
        form.instance.author = self.request.user # add summary author 
        return super().form_valid(form)


# edit summary 
class SummaryUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Summary
    template_name = 'summaries/summary/summary_form_update.html' 
    fields = ['title', 'category', 'body', 'tags']
    success_message = "your summary has been edited successfully"


    def form_valid(self, form):
        # user should be the summary author 
        if form.instance.author == self.request.user:
            return super().form_valid(form)
        else:
            return HttpResponse('you are not summary author')


# delete summary 
class SummaryDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Summary
    template_name = 'summaries/summary/summary_confirm_delete.html' 
    success_message = "your summary has been deleted"
    success_url = reverse_lazy('summaries:summary_list')

    def form_valid(self, form):
        # user should be the summary owner 
        if form.instance.author == self.request.user:
            return super().form_valid(form)
        else:
            return HttpResponse('you are not summary owner')

    def delete(self, request, *args, **kwargs):
        messages.error(request, self.success_message)
        return super().delete(request, *args, **kwargs)


# download summary with weasyprint
class SummaryDownload(View):

    def get(self, request, *args, **kwargs):
        summary = get_object_or_404(Summary, pk=kwargs['pk'])
        context = {'summary': summary, 'date': datetime.datetime.now()}
        html_string = render_to_string('summaries/summary/summary_as_pdf.html', context, request=request)

        html = HTML(string=html_string)
        html.write_pdf(target='/tmp/mypdf.pdf');

        fs = FileSystemStorage('/tmp')
        with fs.open('mypdf.pdf') as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="mypdf.pdf"'
            return response


