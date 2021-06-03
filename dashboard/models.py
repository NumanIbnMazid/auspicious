from django.db import models
from django.conf import settings
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from middlewares.middlewares import RequestMiddleware
from util.helpers import get_dynamic_fields
from util.utils import (
    time_str_mix_slug, upload_project_image_path
)
from django.utils.text import slugify


class ProjectCategory(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="title"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='created at'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='updated at'
    )

    class Meta:
        verbose_name = ("Project Category")
        verbose_name_plural = ("Project Categories")
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_fields(self):
        return [get_dynamic_fields(field, self) for field in self.__class__._meta.fields]


# # -------------------------------------------------------------------
# #                           Project
# # -------------------------------------------------------------------

class Project(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="name"
    )
    slug = models.SlugField(
        unique=True, verbose_name='slug'
    )
    category = models.ForeignKey(
        ProjectCategory, on_delete=models.CASCADE, related_name="project_category", verbose_name="project category"
    )
    client_name = models.CharField(
        max_length=100, verbose_name="client name"
    )
    developement_start_year = models.PositiveIntegerField(
        verbose_name="development start year"
    )
    developement_end_year = models.PositiveIntegerField(
        blank=True, null=True, verbose_name="development end year"
    )
    image = models.ImageField(
        upload_to=upload_project_image_path, blank=True, null=True, verbose_name="image"
    )
    scope = models.TextField(
        blank=True, null=True, verbose_name="scope"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='created at'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='updated at'
    )

    class Meta:
        verbose_name = ("Project")
        verbose_name_plural = ("Projects")
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    def get_fields(self):
        return [get_dynamic_fields(field=field, self=self) for field in self.__class__._meta.fields]


# # -------------------------------------------------------------------
# #                           NewsCategory
# # -------------------------------------------------------------------

class NewsCategory(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="title"
    )
    image = models.ImageField(
        blank=True, null=True, verbose_name="image"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='created at'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='updated at'
    )

    class Meta:
        verbose_name = ("News Category")
        verbose_name_plural = ("News Categories")
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_fields(self):
        return [get_dynamic_fields(field, self) for field in self.__class__._meta.fields]


# # -------------------------------------------------------------------
# #                           News
# # -------------------------------------------------------------------


class News(models.Model):
    title = models.CharField(
        max_length=255, verbose_name="title"
    )
    slug = models.SlugField(
        unique=True, verbose_name='slug'
    )
    category = models.ForeignKey(
        NewsCategory, on_delete=models.CASCADE, related_name="news_category", verbose_name="category"
    )
    image = models.ImageField(
        blank=True, null=True, verbose_name="image"
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="description"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='created at'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='updated at'
    )

    class Meta:
        verbose_name = ("News")
        verbose_name_plural = ("News List")
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_fields(self):
        return [get_dynamic_fields(field=field, self=self) for field in self.__class__._meta.fields]

    def get_fields(self):
        def get_dynamic_fields(field):
            if field.name == 'category':
                return (field.name, self.category.title, field.get_internal_type())
            else:
                return (field.name, field.value_from_object(self), field.get_internal_type())
        return [get_dynamic_fields(field) for field in self.__class__._meta.fields]

# # -------------------------------------------------------------------
# #                           Comment
# # -------------------------------------------------------------------

class Comment(models.Model):
    news = models.ForeignKey(
        News, on_delete=models.CASCADE, related_name='news_comment', verbose_name='news'
    )
    commented_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_comment', verbose_name='commented by'
    )
    comment = models.TextField(
        blank=True, null=True, verbose_name='comment'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='created at'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='updated at'
    )

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['-updated_at']

    def __str__(self):
        return self.news.title

    def get_fields(self):
        def get_dynamic_fields(field):
            if field.name == 'news':
                return (field.name, self.news.title)
            elif field.name == 'commented_by':
                return (field.name, self.commented_by.username, field.get_internal_type())
            else:
                return (field.name, field.value_from_object(self), field.get_internal_type())
        return [get_dynamic_fields(field) for field in self.__class__._meta.fields]


# # -------------------------------------------------------------------
# #                           CommentReply
# # -------------------------------------------------------------------

