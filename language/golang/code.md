# 子struct强制转成父struct (GoLand IDE 代码模板)
```go
func To$STR$(object interface{}) (dst *$STR$, err error) {
	defer func() {
		if e := recover(); e != nil {
			err = e.(error)
		}
	}()
	var isStruct=false
	var v reflect.Value
	switch reflect.TypeOf(object).Kind() {
	case reflect.Ptr, reflect.Interface:
		v = reflect.ValueOf(object).Elem().FieldByName("$STR$")
	case reflect.Struct:
		isStruct=true
		v = reflect.ValueOf(object).FieldByName("$STR$")
	default:
		return nil, errors.New("To$STR$: object type error: " + reflect.TypeOf(object).Kind().String())
	}
	switch v.Kind() {
	case reflect.Ptr:
		return (*$STR$)(unsafe.Pointer(v.Pointer())), err
	case reflect.Struct:
		if isStruct{
			return nil, errors.New("To$STR$: At least one of the parent and the child is a pointer")
		}
		return (*$STR$)(unsafe.Pointer(v.Addr().Pointer())), err
	default:
		return nil, errors.New("To$STR$: $STR$ type error: " + v.Kind().String())
	}

}

```
> 这里子struct里的Peer变量需改成指针形式，也就变成`*Peer`
