# 在build debug apk后自动执行一个task
```gradle
apply plugin: 'com.android.application'

android {
    buildTypes {
        debug {
            afterEvaluate {
                packageDebug.finalizedBy(copyDexToDevice)
            }
        }
    }
}


task copyDexToDevice(type: Exec) {
    workingDir './'
    commandLine 'python', 'copy_dex_to_device.py'

}
```
