from ratelimit.decorators import ratelimit

@ratelimit(key='ip', rate='5/m', block=True)
def my_view(request):
    # Your view logic here
