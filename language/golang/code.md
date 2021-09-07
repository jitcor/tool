# 子struct强制转成父struct
```go
func ToPeer(object interface{}) (peer *Peer, err error) {
	return (*Peer)(unsafe.Pointer(reflect.ValueOf(object).FieldByName("Peer").Pointer())),nil
}
```
