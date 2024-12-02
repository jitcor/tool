# 检查配置cgo环境

编译前需要先检测gcc，g++命令在当前环境是否可用，否则运行go build会报一些莫名其妙的问题，函数未定义，没有可供编译的go源码文件，建议采用msys2下mingw64里的gcc，g++命令

# 条件编译

## 文件名方式
//todo 
## 首行注释方式
//todo 
## cgo 后缀方式
```
#cgo windows CXXFLAGS:xxxx
#cgo linux xxxxxxxx
#cgo amd64 xxxxxx
```
# CPP编译
```go
/*
#cgo CXXFLAGS: -std=gnu++14 -v
#include "mixin.h"
#include <stdlib.h>
*/
import "C"

```
> -v打印详细输出信息，用于排查错误
# Window下 cgo 导入iostream报错
`go build -buildmode=exe`
> 参考:https://github.com/golang/go/issues/45468
# 编译dll文件
- api/api.go
```go
package main
/*
#include <stdlib.h>
*/
import "C"

//export func_name
func func_name(outPath *C.char)C.int {
    //pass
}

func main() {
   // Need a main function to make CGO compile package as C shared library
}

```
```cmd
set GOOS=windows&& set GOARCH=amd64&& go build  -ldflags "-s -w"  -buildmode=c-shared -o build/export.dll api/api.go
```
# 注意事项
- go语言编译的dll文件，不能被go调用  
# 参考
- [CGO学习整理](https://packagewjx.github.io/2018/12/13/cgo-note/)
