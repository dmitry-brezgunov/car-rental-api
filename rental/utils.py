from django.core.mail import send_mail


def rent_car_email(request, instance):
    text = ''
    cars = instance.cleaned_data['cars']
    for i, car in enumerate(cars):
        if i == len(cars) - 1:
            text += f'{car}'
        else:
            text += f'{car}, '

    send_mail(
        'Машины арендованны',
        f'{request.user.username}, вы взяли в аренду машины: {text}!',
        'rent-car.ru <admin@rent-car.ru>', [request.user.email],
        fail_silently=False)
