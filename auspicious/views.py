from django.views.generic import TemplateView, CreateView, UpdateView
from dashboard.models import *
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from datetime import date, datetime, timedelta
from django.urls import reverse
from .forms import CareerManageForm, CommentForm
from django.contrib import messages
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from util.helpers import (
    validate_normal_form, get_simple_context_data, get_simple_object, delete_simple_object, user_has_permission, get_paginated_object
)
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.views.decorators.clickjacking import xframe_options_exempt
from django.core.paginator import Paginator
from django.db.models import Count, Min, Q, query_utils


# # -------------------------------------------------------------------
# #                              404
# # -------------------------------------------------------------------

def get_404_page(request, exception):
    return render(request, 'exceptions/404.html')

# class HomeView(request):
#     project_category_qs = ProjectCategory.objects.all()
#     project_qs = Project.objects.all()
#     contex = {'project_category_qs':project_category_qs,
#               'project_qs':project_qs}
#
#     # template_name = "index.html"
#     return render(request, 'index.html', contex)
#

# # -------------------------------------------------------------------
# #                              Home
# # -------------------------------------------------------------------

# @xframe_options_exempt
def home(request):
    today = timezone.datetime.now()
    datetime_today = datetime.strptime(
        str(today.date()) + " 00:00:00", '%Y-%m-%d %H:%M:%S'
    )
    project_category_qs = ProjectCategory.objects.all()
    project_lists = Project.objects.all()
    ongoing_project_lists = Project.objects.filter(developement_start_year__lte = datetime_today.year,developement_end_year = None).order_by('?')[:4]
    completed_project_lists = Project.objects.filter(developement_start_year__lte = datetime_today.year,developement_end_year__lte = datetime_today.year).order_by('?')[:4]
    latest_project_lists = Project.objects.filter(developement_start_year__lte = datetime_today.year).order_by('-developement_start_year')[:4]
    latest_news_category_lists = NewsCategory.objects.all()
    latest_news_lists = News.objects.all()
    image_lists = Gallery.objects.all().order_by('?')
    clients_lists =  Client.objects.all().order_by('?')[:10]
    contact_qs = Contact.objects.all().last()
    social_account_lists = SocialAccount.objects.all()
    context = {'project_category_qs':project_category_qs,
              'project_lists':project_lists,'ongoing_project_lists':ongoing_project_lists,
               'completed_project_lists':completed_project_lists,'latest_project_lists':latest_project_lists,
               'latest_news_category_lists':latest_news_category_lists,'latest_news_lists':latest_news_lists,
               'image_lists':image_lists,'contact_qs':contact_qs,'clients_lists':clients_lists,
               'social_account_lists': social_account_lists}

    return render(request, 'index.html', context)
#

# # -------------------------------------------------------------------
# #                               About
# # -------------------------------------------------------------------

class AboutView(TemplateView):
    template_name = 'page/about.html'

# class CivilProjectView(TemplateView):
#     template_name = 'page/civil-project.html'

# # -------------------------------------------------------------------
# #                               Civil  Project
# # -------------------------------------------------------------------

def civilproject(request):
    today = timezone.datetime.now()
    datetime_today = datetime.strptime(
        str(today.date()) + " 00:00:00", '%Y-%m-%d %H:%M:%S'
    )
    ongoing_project_lists = Project.objects.filter(developement_end_year=None, category__title__icontains = 'Civil' ).order_by('-developement_start_year')
    completed_project_lists = Project.objects.filter(developement_end_year__lte = datetime_today.year, category__title__icontains = 'Civil' ).order_by('-developement_start_year')
    context ={'ongoing_project_lists':ongoing_project_lists,'completed_project_lists':completed_project_lists}
    return render(request, 'page/civil-project.html', context)
# # -------------------------------------------------------------------
# #                               Civil Project Filter
# # -------------------------------------------------------------------


def filtered_project_lists(request, slug):
    today = timezone.datetime.now()
    datetime_today = datetime.strptime(
        str(today.date()) + " 00:00:00", '%Y-%m-%d %H:%M:%S'
    )
    project_lists = Project.objects.filter(category__slug__iexact=slug)

    completed_projects = project_lists.filter(
        ~Q(developement_end_year=None)
    )
    ongoing_projects = project_lists.filter(
        developement_end_year=None
    )
    context = {
        'ongoing_project_lists':ongoing_projects,
        'completed_project_lists':completed_projects,
    }
    return render(request, "page/civil-project.html", context)


