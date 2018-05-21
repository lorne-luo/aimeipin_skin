from django.http import Http404
from django.utils import timezone
from django.views.generic import ListView, CreateView, UpdateView
from braces.views import SuperuserRequiredMixin
from core.django.views import CommonContextMixin
from .models import Answer, InviteCode
from . import forms


class AnswerListView(SuperuserRequiredMixin, CommonContextMixin, ListView):
    """ List views for Answer """
    model = Answer
    template_name_suffix = '_list'  # answer/answer_list.html

    def get_context_data(self, **kwargs):
        context = super(AnswerListView, self).get_context_data(**kwargs)
        context['table_titles'] = [u'姓名', u'性别', u'年龄', u'职业', u'城市', u'微信号', u'手机', '']
        context['table_fields'] = ['name', 'sex', 'birth', 'job', 'city', 'weixin_id', 'mobile', 'id']
        return context


class AnswerAddView(SuperuserRequiredMixin, CommonContextMixin, CreateView):
    """ Add views for Answer """
    model = Answer
    form_class = forms.AnswerAddForm
    template_name = 'survey/answer_form.html'


class AnswerUpdateView(SuperuserRequiredMixin, CommonContextMixin, UpdateView):
    """ Update views for Answer """
    model = Answer
    form_class = forms.AnswerUpdateForm
    template_name = 'survey/answer_form.html'


class AnswerDetailView(SuperuserRequiredMixin, CommonContextMixin, UpdateView):
    """ Detail views for Answer """
    model = Answer
    form_class = forms.AnswerDetailForm
    template_name = 'adminlte/common_detail_new.html'


class SurveyFillView(CommonContextMixin, CreateView):
    model = Answer
    form_class = forms.SurveyFillForm
    template_name = 'survey/pc/index.html'

    def get_initial(self):
        uuid = self.request.GET.get('code', None)
        code = InviteCode.objects.filter(code=uuid, expiry_at__gt=timezone.now()).first()
        if not code:
            raise Http404
        initial = super(SurveyFillView, self).get_initial()
        initial.update({'code': code})
        return initial

    def get_success_url(self):
        # todo submission success page
        return '/'


class InviteCodeListView(SuperuserRequiredMixin, CommonContextMixin, ListView):
    """ List views for InviteCode """
    model = InviteCode
    template_name_suffix = '_list'  # survey/invitecode_list.html


class InviteCodeAddView(SuperuserRequiredMixin, CommonContextMixin, CreateView):
    """ Add views for InviteCode """
    model = InviteCode
    form_class = forms.InviteCodeAddForm
    template_name = 'survey/invitecode_add.html'


class InviteCodeUpdateView(SuperuserRequiredMixin, CommonContextMixin, UpdateView):
    """ Update views for InviteCode """
    model = InviteCode
    form_class = forms.InviteCodeUpdateForm
    template_name = 'adminlte/common_form.html'


class InviteCodeDetailView(SuperuserRequiredMixin, CommonContextMixin, UpdateView):
    """ Detail views for InviteCode """
    model = InviteCode
    form_class = forms.InviteCodeDetailForm
    template_name = 'adminlte/common_detail_new.html'