class CommentReply(models.Model):
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name='comment_reply', verbose_name='comment'
    )
    replied_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_comment_reply', verbose_name='replied by'
    )
    reply = models.TextField(
        blank=True, null=True, verbose_name='reply'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='created at'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='updated at'
    )

    class Meta:
        verbose_name = 'Comment Reply'
        verbose_name_plural = 'Comment Replies'
        ordering = ['-updated_at']

    def __str__(self):
        return self.comment.commented_by.username

    def get_fields(self):
        def get_dynamic_fields(field):
            if field.name == 'news':
                return (field.name, self.news.title, field.get_internal_type())
            elif field.name == 'replied_by':
                return (field.name, self.replied_by.username, field.get_internal_type())
            else:
                return (field.name, field.value_from_object(self), field.get_internal_type())
        return [get_dynamic_fields(field) for field in self.__class__._meta.fields]


# # -------------------------------------------------------------------
# #                           Client
# # -------------------------------------------------------------------

class Client(models.Model):
    class ClientCategory(models.TextChoices):
        SISTER_CONCERN = "Sister Concern", ("Sister Concern")
        ENLISTMENT = "Enlistment", ("Enlistment")
        LOCAL_REPRESENTATIVE = "Local Representative", ("Local Representative")
        CIVIL = "Civil", ("Civil")
        TELECOM = "Telecom", ("Telecom")

    name = models.CharField(
        max_length=100, verbose_name="name"
    )
    slug = models.SlugField(
        unique=True, verbose_name='slug'
    )
    logo = models.ImageField(
        blank=True, null=True, verbose_name="logo"
    )
    category = models.CharField(
        max_length=50, choices=ClientCategory.choices, default=None, verbose_name="category"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='created at'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='updated at'
    )

    class Meta:
        verbose_name = ("Client")
        verbose_name_plural = ("Clients")
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    def get_fields(self):
        return [get_dynamic_fields(field, self) for field in self.__class__._meta.fields]


# # -------------------------------------------------------------------
# #                           SocialAccount
# # -------------------------------------------------------------------


class SocialAccount(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="title"
    )
    logo = models.ImageField(
        blank=True, null=True, verbose_name="logo"
    )
    url = models.URLField(
        verbose_name="url"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='created at'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='updated at'
    )

    class Meta:
        verbose_name = ("Social Account")
        verbose_name_plural = ("Social Accounts")
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_fields(self):
        return [get_dynamic_fields(field, self) for field in self.__class__._meta.fields]


# # -------------------------------------------------------------------
# #                           JobPosition
# # -------------------------------------------------------------------


class JobPosition(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="title"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='created at'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='updated at'
    )

    class Meta:
        verbose_name = ("Job Position")
        verbose_name_plural = ("Job Positions")
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_fields(self):
        return [get_dynamic_fields(field, self) for field in self.__class__._meta.fields]


# # -------------------------------------------------------------------
# #                               Job
# # -------------------------------------------------------------------


class Job(models.Model):
    class JobType(models.TextChoices):
        PART_TIME = "Part Time", ("Part Time")
        FULL_TIME = "Full Time", ("Full Time")
        INTERNSHIP = "Internship", ("Internship")
    job_position = models.ForeignKey(
        JobPosition, on_delete=models.CASCADE, related_name="career_job_position", verbose_name="job position"
    )
    slug = models.SlugField(
        unique=True, verbose_name='slug'
    )
    job_type = models.CharField(
        max_length=50, choices=JobType.choices, default="Full Time", verbose_name="job type"
    )
    location = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="location"
    )
    hours = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="hours"
    )
    salary = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="salary"
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="description"
    )
    is_active = models.BooleanField(
        default=True, verbose_name="is active"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='created at'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='updated at'
    )

    class Meta:
        verbose_name = ("Job")
        verbose_name_plural = ("Jobs")
        ordering = ["-created_at"]

    def __str__(self):
        return self.job_position.title

    def get_fields(self):
        def get_dynamic_fields(field):
            if field.name == 'job_position':
                return (field.name, self.job_position.title, field.get_internal_type())
            else:
                return (field.name, field.value_from_object(self), field.get_internal_type())
        return [get_dynamic_fields(field) for field in self.__class__._meta.fields]


