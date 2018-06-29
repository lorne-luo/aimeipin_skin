# coding=utf-8
import logging
from django.template.context_processors import csrf
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import Http404, HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from django.contrib import messages
from django.views.generic import TemplateView, FormView
from braces.views import PermissionRequiredMixin

from django.contrib.auth.views import password_change
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from core.django.views import CommonPageViewMixin
from .forms import UserProfileForm, RegisterForm, LoginForm
from . models import AuthUser


class ChangePasswordView(CommonPageViewMixin, TemplateView):
    def post(self, request, **kwargs):
        self.request = request
        context = super(ChangePasswordView, self).get_context_data(**kwargs)
        return self.render_to_response(context)

    def render_to_response(self, context, **response_kwargs):
        context['page_title'] = u'修改密码'
        template_response = password_change(
            self.request,
            template_name='adminlte/change-password.html',
            extra_context=context
        )
        return template_response


class ChangePasswordDoneView(CommonPageViewMixin, TemplateView):
    template_name = 'adminlte/change-password-done.html'


@sensitive_post_parameters()
@csrf_exempt
@ensure_csrf_cookie
@never_cache
def member_login(request):
    if request.method == 'GET':
        c = csrf(request)
        if request.GET.get('next'):
            c.update({'next': request.GET['next']})
        c.update({'form': LoginForm()})
        return render_to_response('adminlte/login.html', c)
    elif request.method == 'POST':
        old_user = request.user or None
        form = LoginForm(request.POST)
        if not form.is_valid():
            form.data = {'mobile': form.data.get('mobile')}
            return render_to_response('adminlte/login.html', {'form': form})

        mobile = form.cleaned_data.get('mobile')
        password = form.cleaned_data.get('password')
        user = authenticate(username=mobile, password=password)
        if user:
            login(request, user)
            next_page = request.POST.get('next', None)
            # If the user was already logged-in before we ignore the ?next
            # parameter, this avoids a loop of login prompts when the user does
            # not have the permission to see the page in ?next
            if old_user == user or not next_page:
                # Redirect chefs to meals page
                next_page = reverse('survey:answer-list')

            return HttpResponseRedirect(next_page)
        else:
            form.add_error(None, u'密码错误，请重试')
            form.data = {'mobile': mobile}
            return render_to_response('adminlte/login.html', {'form': form})


def member_home(request):
    return HttpResponse('123')


def member_logout(request):
    logout(request)
    return redirect('users:login')


class ProfileView(PermissionRequiredMixin, FormView):
    form_class = UserProfileForm
    template_name = 'auth_user/profile.html'
    permission_required = 'auth_user.change_auth_user'
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk', '')
        if pk and self.request.user.is_superuser:  # Admin editing other user's profile
            try:
                return AuthUser.objects.get(auth_user_id=pk)
            except AuthUser.DoesNotExist:
                raise Http404()
        elif self.request.user:  # Editing own profile
            return self.request.user
        else:
            raise Http404()

    def get_initial(self):
        return {'email': self.request.user.email, 'mobile': self.request.user.mobile}

    def get_form_kwargs(self):
        kwargs = super(ProfileView, self).get_form_kwargs()
        self.object = self.get_object()
        kwargs.update({'instance': self.object})
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context.update({'object': self.object})
        return context

    def form_valid(self, form):
        self.object = form.save()
        self.request.user.email = form.cleaned_data.get('email')
        self.request.user.mobile = form.cleaned_data.get('mobile')

        password = form.cleaned_data.get('password')
        if password:
            self.request.user.set_password(password)
        self.request.user.save()
        messages.success(self.request, u'个人资料已更新')
        return super(ProfileView, self).form_valid(form)


class RegisterView(FormView):
    template_name = 'adminlte/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('users:login')

    def get(self, request, *args, **kwargs):
        form = self.get_form()
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        mobile = form.cleaned_data.get('mobile')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        #todo create authuser
        AuthUser.objects.create(mobile, email, password, premium_account=False)
        messages.success(self.request, '注册成功, 请登陆.')

        return super(RegisterView, self).form_valid(form)
