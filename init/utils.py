from django.core.mail import send_mail


def send_email_with_form_data(data):

    # email_to = 'info@adfits.com'
    email_from = 'smooker14@gmail.com'
    email_to = 'smooker14@gmail.com'
    subject = 'demo_subject'
    message = 'First name: {} Last name:{} Email:{} Phone:{} Web:{}'.format(
        data.get('first_name', default=None),
        data.get('last_name', default=None),
        data.get('email', default=None),
        data.get('phone', default=None),
        data.get('url', default=None),
    )

    #send_mail(subject, message, email_from, [email_to], fail_silently=False)
