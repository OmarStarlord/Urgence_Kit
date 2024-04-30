from django.shortcuts import render



def mapping_view(request):
    user_id = request.session.get('user_id')
    if not user_id:
        # Handle case where user_id is not in session
        return JsonResponse({'error': 'User ID not found in session'}, status=400)
    else:
        return render(request, 'mapping.html')