# # -------------------------------------------------------------------
# #                               Telecom Project
# # -------------------------------------------------------------------


def telecomproject(request):
    today = timezone.datetime.now()
    datetime_today = datetime.strptime(
        str(today.date()) + " 00:00:00", '%Y-%m-%d %H:%M:%S'
    )
    ongoing_project_lists = Project.objects.filter(developement_end_year=None, category__title__icontains = 'Telecom' ).order_by('-developement_start_year')
    # paginated_ongoing_project_list = get_paginated_object(
    #     request, queryset=ongoing_project_lists, paginate_by=2
    # )

    completed_project_lists = Project.objects.filter(developement_end_year__lte = datetime_today.year, category__title__icontains = 'Telecom' ).order_by('-developement_start_year')
    # paginated_completed_project_list = get_paginated_object(
    #     request, queryset=completed_project_lists, paginate_by=2
    # )

    context ={
        'ongoing_project_lists': ongoing_project_lists,
        'completed_project_lists': completed_project_lists
    }
    return render(request, 'page/telecom-project.html', context)

# # -------------------------------------------------------------------
# #                              Civil Services
# # -------------------------------------------------------------------

class CivilServicesView(TemplateView):
    template_name = 'page/civil-service.html'

# # -------------------------------------------------------------------
# #                               Telecom Services
# # -------------------------------------------------------------------

class TelecomServicesView(TemplateView):
    template_name = 'page/telecom-service.html'

# class CareerView(TemplateView):
#     template_name = 'page/career.html'

# # -------------------------------------------------------------------
# #                               Career
# # -------------------------------------------------------------------

def career(request):
    last_job_qs = Job.objects.all().last()
    job_position_qs = JobPosition.objects.all()
    # job_count = Job.objects.filter(job_position =job_position_qs).count()

    job_lists = Job.objects.filter(is_active = 'True').order_by("id")[1:5]
    career_qs = Career.objects.all()
    if request.user.is_authenticated:
        user_cv = Career.objects.filter(
            user=request.user, job_id=None
        ).last()
    else:
        user_cv = None
    user = request.user
    
    context = {
        'last_job_qs':last_job_qs,
        'job_lists': job_lists,
        'job_position_qs':job_position_qs,
        'career_qs':career_qs,
        'user':user,
        'user_cv': user_cv
    }
    return render(request, "page/career.html", context)

# # -------------------------------------------------------------------
# #                              Client Details
# # -------------------------------------------------------------------

def client(request):
    sister_client_lists = Client.objects.filter(category = 'Sister Concern')
    enlistment_client_lists = Client.objects.filter(category = 'Enlistment')
    local_client_representative_lists = Client.objects.filter(category = 'Local Representative')
    civil_client_lists = Client.objects.filter(category = 'Civil')
    telecom_client_lists = Client.objects.filter(category = 'Telecom')
    context = {'sister_client_lists':sister_client_lists,
               'enlistment_client_lists':enlistment_client_lists,
               'local_client_representative_lists':local_client_representative_lists,
               'civil_client_lists':civil_client_lists,'telecom_client_lists':telecom_client_lists}
    return render(request, 'page/client.html', context)


# # -------------------------------------------------------------------
# #                              News
# # -------------------------------------------------------------------


def news(request):
    news_lists= News.objects.all().order_by('-id')
    paginated_news = get_paginated_object(
        request, queryset=news_lists, paginate_by=6
    )

    context = {'paginated_news_list': paginated_news}
    return render(request,'page/news.html', context)

# # -------------------------------------------------------------------
# #                              Blog
# # -------------------------------------------------------------------


def blog(request):
    blogs_lists= Blog.objects.all().order_by('-id')
    paginated_news = get_paginated_object(
        request, queryset=blogs_lists, paginate_by=6
    )

    context = {'paginated_news_list': paginated_news}
    return render(request,'page/news.html', context)


# # -------------------------------------------------------------------
# #                               Contact
# # -------------------------------------------------------------------

def contact(request):
    contact_qs = Contact.objects.all().last()
    context ={'contact_qs':contact_qs}
    return render(request, 'page/contact.html', context)

# # -------------------------------------------------------------------
# #                               News Details
# # -------------------------------------------------------------------

