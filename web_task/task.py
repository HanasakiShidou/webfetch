from obj import *
from typing import Dict, List

class webTask(webObj):
    def status(self):
        raise NotImplementedError

    def start(self):
        raise NotImplementedError

    def stop(self):
        raise NotImplementedError

    def pause(self):
        raise NotImplementedError

    def resume(self):
        raise NotImplementedError

class webTaskmgr(webObj):
    def __init__(self) -> None:
        super().__init__()
        self.taskList: Dict[int, webTask] = dict()

    def status(self, id: int = None):
        ret: dict = dict()
        ret['code'] = 0

        if id is not None:
            if id in self.taskList:
                return self.taskList[id].status()
            else:
                ret['code'] = 1
                ret['message'] = 'No such task with given id'
                return ret
        
        status: List[dict] = list()
        for key in self.taskList:
            currStatus: dict = self.taskList[key].status()
            status.append(currStatus)
        
        ret['status'] = status

        return ret

    def id_call(self, id: int, func: str, param: str = None):
        ret: dict = dict()
        ret['code'] = 0

        if id is not None:
            if id in self.taskList:
                return self.taskList[id].call(func=func, param=param)
            else:
                ret['code'] = 1
                ret['message'] = 'No such task with given id'
                return ret

'''
    def start(self, id: int):
        ret: dict = dict()
        ret['code'] = 0

        if id is not None:
            if id in self.taskList:
                return self.taskList[id].start()
            else:
                ret['code'] = 1
                ret['message'] = 'No such task with given id'
                return ret
        else:
            ret['code'] = 1
            ret['message'] = 'Operation start requires an id'
'''         

if __name__ == '__main__':
    mgr = webTaskmgr()

    print(mgr.call('status', 'id=2,k=8'))