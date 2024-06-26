from django.shortcuts import redirect

def employee_required(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if request.user.is_authenticated and hasattr(request.user, 'employee'):
            return view_func(request, *args, **kwargs)
        else:
            return redirect('dashboard')
    return _wrapped_view_func
