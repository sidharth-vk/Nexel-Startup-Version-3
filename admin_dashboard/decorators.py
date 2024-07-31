from django.contrib.auth.decorators import user_passes_test

def superuser_required(view_func):
    decorated_view_func = user_passes_test(
        lambda u: u.is_superuser,
        login_url='/auth/login',
        redirect_field_name=None
    )(view_func)
    return decorated_view_func
