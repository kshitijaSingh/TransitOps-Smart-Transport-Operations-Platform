from functools import wraps

from django.contrib.auth.decorators import user_passes_test


def role_required(*allowed_roles):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated and any(
                request.user.groups.filter(name=role).exists() for role in allowed_roles
            ):
                return view_func(request, *args, **kwargs)
            return user_passes_test(lambda u: u.is_authenticated)(view_func)(request, *args, **kwargs)

        return _wrapped_view

    return decorator
