## nodejs安装和更新

直接官网下载安装包即可

## npm更新

```
npm install -g npm
```

## 切换到官方仓库镜像

```
npm config set registry https://registry.npmjs.org/
```
OR 淘宝镜像
```
npm config set registry https://registry.npm.taobao.org/
```



## 清除npm缓存

```
npm cache clean -f
```

## 注册

```
npm adduser
```

## 登录

```
npm login
```

## 导出函数

```ts
export function add(a:number,b:number){
    return a+b;
}
export function sub(a:number,b:number){
    return a-b;
}
```



## 发布

```
npm publish
```



## 导入函数

```ts
import {add} from "moduleName";
```

