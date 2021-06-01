from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "index.html"

class AboutView(TemplateView):
    template_name = 'page/about.html'

class CivilProjectView(TemplateView):
    template_name = 'page/civil-project.html'

class TelecomProjectView(TemplateView):
    template_name = 'page/telecom-project.html'

class CivilServicesView(TemplateView):
    template_name = 'page/civil-service.html'

class TelecomServicesView(TemplateView):
    template_name = 'page/telecom-service.html'

class CareerView(TemplateView):
    template_name = 'page/career.html'

class ClientView(TemplateView):
    template_name = 'page/client.html'

class NewsView(TemplateView):
    template_name = 'page/news.html'

class ContactView(TemplateView):
    template_name = 'page/contact.html'

class NewsDetailsView(TemplateView):
    template_name = 'page/news-details.html'
