from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login
from django.utils import timezone
from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from braces.views import SuperuserRequiredMixin
from django.views.generic.edit import BaseUpdateView

from apps.survey.forms import AnswerProductFormSet
from core.auth_user.models import AuthUser
from core.django.utils.ip import get_client_ip
from core.django.views import CommonContextMixin
from .models import Answer, InviteCode, AnswerProduct
from . import forms


class AnswerListView(SuperuserRequiredMixin, CommonContextMixin, ListView):
    """ List views for Answer """
    model = Answer
    template_name_suffix = '_list'  # answer/answer_list.html

    def get_context_data(self, **kwargs):
        context = super(AnswerListView, self).get_context_data(**kwargs)
        context['table_titles'] = ['目标', '姓名', u'性别', u'年龄', u'城市', u'微信号', u'手机', '可否修改', '问卷链接', '最后修改', '查看报告', '']
        context['table_fields'] = ['name', 'purpose', 'sex', 'age', 'city', 'weixin_id', 'mobile',
                                   'is_changeable_display', 'survey_url', 'modified_at', 'uuid', 'id']
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
    template_name = 'survey/answer_detail.html'

    def get_context_data(self, **kwargs):
        context = super(AnswerDetailView, self).get_context_data(**kwargs)
        fields = ['name', 'sex', 'portrait', 'portrait_part', 'cosmetics', 'birth', 'height', 'weight', 'job',
                  'monthly_income', 'weixin_id', 'mobile', 'question1', 'question2', 'question3', 'question4',
                  'question5', 'question6', 'question7', 'question8', 'question9', 'question10', 'question11',
                  'question12', 'question13', 'question14', 'question15', 'question16', 'question17', 'question18',
                  'question19', 'question20', 'question21', 'question22', 'question23', 'question24', 'question25',
                  'question26', 'question27', 'question28', 'question29', 'question30', 'question31', 'question32',
                  'question33', 'question34', 'question35', 'question36', 'question37', 'question38',
                  'non_score_question1', 'non_score_question2', 'non_score_question3', 'non_score_question4',
                  'non_score_question5', 'non_score_question6', 'non_score_question7', 'non_score_question8',
                  'non_score_question9', 'non_score_question10', 'non_score_question11', 'non_score_question12',
                  'non_score_question13', 'non_score_question14', 'non_score_question15', 'cosmetic_products1',
                  'cosmetic_products2', 'cosmetic_products3', 'cosmetic_products4', 'cosmetic_products5',
                  'cosmetic_products6', 'cosmetic_products7', 'cosmetic_products8', 'other_question1',
                  'other_question2']
        cosmetics_title = {'cosmetic_products1': '51. 日间-洁面', 'cosmetic_products2': '52. 日间-化妆水', 'cosmetic_products3': '53. 日间-精华',
                           'cosmetic_products4': '54. 日间-乳液或面霜', 'cosmetic_products5': '55.日间-防晒', 'cosmetic_products6': '56. 夜间-卸妆',
                           'cosmetic_products7': '57. 夜间-洁面', 'cosmetic_products8': '58. 夜间-化妆水'}
        context.update({
            'fields': fields,
            'cosmetics_title': cosmetics_title
        })
        return context


