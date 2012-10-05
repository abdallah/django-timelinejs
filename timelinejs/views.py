from django.http import HttpResponse
from django.utils import simplejson as json 
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin
from timelinejs.models import Timeline

class JSONResponseMixin(object):
    response_class = HttpResponse
    
    def render_to_response(self, context):
        return self.get_json_response(self.convert_context_to_json(context))
    
    def get_json_response(self, content, **httpresponse_kwargs):  
        "Construct an `HttpResponse` object."  
        return HttpResponse(content,  
                                 content_type='application/json',  
                                 **httpresponse_kwargs)  

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        tl = context['timeline']
        return json.dumps(tl.to_dict()) 

class TimelineView(SingleObjectMixin, ListView, JSONResponseMixin):
    template_name = "timelineview.html"
    
    def get_context_data(self, **kwargs):
        kwargs['timeline'] = self.object
        kwargs['options'] = self.options
        return super(TimelineView, self).get_context_data(**kwargs)
    
    def get_queryset(self):
        self.object = self.get_object(Timeline.objects.all())
        self.options = self.object.timelineoptions
        return self.object.timelineevent_set.all()
    
    def render_to_response(self, context):
        if self.request.GET.get('format', 'html') != 'json':
            return ListView.render_to_response(self, context)
        else: 
            return JSONResponseMixin.render_to_response(self, context)
timeline_view = TimelineView.as_view()