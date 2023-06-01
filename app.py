import os

from flask import Flask, render_template, jsonify, send_from_directory
from Spider.daemon import SpiderDaemon as daemon
#from Spider.task.bilivideoinfo.videoinfo_analyzer import gendata

main = Flask(__name__)


# Static files
@main.route('/favicon.ico')
def favicon():
    return main.send_static_file('favicon.ico')


@main.route('/')
def index():
    return main.send_static_file('index.html')

@main.route('/taskinfo.html')
def taskInfo():
    return main.send_static_file('taskinfo.html')

@main.route('/csv/<int:uid>')
def sendcsv(uid):
    dirpath = os.path.join(main.root_path, 'videoInfo')
    #print(dirpath)
    return send_from_directory(dirpath,str(uid)+'.csv',as_attachment=True)

@main.route('/pic/<int:uid>')
def sendpic(uid):
    dirpath = os.path.join(main.root_path, 'videoInfo')
    #print(dirpath)
    return send_from_directory(dirpath,str(uid)+'.jpg',as_attachment=True)

'''
@main.route('/analyze/<int:uid>')
def analyzer(uid):
    kvalue = 3
    taskanalyze = gendata(kvalue=kvalue,uid=uid)
    return render_template('analyze.html',taskanalyze=taskanalyze,uid=uid,kvalue=kvalue)
'''

# taskmgr Action
# 不带参数输出所有任务状态
@main.route('/taskinfo')
def taskInfo_all():
    tasklist = daemon().gettasks()
    return render_template('taskinfo_all.html', tasklist=tasklist)


@main.route('/taskinfo/<int:uid>')
def taskInfo_usr(uid):
    info = daemon().getstatus(uid)
    if len(info) == 0:
        return "no such task with given uid!"
    return render_template('taskinfo_single.html',info=info)


# 参数 stop pause create
@main.route('/taskmgr/<string:action>/<int:uid>')
def taskmgr(action, uid):
    result = dict()
    if action == "create":
        if uid > 0:
            daemon().create(uid=uid)
            result['code'] = 0
    elif action == "stop":
        if uid in daemon().taskArray:
            if daemon().taskArray[uid].isStop:
                daemon().taskArray[uid].isStop = False
                daemon().start(uid)
                result['code'] = 0
                result['status'] = daemon().taskArray[uid].isStop
            else:
                daemon().taskArray[uid].stop()
                result['code'] = 0
                result['status'] = daemon().taskArray[uid].isStop
        else:
            result['code'] = 1
            result['message'] = 'no such task with given uid!'
        #返回值为真代表 是停止
    elif action == "pause":
        if uid in daemon().taskArray:
            if not daemon().taskArray[uid].isPause.isSet():
                daemon().taskArray[uid].resume()
                result['code'] = 0
                result['status'] = not daemon().taskArray[uid].isPause.isSet() #返回true代表暂停
            else:
                daemon().taskArray[uid].pause()
                result['code'] = 0
                result['status'] = not daemon().taskArray[uid].isPause.isSet() #返回false代表未暂停
    else:
        result['code'] = 1
        result['message'] = 'undefined action'
    return jsonify(result)

# 参数 stop pause create
#@main.route('/taskmgr/<string:action>/<int:uid>')


class Task:
    def do_action(action :str, param: str):
        pass

    def get_action(action :str, param: str):
        pass

    def get_status():
        pass

    def start():
        pass

    def stop():
        pass

    def pause():
        pass

    def resume():
        pass


if __name__ == '__main__':
    main.run()
