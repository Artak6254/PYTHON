#sa menq stexcum en authetnikacia vorpisi karanq jnjenq avelecnenq tvjal
from tastypie.authentication import ApiKeyAuthentication

class CustomAuthentication(ApiKeyAuthentication):
    def is_authenticated(self, request, **kwargs):
        #sa ruchnoy avelacnum enq
        if request.method == "GET":
            return True
        
        return super().is_authenticated(request, **kwargs)