# 公众号开发
# 后台
### 域名注册
google domains
### 服务器
google cloud
> 服务器区域需要选择台湾，不能选择香港，其不支持域名映射
### 依赖库
https://github.com/silenceper/wechat
### token 验证
```golang

func handlerTokenCheck(w http.ResponseWriter, r *http.Request) {
        r.ParseForm()
        if !validateUrl(w, r) {
                log.Println("Wechat Service: this http request is not from Wechat platform!")
                return
        }
        log.Println("Wechat Service: validateUrl Ok!")
}
func makeSignature(timestamp, nonce string) string {
        sl := []string{TOKEN, timestamp, nonce}
        sort.Strings(sl)
        s := sha1.New()
        io.WriteString(s, strings.Join(sl, ""))
        return fmt.Sprintf("%x", s.Sum(nil))
}

func validateUrl(w http.ResponseWriter, r *http.Request) bool {
        timestamp := strings.Join(r.Form["timestamp"], "")
        nonce := strings.Join(r.Form["nonce"], "")
        signatureGen := makeSignature(timestamp, nonce)

        signatureIn := strings.Join(r.Form["signature"], "")
        if signatureGen != signatureIn {
                return false
        }
        echostr := strings.Join(r.Form["echostr"], "")
        fmt.Fprintf(w, echostr)
        return true
}

```
