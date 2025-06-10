# Django's Messages Framework
Django's messages framework lets you store messages in one request and retrieve them for display in a subsequent request (typically the next page). These are one-time messages, often used to give feedback to users.

### Example:-
User updates it's profile so a message pops up- “Your profile was updated successfully.”
That message didn’t live in the URL or the session manually—it was handled by the messages framework.

## Setup in settings.py-

To use messages framework, updates settings.py with following:-

     INSTALLED_APPS = [
        ...
        'django.contrib.messages',
     ]

     MIDDLEWARE = [
        ...
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
     ]

     TEMPLATES = [
     {
            ...
            'OPTIONS': {
                'context_processors': [
                    ...
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
     ]

## Using messages in Views:-

Using success message in views,

    from django.contrib import messages

    def update_profile(request):
        if request.method == 'POST':
            # suppose form is valid
            messages.success(request, "Your profile was updated successfully!")
            return redirect('dashboard')

## Types of message types:-

1. messages.debug(request, 'This is a debug message.')
2. messages.info(request, 'Just FYI...')
3. messages.success(request, 'Action was successful!')
4. messages.warning(request, 'Be careful!')
5. messages.error(request, 'Something went wrong.')