# @login_required
def news_details(request, slug):
    news_qs = News.objects.filter(slug = slug).first()
    comment_qs = Comment.objects.filter(news=news_qs, is_approved=True)
    news_category_lists = NewsCategory.objects.all().order_by('-id')
    reply_qs = CommentReply.objects.filter(comment=comment_qs.first(), is_approved=True)
    last_three_job_lists = News.objects.all().exclude(slug = slug).order_by('-id')[0:3]

    pre_news = News.objects.filter(
        id__lt=news_qs.id
    ).first()
    next_news = News.objects.filter(
        id__gt=news_qs.id
    ).first()

    context ={'news_qs':news_qs,'comment_qs':comment_qs,
                'total_comment':comment_qs.count(),
                'reply_qs':reply_qs,'news_category_lists':news_category_lists,
                'last_three_job_lists':last_three_job_lists,
                'pre_news':pre_news,'next_news':next_news
            }

    if request.method == 'POST':
        if request.user.is_authenticated:
            comment = request.POST.get("comment")
            Comment.objects.create(
                news=news_qs,
                commented_by=request.user,
                comment=comment
            )
            return HttpResponseRedirect(reverse("news_details", kwargs={"slug": slug}))
        else:
            return HttpResponseRedirect(reverse("account_login"))

    return render(request, "page/news-details.html", context)


# # -------------------------------------------------------------------
# #                               Blog Details
# # -------------------------------------------------------------------

# @login_required
def blog_details(request, slug):
    blog_qs = Blog.objects.filter(slug = slug).first()
    comment_qs = BlogComment.objects.filter(blog = blog_qs)
    blog_category_lists = BlogCategory.objects.all().order_by('-id')
    reply_qs = BlogCommentReply.objects.filter(blog_comment = comment_qs.first())
    last_three_job_lists = Blog.objects.all().exclude(slug = slug).order_by('-id')[0:4]

    if blog_qs:
        pre_blog = Blog.objects.filter(
            id__lt=blog_qs.id
        ).first()
        next_blog = Blog.objects.filter(
            id__gt=blog_qs.id
        ).first()
    else:
        pre_blog = ''
        next_blog = ''

    context ={'blog_qs':blog_qs,
                'blog_category_lists':blog_category_lists,
                'last_three_job_lists':last_three_job_lists,
                'pre_blog':pre_blog,'next_blog':next_blog,
                'comment_qs':comment_qs,
                'total_comment':comment_qs.count(),
            }

    if request.method == 'POST':
        if request.user.is_authenticated:
            comment = request.POST.get("comment")
            BlogComment.objects.create(
                blog=blog_qs,
                commented_by=request.user,
                comment=comment
            )
            return HttpResponseRedirect(reverse("blog_details", kwargs={"slug": slug}))
        else:
            return HttpResponseRedirect(reverse("account_login"))

    return render(request, "page/blog-details.html", context)

# # -------------------------------------------------------------------
# #                              Comment
# # -------------------------------------------------------------------


@method_decorator(login_required, name='dispatch')
class CommentCreateView(CreateView):
    template_name = "page/news-details.html"
    form_class = CommentForm

    def form_valid(self, form, **kwargs):
        slug = self.kwargs['slug']
        comment_qs = Comment.objects.filter(news__slug=slug)
        if comment_qs.exists():
            qs = Comment.objects.filter(
                news__slug = slug, user=self.request.user
            )
            if not qs.exists():
                form.instance.user = self.request.user
                form.instance.news = comment_qs.last()
                messages.add_message(
                    self.request, messages.SUCCESS, "Comment successfully!"
                )
                return super().form_valid(form)
        messages.add_message(
            self.request, messages.ERROR, "Failed to Comment!"
        )
        return super().form_invalid(form)

    def get_success_url(self):
        return self.request.POST.get('next', reverse('home'))

    def get_context_data(self, **kwargs):
        context = super(
            JobApplyCreateView, self
        ).get_context_data(**kwargs)
        qs = Job.objects.filter(slug=self.kwargs['slug'])
        if qs.exists():
            context['job'] = qs.last()
        else:
            context['job'] = None
        return context


# # -------------------------------------------------------------------
# #                              News Comment Reply
# # -------------------------------------------------------------------


