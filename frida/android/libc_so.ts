function commonNativeHook(moduleName:string,funcName:string,retType:string,argTypes:string[],implementation:(originalFunc:any,args:any) => any){
    const module=Process.getModuleByName(moduleName)
    const func=module.findExportByName(funcName)
    // @ts-ignore
    const oldFuncImpl=new NativeFunction(func,retType,argTypes)
    // @ts-ignore
    Interceptor.replace(func,new NativeCallback(function () {
        return implementation(oldFuncImpl,arguments)
    },retType,argTypes))
}

commonNativeHook("libc.so","strstr",'pointer',['pointer','pointer'],function (originalFunc, args){
    console.log('commonNativeHook:strstr0:',args[0].readCString())
    console.log('commonNativeHook:strstr1:',args[1].readCString())
    return originalFunc(args)
})
