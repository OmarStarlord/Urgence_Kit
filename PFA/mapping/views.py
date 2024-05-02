from django.shortcuts import render
from django.shortcuts import redirect



def mapping_view(request):
    user_id = request.session.get('user_id')
    if not user_id:
        # Handle case where user_id is not in session
        return redirect('users:login')
    else:
        return render(request, 'mapping.html')