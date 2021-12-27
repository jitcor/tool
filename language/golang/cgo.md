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
# 参考
- [CGO学习整理](https://packagewjx.github.io/2018/12/13/cgo-note/)
