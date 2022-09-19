
class ProblemDetails():
    def __init__(self,type:str=None,title:str=None,status:str=None,traceId:str=None,errors:str=None):
        self._type=type
        self._title=title
        self._status=status
        self._traceId=traceId
        self._errors=errors
