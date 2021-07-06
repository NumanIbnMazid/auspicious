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
from ckeditor_uploader.fields import RichTextUploadingField


class ProjectCategory(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="title"
    )
    slug = models.SlugField(
        unique=True, verbose_name='slug'
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

    def get_project_count(self):
        return len(Project.objects.filter(
            category__id=self.id
        ))

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
    # scope = models.TextField(
    #     blank=True, null=True, verbose_name="scope"
    # )
    scope = RichTextUploadingField(blank=True, null=True)
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
        def get_dynamic_fields(field):
            if field.name == 'category':
                return (field.name, self.category.title, field.get_internal_type())
            else:
                return (field.name, field.value_from_object(self), field.get_internal_type())
        return [get_dynamic_fields(field) for field in self.__class__._meta.fields]


# # -------------------------------------------------------------------
# #                           NewsCategory
# # -------------------------------------------------------------------

class NewsCategory(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="title"
    )
    slug = models.SlugField(
        unique=True, verbose_name='slug'
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

    def get_news_count(self):
        return len(News.objects.filter(
            category__id=self.id
        ))


# # -------------------------------------------------------------------
# #                           News
# # -------------------------------------------------------------------


class News(models.Model):
    title = models.CharField(
        max_length=255, verbose_name="title"
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="news_created_by", verbose_name="created by"
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
    # description = models.TextField(
    #     blank=True, null=True, verbose_name="description"
    # )
    description = RichTextUploadingField(blank=True, null=True)
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
        def get_dynamic_fields(field):
            if field.name == 'category':
                return (field.name, self.category.title, field.get_internal_type())
            elif field.name == 'created_by':
                return (field.name, self.created_by.username, field.get_internal_type())
            else:
                return (field.name, field.value_from_object(self), field.get_internal_type())
        return [get_dynamic_fields(field) for field in self.__class__._meta.fields]




# # -------------------------------------------------------------------
# #                           BlogCategory
# # -------------------------------------------------------------------

class BlogCategory(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="title"
    )
    slug = models.SlugField(
        unique=True, verbose_name='slug'
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
        verbose_name = ("Blog Category")
        verbose_name_plural = ("Blog Categories")
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_fields(self):
        return [get_dynamic_fields(field, self) for field in self.__class__._meta.fields]

    def get_blog_count(self):
        return len(Blog.objects.filter(
            category__id=self.id
        ))


# # -------------------------------------------------------------------
# #                           Blog
# # -------------------------------------------------------------------


class Blog(models.Model):
    title = models.CharField(
        max_length=255, verbose_name="title"
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="blogs_created_by", verbose_name="created by"
    )
    slug = models.SlugField(
        unique=True, verbose_name='slug'
    )
    category = models.ForeignKey(
        BlogCategory, on_delete=models.CASCADE, related_name="blog_categories", verbose_name="category"
    )
    image = models.ImageField(
        blank=True, null=True, verbose_name="image"
    )
    description = RichTextUploadingField(blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='created at'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='updated at'
    )

    class Meta:
        verbose_name = ("Blog")
        verbose_name_plural = ("Blog List")
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_fields(self):
        def get_dynamic_fields(field):
            if field.name == 'category':
                return (field.name, self.category.title, field.get_internal_type())
            elif field.name == 'created_by':
                return (field.name, self.created_by.username, field.get_internal_type())
            else:
                return (field.name, field.value_from_object(self), field.get_internal_type())
        return [get_dynamic_fields(field) for field in self.__class__._meta.fields]


# # -------------------------------------------------------------------
# #                           News Comment
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
    is_approved = models.BooleanField(
        default=False, verbose_name="is approved"
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
        return str(self.comment) if len(str(self.comment)) <= 10 else str(self.comment)[:10] + " ..."

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
# #                           News CommentReply
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
    is_approved = models.BooleanField(
        default=False, verbose_name="is approved"
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
        return str(self.reply) if len(str(self.reply)) <= 10 else str(self.reply)[:10] + " ..."

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
# #                           Blog Comment
# # -------------------------------------------------------------------

class BlogComment(models.Model):
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name='blog_comments', verbose_name='blog'
    )
    commented_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_blog_comments', verbose_name='commented by'
    )
    comment = models.TextField(
        blank=True, null=True, verbose_name='comment'
    )
    is_approved = models.BooleanField(
        default=False, verbose_name="is approved"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='created at'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='updated at'
    )

    class Meta:
        verbose_name = 'Blog Comment'
        verbose_name_plural = 'Blog Comments'
        ordering = ['-updated_at']

    def __str__(self):
        return str(self.comment) if len(str(self.comment)) <= 10 else str(self.comment)[:10] + " ..."

    def get_fields(self):
        def get_dynamic_fields(field):
            if field.name == 'blog':
                return (field.name, self.blog.title)
            elif field.name == 'commented_by':
                return (field.name, self.commented_by.username, field.get_internal_type())
            else:
                return (field.name, field.value_from_object(self), field.get_internal_type())
        return [get_dynamic_fields(field) for field in self.__class__._meta.fields]


# # -------------------------------------------------------------------
# #                           Blog CommentReply
# # -------------------------------------------------------------------

class BlogCommentReply(models.Model):
    blog_comment = models.ForeignKey(
        BlogComment, on_delete=models.CASCADE, related_name='blog_comment_replays', verbose_name='blog comment'
    )
    replied_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_blog_comment_replays', verbose_name='replied by'
    )
    reply = models.TextField(
        blank=True, null=True, verbose_name='reply'
    )
    is_approved = models.BooleanField(
        default=False, verbose_name="is approved"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='created at'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='updated at'
    )

    class Meta:
        verbose_name = 'Blog Comment Reply'
        verbose_name_plural = 'Blog Comment Replies'
        ordering = ['-updated_at']

    def __str__(self):
        return str(self.reply) if len(str(self.reply)) <= 10 else str(self.reply)[:10] + " ..."

    def get_fields(self):
        def get_dynamic_fields(field):
            if field.name == 'blog':
                return (field.name, self.blog.title, field.get_internal_type())
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
    url = models.URLField(
        blank=True, null=True, verbose_name="url"
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
    slug = models.SlugField(
        unique=True, verbose_name='slug'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='created at'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='updated at'
    )

    def get_job_count(self):
        return len(Job.objects.filter(
            job_position__id=self.id
        ))

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
    # description = models.TextField(
    #     blank=True, null=True, verbose_name="description"
    # )
    description = RichTextUploadingField(blank=True, null=True)
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
    slug = models.SlugField(
        unique=True, verbose_name='slug'
    )
    job = models.ForeignKey(
        Job, blank=True, null=True, on_delete=models.CASCADE, related_name="career_job", verbose_name="job"
    )
    file = models.FileField(
        verbose_name="file"
    )
    contact = models.CharField(
        max_length=50, verbose_name="contact number"
    )
    subject = models.CharField(
        max_length=250, verbose_name="subject"
    )
    university_name = models.CharField(
        max_length=100, verbose_name="university name"
    )
    passing_year = models.CharField(
        max_length=50, verbose_name="passing year"
    )
    expected_salary = models.CharField(
        max_length=250, verbose_name="expected salary"
    )
    year_of_experience = models.CharField(
        max_length=50, verbose_name="year of experience"
    )
    status = models.CharField(
        max_length=50, choices=Status.choices, default="Pending", verbose_name="status"
    )
    remarks = models.TextField(
        blank=True, null=True, verbose_name="remarks"
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
                if not self.job == None:
                    return (field.name, self.job.job_position.title, field.get_internal_type())
                else:
                    return (field.name, "-", field.get_internal_type())
            else:
                return (field.name, field.value_from_object(self), field.get_internal_type())
        return [get_dynamic_fields(field) for field in self.__class__._meta.fields]


# # -------------------------------------------------------------------
# #                           Image Group
# # -------------------------------------------------------------------

class ImageGroup(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="title"
    )
    slug = models.SlugField(
        unique=True, verbose_name='slug'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='created at'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='updated at'
    )

    class Meta:
        verbose_name = ("Image Group")
        verbose_name_plural = ("Image Groups")
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_fields(self):
        return [get_dynamic_fields(field, self) for field in self.__class__._meta.fields]


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
    image_group = models.ForeignKey(
        ImageGroup, on_delete=models.CASCADE, related_name="gallery_image_groups", verbose_name="image group", blank=True, null=True
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
        def get_dynamic_fields(field):
            if field.name == 'image_group':
                if not self.image_group == None:
                    return (field.name, self.image_group.title, field.get_internal_type())
                else:
                    return (field.name, "-", field.get_internal_type())
            else:
                return (field.name, field.value_from_object(self), field.get_internal_type())
        return [get_dynamic_fields(field) for field in self.__class__._meta.fields]


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


# # Project Category

def project_category_slug_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        title = slugify(instance.title.lower()[:17])
        slug_binding = title + '-' + time_str_mix_slug()
        instance.slug = slug_binding


pre_save.connect(project_category_slug_pre_save_receiver, sender=ProjectCategory)


# # NewsCategory

def news_category_slug_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        title = slugify(instance.title.lower()[:17])
        slug_binding = title + '-' + time_str_mix_slug()
        instance.slug = slug_binding


pre_save.connect(news_category_slug_pre_save_receiver, sender=NewsCategory)

# # News

def news_slug_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        title = slugify(instance.title.lower()[:17])
        slug_binding = title + '-' + time_str_mix_slug()
        instance.slug = slug_binding
        # save created by
        try:
            request = RequestMiddleware(get_response=None)
            request = request.thread_local.current_request
            instance.created_by = request.user
        except Exception as E:
            raise (
                f"Failed to save user instance! [{str(E)}]"
            )


pre_save.connect(news_slug_pre_save_receiver, sender=News)


# # BlogCategory

def blog_category_slug_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        title = slugify(instance.title.lower()[:17])
        slug_binding = title + '-' + time_str_mix_slug()
        instance.slug = slug_binding


pre_save.connect(blog_category_slug_pre_save_receiver, sender=BlogCategory)

# # Blog

def blog_slug_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        title = slugify(instance.title.lower()[:17])
        slug_binding = title + '-' + time_str_mix_slug()
        instance.slug = slug_binding
        # save created by
        try:
            request = RequestMiddleware(get_response=None)
            request = request.thread_local.current_request
            instance.created_by = request.user
        except Exception as E:
            raise (
                f"Failed to save user instance! [{str(E)}]"
            )


pre_save.connect(blog_slug_pre_save_receiver, sender=Blog)

# # Client

def client_slug_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        title = slugify(instance.name.lower()[:17])
        slug_binding = title + '-' + time_str_mix_slug()
        instance.slug = slug_binding


pre_save.connect(client_slug_pre_save_receiver, sender=Client)

# # ImageGroup

def image_group_slug_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        title = slugify(instance.title.lower()[:17])
        slug_binding = title + '-' + time_str_mix_slug()
        instance.slug = slug_binding


pre_save.connect(image_group_slug_pre_save_receiver, sender=ImageGroup)

# # Gallery

def gallery_slug_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        title = slugify(instance.title.lower()[:17])
        slug_binding = title + '-' + time_str_mix_slug()
        instance.slug = slug_binding


pre_save.connect(gallery_slug_pre_save_receiver, sender=Gallery)

# # JobPosition

def job_position_slug_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        title = slugify(instance.title.lower()[:17])
        slug_binding = title + '-' + time_str_mix_slug()
        instance.slug = slug_binding


pre_save.connect(job_position_slug_pre_save_receiver, sender=JobPosition)

# # Job

def job_slug_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        title = slugify(instance.job_position.title.lower()[:17])
        slug_binding = title + '-' + time_str_mix_slug()
        instance.slug = slug_binding


pre_save.connect(job_slug_pre_save_receiver, sender=Job)

# # Career

def career_slug_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        if not instance.job == None:
            title = slugify(instance.job.job_position.title.lower()[:17])
            slug_binding = title + '-' + time_str_mix_slug()
            instance.slug = slug_binding
        else:
            request = RequestMiddleware(get_response=None)
            request = request.thread_local.current_request
            title = slugify(request.user.username.lower()[:17])
            slug_binding = title + '-' + time_str_mix_slug()
            instance.slug = slug_binding


pre_save.connect(career_slug_pre_save_receiver, sender=Career)


