from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView
from .models import Blog, Comment
from project_slider_blog.models import BlogSlider
from .forms import CommentCreateForm



# Create your views here.


class BlogListView(ListView):
    template_name = 'blog.html'
    paginate_by = 2

    def get_queryset(self):
        return Blog.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slider'] = BlogSlider.objects.all()
        return context


class BlogDetailView(View):
    form_class = CommentCreateForm

    def setup(self, request, *args, **kwargs):
        self.detail_blog_instance = Blog.objects.get(id=kwargs['id'], slug=kwargs['slug'])
        return super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        # detail_blog = Blog.objects.get(id=id, slug=slug)
        comments = self.detail_blog_instance.pcomments.all()
        slider = BlogSlider.objects.all()
        context = {
            'detail_blog': self.detail_blog_instance,
            'slider': slider,
            'comments': comments,
            'form': self.form_class}
        return render(request, 'blog_detail.html', context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = self.detail_blog_instance
            new_comment.save()
            messages.success(request, 'دیدگاه شما با موفقیت ثبت شد', 'success')
            return redirect('/')








