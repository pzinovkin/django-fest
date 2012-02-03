# -*- coding: utf-8 -*-
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'app/index.xml'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        return context


index = IndexView.as_view()
