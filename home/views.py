from django.shortcuts import render


def home(request):
    packages = [
	{'name':'AuditBWC', 'url': 'http://pypi.python.org/pypi/AuditBWC/0.1.1'},
	{'name':'BlazeForm', 'url': 'http://pypi.python.org/pypi/BlazeForm/0.4.1'},
	{'name':'BlazeUtils', 'url': 'http://pypi.python.org/pypi/BlazeUtils/0.5.3'},
	{'name':'BlazeWeb', 'url': 'http://pypi.python.org/pypi/BlazeWeb/0.5.2'},
	{'name':'blaze', 'url': 'http://pypi.python.org/pypi/blaze/0.10.1'},
	{'name':'django-allauth', 'url': 'https://pypi.org/project/django-allauth/0.38.0/'},
	{'name':'django-bootstrap4', 'url': 'https://pypi.org/project/django-bootstrap4/0.0.7/'},
	{'name':'djangorestframework', 'url': 'https://pypi.org/project/djangorestframework/3.9.0/'},
    ]
    context = {
        'packages': packages
    }
    return render(request, 'home/index.html', context)
