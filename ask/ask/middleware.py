from datetime import datetime, timedelta

from django.utils.deprecation import MiddlewareMixin

class MyTestMiddleware(MiddlewareMixin):
    # def __init__(self, get_response):
    #     self.get_response = get_response

    # def __call__(self, request):
    #     # Code to be executed for each request before
    #     # the view (and later middleware) are called.

    #     response = self.get_response(request)

    #     # Code to be executed for each request/response after
    #     # the view is called.

    #     return response

    # def process_request(self, request):
    #     import pdb; pdb.set_trace()
    #     print('My Middleware was run!')

    def process_response(self, request, response):
        response.set_cookie('mytestcookie', 'Value of my test cookie from my middleware. Keep Rock \\m/',
               expires = datetime.now()+timedelta(days=5)
            )
        # import pdb; pdb.set_trace()
        return response





# class SecurityMiddleware(MiddlewareMixin):
#     def __init__(self, get_response=None):
#         self.sts_seconds = settings.SECURE_HSTS_SECONDS
#         self.sts_include_subdomains = settings.SECURE_HSTS_INCLUDE_SUBDOMAINS
#         self.content_type_nosniff = settings.SECURE_CONTENT_TYPE_NOSNIFF
#         self.xss_filter = settings.SECURE_BROWSER_XSS_FILTER
#         self.redirect = settings.SECURE_SSL_REDIRECT
#         self.redirect_host = settings.SECURE_SSL_HOST
#         self.redirect_exempt = [re.compile(r) for r in settings.SECURE_REDIRECT_EXEMPT]
#         self.get_response = get_response

#     def process_request(self, request):
#         path = request.path.lstrip("/")
#         if (self.redirect and not request.is_secure() and
#                 not any(pattern.search(path)
#                         for pattern in self.redirect_exempt)):
#             host = self.redirect_host or request.get_host()
#             return HttpResponsePermanentRedirect(
#                 "https://%s%s" % (host, request.get_full_path())
#             )

#     def process_response(self, request, response):
#         if (self.sts_seconds and request.is_secure() and
#                 'strict-transport-security' not in response):
#             sts_header = "max-age=%s" % self.sts_seconds

#             if self.sts_include_subdomains:
#                 sts_header = sts_header + "; includeSubDomains"

#             response["strict-transport-security"] = sts_header

#         if self.content_type_nosniff and 'x-content-type-options' not in response:
#             response["x-content-type-options"] = "nosniff"

#         if self.xss_filter and 'x-xss-protection' not in response:
#             response["x-xss-protection"] = "1; mode=block"

#         return response