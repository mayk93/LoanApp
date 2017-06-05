import logging

with open("/tmp/api_log.log", "a+") as _open:
    pass
logging.basicConfig(level=logging.INFO, filename="/tmp/api_log.log")


def request_to_log(request):
    log = "API Host: %s - " % request.META.get("HTTP_HOST", "Unknown API host")
    log += "Origin: %s - " % request.META.get("HTTP_ORIGIN", "Unknown origin")
    log += "Endpoint: %s - " % request.META.get("PATH_INFO", "Unknown endpoint")
    log += "User: %s - " % request.user.username
    log += "User Auth: %s" % request.user.is_authenticated

    return log


def request_logging_middelware(get_response):
    def middleware(request):
        logging.info("[Logging Middleware] Received request: %s" % request_to_log(request))

        response = get_response(request)

        return response

    return middleware