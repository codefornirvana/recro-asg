from social_core.pipeline.partial import partial
from django.shortcuts import redirect



from .models import CustomUser

def associate_by_phone_number(strategy, backend, request, details, *args, **kwargs):
    phone_number = strategy.session_get('phone_number', None)
    users = CustomUser.objects.filter(phonenumber=phone_number)
    if len(users) > 0:
        user = users[0]

        print('------ showing the backend ------ ')
        print(backend.name)
        user.meta[backend.name] = details
        user.save()
        kwargs['user'] = user
        print('--------------------------------------')
    return kwargs

@partial
def get_phonenumber_details_from_user(strategy, backend, request, details, *args, **kwargs):
    print(' ------- this is the breaking pipeline ------- ')
    print(request)
    print(" =============================================== ")
    phone_number = strategy.session_get('phone_number', None)
    password = strategy.session_get('password', None)
    if not phone_number:
        return redirect("/complete_signup/{}/".format(backend.name))

    print('---- received the phone number from user ----- ')
    print(phone_number)
    return

def create_social_user(strategy, details, **kwargs):

    USER_FIELDS = ['phonenumber', 'password']
    print(' --- came to the custom create user flow . Showing the details receivved ----- ')
    print(details)
    print(kwargs)
    print('------------------------------------------------------------------------------ ')



    # fields = dict((name, kwargs.get(name, details.get(name)))
    #               for name in backend.setting('USER_FIELDS', USER_FIELDS))
    #
    fields = {
        'phonenumber': strategy.session_get('phone_number', None),
        'password': strategy.session_get('password', None),
        'name':  kwargs.get('fullname', details.get('fullname')),
        #'email': kwargs.get('fullname', details.get('email')),
        'meta': {}
    }
    if kwargs.get('user'):
        print(' OH ! SHIT THE USER IS PRESENT !!!! ')
        print(' ----showing the backend name ----- ')
        print(kwargs.get('backend').name)
        return {'is_new': False}
    print(' ------ showing the fields ---- ')
    print(fields)
    if not fields:
        return

    return {
        'is_new': True,
        'user': strategy.create_user(**fields)
    }

