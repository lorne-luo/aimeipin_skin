from io import BytesIO

from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import TemplateView
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from xhtml2pdf import pisa
from xhtml2pdf.default import DEFAULT_FONT

from config import settings

pdfmetrics.registerFont(TTFont('yh', '%s/static/fonts/STSong.ttf' % settings.BASE_DIR))


class PdfGenerateBaseView(TemplateView):
    """convert templateview into pdf and serve as downloading"""
    template_name = None

    def render_to_pdf(self, template_src, context_dict=None, direct_download=None):
        if context_dict is None:
            context_dict = {}

        template = get_template(template_src)
        html = template.render(context_dict)
        result = BytesIO()
        DEFAULT_FONT['helvetica'] = 'yh'

        pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result)
        if not pdf.err:
            if direct_download:
                return result.getvalue()
            return HttpResponse(result.getvalue(), content_type='application/pdf')
        return None

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        pdf = self.render_to_pdf(self.get_template_names(), context)
        return HttpResponse(pdf, content_type='application/pdf')
