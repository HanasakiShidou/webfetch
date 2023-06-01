    function stopTask(uid){
        jQuery.get({
            url:'/taskmgr/stop/'+uid,
            success:function (response){
                if(response.code === 0){ //code=0 操作成功 status 为真表示当前任务是停止
                    if(response.status === true){
                        document.getElementsByName('btnStop'+uid).item(0).innerText="开始"
                    }else {
                        document.getElementsByName('btnStop'+uid).item(0).innerText="停止"
                    }
                }else{
                    alert(response.message)
                }
            },
            dataType:"json"
        })
    }
    function pauseTask(uid){
        jQuery.get({
            url:'/taskmgr/pause/'+uid,
            success:function (response){
                if(response.code === 0){ //code=0 操作成功 status 为真表示当前任务是停止
                    if(response.status === true){
                        document.getElementsByName('btnPause'+uid).item(0).innerText="继续"
                    }else {
                        document.getElementsByName('btnPause'+uid).item(0).innerText="暂停"
                    }
                }else{
                    alert(response.message)
                }
            },
            dataType:"json"
        })
    }
    function createTask(uid){
        console.log('param:'+uid)
        jQuery.get({
            url:'/taskmgr/create/'+uid,
            success:function (response){
                if(response.code === 0){ //code=0 操作成功 status 为真表示当前任务是停止
                    alert('操作成功')
                }
            },
            dataType:"json"
        })
    }