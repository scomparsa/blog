---
title: 人脸识别
date: 2017-08-11 09:35:12
tags:
  - research
  - canvas
---

最近有个业务需要做人脸识别，并且把脸型扣出来融合到另一个提前准备好的图片模板里。类似前
段时间微信的【穿上军装】H5 应用。之前还真没有接触过类似的项目，于是开始了探索之路。。。

## 人脸识别
这是遇到的第一个难点，怎样识别出用户上传的照片中必须包含人脸。查了相关资料，找到一个免费
提供人脸识别的 Library (OpenCV)[http://opencv.org/]，开始搞起。

> 开发环境为 Mac 系统

### 安装 OpenCV Library
```shell
brew tap homebrew/science # 使用这个命令增加扩展源
brew install opencv
```

### 安装 OpenCV Node Bindings
```javascript
npm i opencv --save
```

### 检测
有一个用于 (Viola-Jones Haar Cascade)[http://www.cognotics.com/opencv/servo_2007_series/part_2/sidebar.html] 对象检测的快捷方法可用于脸部检测。*为了便于记忆，OpenCV 帮我们定义了一系列 cascade 来识别面部，这里我们使用 `cv.FACE_CASCADE`*

```javascript
// 读取一张包含人脸的图片
cv.readImage('./face.jpg', (err, im) => {
  const [width, height] = im.size()

  // 开始进行人脸识别
  im.detectObject(cv.FACE_CASCADE, {}, (err, faces) => {
    if (!faces.length) {
      return console.log('没有检测到人脸')
    }
    ...
  })
})
```

现在，我们已经检测出图片中是否包含人脸及人脸的数量，使用 `canvas` 保存人脸区域的图片。

```javascript
const img = new Image()
const ctx = canvas.getContext('2d')
ctx.drawImage(img, 0, 0, width, height)
ctx.globalCompositeOperation = 'source-over'

console.log('Image saved to ./tmp/take-face-pics.jpg');
```
