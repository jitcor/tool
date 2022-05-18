Interceptor.attach(AIM.add(0x28ddcc),{
        onEnter:function (args){//好像只能在onEnter里操作
            try {
                console.log('call 0x28ddcc: ');
                // @ts-ignore
                console.log('call 0x28ddcc: x1:',this.context.x1);
            }catch (e){
                console.log("call 0x28ddcc error:",e);
            }
        }
    })
