## 导出函数
```c
#define DLLEXPORT __declspec(dllexport)
 
#ifdef __cplusplus
extern "C" {
#endif
 
DLLEXPORT void test();
 
#ifdef __cplusplus
}
#endif
```