@login_required
def comment_reply(request, id):
    comment_qs = Comment.objects.filter(id=id)
    if comment_qs.exists():
        comment_object = comment_qs.last()
        slug = comment_object.news.slug
        news_qs = News.objects.filter(slug=slug).first()
        comment_qs = Comment.objects.filter(news=news_qs)
        news_category_lists = NewsCategory.objects.all().order_by('-id')
        reply_qs = CommentReply.objects.filter(comment=comment_qs.first())
        last_three_job_lists = News.objects.all().exclude(
            slug=slug).order_by('-id')[0:3]

        pre_news = News.objects.filter(
            id__lt=news_qs.id
        ).first()
        next_news = News.objects.filter(
            id__gt=news_qs.id
        ).first()

        context = {'news_qs': news_qs, 'comment_qs': comment_qs,
                'total_comment': comment_qs.count(),
                'reply_qs': reply_qs, 'news_category_lists': news_category_lists,
                'last_three_job_lists': last_three_job_lists,
                'pre_news': pre_news, 'next_news': next_news
                }
        if request.method == "POST":
            reply = request.POST.get("reply")
            CommentReply.objects.create(
                comment=comment_object,
                replied_by=request.user,
                reply=reply
            )
        return HttpResponseRedirect(reverse("news_details", kwargs={"slug": slug}))
    return render(request, "page/news-details.html")

# # -------------------------------------------------------------------
# #                              Blog Comment Reply
# # -------------------------------------------------------------------


@login_required
def comment_reply(request, id):
    comment_qs = BlogComment.objects.filter(id=id)
    if comment_qs.exists():
        comment_object = comment_qs.last()
        slug = comment_object.blog.slug
        blog_qs = Blog.objects.filter(slug=slug).first()
        comment_qs = BlogComment.objects.filter(blog=blog_qs)
        blog_category_lists = BlogCategory.objects.all().order_by('-id')
        reply_qs = BlogCommentReply.objects.filter(blog_comment=comment_qs.first())
        last_three_blog_lists = Blog.objects.all().exclude(
            slug=slug).order_by('-id')[0:4]

        pre_blog = Blog.objects.filter(
            id__lt=blog_qs.id
        ).first()
        next_blog = Blog.objects.filter(
            id__gt=blog_qs.id
        ).first()

        context = {'blog_qs': blog_qs, 'comment_qs': comment_qs,
                'total_comment': comment_qs.count(),
                'reply_qs': reply_qs, 'blog_category_lists': blog_category_lists,
                'last_three_bloglists': last_three_blog_lists,
                'pre_blog': pre_blog, 'next_blog': next_blog
                }
        if request.method == "POST":
            reply = request.POST.get("reply")
            BlogCommentReply.objects.create(
                blog_comment=comment_object,
                replied_by=request.user,
                reply=reply
            )
        return HttpResponseRedirect(reverse("blog_details", kwargs={"slug": slug}))
    return render(request, "page/blog-details.html")


# # -------------------------------------------------------------------
# #                              Filtered News
# # -------------------------------------------------------------------

def filtered_news_lists(request, slug):
    news_lists = News.objects.filter(
        category__slug__iexact=slug
    )
    context = {
        'paginated_news_list':news_lists,
        'filtered_news_title': news_lists.first().category.title if len(news_lists) > 0 else ""
    }
    return render(request, "page/news.html", context)

# # -------------------------------------------------------------------
# #                              Filtered Blog
# # -------------------------------------------------------------------

def filtered_blog_lists(request, slug):
    blog_lists = Blog.objects.filter(
        category__slug__iexact=slug
    )
    context = {
        'paginated_news_list':blog_lists,
        'filtered_news_title': blog_lists.first().category.title if len(blog_lists) > 0 else ""
    }
    return render(request, "page/news.html", context)

# # -------------------------------------------------------------------
# #                               Job Details
# # -------------------------------------------------------------------

def job_details(request, slug):
    job_qs = Job.objects.filter(slug = slug, is_active = 'True').first()
    job_position_qs = JobPosition.objects.all()
    contact_qs =  Contact.objects.all().last()
    context ={'job_qs':job_qs, 'job_position_qs':job_position_qs,
              'contact_qs':contact_qs}
    return render(request, "page/job-page.html", context)

# # -------------------------------------------------------------------
# #                              All Job Lists
# # -------------------------------------------------------------------

