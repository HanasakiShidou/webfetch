
def parseline(line: str) -> dict:
    line: list = line.split('&')
    kw: dict = dict()
    for line in line:
        if len(line) == 0:
            continue
        pair = line.split('=', maxsplit=2)
        if len(pair) > 1:
            if len(pair[1]) > 0:
                kw[pair[0]] = pair[1]
    return kw

class webObj:
    def getfunc(self, func: str):
        if (hasattr(self, func)):
            if (callable(getattr(self, func))):
                return getattr(self, func)
        return None
    
    # get_call
    def call(self, func: str, param: str) -> dict:
        ret: dict = dict()
        ret['code'] = 0

        if (self.getfunc(func=func) is not None):
            try:
                ret = self.getfunc(func=func)(**parseline(param))
            except Exception as err:
                ret['code'] = 1
                ret['message'] = f"Unexpected {err=}, {type(err)=}"
        else:
            return ret


        return ret

class tobj(webObj):
    def test(self, id, **kwargs):
        print(id)

if __name__ == '__main__':
    web = tobj()

    print(web.call('test','id=&k=3'))

