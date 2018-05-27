from django.http import Http404, HttpResponseRedirect
from django.utils import timezone
from django.views.generic import ListView, CreateView, UpdateView
from braces.views import SuperuserRequiredMixin

from apps.survey.forms import AnswerProductFormSet
from core.django.utils.ip import get_client_ip
from core.django.views import CommonContextMixin
from .models import Answer, InviteCode
from . import forms


class AnswerListView(SuperuserRequiredMixin, CommonContextMixin, ListView):
    """ List views for Answer """
    model = Answer
    template_name_suffix = '_list'  # answer/answer_list.html

    def get_context_data(self, **kwargs):
        context = super(AnswerListView, self).get_context_data(**kwargs)
        context['table_titles'] = [u'姓名', u'性别', u'年龄', u'职业', u'城市', u'微信号', u'手机', '可否修改', '修改连接', '']
        context['table_fields'] = ['name', 'sex', 'birth', 'job', 'city', 'weixin_id', 'mobile',
                                   'is_changeable_display', 'survey_url', 'id']
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


class SurveyFillView(CommonContextMixin, UpdateView):
    model = Answer
    form_class = forms.SurveyFillForm
    template_name = 'survey/pc/index.html'
    code = None  # InviteCode
    uuid = None  # InviteCode

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
        if not self.object:
            initial.update({
                'uuid': self.uuid,
                'name': self.code.name,
            })
        return initial

    def get_context_data(self, **kwargs):
        context = super(SurveyFillView, self).get_context_data(**kwargs)
        if self.request.method == "GET":
            if self.object:
                initial1 = [{'id': cosmetic.id, 'product': cosmetic.product_id, 'name': cosmetic.name}
                            for cosmetic in self.object.cosmetic_products1.all()]
                initial2 = [{'id': cosmetic.id, 'product': cosmetic.product_id, 'name': cosmetic.name}
                            for cosmetic in self.object.cosmetic_products2.all()]
                initial3 = [{'id': cosmetic.id, 'product': cosmetic.product_id, 'name': cosmetic.name}
                            for cosmetic in self.object.cosmetic_products3.all()]
                initial4 = [{'id': cosmetic.id, 'product': cosmetic.product_id, 'name': cosmetic.name}
                            for cosmetic in self.object.cosmetic_products4.all()]
                initial5 = [{'id': cosmetic.id, 'product': cosmetic.product_id, 'name': cosmetic.name}
                            for cosmetic in self.object.cosmetic_products5.all()]
                initial6 = [{'id': cosmetic.id, 'product': cosmetic.product_id, 'name': cosmetic.name}
                            for cosmetic in self.object.cosmetic_products6.all()]
                initial7 = [{'id': cosmetic.id, 'product': cosmetic.product_id, 'name': cosmetic.name}
                            for cosmetic in self.object.cosmetic_products7.all()]
                initial8 = [{'id': cosmetic.id, 'product': cosmetic.product_id, 'name': cosmetic.name}
                            for cosmetic in self.object.cosmetic_products8.all()]
                cosmetic_products1_formset = AnswerProductFormSet(prefix='cosmetic_products1_formset', initial=initial1)
                cosmetic_products2_formset = AnswerProductFormSet(prefix='cosmetic_products2_formset', initial=initial2)
                cosmetic_products3_formset = AnswerProductFormSet(prefix='cosmetic_products3_formset', initial=initial3)
                cosmetic_products4_formset = AnswerProductFormSet(prefix='cosmetic_products4_formset', initial=initial4)
                cosmetic_products5_formset = AnswerProductFormSet(prefix='cosmetic_products5_formset', initial=initial5)
                cosmetic_products6_formset = AnswerProductFormSet(prefix='cosmetic_products6_formset', initial=initial6)
                cosmetic_products7_formset = AnswerProductFormSet(prefix='cosmetic_products7_formset', initial=initial7)
                cosmetic_products8_formset = AnswerProductFormSet(prefix='cosmetic_products8_formset', initial=initial8)

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

    def process_formsets(self):
        self.process_formset(self.object.cosmetic_products1, 'cosmetic_products1_formset')
        self.process_formset(self.object.cosmetic_products2, 'cosmetic_products2_formset')
        self.process_formset(self.object.cosmetic_products3, 'cosmetic_products3_formset')
        self.process_formset(self.object.cosmetic_products4, 'cosmetic_products4_formset')
        self.process_formset(self.object.cosmetic_products5, 'cosmetic_products5_formset')
        self.process_formset(self.object.cosmetic_products6, 'cosmetic_products6_formset')
        self.process_formset(self.object.cosmetic_products7, 'cosmetic_products7_formset')
        self.process_formset(self.object.cosmetic_products8, 'cosmetic_products8_formset')

    def process_formset(self, product_set, prefix):
        cosmetic_products1_formset = AnswerProductFormSet(data=self.request.POST, prefix=prefix)
        ids = []
        for p in cosmetic_products1_formset:
            if p.is_valid():
                p.save()
                product_set.add(p)
                ids.append(p.id)
        deletes = product_set.all().exclude(id__in=ids)
        deletes.delete()

    def form_valid(self, form):
        if self.object and self.object.id:
            # update existed
            self.process_formsets()
            self.object = form.save()
            if not self.object.ip:
                self.object.ip = get_client_ip(self.request)
                self.object.update_location()
            return HttpResponseRedirect(self.get_success_url())
        else:
            # create new
            self.object = form.save()
            self.process_formsets()
            self.object.ip = get_client_ip(self.request)
            self.object.save()
            return HttpResponseRedirect(self.get_success_url())

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
    template_name = 'adminlte/common_detail.html'