def all_job_lists(request):
    last_job_qs = Job.objects.filter(is_active=True).last()
    job_lists = Job.objects.filter(is_active=True).order_by("id")

    job_list_qs = Job.objects.filter(is_active=True)
    paginated_jobs = get_paginated_object(
        request, queryset=job_list_qs, paginate_by=6
    )

    context = {
        'last_job_qs':last_job_qs,
        'job_lists': job_lists,
        "paginated_jobs": paginated_jobs
    }
    return render(request, "page/all-jobs.html", context)

# # -------------------------------------------------------------------
# #                              Filtered Job
# # -------------------------------------------------------------------

def filtered_job_lists(request, slug):
    job_qs = Job.objects.filter(
        job_position__slug__iexact=slug
    )
    context = {
        'paginated_jobs':job_qs,
        'filtered_job_title': job_qs.first().job_position.title if len(job_qs) > 0 else ""
    }
    return render(request, "page/all-jobs.html", context)


# # -------------------------------------------------------------------
# #                              Gallery
# # -------------------------------------------------------------------
def gallery(request):
    image_groups = ImageGroup.objects.all()
    other_images = Gallery.objects.filter(
        image_group=None
    )
    context = {
        "image_groups": image_groups,
        "other_images": other_images
    }
    return render(request, 'page/galleries.html', context)


# # -------------------------------------------------------------------
# #                              Project Details
# # -------------------------------------------------------------------
def project_details(request, slug):
    project_qs = Project.objects.filter(slug = slug).first()
    latest_project_lists = Project.objects.all().exclude(slug=slug)[0:4]
    project_category_lists = ProjectCategory.objects.all()
    context = {'project_qs':project_qs,
    'project_category_lists':project_category_lists,
    'latest_project_lists':latest_project_lists}
    return render(request, 'page/project-detail.html', context)

# # -------------------------------------------------------------------
# #                               Job Apply
# # -------------------------------------------------------------------