class SurveyFillView(CommonContextMixin, UpdateView):
    model = Answer
    form_class = forms.SurveyFillForm
    template_name = 'survey/answer/index.html'
    code = None  # InviteCode
    uuid = None  # InviteCode
    purpose = None
    level = None

    def get_object(self, queryset=None):
        uuid = self.kwargs.get('uuid') or self.request.GET.get('code')
        self.uuid = uuid
        if queryset is None:
            queryset = self.get_queryset()
        answer = queryset.filter(uuid=uuid).first() or queryset.filter(code__uuid=uuid).first()

        if answer:
            # existed,return directly
            return answer
        else:
            # new, check invite code
            self.code = InviteCode.objects.filter(uuid=uuid, expiry_at__gt=timezone.now()).first()
            if not self.code or self.code.is_used:
                # invitecode not existed,
                raise Http404
            # else:
            #     Answer.objects.filter()
            return None

    def get_initial(self):
        initial = super(SurveyFillView, self).get_initial()
        if self.object and self.object.id and self.object.purpose:
            self.purpose = self.object.purpose
        elif self.code and self.code.purpose:
            self.purpose = self.code.purpose
            self.level = self.code.level

        if not self.object:
            initial.update({
                'uuid': self.uuid,
                'name': self.code.name,
            })
        initial.update({
            'purpose': self.purpose,
            'level': self.level,
        })

        return initial

    def get_context_data(self, **kwargs):
        context = super(SurveyFillView, self).get_context_data(**kwargs)
        if self.request.method == "GET":
            if self.object:
                cosmetic_products1_formset = AnswerProductFormSet(prefix='cosmetic_products1_formset',
                                                                  instance=self.object,
                                                                  queryset=self.object.answerproduct_set.filter(
                                                                      category='卸妆'))
                cosmetic_products2_formset = AnswerProductFormSet(prefix='cosmetic_products2_formset',
                                                                  instance=self.object,
                                                                  queryset=self.object.answerproduct_set.filter(
                                                                      category='洁面'))
                cosmetic_products3_formset = AnswerProductFormSet(prefix='cosmetic_products3_formset',
                                                                  instance=self.object,
                                                                  queryset=self.object.answerproduct_set.filter(
                                                                      category='化妆'))
                cosmetic_products4_formset = AnswerProductFormSet(prefix='cosmetic_products4_formset',
                                                                  instance=self.object,
                                                                  queryset=self.object.answerproduct_set.filter(
                                                                      category='面霜'))
                cosmetic_products5_formset = AnswerProductFormSet(prefix='cosmetic_products5_formset',
                                                                  instance=self.object,
                                                                  queryset=self.object.answerproduct_set.filter(
                                                                      category='精华'))
                cosmetic_products6_formset = AnswerProductFormSet(prefix='cosmetic_products6_formset',
                                                                  instance=self.object,
                                                                  queryset=self.object.answerproduct_set.filter(
                                                                      category='去角质'))
                cosmetic_products7_formset = AnswerProductFormSet(prefix='cosmetic_products7_formset',
                                                                  instance=self.object,
                                                                  queryset=self.object.answerproduct_set.filter(
                                                                      category='面膜'))
                cosmetic_products8_formset = AnswerProductFormSet(prefix='cosmetic_products8_formset',
                                                                  instance=self.object,
                                                                  queryset=self.object.answerproduct_set.filter(
                                                                      category='防晒'))

            else:
                cosmetic_products1_formset = AnswerProductFormSet(prefix='cosmetic_products1_formset')
                cosmetic_products2_formset = AnswerProductFormSet(prefix='cosmetic_products2_formset')
                cosmetic_products3_formset = AnswerProductFormSet(prefix='cosmetic_products3_formset')
                cosmetic_products4_formset = AnswerProductFormSet(prefix='cosmetic_products4_formset')
                cosmetic_products5_formset = AnswerProductFormSet(prefix='cosmetic_products5_formset')
                cosmetic_products6_formset = AnswerProductFormSet(prefix='cosmetic_products6_formset')
                cosmetic_products7_formset = AnswerProductFormSet(prefix='cosmetic_products7_formset')
                cosmetic_products8_formset = AnswerProductFormSet(prefix='cosmetic_products8_formset')

            context.update({
                'cosmetic_products1_formset': cosmetic_products1_formset,
                'cosmetic_products2_formset': cosmetic_products2_formset,
                'cosmetic_products3_formset': cosmetic_products3_formset,
                'cosmetic_products4_formset': cosmetic_products4_formset,
                'cosmetic_products5_formset': cosmetic_products5_formset,
                'cosmetic_products6_formset': cosmetic_products6_formset,
                'cosmetic_products7_formset': cosmetic_products7_formset,
                'cosmetic_products8_formset': cosmetic_products8_formset,
            })

            if self.object and self.object.id and self.object.purpose:
                self.purpose = self.object.purpose
            elif self.code and self.code.purpose:
                self.purpose = self.code.purpose
            context.update({
                'purpose': self.purpose
            })
        return context

    def process_formsets(self):
        self.process_formset('cosmetic_products1_formset'),
        self.process_formset('cosmetic_products2_formset'),
        self.process_formset('cosmetic_products3_formset'),
        self.process_formset('cosmetic_products4_formset'),
        self.process_formset('cosmetic_products5_formset'),
        self.process_formset('cosmetic_products6_formset'),
        self.process_formset('cosmetic_products7_formset'),
        self.process_formset('cosmetic_products8_formset'),

    def process_formset(self, prefix):
        products_formset = AnswerProductFormSet(self.request.POST, self.request.FILES,
                                                prefix=prefix, instance=self.object)
        products_formset.instance = self.object
        if products_formset.is_valid():
            products_formset.save()
            return True
        else:
            messages.error(self.request, str(products_formset.errors))
            return False

    def form_valid(self, form):
        self.object = form.save()

        if self.object:
            update_fields = []
            if not self.object.ip or not self.object.city:
                self.object.ip = get_client_ip(self.request)
                self.object.update_location()
                update_fields += ['ip', 'city']
            if not self.object.customer and self.request.user.is_authenticated():
                if not self.request.user.is_superuser and hasattr(self.request.user, 'wxuser'):
                    self.object.customer = self.request.user.wxuser
                    update_fields.append('customer')
            if update_fields:
                self.object.save(update_fields=update_fields)

        if not all([self.process_formset('cosmetic_products1_formset'),
                    self.process_formset('cosmetic_products2_formset'),
                    self.process_formset('cosmetic_products3_formset'),
                    self.process_formset('cosmetic_products4_formset'),
                    self.process_formset('cosmetic_products5_formset'),
                    self.process_formset('cosmetic_products6_formset'),
                    self.process_formset('cosmetic_products7_formset'),
                    self.process_formset('cosmetic_products8_formset')]):
            return self.form_invalid(form)

        for r in self.object.report_set.all():
            r.regenerate()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('survey:answer-score', args=[self.uuid])
        # return reverse('survey:answer', args=[self.uuid])

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        wx_openid = self.request.session.get('wx_openid', None)
        user = AuthUser.objects.filter(username=wx_openid).first()
        if wx_openid and user:
            login(request, user)
            if self.object and not self.object.customer and hasattr(user, 'wxuser'):
                self.object.customer = user.wxuser
                self.object.save()

        if self.object and self.object.id and not self.object.is_changeable:
            # cant change, redirect to score page
            return HttpResponseRedirect(reverse('survey:answer-score', args=[self.object.uuid]))
        return BaseUpdateView.get(self, request, *args, **kwargs)


class AnswerScoreView(TemplateView):
    template_name = 'survey/answer/score.html'

    def get_object(self):
        uuid = self.kwargs.get('uuid') or self.request.GET.get('code')
        answer = Answer.objects.filter(uuid=uuid).first() or Answer.objects.filter(code__uuid=uuid).first()
        if answer:
            return answer
        raise Http404

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(**kwargs)
        context.update({'object': self.object})
        return self.render_to_response(context)


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
    template_name = 'adminlte/common_detail.html'
