# java random
```go
package main

import (
	"sync/atomic"
)

const multiplier = int64(0x5DEECE66D)
const addend = int64(0xB)
const mask = int64((1 << 48) - 1)

type JRandom struct {
	seed *atomic.Value
}

func NewJRandom(seed int64) *JRandom {
	ptr := &JRandom{}
	ptr.seed = new(atomic.Value)
	ptr.seed.Store(ptr.initialScramble(seed))
	return ptr
}
func (that *JRandom) NextInt(bound int32) int32 {
	r := that.next(31)
	m := bound - 1
	if bound&m == 0 {
		r = (bound * r) >> 31
	} else {
		for u := r; ; {
			r = u % bound
			if u-r+m < 0 {
				u = that.next(31)
			} else {
				break
			}
		}
	}
	return r
}
func (that *JRandom) NextLong() int64 {
	return (int64(that.next(32)) << 32) + int64(that.next(32))
}
func (that *JRandom) initialScramble(seed int64) int64 {
	return (seed ^ multiplier) & mask
}
func (that *JRandom) next(bits int32) int32 {
	oldSeed := int64(0)
	nextSeed := int64(0)
	for {
		oldSeed = that.seed.Load().(int64)
		nextSeed = (oldSeed*multiplier + addend) & mask
		if that.seed.CompareAndSwap(oldSeed, nextSeed) {
			break
		}
	}
	return int32(nextSeed >> (48 - bits))
}

```
# java hashcode
```go
func _JavaHashCode(text string) int32 {
	l:= len(text)
	h:=int32(0)
	if l>0{
		for i:=0;i<l;i++{
			h=31*h+int32(text[i])
		}
	}
	return h
}

```
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
# 排列与组合
- https://github.com/kokardy/listing
- gonum.org/v1/gonum/stat/combin
