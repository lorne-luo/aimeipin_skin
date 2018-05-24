from django.http import Http404
from django.utils import timezone
from django.views.generic import ListView, CreateView, UpdateView
from braces.views import SuperuserRequiredMixin

from apps.survey.forms import AnswerProductFormSet
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


class SurveyFillView(CommonContextMixin, UpdateView):
    model = Answer
    form_class = forms.SurveyFillForm
    template_name = 'survey/pc/index.html'
    slug_url_kwarg = 'code'
    code = None  # InviteCode

    def get_object(self, queryset=None):
        uuid = self.request.GET.get(self.slug_url_kwarg)
        self.code = InviteCode.objects.filter(code=uuid, expiry_at__gt=timezone.now()).first()
        if not self.code:
            raise Http404
        if queryset is None:
            queryset = self.get_queryset()

        return queryset.filter(code=self.code).first()

    def get_initial(self):
        initial = super(SurveyFillView, self).get_initial()
        initial.update({'code': self.code})
        return initial

    def get_context_data(self, **kwargs):
        context = super(SurveyFillView, self).get_context_data(**kwargs)
        if self.request.method == "GET":
            if self.object:
                cosmetic_products1_formset = AnswerProductFormSet(queryset=self.object.cosmetic_products1.all(),
                                                                  prefix='cosmetic_products1_formset')
                cosmetic_products2_formset = AnswerProductFormSet(queryset=self.object.cosmetic_products2.all(),
                                                                  prefix='cosmetic_products2_formset')
                cosmetic_products3_formset = AnswerProductFormSet(queryset=self.object.cosmetic_products3.all(),
                                                                  prefix='cosmetic_products3_formset')
                cosmetic_products4_formset = AnswerProductFormSet(queryset=self.object.cosmetic_products4.all(),
                                                                  prefix='cosmetic_products4_formset')
                cosmetic_products5_formset = AnswerProductFormSet(queryset=self.object.cosmetic_products5.all(),
                                                                  prefix='cosmetic_products5_formset')
                cosmetic_products6_formset = AnswerProductFormSet(queryset=self.object.cosmetic_products6.all(),
                                                                  prefix='cosmetic_products6_formset')
                cosmetic_products7_formset = AnswerProductFormSet(queryset=self.object.cosmetic_products7.all(),
                                                                  prefix='cosmetic_products7_formset')
                cosmetic_products8_formset = AnswerProductFormSet(queryset=self.object.cosmetic_products8.all(),
                                                                  prefix='cosmetic_products8_formset')
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
        return context

    def form_valid(self, form):
        cosmetic_products1_formset = AnswerProductFormSet(data=self.request.POST, prefix='cosmetic_products1_formset')
        ids = []
        for p in cosmetic_products1_formset:
            if p.is_valid():
                p.save()
                self.object.cosmetic_products1.add(p)
                ids.append(p.id)
        deletes = self.object.cosmetic_products1.all().exclude(id__in=ids)
        self.object.cosmetic_products1.remove(deletes)
        deletes.delete()

        super(SurveyFillView, self).form_valid(form)

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
