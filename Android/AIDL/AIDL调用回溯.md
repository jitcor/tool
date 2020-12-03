# AIDL调用DEMO
## 服务端
- aidl文件
```java
// IPerson.aidl
package com.ihbing.aidltest;

// Declare any non-default types here with import statements

interface IPerson {
    /**
     * Demonstrates some basic types that you can use as parameters
     * and return values in AIDL.
     */
    void basicTypes(int anInt, long aLong, boolean aBoolean, float aFloat,
            double aDouble, String aString);
    String queryPerson(int num);
}

```
- AIDLService
```java

package com.ihbing.aidltest;

import android.app.Service;
import android.content.Intent;
import android.os.IBinder;
import android.os.RemoteException;
import android.support.annotation.Nullable;
import android.widget.Toast;

public class AIDLService extends Service{
    private IBinder binder = new PersonQueryBinder();
    private String[] names = {"B神","艹神","基神","J神","翔神"};

    private String query(int num)
    {
        if(num > 0 && num < 6){
            return names[num - 1];
        }
        return null;
    }
    @Nullable
    @Override
    public IBinder onBind(Intent intent) {
        return binder;
    }
    private final class PersonQueryBinder extends IPerson.Stub{

        @Override
        public void basicTypes(int anInt, long aLong, boolean aBoolean, float aFloat, double aDouble, String aString) throws RemoteException {

        }

        @Override
        public String queryPerson(int num) throws RemoteException {
//            Toast.makeText(AIDLService.this,"The queryPerson(num:"+num,Toast.LENGTH_LONG).show();
            return query(num);
        }
    }
}

```
## 客户端
- 将服务端aidl文件复制过来(包名保持一致)
- MainActivity
```java

package com.ihbing.clienttest;

import android.app.Activity;
import android.content.ComponentName;
import android.content.Intent;
import android.content.ServiceConnection;
import android.os.Bundle;
import android.os.IBinder;
import android.os.RemoteException;
import android.view.View;
import android.widget.Toast;

import com.ihbing.aidltest.IPerson;

public class MainActivity extends Activity {
    private IPerson iPerson;
    private PersonConnection conn = new PersonConnection();
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        try{
            Intent service = new Intent("android.intent.action.AIDLService");
            service.setPackage("com.ihbing.aidltest");
           boolean ret= bindService(service,conn,BIND_AUTO_CREATE);
           Toast.makeText(this,"Bind ret:"+ret,Toast.LENGTH_LONG).show();
        }catch (Exception e){
            Toast.makeText(this,"Bind failed",Toast.LENGTH_LONG).show();
        }


    }

    public void query(View view) {
        if(iPerson!=null){
            try {
                Toast.makeText(this,"Query:"+iPerson.queryPerson(2),Toast.LENGTH_LONG).show();
            } catch (RemoteException e) {
                e.printStackTrace();
            }
        }else {
            Toast.makeText(this,"Remote service is not bound",Toast.LENGTH_LONG).show();
        }
    }

    private final class PersonConnection implements ServiceConnection {
        public void onServiceConnected(ComponentName name, IBinder service) {
            iPerson = IPerson.Stub.asInterface(service);
            Toast.makeText(MainActivity.this,"Service connected",Toast.LENGTH_LONG).show();
        }
        public void onServiceDisconnected(ComponentName name) {
            iPerson = null;
            Toast.makeText(MainActivity.this,"Service disconnected",Toast.LENGTH_LONG).show();
        }
    }
}

```
# 如何查找远程调用的具体实现代码
- 直接查找谁extends了stub这个类就可以找到具体实现代码
- 查找谁extends了android.os.IInterface接口就可以找到stub类
- 至于如何找到stub类，看下面例子说明
- 如下一个正常的堆栈打印例子
```java
java.lang.Exception
	at f.a.a.b.a.a.readString(Native Method)
	at com.tencent.mm.protocal.protobuf.bty.op(SourceFile:2051)
	at com.tencent.mm.bw.a.populateBuilderWithField(SourceFile:60)
	at com.tencent.mm.protocal.protobuf.baa.op(SourceFile:377)
	at com.tencent.mm.bw.a.populateBuilderWithField(SourceFile:60)
	at com.tencent.mm.protocal.protobuf.baa.op(SourceFile:195)
	at com.tencent.mm.bw.a.parseFrom(SourceFile:55)
	at com.tencent.mm.ak.b$c.fromProtoBuf(SourceFile:267)
	at com.tencent.mm.ak.w.a(SourceFile:149)
	at com.tencent.mm.protocal.i$a.onTransact(SourceFile:56)
	at android.os.Binder.execTransactInternal(Binder.java:1021)
	at android.os.Binder.execTransact(Binder.java:994)
```
- 先找到onTransact所在位置
- onTransact所在类必然有如下特征
```java
public interface IPerson extends android.os.IInterface
{

    public static abstract class Stub extends android.os.Binder implements IPerson
    {
          //·····
          @Override public boolean onTransact(int code, android.os.Parcel data, android.os.Parcel reply, int flags) throws android.os.RemoteException
          {
          //····
          }

    }
｝
```
- 然后根据上面特征即可找到stub函数
