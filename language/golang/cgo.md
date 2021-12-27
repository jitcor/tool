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
