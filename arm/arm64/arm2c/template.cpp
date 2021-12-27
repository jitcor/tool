

#include <iostream>

#define _CHAR  int8_t
#define _BYTE  uint8_t
#define _WORD  uint16_t
#define _DWORD uint32_t
#define _QWORD uint64_t
#define _OWORD __int128
#if !defined(_MSC_VER)
#define _LONGLONG __int128
#endif


uint32_t wzr = 0;
uint64_t xzr = 0;
uint64_t x0 = 0, x1 = 0, x2 = 0, x3 = 0, x4 = 0, x5 = 0, x6 = 0, x7 = 0, x8 = 0, x9 = 0, x10 = 0, x11 = 0, x12 = 0, x13 = 0, x14 = 0, x15 = 0, x16 = 0, x17 = 0, x18 = 0, x19 = 0, x20 = 0, x21 = 0, x22 = 0, x23 = 0, x24 = 0, x25 = 0, x26 = 0, x27 = 0, x28 = 0, x29 = 0, x30 = 0, x31 = 0;
_OWORD q0 = 0;

// 初始化堆栈
uint64_t sp_init() {
    
    void *_sp = calloc(1, 60000);
    uint64_t sp = (uint64_t)((char *)_sp+30000);
    x29 = sp;
    memset(_sp, 0xff, 40000);
    return sp;
}

uint64_t sp = sp_init();

#define w0 *(uint32_t *)&x0
#define w1 *(uint32_t *)&x1
#define w2 *(uint32_t *)&x2
#define w3 *(uint32_t *)&x3
#define w4 *(uint32_t *)&x4
#define w5 *(uint32_t *)&x5
#define w6 *(uint32_t *)&x6
#define w7 *(uint32_t *)&x7
#define w8 *(uint32_t *)&x8
#define w9 *(uint32_t *)&x9
#define w10 *(uint32_t *)&x10
#define w11 *(uint32_t *)&x11
#define w12 *(uint32_t *)&x12
#define w13 *(uint32_t *)&x13
#define w14 *(uint32_t *)&x14
#define w15 *(uint32_t *)&x15
#define w16 *(uint32_t *)&x16
#define w17 *(uint32_t *)&x17
#define w18 *(uint32_t *)&x18
#define w19 *(uint32_t *)&x19
#define w20 *(uint32_t *)&x20
#define w21 *(uint32_t *)&x21
#define w22 *(uint32_t *)&x22
#define w23 *(uint32_t *)&x23
#define w24 *(uint32_t *)&x24
#define w25 *(uint32_t *)&x25
#define w26 *(uint32_t *)&x26
#define w27 *(uint32_t *)&x27
#define w28 *(uint32_t *)&x28
#define w29 *(uint32_t *)&x29
#define w30 *(uint32_t *)&x30
#define w31 *(uint32_t *)&x31

//your code
