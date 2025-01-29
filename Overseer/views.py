from django.shortcuts import render , redirect 
from django.http import HttpResponse
from .models import Board , Lists
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView , DetailView,CreateView
# Create your views here.
def home(request , boards):
    return render(request , 'Overseer/home.html')


@login_required
def create_board(request):
    if request.method == 'POST':
        # Since @login_required ensures the user is authenticated, this check is redundant
        author = request.user  # Get the logged-in user
        name = request.POST['name']
        description = request.POST['description']

        # Pass the author when creating the Board instance
        board = Board(name=name, description=description, author=author)
        board.save()
        messages.success(request, "Board created successfully!")
        return redirect('home' , {'boards':board})
     

    return render(request, 'Overseer/create_board.html')

class BoardListView(ListView):
    model = Board
    context_object_name = 'boards'
    ordering = ['-created_at']


class BoardDetailView(DetailView):
    model = Board
    context_object_name = 'board'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lists'] = Lists.objects.filter(board=self.object)
        return context
    
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Lists, Board

class ListCreationView(CreateView):
    model = Lists
    fields = ['name', 'description']  # Fields to display in the form 
    context_object_name = 'lists'

    def form_valid(self, form):
        # Get the board associated with the list from the URL
        board_id = self.kwargs['pk']
        board = get_object_or_404(Board, id=board_id)
        
        # Associate the list with the retrieved board
        form.instance.board = board
        
        # Optionally set the author if lists have an author field
        form.instance.author = self.request.user
        
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect to the detail view of the board after creating the list
        return reverse_lazy('board_detail', kwargs={'pk': self.kwargs['pk']})




