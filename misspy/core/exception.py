class MiError(Exception):
    pass

class HTTPError(Exception):
    pass

class MisskeyAPIError(MiError):
    pass

class ParseError(Exception):
    pass

class RegistedError(Exception):
    pass

class AlreadyRegisted(RegistedError):
    pass

class NotRegisted(RegistedError):
    pass