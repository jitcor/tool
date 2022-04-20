// @ts-ignore
function findClass(cls:string,func){
    var isFind=false;
    Java.choose("dalvik.system.DexClassLoader",{
        onMatch:function (instance) {
            if(isFind)return;
            if(instance!=null){
                // console.log('classloader str:',instance)
                try{
                    // @ts-ignore
                    Java.classFactory.loader=instance
                    func(Java.use(cls));
                    isFind=true;
                }catch (e){
                }
            }
        },
        onComplete:function () {
            console.log('finish')
        }
    })
}
