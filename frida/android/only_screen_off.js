
testCode(true,function (){
   // < android Q 
   const SurfaceControl=Java.use('android.view.SurfaceControl');
   var token =SurfaceControl.getBuiltInDisplay(0);
   SurfaceControl.setDisplayPowerMode(token,0);//0:off,2:no
})
