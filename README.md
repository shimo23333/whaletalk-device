# Whaletalk Device 裝置端程式碼
使用 Raspberry PI Zero 2 + MAX98357A 控制喇叭，接收 API 的播放列表來即時播放錄音、使用 500歐姆可變電阻調整聲音大小。

## 一、建立裝置
### 1. 安裝 Raspberry Pi OS (Debian)
使用 Raspberry Pi Imager 將標準的 Raspberry Pi OS 燒錄進 SD 卡中。[官方教學](https://www.raspberrypi.com/documentation/computers/getting-started.html#installing-the-operating-system)

進階設定：
1. 開啟 SSH
1. 設定 WIFI 密碼
1. 預設使用者帳號：shimo/shimo

### 2.（進桌面設定 WIFI) 
1. 裝回 SD 卡、接上電源、滑鼠後自動開機
1. 進桌面後，從右上角設定 WIFI 連線
### 3. 取消開機自動進桌面
1. 開啟選單 / Preferences / Raspberry Pi Configuration
1. System / Boot 選擇為 to CLI
1. Interfaces / SSH 開啟
1. 按下 OK
1. 重新開機

下次開機就會停留在指令畫面，以後要進桌面時，輸入下方指令即可：
```
startx
```
## 二、觀看 Raspberry Pi 的內網 IP
重開後輸入指令：
```
ip a
```

## 三、用電腦連線遠端
### Windows 使用 Putty 連線
1. 開啟 Putty
1. Host/Name 輸入：172.20.10.5 (內網IP)
1. 按下 Open 進入
1. 進入後輸入帳號、密碼

最後有出現 ***shimo@raspberrypi: ~ $*** 就是成功進入。

## 四、檔案指令操作

### 一般檔案操作
|指令|操作|
|---|---|
|ls|列出目前資料夾內容（橫式）|
|cd <資料夾名稱>|進入資料夾|
|cd ..|回到上一層資料夾|
|cd ~|直接回到使用者資料夾|
|cat <檔案名稱>|預覽文字檔|
|python <檔案名稱>|執行 .py 的程式|

### Git 操作
|指令|操作|
|---|---|
|git clone <github專案連結>|第一次將github專案抓下來|
|git pull|抓下來最新的版本(要先進到專案資料夾內)|