@method_decorator(login_required, name='dispatch')
class JobApplyCreateView(CreateView):
    template_name = "page/job-apply.html"
    form_class = CareerManageForm

    def form_valid(self, form, **kwargs):
        slug = self.kwargs['slug']
        job_qs = Job.objects.filter(slug=slug)
        if job_qs.exists():

            qs = Career.objects.filter(
                job__slug=slug, user=self.request.user
            )
            if not qs.exists():
                form.instance.user = self.request.user
                form.instance.job = job_qs.last()
                messages.add_message(
                    self.request, messages.SUCCESS, "Applied successfully!"
                )
                return super().form_valid(form)
            else:
                form.add_error(
                    None, forms.ValidationError(
                        "You already applied for this job! Please update the application if required!"
                    )
                )
        messages.add_message(
            self.request, messages.ERROR, "Failed to apply!"
        )
        return super().form_invalid(form)

    def dispatch(self, request, *args, **kwargs):
        slug = self.kwargs['slug']
        qs = Career.objects.filter(
            job__slug=slug, user=self.request.user
        )
        if qs.exists():
            messages.add_message(
                self.request, messages.WARNING, "Already Applied!"
            )
            return HttpResponseRedirect(reverse('home'))
        return super(JobApplyCreateView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return self.request.POST.get('next', reverse('home'))

    def get_context_data(self, **kwargs):
        context = super(
            JobApplyCreateView, self
        ).get_context_data(**kwargs)
        qs = Job.objects.filter(slug=self.kwargs['slug'])
        if qs.exists():
            context['job'] = qs.last()
        else:
            context['job'] = None
        return context

@method_decorator(login_required, name='dispatch')
class JobApplyUpdateView(UpdateView):
    template_name = "page/job-apply.html"
    form_class = CareerManageForm

    def get_object(self):
        qs = Career.objects.filter(
            job__slug=self.kwargs['slug'], user=self.request.user
        )
        if qs.exists():
            return qs.last()
        return None

    def get_form_kwargs(self):
        kwargs = super(JobApplyUpdateView, self).get_form_kwargs()
        if self.form_class:
            kwargs.update({'object': self.get_object()})
        return kwargs

    def form_valid(self, form, **kwargs):
        slug = self.kwargs['slug']
        job_qs = Job.objects.filter(slug=slug)
        if job_qs.exists():
            form.instance.user = self.request.user
            form.instance.job = job_qs.last()
            messages.add_message(
                self.request, messages.SUCCESS, "Application Updated successfully!"
            )
            return super().form_valid(form)
        messages.add_message(
            self.request, messages.ERROR, "Failed to update application!"
        )
        return super().form_invalid(form)

    def get_success_url(self):
        return self.request.POST.get('next', reverse('home'))

    def get_context_data(self, **kwargs):
        context = super(
            JobApplyUpdateView, self
        ).get_context_data(**kwargs)
        qs = Job.objects.filter(slug=self.kwargs['slug'])
        if qs.exists():
            context['job'] = qs.last()
        else:
            context['job'] = None
        return context


# # -------------------------------------------------------------------
# #                              CV Drop
# # -------------------------------------------------------------------

@method_decorator(login_required, name='dispatch')
class CvDropCreateView(CreateView):
    template_name = "page/job-apply.html"
    form_class = CareerManageForm

    def form_valid(self, form, **kwargs):
        # slug = self.kwargs['slug']
        # job_qs = Job.objects.filter(slug=slug)
        # if job_qs.exists():

        qs = Career.objects.filter(
            user=self.request.user
        )
        if not qs.exists():
            form.instance.user = self.request.user
            # form.instance.job = job_qs.last()
            messages.add_message(
                self.request, messages.SUCCESS, "Applied successfully!"
            )
            return super().form_valid(form)
        else:
            form.add_error(
                None, forms.ValidationError(
                    "You already applied for this job! Please update the application if required!"
                )
            )
        messages.add_message(
            self.request, messages.ERROR, "Failed to apply!"
        )
        return super().form_invalid(form)

    def dispatch(self, request, *args, **kwargs):
        # slug = self.kwargs['slug']
        qs = Career.objects.filter(
            user=self.request.user
        )
        if qs.exists():
            messages.add_message(
                self.request, messages.WARNING, "Already Applied!"
            )
            return HttpResponseRedirect(reverse('home'))
        return super(CvDropCreateView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return self.request.POST.get('next', reverse('home'))

    def get_context_data(self, **kwargs):
        context = super(
            CvDropCreateView, self
        ).get_context_data(**kwargs)
        # qs = Job.objects.filter(slug=self.kwargs['slug'])
        # if qs.exists():
        #     context['job'] = qs.last()
        # else:
        #     context['job'] = None
        return context

@method_decorator(login_required, name='dispatch')
class CvDropUpdateView(UpdateView):
    template_name = "page/job-apply.html"
    form_class = CareerManageForm

    def get_object(self):
        qs = Career.objects.filter(
            user=self.request.user, slug = self.kwargs['slug']
        )
        if qs.exists():
            return qs.last()
        return None
    
    def get_form_kwargs(self):
        kwargs = super(CvDropUpdateView, self).get_form_kwargs()
        if self.form_class:
            kwargs.update({'object': self.get_object()})
        return kwargs

    def form_valid(self, form, **kwargs):
        # slug = self.kwargs['slug']
        career_qs = Career.objects.filter(user = self.request.user,
                    slug=self.kwargs['slug'])
        if career_qs.exists():
            form.instance.user = self.request.user
            # form.instance = career_qs.last()
            messages.add_message(
                self.request, messages.SUCCESS, "Application Updated successfully!"
            )
            return super().form_valid(form)
        messages.add_message(
            self.request, messages.ERROR, "Failed to update application!"
        )
        return super().form_invalid(form)

    def get_success_url(self):
        return self.request.POST.get('next', reverse('home'))

    def get_context_data(self, **kwargs):
        context = super(
            CvDropUpdateView, self
        ).get_context_data(**kwargs)
        # qs = Career.objects.filter(user = self.request.user)
        # if qs.exists():
        #     context['user'] = qs.last()
        # else:
        #     context['user'] = None
        return context


# # -------------------------------------------------------------------
# #                              Contact
# # -------------------------------------------------------------------

def post_contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        mail_from = email
        mail_to = settings.RECEIVER_EMAIL
        mail_text = 'Please do not Reply'
        html_content = message + "<br><br>" + f"Name: {name} <br>" + f"Email: {email}"
        msg = EmailMultiAlternatives(
            subject, mail_text, mail_from, [mail_to]
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        messages.add_message(request, messages.SUCCESS,
                             "Message sent successfully!"
                             )
    return render(request, "page/contact.html")
