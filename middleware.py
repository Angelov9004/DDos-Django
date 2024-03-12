# middleware.py
from django.http import HttpResponseForbidden

class IPBlockMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the request IP is in the blacklist
        blocked_ips = ['192.168.1.1', '10.0.0.1']  # Example list of blocked IPs
        if request.META['REMOTE_ADDR'] in blocked_ips:
            return HttpResponseForbidden("Your IP is blocked.")

        return self.get_response(request)
