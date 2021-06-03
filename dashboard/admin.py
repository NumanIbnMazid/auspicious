from django.contrib import admin
from util.mixings import CustomModelAdminMixin
from .models import (
    ProjectCategory, Project, NewsCategory, News, Comment, CommentReply, Client, SocialAccount, JobPosition, Job, Career, Gallery, Contact
)

admin.site.register(ProjectCategory)
class ProjectAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass

    class Meta:
        model = Project


admin.site.register(Project, ProjectAdmin)


class NewsCategoryAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass

    class Meta:
        model = NewsCategory


admin.site.register(NewsCategory, NewsCategoryAdmin)


class NewsAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass

    class Meta:
        model = News


admin.site.register(News, NewsAdmin)


class CommentAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass

    class Meta:
        model = Comment


admin.site.register(Comment, CommentAdmin)


class CommentReplyAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass

    class Meta:
        model = CommentReply


admin.site.register(CommentReply, CommentReplyAdmin)


class ClientAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass

    class Meta:
        model = Client


admin.site.register(Client, ClientAdmin)


class SocialAccountAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass

    class Meta:
        model = SocialAccount


admin.site.register(SocialAccount, SocialAccountAdmin)


class JobPositionAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass

    class Meta:
        model = JobPosition


admin.site.register(JobPosition, JobPositionAdmin)


class JobAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass

    class Meta:
        model = Job


admin.site.register(Job, JobAdmin)


class CareerAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass

    class Meta:
        model = Career


admin.site.register(Career, CareerAdmin)


class GalleryAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass

    class Meta:
        model = Gallery


admin.site.register(Gallery, GalleryAdmin)


class ContactAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    pass

    class Meta:
        model = Contact


admin.site.register(Contact, ContactAdmin)
