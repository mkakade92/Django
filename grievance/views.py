from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.http import Http404
from braces.views import SelectRelatedMixin
from django.contrib import messages
from . import models
from . import forms
from django.contrib.auth import get_user_model
Student=get_user_model()

#POSTS VIEWS
# Create your views here.


class GrievanceList(LoginRequiredMixin,generic.ListView):
    context_object_name = 'Grievances'
    model = models.Grievance
    template_name='grievance/grievance_list.html'

    def get_queryset(self):
        try:
            self.grievance_user=Student.objects.prefetch_related('grievances').get(username__iexact=self.kwargs.get('username'))
        except Student.DoesNotExist:
            raise Http404
        else :
            return self.grievance_user.grievances.all()

    def get_context_date(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['grievance_user'] = self.grievance_user
        return context


class GrievanceDetail(LoginRequiredMixin,generic.DetailView):
    model=models.Grievance
    template_name= 'grievance/grievance_detail.html'

    def get_queryset(self):
        queryset=super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))
    

class CreateGrievance(LoginRequiredMixin,generic.CreateView):
    fields=('title','description','against')
    model=models.Grievance

    def form_valid(self,form):
        self.object=form.save(commit=False)
        self.object.user=self.request.user
        self.object.save()
        return super().form_valid(form)

class DeleteGrievance(LoginRequiredMixin,generic.DeleteView):

    model=models.Grievance
    success_url=reverse_lazy('home')

    def get_queryset(self):
        query_set=super().get_queryset()
        return query_set.filter(user_id=self.request.user.id)

    def delete(self,*args,**kwargs):
        messages.success(self.request,'Grievance Deleted')
        return super().delete(*args,**kwargs)
