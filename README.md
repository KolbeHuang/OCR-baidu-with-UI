# OCR-baidu-with-UI

## Functions of important files / 文件功能
OCR_baidu.py: <br>
&nbsp;&nbsp;&nbsp;&nbsp;This file contains the essential code to use baidu SDK to realize OCR of Chinese and English characters. <br>
&nbsp;&nbsp;&nbsp;&nbsp;此文件包含了应用百度SDK进行中英文的OCR的代码（函数）。<br>
UI.py: <br> 
&nbsp;&nbsp;&nbsp;&nbsp;This file contains the code for creating a simple graphic user interface to select the image for recognition and display the results. <br>
&nbsp;&nbsp;&nbsp;&nbsp;此文件主要包含了应用tkinter来制作一个简易的OCR识别的界面的代码，以选择识别的图片并展示识别结果。<br>

## To run the code / 运行程序
### Use the OCR with baidu SDK
1. In the commandline, install baidu-aip by "pip install baidu-aip".
2. Run the UI.py by "python3 UI.py".
3. Choose the mode that you would like to recognize an image (depends on the needs and images).
4. On the menu bar, select "File" and then "Open" to pick the image for OCR.
5. Click "识别 recognize" on the bottom right and the result text will show in the center text box.

Tips: You are free to use your own baidu ID and keys to run the recognition by changing the default information in the UI. <br>

Currently this UI does not support any error reports and copy and paste by right click. Please use ctrl+c and ctrl+v to copy the recognized results onto the text box. Further development will try to improve and solve these problems.

### 使用百度SDK支持的OCR程序
1. 在命令行中，输入"pip install baidu-aip" 以安装SDK。
2. 输入"python3 UI.py"以运行程序。
3. 选择所需要的识别模式（根据需求以及所识别的图像）
4. 在UI界面的菜单栏中，选择“File”下的“Open”，找到并点击需要识别的图片。
5. 点击右下角的 "识别 recognize" 按钮，识别结果会显示在界面正中的文本框中。

附：如果可以，请使用自己的百度账号以及私钥进行OCR程序的识别（可以在UI界面中更改）。 <br>

目前此UI界面尚不支持报错以及右键的复制粘贴，请使用ctrl+c 和 ctrl+v以复制得到的识别结果。后续更新会尽快解决这些问题。

## Development environment / 开发环境
baidu-aip          2.2.18.0 <br>
pytesseract        0.3.8 <br>
python             3.9.6 <br>
tkinter            8.6

## Upcoming update / 后续更新
The Java version of OCR with baidu SDK is still in development and corresponding Android Studio environment could be updated.
Java版本的百度OCR正在开发当中，相应的Android studio配置也会更新（使OCR也可以在手机上运行）。

## UI demo