# # -------------------------------------------------------------------
# #                              Career
# # -------------------------------------------------------------------


class Career(models.Model):
    class Status(models.TextChoices):
        PENDING = "Pending", ("Pending")
        REVIEW = "Review", ("Review")
        CONFIRMED = "Confirmed", ("Confirmed")
        REJECTED = "Rejected", ("Rejected")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="career_user", verbose_name="user"
    )
    job = models.ForeignKey(
        Job, on_delete=models.CASCADE, related_name="career_job", verbose_name="job"
    )
    file = models.FileField(
        blank=True, null=True, verbose_name="file"
    )
    status = models.CharField(
        max_length=50, choices=Status.choices, default="Pending", verbose_name="status"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='created at'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='updated at'
    )

    class Meta:
        verbose_name = ("Career")
        verbose_name_plural = ("Career")
        ordering = ["-created_at"]

    def __str__(self):
        return self.user.username

    def get_fields(self):
        def get_dynamic_fields(field):
            if field.name == 'user':
                return (field.name, self.user.username, field.get_internal_type())
            elif field.name == 'job':
                return (field.name, self.job.job_position.title, field.get_internal_type())
            else:
                return (field.name, field.value_from_object(self), field.get_internal_type())
        return [get_dynamic_fields(field) for field in self.__class__._meta.fields]


# # -------------------------------------------------------------------
# #                           Gallery
# # -------------------------------------------------------------------


class Gallery(models.Model):
    title = models.CharField(
        max_length=255, verbose_name="title"
    )
    slug = models.SlugField(
        unique=True, verbose_name='slug'
    )
    image = models.ImageField(
        verbose_name="image"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='created at'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='updated at'
    )

    class Meta:
        verbose_name = ("Gallery")
        verbose_name_plural = ("Gallery")
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_fields(self):
        return [get_dynamic_fields(field, self) for field in self.__class__._meta.fields]


# # -------------------------------------------------------------------
# #                           Contact
# # -------------------------------------------------------------------


class Contact(models.Model):
    phone1 = models.CharField(
        max_length=50, verbose_name="phone 1"
    )
    phone2 = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="phone 2"
    )
    email = models.EmailField(
        blank=True, null=True, verbose_name="email"
    )
    address = models.CharField(
        blank=True, null=True, max_length=255, verbose_name="address"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='created at'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='updated at'
    )

    class Meta:
        verbose_name = ("Contact")
        verbose_name_plural = ("Contacts")
        ordering = ["-created_at"]

    def __str__(self):
        return self.phone1

    def get_fields(self):
        return [get_dynamic_fields(field, self) for field in self.__class__._meta.fields]


# # -------------------------------------------------------------------
# #                  Pre-Save Post-Save Configurations
# # -------------------------------------------------------------------


# # Project

def project_slug_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        title = slugify(instance.name.lower()[:17])
        slug_binding = title + '-' + time_str_mix_slug()
        instance.slug = slug_binding


pre_save.connect(project_slug_pre_save_receiver, sender=Project)

# # News

def news_slug_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        title = slugify(instance.title.lower()[:17])
        slug_binding = title + '-' + time_str_mix_slug()
        instance.slug = slug_binding


pre_save.connect(news_slug_pre_save_receiver, sender=News)

# # Client

def client_slug_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        title = slugify(instance.name.lower()[:17])
        slug_binding = title + '-' + time_str_mix_slug()
        instance.slug = slug_binding


pre_save.connect(client_slug_pre_save_receiver, sender=Client)

# # Gallery

def gallery_slug_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        title = slugify(instance.title.lower()[:17])
        slug_binding = title + '-' + time_str_mix_slug()
        instance.slug = slug_binding


pre_save.connect(gallery_slug_pre_save_receiver, sender=Gallery)

# # Job

def job_slug_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        title = slugify(instance.job_position.title.lower()[:17])
        slug_binding = title + '-' + time_str_mix_slug()
        instance.slug = slug_binding


pre_save.connect(job_slug_pre_save_receiver, sender=Job)
