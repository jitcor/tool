# 子struct强制转成父struct
```go
func ToPeer(object interface{}) (peer *Peer, err error) {
	return (*Peer)(unsafe.Pointer(reflect.ValueOf(object).FieldByName("Peer").Pointer())),nil
}
```
> 这里子struct里的Peer变量需改成指针形式，也就变成`*Peer`
