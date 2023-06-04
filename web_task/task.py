from obj import *

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

class webTaskmgr(webTask):
    def __init__(self) -> None:
        super().__init__()
        self.taskList: list = list()

if __name__ == '__main__':
    mgr = webTaskmgr()

    print(mgr.call('start', ''))