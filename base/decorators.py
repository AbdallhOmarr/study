from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

def requires_permission(permission_codename):
    def decorator(view_func):
        @login_required
        def wrapped_view(request, *args, **kwargs):
            if not request.user.has_perm(permission_codename):
                raise PermissionDenied('You do not have permission to access this view.')
            return view_func(request, *args, **kwargs)
        return wrapped_view
    return decorator
