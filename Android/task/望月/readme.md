# 通过ucrack分析网络请求堆栈

# 打印umeng调试日志
`adb shell setprop debug.umeng.rtlog 1`
# 开启umeng调试模式
`com.umeng.commonsdk.UMConfigure.setLogEnabled(true)`
# 编码函数
`com.umeng.commonsdk.statistics.idtracking.Envelope.toBinary()`
```java
public byte[] toBinary() {
    ay ayVar = new ay();
    ayVar.a(this.mVersion);
    ayVar.b(this.mAddress);
    ayVar.c(DataHelper.toHexString(this.mSignature));
    ayVar.a(this.mSerialNo);
    ayVar.b(this.mTimestamp);
    ayVar.c(this.mLength);
    ayVar.a(this.mEntity);
    ayVar.d(this.encrypt ? 1 : 0);
    ayVar.d(DataHelper.toHexString(this.mGuid));
    ayVar.e(DataHelper.toHexString(this.mChecksum));
    try {
        return new bo().a(ayVar);
    } catch (Exception e) {
        e.printStackTrace();
        return null;
    }
}

```
# 解码函数
`com.umeng.commonsdk.statistics.b.a(Context context, byte[] bArr)->Envelope`
```java
private Envelope a(Context context, byte[] bArr) {
    String imprintProperty = UMEnvelopeBuild.imprintProperty(context, "codex", (String) null);
    int i = -1;
    try {
        if (!TextUtils.isEmpty(imprintProperty)) {
            i = Integer.valueOf(imprintProperty).intValue();
        }
    } catch (NumberFormatException e2) {
        UMCrashManager.reportCrash(context, e2);
    }
    if (i == 0) {
        return Envelope.genEnvelope(context, UMUtils.getAppkey(context), bArr);//具体实现
    }
    if (i == 1) {
        return Envelope.genEncryptEnvelope(context, UMUtils.getAppkey(context), bArr);//具体实现
    }
    if (f) {
        return Envelope.genEncryptEnvelope(context, UMUtils.getAppkey(context), bArr);//具体实现
    }
    return Envelope.genEnvelope(context, UMUtils.getAppkey(context), bArr);//具体实现
}

```
# 保存编码数据
`com.umeng.commonsdk.framework.UMFrUtils.saveEnvelopeFile(Context context, String str, byte[] bArr)->int`
# 构建原始json数据函数
`com.umeng.commonsdk.framework.UMEnvelopeBuild.buildEnvelopeWithExtHeader(Context context, JSONObject jSONObject, JSONObject jSONObject2)->JSONObject`
# 拦截日志
```
"D:\Program Files\Python3.7.0\python.exe" D:/Project/python/fridaPy/wangy/wangy.py
frida version:12.7.22
Success
common_enabled_debug running....
getStringValue传入参数:  new_user_channel
[call saveEnvelopeFile] [object Object] , z==1.2.0&&2.0.4_1599675543797_envelope.log :
Error: java.lang.ClassNotFoundException: Didn't find class "org.lasinger.tools.hexdump.Hexdump" on path: DexPathList[[zip file "/data/app/com.wangyue9.phonelive05-1/base.apk"],nativeLibraryDirectories=[/data/app/com.wangyue9.phonelive05-1/lib/arm, /data/app/com.wangyue9.phonelive05-1/base.apk!/lib/armeabi-v7a, /vendor/lib, /system/lib]]
load hexdump.dex ok
00000000  18 03 31 2e 30 18 18 35  66 34 61 31 39 30 31 31  |□□1.0□□5f4a19011|
00000010  32 39 38 31 64 33 63 61  33 30 61 37 38 30 61 18  |2981d3ca30a780a□|
00000020  40 39 37 31 63 32 65 35  61 66 37 33 31 31 34 66  |@971c2e5af73114f|
00000030  65 61 38 30 37 32 33 62  34 32 64 64 39 32 66 62  |ea80723b42dd92fb|
00000040  65 33 36 37 32 36 64 65  31 63 64 65 31 39 32 38  |e36726de1cde1928|
00000050  31 36 66 32 62 39 37 31  61 64 64 63 33 35 39 35  |16f2b971addc3595|
00000060  66 15 02 15 ae f2 c8 f5  0b 15 aa 01 18 57 78 9c  |f□□□□□□□□□□□□Wx□|
00000070  ab 56 ca 48 4d 4c 49 2d  52 b2 aa 56 4a 2c 28 c8  |□V□HMLI-R□□VJ,(□|
00000080  4e ad 54 b2 52 32 4d 33  49 34 b4 34 30 34 34 b2  |N□T□R2M3I4□4044□|
00000090  b4 30 4c 31 4e 4e 34 36  48 34 b7 30 48 54 d2 01  |□0L1NN46H4□0HT□□|
000000a0  a9 89 2f 4b 2d 2a ce cc  cf 03 2a 34 d2 33 d0 33  |□□/K-*□□□□*4□3□3|
000000b0  01 8a e6 17 03 39 8e 79  29 45 f9 99 29 4a b5 b5  |□□□□□9□y)E□□)J□□|
000000c0  00 47 75 19 5a 18 40 30  30 30 30 32 65 35 61 66  |□Gu□Z□@00002e5af|
000000d0  37 33 31 31 34 66 65 61  38 30 37 32 33 62 34 32  |73114fea80723b42|
000000e0  64 64 39 32 66 62 65 33  36 37 32 36 64 65 31 63  |dd92fbe36726de1c|
000000f0  64 65 31 39 32 38 31 36  66 32 62 39 37 31 61 64  |de192816f2b971ad|
00000100  64 63 33 30 30 30 30 18  20 30 35 63 38 64 37 36  |dc30000□␣05c8d76|
00000110  61 62 63 64 32 39 34 65  62 65 39 37 63 34 61 38  |abcd294ebe97c4a8|
00000120  33 32 32 39 64 66 33 66  35 15 00 00              |3229df3f5□□□|
0000012c

java.lang.Exception
	at com.umeng.commonsdk.framework.UMFrUtils.saveEnvelopeFile(Native Method)
	at com.umeng.commonsdk.statistics.b.a(EnvelopeManager.java:818)
	at com.umeng.commonsdk.statistics.b.b(EnvelopeManager.java:471)
	at com.umeng.commonsdk.framework.UMEnvelopeBuild.buildZeroEnvelopeWithExtHeader(UMEnvelopeBuild.java:275)
	at com.umeng.commonsdk.internal.c.a(UMInternalDataProtocol.java:131)
	at com.umeng.commonsdk.internal.c.workEvent(UMInternalDataProtocol.java:374)
	at com.umeng.commonsdk.framework.UMWorkDispatch.handleEvent(UMWorkDispatch.java:239)
	at com.umeng.commonsdk.framework.UMWorkDispatch.access$000(UMWorkDispatch.java:21)
	at com.umeng.commonsdk.framework.UMWorkDispatch$1.handleMessage(UMWorkDispatch.java:192)
	at android.os.Handler.dispatchMessage(Handler.java:102)
	at android.os.Looper.loop(Looper.java:148)
	at android.os.HandlerThread.run(HandlerThread.java:61)
	at de.robv.android.xposed.XposedBridge.invokeOriginalMethodNative(Native Method)
	at de.robv.android.xposed.XposedBridge.handleHookedMethod(XposedBridge.java:360)
	at android.os.HandlerThread.run(<Xposed>)

result: 0
[call buildEnvelopeWithExtHeader]
 {
  "vertical_type": 0,
  "sdk_version": "9.1.0",
  "pro_ver": "1.0.0",
  "atm": "1",
  "$pr_ve": "0",
  "$ud_da": "2020-09-10",
  "st": "1",
  "app_version": "2.0.4",
  "version_code": "10"
} ,
 {
  "analytics": {
    "sessions": [
      {
        "id": "73E93C23FEEE44239EE3FDF838938535",
        "start_time": "1599675543782"
      }
    ]
  }
} :
[call saveEnvelopeFile] [object Object] , t==9.1.0&&2.0.4_1599675545936_envelope.log :
00000000  18 03 31 2e 30 18 18 35  66 34 61 31 39 30 31 31  |□□1.0□□5f4a19011|
00000010  32 39 38 31 64 33 63 61  33 30 61 37 38 30 61 18  |2981d3ca30a780a□|
00000020  40 39 37 31 63 32 65 35  61 66 37 33 31 31 34 66  |@971c2e5af73114f|
00000030  65 61 38 30 37 32 33 62  34 32 64 64 39 32 66 62  |ea80723b42dd92fb|
00000040  65 33 36 37 32 36 64 65  31 63 64 65 31 39 32 38  |e36726de1cde1928|
00000050  31 36 66 32 62 39 37 31  61 64 64 63 33 35 39 35  |16f2b971addc3595|
00000060  66 15 04 15 b2 f2 c8 f5  0b 15 ce 22 18 c5 0a 78  |f□□□□□□□□□□"□□¶x|
00000070  9c a5 56 c9 72 a3 48 10  fd 15 87 a2 0f b3 b4 3d  |□□V□r□H□□□□□□□□=|
00000080  55 2c 02 2a a2 0f 20 40  2d 8f 81 96 2c 09 a3 f1  |U,□*□□␣@-□□□,→□□|
00000090  84 a2 04 08 21 d6 06 b4  40 47 df e7 1f a6 bf af  |□□□□!□□□@G□□□□□□|
000000a0  bf 63 b2 b0 dd 96 0f 13  73 98 83 22 2a d7 ca 7c  |□c□□□□□□s□□"*□□||
000000b0  2f 2b d1 97 c1 2e a4 41  58 0d c8 97 01 2d cb 75  |/+□□□.□AX¤□□□-□u|
000000c0  1d 47 39 6d 0e 55 38 20  03 3c 24 a6 48 04 91 20  |□G9m□U8␣□<$□H□□␣|
000000d0  95 48 88 8c 24 22 8e 88  a2 10 45 24 06 4f f8 fe  |□H□□$"□□□□E$□O□□|
000000e0  60 9a 84 d7 89 32 22 a2  38 78 ff 92 61 5d ef 28  |`□□□□2"□8x□□a]□(|
000000f0  86 04 23 85 c8 1c 19 aa  04 4b 04 43 02 8d 20 85  |□□#□□□□□□K□C□□␣□|
00000100  18 26 19 ca c4 e4 08 8f  88 2a 12 9d 23 0a 26 23  |□&□□□□□□□*□□#¶&#|
00000110  9d f0 12 e1 54 66 15 65  c2 0f df 26 83 5c ad 77  |□□□□Tf□e□□□&□\□w|
00000120  fb d9 3c eb 77 a3 50 29  e4 fd 28 45 e5 47 db 6e  |□□<□w□P)□□(E□G□n|
00000130  ab a3 ab 7b 1f 9e 9d 8f  61 55 c7 45 0e ce dc 0d  |□□□{□□□□aU□E□□□¤|
00000140  ba 11 40 fb ac 59 fb 45  d0 37 84 40 17 07 59 20  |□□@□□Y□E□7□@□□Y␣|
00000150  82 a0 6c 15 39 90 24 de  47 01 c2 22 e7 0b 38 c0  |□□l□9□$□G□□"□□8□|
00000160  b2 28 08 1b 4e e6 a8 cf  a2 fd f2 00 7e ea cc 3a  |□(□□N□□□□□□□~□□:|
00000170  4a 57 9f aa c2 0f eb ba  a8 ae aa f0 78 85 ae 7e  |JW□□□□□□□□□□x□□~|
00000180  3a 4a e9 cf e0 93 f9 7e  96 fb e0 06 e7 20 3c c6  |:J□□□□□~□□□□□␣<□|
00000190  7e b8 6e da 92 5d f6 69  57 e4 21 68 4b ea 27 34  |~□n□□]□iW□!hK□'4|
000001a0  0a d7 39 cd 98 da 2f b2  9b 13 cd a3 f6 10 2a 37  |¶□9□□□/□□□□□□□*7|
000001b0  25 f3 49 e3 63 88 18 7a  75 90 bc 04 ab 79 50 15  |%□I□c□□zu□□□□yP□|
000001c0  71 f0 9a 14 ce 64 20 cb  c4 57 48 80 48 b8 25 21  |q□□□□d␣□□WH□H□%!|
000001d0  e0 76 61 cf a0 c3 14 5c  ec f0 7c a8 af c4 57 c3  |□va□□□□\□□|□□□W□|
000001e0  a6 a0 15 8b dd d1 2c 0b  2b 46 f6 85 ad a2 39 b3  |□□□□□□,□+F□□□□9□|
000001f0  45 45 11 a5 e1 45 32 9a  1f 9a 98 95 8b 05 09 29  |EE□□□E2□□□□□□□→)|
00000200  43 89 e3 25 84 d0 1b fb  96 fa 6c 4c 60 70 06 77  |C□□%□□□□□□lL`p□w|
00000210  63 e3 6d 6c 5f ac e5 68  3c be 30 3c f7 ff a6 8e  |c□ml_□□h<□0<□□□□|
00000220  a2 be 20 6d 08 a4 e1 5e  f9 06 80 2a ac 8b 14 ca  |□□␣m□□□^□□□*□□□□|
00000230  e9 7d b0 24 0d 7f c1 48  46 3d f4 ff 02 09 2b bd  |□}□$¤□□HF=□□□→+□|
00000240  63 e0 13 19 48 2c 0e 79  53 b5 6c 1a 6d b0 a5 00  |c□□□H,□yS□l□m□□□|
00000250  fd 01 e8 00 b9 db 31 8e  69 55 c5 7d 17 ac d2 b8  |□□□□□□1□iU□}□□□□|
00000260  2e 53 da be 94 fa fd db  df df bf fd c5 86 cb 67  |.S□□□□□□□□□□□□□g|
00000270  dc 83 e6 14 6f 63 96 a4  f0 69 ba 8e 4b 56 90 c2  |□□□□oc□□□i□□KV□□|
00000280  dd e0 a1 7c 83 6f 24 30  e4 61 73 2a aa 17 16 11  |□□□|□o$0□as*□□□□|
00000290  bb 3d 63 1d b2 71 03 17  56 35 d3 fc 30 03 6b 87  |□=c□□q□□V5□□0□k□|
000002a0  94 5d 45 bb b8 f0 fb 31  8e d7 69 78 64 54 72 3c  |□]E□□□□1□□ixdTr<|
000002b0  4c 04 5c cb e6 b7 07 54  0a 43 19 71 ca f6 3a e0  |L□\□□□□T¶C□q□□:□|
000002c0  85 ed b5 c0 63 74 bd e1  f8 e0 5a 92 31 e5 87 be  |□□□□ct□□□□Z□1□□□|
000002d0  2c 28 fe 86 c1 47 e3 60  5d 85 9f 0f 71 15 06 eb  |,(□□□G□`]□□□q□□□|
000002e0  27 1a 59 73 f5 a1 ef 62  7b 48 7b 6b 58 37 d0 11  |'□Ys□□□b{H{kX7□□|
000002f0  7e 3f d8 d2 38 0d 83 0b  1d 62 98 7f 7e 8e c4 9c  |~?□□8¤□□□b□□~□□□|
00000300  c8 40 dc d1 3c ef e7 eb  d4 ae f7 87 2e 5e fb f5  |□@□□<□□□□□□□.^□□|
00000310  5a 5c e3 a7 87 97 84 0c  5e 71 2b 50 ac 20 8c 39  |Z\□□□□□□^q+P□␣□9|
00000320  45 c6 01 ef 53 1e 51 49  46 14 7c 4e 15 78 85 d5  |E□□□S□QIF□|N□x□□|
00000330  cb 70 c3 82 81 91 bf d0  bf ce 00 63 8f 56 51 d8  |□p□□□□□□□□□c□VQ□|
00000340  dc 07 c9 92 e1 c6 49 50  4d 59 af 4b 86 61 5e f4  |□□□□□□IPMY□K□a^□|
00000350  64 a4 97 d2 f6 52 8a b3  b2 8a f3 06 c4 f1 49 5d  |d□□□□R□□□□□□□□I]|
00000360  aa bb 28 b2 bb a8 f3 5c  4f 70 f4 34 59 e9 46 eb  |□□(□□□□\Op□4Y□F□|
00000370  71 1e 6f 73 13 ec 75 09  b6 c6 5e e7 e8 2a ef b9  |q□os□□u→□□^□□*□□|
00000380  e6 1e 7c d4 c7 fc 69 65  34 31 a3 f7 07 49 ec 59  |□□|□□□ie41□□□I□Y|
00000390  be 56 f8 c2 63 59 15 cf  cc 82 dc 6b 68 93 31 09  |□V□□cY□□□□□kh□1→|
000003a0  4e ef 4a d6 13 08 4c fd  ee 10 ac 03 b6 c1 38 c4  |N□J□□□L□□□□□□□8□|
000003b0  a1 6b a4 5c f7 5b a8 6e  9e 7d 81 ac a6 82 15 11  |□k□\□[□n□}□□□□□□|
000003c0  e7 51 5f 36 b5 b4 87 25  5a 8d d3 64 ac ed 3c cb  |□Q_6□□□%Z□□d□□<□|
000003d0  6d f6 9b a5 ad 5b 49 7a  ba 5f cc b4 fb 8f 9a 13  |m□□□□[Iz□_□□□□□□|
000003e0  20 e3 ec 3e 94 e5 42 9f  b8 8f bf 1d 1c e5 e4 89  |␣□□>□□B□□□□□□□□□|
000003f0  81 39 9d a8 1a 04 ad 32  c3 bb d5 55 e4 8c 27 ed  |□9□□□□□2□□□U□□'□|
00000400  63 6e cd d3 e4 6e 6e b5  20 35 b6 3e 3d 39 23 bc  |cn□□□nn□␣5□>=9#□|
00000410  f3 e6 11 be 9b fb 9d ad  af 62 6f 3e e1 6d b0 5b  |□□□□□□□□□bo>□m□[|
00000420  e7 8d 2a de f1 da 3e 45  4b 35 52 c7 3e b7 6c a9  |□□*□□□>EK5R□>□l□|
00000430  6b d6 63 4d 3d 39 73 5f  74 f4 29 ff 98 db 7b 2d  |k□cM=9s_t□)□□□{-|
00000440  b3 dc 05 b2 e7 0b 64 d6  7a 72 f4 c7 ce c3 6c 31  |□□□□□□d□zr□□□□l1|
00000450  52 d5 65 b9 1a e3 c4 9e  45 5b c7 f5 44 67 3c e5  |R□e□□□□□E[□□Dg<□|
00000460  ed ce de 5b e3 e9 c9 9a  2f 5a af 9b 9e 01 7b c1  |□□□[□□□□/Z□□□□{□|
00000470  9e 4f 91 b7 9f 08 56 66  ee 21 9b b6 59 5c dc f9  |□O□□□□Vf□!□□Y\□□|
00000480  bb e7 8a 89 9f 29 e5 ca  84 9f 16 4d 57 d9 e4 e4  |□□□□□)□□□□□MW□□□|
00000490  e8 16 f2 32 3b b6 e7 ea  c9 e6 a6 ad 33 7b 13 a3  |□□□2;□□□□□□□3{□□|
000004a0  6f 80 b9 b1 66 08 8f b9  a3 97 7b 67 5e 26 96 5e  |o□□□f□□□□□{g^&□^|
000004b0  a6 ab 7d 99 5a fb 42 5c  69 f4 fe c2 7b b5 d1 22  |□□}□Z□B\i□□□{□□"|
000004c0  33 78 98 25 d4 9d 16 63  33 3a 53 ce 6e 16 c8 6a  |3x□%□□□c3:S□n□□j|
000004d0  ef 1f b4 db 99 61 4e 7c  43 e4 a7 73 73 f5 98 87  |□□□□□aN|C□□ss□□□|
000004e0  59 3a b5 76 9b 5f 05 a9  8f 56 c7 aa dd 78 ae 55  |Y:□v□_□□□V□□□x□U|
000004f0  18 f3 48 70 32 4b 74 32  c0 32 5b 66 4e b6 68 9d  |□□Hp2Kt2□2[fN□h□|
00000500  7d 9a 98 e5 dd 13 1a 53  d5 7b 66 a1 f8 5f 2c c0  |}□□□□□□S□{f□□_,□|
00000510  8d ab 6e f5 70 5b 7a ee  a9 30 74 55 b4 bb 44 b0  |□□n□p[z□□0tU□□D□|
00000520  75 9f 83 6c 63 ef bc 9a  4f 31 a0 e9 9e 9c fb 9e  |u□□lc□□□O1□□□□□□|
00000530  7d 15 3a a3 ee ac 59 e9  8b e2 63 97 66 ce 7c 97  |}□:□□□Y□□□c□f□|□|
00000540  d8 9d df 79 9d 06 88 18  d8 ca 2c 64 b9 d3 b3 a3  |□□□y□□□□□□,d□□□□|
00000550  03 7b 50 93 a3 df ee 80  15 f7 31 c7 af 19 de 32  |□{P□□□□□□□1□□□□2|
00000560  30 fa 4f 06 54 55 fd f0  01 de cc 57 18 fd 9c a6  |0□O□TU□□□□□W□□□□|
00000570  2d 3c 9b 9a fd 8d 78 5e  5a 70 fe e3 cb e0 69 73  |-<□□□□x^Zp□□□□is|
00000580  f1 86 c2 8f 38 de 34 0c  43 10 38 5e 31 0c de d4  |□□□□8□4□C□8^1□□□|
00000590  4d 99 97 15 5e 16 f9 fe  db 07 cf be 79 d9 56 58  |M□□□^□□□□□□□y□VX|
000005a0  54 e0 a3 23 8a 02 2f c9  dc e0 eb 9f 5f bf fe 03  |T□□#□□/□□□□□_□□□|
000005b0  df 72 b6 13 18 40 30 65  30 30 38 63 35 61 30 34  |□r□□□@0e008c5a04|
000005c0  33 31 38 62 66 65 64 63  30 37 34 64 62 34 64 34  |318bfedc074db4d4|
000005d0  64 39 37 38 62 65 61 66  37 32 32 36 65 31 36 32  |d978beaf7226e162|
000005e0  65 31 37 61 38 31 65 65  32 62 62 63 31 61 62 63  |e17a81ee2bbc1abc|
000005f0  63 33 30 30 30 30 18 20  65 63 32 63 62 61 33 36  |c30000□␣ec2cba36|
00000600  61 62 66 31 35 62 32 35  33 30 64 33 31 31 63 66  |abf15b2530d311cf|
00000610  62 33 63 36 31 35 39 65  15 00 00                 |b3c6159e□□□|
0000061b

java.lang.Exception
	at com.umeng.commonsdk.framework.UMFrUtils.saveEnvelopeFile(Native Method)
	at com.umeng.commonsdk.statistics.b.a(EnvelopeManager.java:818)
	at com.umeng.commonsdk.statistics.b.a(EnvelopeManager.java:334)
	at com.umeng.commonsdk.framework.UMEnvelopeBuild.buildEnvelopeWithExtHeader(UMEnvelopeBuild.java:245)
	at com.umeng.commonsdk.framework.UMEnvelopeBuild.buildEnvelopeWithExtHeader(Native Method)
	at com.umeng.analytics.pro.m.h(CoreProtocolImpl.java:435)
	at com.umeng.analytics.pro.m.a(CoreProtocolImpl.java:2245)
	at com.umeng.analytics.pro.m.a(CoreProtocolImpl.java:358)
	at com.umeng.analytics.CoreProtocol.workEvent(CoreProtocol.java:38)
	at com.umeng.commonsdk.framework.UMWorkDispatch.handleEvent(UMWorkDispatch.java:239)
	at com.umeng.commonsdk.framework.UMWorkDispatch.access$000(UMWorkDispatch.java:21)
	at com.umeng.commonsdk.framework.UMWorkDispatch$1.handleMessage(UMWorkDispatch.java:192)
	at android.os.Handler.dispatchMessage(Handler.java:102)
	at android.os.Looper.loop(Looper.java:148)
	at android.os.HandlerThread.run(HandlerThread.java:61)
	at de.robv.android.xposed.XposedBridge.invokeOriginalMethodNative(Native Method)
	at de.robv.android.xposed.XposedBridge.handleHookedMethod(XposedBridge.java:360)
	at android.os.HandlerThread.run(<Xposed>)

result: 0
result: {
  "header": {
    "app_signature": "16:F5:45:0A:70:C7:5C:99:95:E3:39:95:FF:3D:9C:55",
    "app_sig_sha1": "C9:82:6A:17:10:CB:09:EF:68:F2:30:A5:D2:91:CD:37:2A:EF:58:36",
    "app_sig_sha": "yYJqFxDLCe9o8jCl0pHNNyrvWDY=",
    "app_version": "2.0.4",
    "version_code": "10",
    "idmd5": "9f98d773c0d0152c41d18544b282ac4",
    "cpu": "ARMv7 Processor rev 0 (v7l)",
    "mccmnc": "",
    "device_type": "Phone",
    "package_name": "com.wangyue9.phonelive05",
    "sdk_type": "Android",
    "device_id": "88:c9:d0:ef:e2:9d",
    "device_model": "Nexus 5",
    "device_board": "hammerhead",
    "device_brand": "google",
    "device_manutime": 1470967237000,
    "device_manufacturer": "LGE",
    "device_manuid": "MOB31E",
    "device_name": "hammerhead",
    "os_version": "6.0.1",
    "os": "Android",
    "resolution": "1776*1080",
    "mc": "88:c9:d0:ef:e2:9d",
    "timezone": 8,
    "country": "CN",
    "language": "zh",
    "carrier": "",
    "display_name": "望月",
    "access": "wifi",
    "local_ip": "192.168.1.7",
    "network_type": 0,
    "com_ver": "9.1.0",
    "com_type": 0,
    "module": "azioc",
    "api_level": 23,
    "session_id": "7ee8029f-d34f-4310-b23d-781a36c849cb",
    "oaid_required_time": "",
    "successful_requests": 1,
    "failed_requests": 0,
    "req_time": 1258,
    "channel": "wy_juzi_cs_5_1",
    "appkey": "5f4a190112981d3ca30a780a",
    "wrapper_type": "native",
    "wrapper_version": "",
    "targetSdkVer": 27,
    "rps_pr": "no",
    "acl_pr": "no",
    "afl_pr": "no",
    "imprint": "GwAVAhggNzgzYWY4ODlkZDEyY2Y3N2I1Yzk1MGYzODA3YWFjYWYA\n",
    "vertical_type": 0,
    "sdk_version": "9.1.0",
    "pro_ver": "1.0.0",
    "atm": "1",
    "$pr_ve": "0",
    "$ud_da": "2020-09-10",
    "st": "1",
    "id_tracking": "GwaMBXV0ZGlkGBhYMWtjbVNDMklwSURBSHBOd0ExWXppUDIW\/uO9wY5dFQIABGlkZmEYJDA0OGIy\nMTlkLTMyOGItNDQwOC1hYTg1LTczNDZiYTI3NTMyMxbA5L3Bjl0VAgAGc2VyaWFsGBAwOTc5ODQ3\nNjBmMWU0NTU0FsDkvcGOXRUCAAVpZG1kNRgfOWY5OGQ3NzNjMGQwMTUyYzQxZDE4NTQ0YjI4MmFj\nNBbU5L3Bjl0VAgAKYW5kcm9pZF9pZBgQZmIwODM0YmNiNTAwN2QyORbU5L3Bjl0VAgADbWFjGBE4\nODpjOTpkMDplZjplMjo5ZBaS5L3Bjl0VAgAZbBgFdXRkaWQoGFgxa2NtU0MySXBJREFIcE53QTFZ\nemlQMhb+473Bjl0AGANtYWMoETg4OmM5OmQwOmVmOmUyOjlkFpLkvcGOXQAYBGlkZmEoJDA0OGIy\nMTlkLTMyOGItNDQwOC1hYTg1LTczNDZiYTI3NTMyMxbA5L3Bjl0AGAZzZXJpYWwoEDA5Nzk4NDc2\nMGYxZTQ1NTQWwOS9wY5dABgFaWRtZDUoHzlmOThkNzczYzBkMDE1MmM0MWQxODU0NGIyODJhYzQW\n1OS9wY5dABgKYW5kcm9pZF9pZCgQZmIwODM0YmNiNTAwN2QyORbU5L3Bjl0AAA==\n"
  },
  "analytics": {
    "sessions": [
      {
        "id": "73E93C23FEEE44239EE3FDF838938535",
        "start_time": "1599675543782"
      }
    ]
  }
}
[call buildEnvelopeWithExtHeader]
 {
  "vertical_type": 0,
  "sdk_version": "9.1.0",
  "pro_ver": "1.0.0",
  "$pr_ve": "0",
  "$ud_da": "2020-09-10",
  "app_version": "2.0.4",
  "version_code": "10"
} ,
 {
  "analytics": {
    "ekv": [
      {
        "73E93C23FEEE44239EE3FDF838938535": [
          {
            "id": "Launcher",
            "ts": 1599675543665,
            "Launcher": "",
            "ds": 0,
            "pn": "com.wangyue9.phonelive05"
          },
          {
            "id": "$$_onUMengEnterForeground",
            "ts": 1599675543778,
            "activityName": "com.huaji.phonelive.activity.LauncherActivity@9b897bf",
            "isMainProcess": 1,
            "pairUUID": "d541a7b3-7423-4e46-af19-c2ba74c290a7",
            "pid": 25292,
            "ds": 0,
            "pn": "com.wangyue9.phonelive05"
          }
        ]
      }
    ]
  }
} :
[call saveEnvelopeFile] [object Object] , a==9.1.0&&2.0.4_1599675546102_envelope.log :
00000000  18 03 31 2e 30 18 18 35  66 34 61 31 39 30 31 31  |□□1.0□□5f4a19011|
00000010  32 39 38 31 64 33 63 61  33 30 61 37 38 30 61 18  |2981d3ca30a780a□|
00000020  40 39 37 31 63 32 65 35  61 66 37 33 31 31 34 66  |@971c2e5af73114f|
00000030  65 61 38 30 37 32 33 62  34 32 64 64 39 32 66 62  |ea80723b42dd92fb|
00000040  65 33 36 37 32 36 64 65  31 63 64 65 31 39 32 38  |e36726de1cde1928|
00000050  31 36 66 32 62 39 37 31  61 64 64 63 33 35 39 35  |16f2b971addc3595|
00000060  66 15 06 15 b4 f2 c8 f5  0b 15 fa 26 18 c4 0b 78  |f□□□□□□□□□□&□□□x|
00000070  9c a5 56 eb 6e a3 48 16  7e 95 c8 ea 1f 7b 69 7b  |□□V□n□H□~□□□□{i{|
00000080  8b 9b 81 92 5a 5a 30 e0  76 36 c0 38 b1 43 f0 66  |□□□□ZZ0□v6□8□C□f|
00000090  85 ca 50 c6 98 6b 03 b6  03 ad fe 3f ef 30 f3 7c  |□□P□□k□□□□□?□0□||
000000a0  f3 1c 7b 8a 38 13 47 ab  bd 48 2b cb 12 e7 5a e7  |□□{□8□G□□H+□□□Z□|
000000b0  7c df a9 03 df 47 7b 4a  22 5a 8f f0 f7 11 a9 aa  ||□□□□G{J"Z□□□□□□|
000000c0  a0 49 e2 82 b4 c7 9a 8e  f0 88 9b 62 4b c2 a2 84  |□I□□□□□□□□□bK□□□|
000000d0  91 86 65 84 67 32 96 66  58 55 b1 2a 61 53 c0 c2  |□□e□g2□fXU□*aS□□|
000000e0  f0 60 59 58 30 b0 3a c3  92 34 fa fc 96 21 68 f6  |□`YX0□:□□4□□□!h□|
000000f0  84 83 04 33 15 2b 3c 9e  6a 98 93 31 07 09 74 8c  |□□□3□+<□j□□1□→t□|
00000100  54 6c 5a 78 aa 60 8b c7  02 c2 9a 84 0d 1e ab 1c  |TlZx□`□□□□□□¤□□□|
00000110  9e 19 58 90 31 af 31 ab  a4 60 61 fa 31 19 e4 ea  |□□X□1□1□□`a□1□□□|
00000120  fc db 6f d6 8b 71 37 a3  6a a9 1c 66 19 aa be 3a  |□□o□□q7□j□□f□□□:|
00000130  4e 57 9f 3c c3 ff 72 71  3e d1 ba 49 ca 02 9c f9  |NW□<□□rq>□□I□□□□|
00000140  09 9a 88 a0 bd 68 82 b0  8c 86 86 10 e8 92 28 8f  |→□□□□h□□□□□□□□(□|
00000150  24 10 d4 9d aa 44 b2 2c  84 28 42 9c c4 87 22 17  |$□□□□D□,□(B□□□"□|
00000160  71 8a 24 8a 5b 5e e1 49  c8 a2 c3 ea 08 7e da bd  |q□$□[^□I□□□□□~□□|
00000170  7d 92 6f 7e aa cb 90 36  4d 59 df d4 f4 74 83 6e  |}□o~□□□6MY□□□t□n|
00000180  fe 70 92 b3 3f 82 4f 1e  86 79 11 82 1b 3c 47 f4  |□p□□?□O□□y□□□<G□|
00000190  94 84 34 68 bb 8a 1d f6  d3 be 2c 28 68 2b 12 a6  |□□4h□□□□□□,(h+□□|
000001a0  24 a6 41 41 72 a6 0e cb  7c 72 26 45 dc 1d a9 3a  |$□AAr□□□|r&E□□□:|
000001b0  a9 98 4f 96 9c 28 62 e8  35 51 fa 16 ac 15 51 5d  |□□O□□(b□5Q□□□□Q]|
000001c0  26 d1 7b 52 78 c6 23 45  c1 a1 8a 23 84 e9 0e 53  |&□{Rx□#E□□□#□□□S|
000001d0  c0 ed ca 9e 43 87 19 b8  38 f4 e5 d8 dc 48 ef 86  |□□□□C□□□8□□□□H□□|
000001e0  6d 49 6a 16 bb 27 79 4e  6b 46 f6 95 ad 26 05 b3  |mIj□□'yNkF□□□&□□|
000001f0  c5 65 19 67 f4 2a 19 29  8e 6d c2 ca e5 44 19 a9  |□e□g□*□)□m□□□D□□|
00000200  53 99 17 64 84 d0 07 fb  8e 84 6c 4c 60 70 46 77  |S□□d□□□□□□lL`pFw|
00000210  73 f3 63 ec 50 ac ed ea  02 77 65 b8 f4 ff a1 8e  |s□c□P□□□□we□□□□□|
00000220  b2 b9 22 6d 0a a4 71 83  f2 03 00 35 6d ca 0c ca  |□□"m¶□q□□□□5m□□□|
00000230  19 7c 38 59 9e fe 89 43  0a 1a a0 ff 37 90 b0 d2  |□|8Y□□□C¶□□□7□□□|
00000240  7b 06 3e 56 80 c4 f2 58  b4 75 c7 a6 d1 01 5b 06  |{□>V□□□X□u□□□□[□|
00000250  d0 1f 81 0e 90 fb 3d e3  98 d4 75 32 74 c1 2a 4d  |□□□□□□=□□□u2t□*M|
00000260  9a 2a 23 dd 5b a9 bf fd  fa cb 6f bf fe cc 86 2b  |□*#□[□□□□□o□□□□+|
00000270  64 dc 83 e6 9c ec 12 96  a4 0c 49 16 24 15 2b 48  |d□□□□□□□□□I□$□+H|
00000280  e5 27 dc 54 99 70 13 19  0c 05 6d cf 65 fd c6 22  |□'□T□p□□□□m□e□□"|
00000290  62 a7 e7 ac 43 36 6e e0  c2 aa 66 9a df cd c0 da  |b□□□C6n□□□f□□□□□|
000002a0  31 63 47 91 3e 29 c3 61  8c 93 20 a3 27 46 25 2f  |1cG□>)□a□□␣□'F%/|
000002b0  c0 44 c0 b1 6c 7e 07 40  65 4a 15 c4 ab bb 71 24  |□D□□l~□@eJ□□□□q$|
000002c0  88 bb b1 28 70 68 bc e5  85 68 2c 2b 1c 11 a6 a1  |□□□(ph□□□h,+□□□□|
000002d0  22 aa e1 96 c1 47 92 28  a8 e9 b7 63 52 d3 28 78  |"□□□□G□(□□□cR□(x|
000002e0  a5 91 35 d7 1c 87 2e 76  c7 6c b0 d2 a6 85 8e b8  |□□5□□□.v□l□□□□□□|
000002f0  cf a3 1d 49 32 1a 5d e9  10 c3 fc db 25 92 e3 25  |□□□I2□]□□□□□%□□%|
00000300  06 e2 9e 14 c5 30 5f e7  2e 38 1c fb 24 08 9b 40  |□□□□□0_□.8□□$□□@|
00000310  0a b8 d7 8b 97 52 06 af  b4 13 09 a7 22 8e e3 55  |¶□□□□R□□□□→□"□□U|
00000320  85 8b 84 90 08 88 c8 0a  22 e0 73 ae c1 8b d6 6f  |□□□□□□□¶"□s□□□□o|
00000330  c3 0d 0b 06 46 fe 4a ff  3e 03 8c 3d 52 c7 b4 7d  |□¤□□F□J□>□□=R□□}|
00000340  88 d2 47 86 1b 2f 43 35  55 13 54 0c c3 a2 1c c8  |□□G□□/C5U□T□□□□□|
00000350  c8 ae a5 dd b5 94 e4 55  9d 14 2d 88 f3 b3 f6 a8  |□□□□□□□U□□-□□□□□|
00000360  ed e3 d8 e9 e3 de f7 7c  d1 35 b2 74 63 98 9d cf  |□□□□□□□|□5□tc□□□|
00000370  fb 82 c3 2f 38 bf 4f 39  7b ee f7 ae a1 09 be 67  |□□□/8□O9{□□□□→□g|
00000380  1d c0 47 7b 2e 5e 57 46  9b 30 7a 7f 27 89 5d cb  |□□G{.^WF□0z□'□]□|
00000390  f7 0a df 78 ac ea f2 c2  2c c8 83 e6 53 c5 3a 01  |□¶□x□□□□,□□□S□:□|
000003a0  c5 20 1c a3 20 62 7b 8b  47 3c 1a 23 75 7c d9 3d  |□␣□□␣b{□G<□#u|□=|
000003b0  41 5b c3 3e 48 8a 78 a8  91 d8 fa d3 23 da cc b3  |A[□>H□x□□□□□#□□□|
000003c0  74 ae ef 7d db 6b 0f db  47 c7 b0 d3 ec fc b0 be  |t□□}□k□□G□□□□□□□|
000003d0  d7 1f be ea 6e 84 cc 17  ef a9 aa d6 c6 c2 7b fe  |□□□□n□□□□□□□□□{□|
000003e0  cb d1 55 cf be 14 59 cb  85 a6 43 d0 26 37 fd 5b  |□□U□□□Y□□□C□&7□[|
000003f0  43 43 ee 7c d1 3d 17 f6  2a 4b ef 56 76 07 52 eb  |CC□|□=□□*K□Vv□R□|
00000400  18 cb b3 3b e3 f6 fe 2a  e6 ee 56 61 ef 18 9b c4  |□□□;□□□*□□Va□□□□|
00000410  5f 2d 04 07 ec f6 cb 56  93 ee 04 fd 90 a1 47 2d  |_-□□□□□V□□□□□□G-|
00000420  d6 e6 21 ff d8 11 cf 6a  e6 ba 76 76 57 a1 e4 1a  |□□!□□□□j□□vvW□□□|
00000430  4b e1 b9 70 0e 7a 6e 7b  6b e4 ac d6 c8 6a 8c f4  |K□□p□zn{k□□□□j□□|
00000440  14 ce dd a7 fb f5 4c d3  1e ab cd 9c 4b 9d fb 78  |□□□□□□L□□□□□K□□x|
00000450  e7 7a be e4 ce 97 82 d3  3b 07 7b be 3c db ab 75  |□z□□□□□□;□{□<□□u|
00000460  e7 f7 cb 17 00 5a 74 56  4b e4 1f 16 a2 9d 5b 07  |□□□□□ZtVK□□□□□[□|
00000470  c8 a6 6f d7 57 67 fe cd  f7 a4 34 cc d5 6a 63 c1  |□□o□Wg□□□□4□□jc□|
00000480  5f 8f 97 9b 7c 71 76 0d  1b f9 b9 93 38 2b ed ec  |_□□□|qv¤□□□□8+□□|
00000490  f0 cb ce bd ff 10 63 6c  81 a6 b9 6e 8a cf 85 6b  |□□□□□□cl□□□n□□□k|
000004a0  54 07 77 55 a5 b6 51 65  9b 43 95 d9 87 52 da e8  |T□wU□□Qe□C□□□R□□|
000004b0  e4 e1 ca 7b b3 d5 63 2b  7a ba 4f 89 b7 2c e7 56  |□□□{□□c+z□O□□,□V|
000004c0  fc 42 78 a7 5d 23 bb 7b  78 d2 6f ef 4d 6b 11 9a  |□Bx□]#□{x□o□Mk□□|
000004d0  92 b0 5c 59 9b e7 82 e6  d9 d2 de 6f ff 2c ca 43  |□□\Y□□□□□□□o□,□C|
000004e0  b4 36 d7 9c d6 f7 ec d2  5c c5 a2 9b db 92 9b 03  |□6□□□□□□\□□□□□□□|
000004f0  96 f9 63 ee e6 eb ce 3d  64 a9 55 dd bd a2 b1 d4  |□□c□□□□=d□U□□□□□|
00000500  fc 0b 0b e5 ff c5 02 9c  b8 e9 37 4f b7 95 ef 9d  |□□□□□□□□□□7O□□□□|
00000510  4b d3 d0 24 a7 4f 45 c7  08 79 c8 36 f7 5f 36 ab  |K□□$□OE□□y□6□_6□|
00000520  25 07 68 7a 67 f7 61 60  5f 83 ce 88 77 df 6e 8c  |%□hzg□a`_□□□w□n□|
00000530  75 f9 b5 cf 72 77 b5 4f  9d 3e ec fd 5e 07 44 4c  |u□□□rw□O□>□□^□DL|
00000540  ce ce 6d 64 7b cb 17 d7  00 f6 a0 26 d7 b8 dd 03  |□□md{□□□□□□&□□□□|
00000550  2b de 73 c1 bd 67 f8 c8  c0 ec bf 32 a0 69 da 97  |+□s□□g□□□□□2□i□□|
00000560  2f 70 41 7e c0 95 2b 48  d6 c1 1d 69 d8 37 03 4d  |/pA~□□+H□□□i□7□M|
00000570  4f 23 fc f7 ef 23 59 30  55 61 c6 0b 96 69 9a a2  |O#□□□#Y0Ua□□□i□□|
00000580  c8 0b aa 69 0a 96 61 29  82 a2 0a 8a 24 48 83 d3  |□□□i¶□a)□□¶□$H□□|
00000590  b0 c6 ee c8 b1 08 f7 70  73 e0 aa b3 0d 24 a9 f0  |□□□□□□□ps□□□¤$□□|
000005a0  82 91 24 51 98 4e a5 cf  ef d6 d7 85 fc ba 8e aa  |□□$Q□N□□□□□□□□□□|
000005b0  e2 3f bd 38 7f 7c be 64  fe f4 29 28 8b b5 4d 8b  |□?□8□|□d□□)(□□M□|
000005c0  d8 2c 5a 5a 5b 65 4d e3  1a d6 7f f4 2f 47 c9 b2  |□,ZZ[eM□□□□□/G□□|
000005d0  c2 16 09 ac a1 a4 ed 9c  f7 17 f3 fe 48 0e c9 7b  |□□→□□□□□□□□□H□□{|
000005e0  f2 c9 9b cb e4 ad 2c ed  a2 f8 ab ba 55 54 79 bb  |□□□□□□,□□□□□UTy□|
000005f0  63 77 ba b1 49 52 5c be  0f 86 8d 5a 91 a4 5e af  |cw□□IR\□□□□Z□□^□|
00000600  17 06 24 8d 24 91 23 f2  56 18 cb 80 c9 58 a4 e2  |□□$□$□#□V□□□□X□□|
00000610  74 4c 76 9c 3a 0e f9 2d  91 c5 90 57 61 47 b2 65  |tLv□:□□-□□□WaG□e|
00000620  c2 ea e7 25 5e e5 ff d7  9e ff 01 bf 1f ff 04 e4  |□□□%^□□□□□□□□□□□|
00000630  12 0e e2 18 40 30 64 30  30 36 34 35 61 33 61 33  |□□□□@0d00645a3a3|
00000640  31 66 37 66 65 30 30 30  37 30 32 62 34 64 39 64  |1f7fe000702b4d9d|
00000650  39 61 33 62 65 38 36 37  32 66 35 65 31 30 65 65  |9a3be8672f5e10ee|
00000660  31 36 32 38 31 61 65 32  62 63 34 31 61 61 63 63  |16281ae2bc41aacc|
00000670  33 30 30 30 30 18 20 62  61 37 39 64 39 39 66 64  |30000□␣ba79d99fd|
00000680  39 37 34 35 35 32 61 63  32 66 34 32 31 36 31 35  |974552ac2f421615|
00000690  38 38 62 31 63 32 35 15  00 00                    |88b1c25□□□|
0000069a

java.lang.Exception
	at com.umeng.commonsdk.framework.UMFrUtils.saveEnvelopeFile(Native Method)
	at com.umeng.commonsdk.statistics.b.a(EnvelopeManager.java:818)
	at com.umeng.commonsdk.statistics.b.a(EnvelopeManager.java:334)
	at com.umeng.commonsdk.framework.UMEnvelopeBuild.buildEnvelopeWithExtHeader(UMEnvelopeBuild.java:245)
	at com.umeng.commonsdk.framework.UMEnvelopeBuild.buildEnvelopeWithExtHeader(Native Method)
	at com.umeng.analytics.pro.m.i(CoreProtocolImpl.java:474)
	at com.umeng.analytics.pro.m.a(CoreProtocolImpl.java:410)
	at com.umeng.analytics.pro.m.c(CoreProtocolImpl.java:167)
	at com.umeng.analytics.pro.m.a(CoreProtocolImpl.java:310)
	at com.umeng.analytics.CoreProtocol.workEvent(CoreProtocol.java:38)
	at com.umeng.commonsdk.framework.UMWorkDispatch.handleEvent(UMWorkDispatch.java:239)
	at com.umeng.commonsdk.framework.UMWorkDispatch.access$000(UMWorkDispatch.java:21)
	at com.umeng.commonsdk.framework.UMWorkDispatch$1.handleMessage(UMWorkDispatch.java:192)
	at android.os.Handler.dispatchMessage(Handler.java:102)
	at android.os.Looper.loop(Looper.java:148)
	at android.os.HandlerThread.run(HandlerThread.java:61)
	at de.robv.android.xposed.XposedBridge.invokeOriginalMethodNative(Native Method)
	at de.robv.android.xposed.XposedBridge.handleHookedMethod(XposedBridge.java:360)
	at android.os.HandlerThread.run(<Xposed>)

result: 0
result: {
  "header": {
    "app_signature": "16:F5:45:0A:70:C7:5C:99:95:E3:39:95:FF:3D:9C:55",
    "app_sig_sha1": "C9:82:6A:17:10:CB:09:EF:68:F2:30:A5:D2:91:CD:37:2A:EF:58:36",
    "app_sig_sha": "yYJqFxDLCe9o8jCl0pHNNyrvWDY=",
    "app_version": "2.0.4",
    "version_code": "10",
    "idmd5": "9f98d773c0d0152c41d18544b282ac4",
    "cpu": "ARMv7 Processor rev 0 (v7l)",
    "mccmnc": "",
    "device_type": "Phone",
    "package_name": "com.wangyue9.phonelive05",
    "sdk_type": "Android",
    "device_id": "88:c9:d0:ef:e2:9d",
    "device_model": "Nexus 5",
    "device_board": "hammerhead",
    "device_brand": "google",
    "device_manutime": 1470967237000,
    "device_manufacturer": "LGE",
    "device_manuid": "MOB31E",
    "device_name": "hammerhead",
    "os_version": "6.0.1",
    "os": "Android",
    "resolution": "1776*1080",
    "mc": "88:c9:d0:ef:e2:9d",
    "timezone": 8,
    "country": "CN",
    "language": "zh",
    "carrier": "",
    "display_name": "望月",
    "access": "wifi",
    "local_ip": "192.168.1.7",
    "network_type": 0,
    "com_ver": "9.1.0",
    "com_type": 0,
    "module": "azioc",
    "api_level": 23,
    "session_id": "7ee8029f-d34f-4310-b23d-781a36c849cb",
    "oaid_required_time": "",
    "successful_requests": 1,
    "failed_requests": 0,
    "req_time": 1258,
    "channel": "wy_juzi_cs_5_1",
    "appkey": "5f4a190112981d3ca30a780a",
    "wrapper_type": "native",
    "wrapper_version": "",
    "targetSdkVer": 27,
    "rps_pr": "no",
    "acl_pr": "no",
    "afl_pr": "no",
    "imprint": "GwAVAhggNzgzYWY4ODlkZDEyY2Y3N2I1Yzk1MGYzODA3YWFjYWYA\n",
    "vertical_type": 0,
    "sdk_version": "9.1.0",
    "pro_ver": "1.0.0",
    "$pr_ve": "0",
    "$ud_da": "2020-09-10",
    "id_tracking": "GwaMBXV0ZGlkGBhYMWtjbVNDMklwSURBSHBOd0ExWXppUDIW\/uO9wY5dFQIABGlkZmEYJDA0OGIy\nMTlkLTMyOGItNDQwOC1hYTg1LTczNDZiYTI3NTMyMxbA5L3Bjl0VAgAGc2VyaWFsGBAwOTc5ODQ3\nNjBmMWU0NTU0FsDkvcGOXRUCAAVpZG1kNRgfOWY5OGQ3NzNjMGQwMTUyYzQxZDE4NTQ0YjI4MmFj\nNBbU5L3Bjl0VAgAKYW5kcm9pZF9pZBgQZmIwODM0YmNiNTAwN2QyORbU5L3Bjl0VAgADbWFjGBE4\nODpjOTpkMDplZjplMjo5ZBaS5L3Bjl0VAgAZbBgFdXRkaWQoGFgxa2NtU0MySXBJREFIcE53QTFZ\nemlQMhb+473Bjl0AGANtYWMoETg4OmM5OmQwOmVmOmUyOjlkFpLkvcGOXQAYBGlkZmEoJDA0OGIy\nMTlkLTMyOGItNDQwOC1hYTg1LTczNDZiYTI3NTMyMxbA5L3Bjl0AGAZzZXJpYWwoEDA5Nzk4NDc2\nMGYxZTQ1NTQWwOS9wY5dABgFaWRtZDUoHzlmOThkNzczYzBkMDE1MmM0MWQxODU0NGIyODJhYzQW\n1OS9wY5dABgKYW5kcm9pZF9pZCgQZmIwODM0YmNiNTAwN2QyORbU5L3Bjl0AAA==\n"
  },
  "analytics": {
    "ekv": [
      {
        "73E93C23FEEE44239EE3FDF838938535": [
          {
            "id": "Launcher",
            "ts": 1599675543665,
            "Launcher": "",
            "ds": 0,
            "pn": "com.wangyue9.phonelive05"
          },
          {
            "id": "$$_onUMengEnterForeground",
            "ts": 1599675543778,
            "activityName": "com.huaji.phonelive.activity.LauncherActivity@9b897bf",
            "isMainProcess": 1,
            "pairUUID": "d541a7b3-7423-4e46-af19-c2ba74c290a7",
            "pid": 25292,
            "ds": 0,
            "pn": "com.wangyue9.phonelive05"
          }
        ]
      }
    ]
  }
}
```
