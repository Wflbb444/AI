# Project2：CSGO_Aimbot

## 一、项目简介

本项目是基于YOLOv5模型的一款AI自瞄脚本，由于只使用了录屏和鼠标移动的操作，很难被传统反作弊系统检测。本项目仅作为学习用途。

## 二、版本介绍

本项目有三个版本，运行效率依次提升。

- `main.py`：使用pytorch，安装最简单，运行在CPU上。

- `main_onnx.py`：需要修改配置文件。

- `main_tensorrt.py`：使用TensorRT框架进行性能优化，需要Nvidia GPU。


## 三、安装依赖

### 1.Python 3.11

### 2.PyTorch

我采用的方法是在`Anaconda`配置Pytorch环境，步骤参考[这里](https://blog.csdn.net/qq_45057249/article/details/130438318)

配置完成以后，需要以管理员身份打开`Anaconda Prompt`，进入文件夹位置，并切换到pytorch环境：

```
activate pytorch
```
### 3.在命令行里输入：
```
pip install -r requirements.txt
```

## 四、三种运行方式

### Pytorch

1.以1920x1080的分辨率运行CS2，并在游戏内的`视频设置`/`视频`/`显示模式`中选择`窗口`选项。

2.接着在`Anaconda Prompt`中运行以下命令：
```
python main.py
```
启动后会要求你输入窗口编号，输入游戏窗口的编号。

3.进入游戏，在需要的时候，按下**大写锁定**键开启自动瞄准。这个功能默认是关闭的。

4.需要结束的时候，就在命令行里输入`q`关闭程序。


### Onnx

1. 在`config.py` 文件中，根据硬件需求修改`onnxChoice`参数：
    - `onnxChoice = 1` # CPU ONLY
    - `onnxChoice = 2` # AMD/NVIDIA ONLY
    - `onnxChoice = 3` # NVIDIA ONLY 
2. 如果电脑安装了NVIDIA，运行以下命令：
    ```
    pip install onnxruntime-gpu
    pip install cupy-cuda11x
    ```
3.在`Anaconda Prompt`中运行以下命令：
```
python main_onnx.py
```

4.后续步骤同上。

### TensorRT

1.安装[CUDA Toolkit 11.8](https://developer.nvidia.com/cuda-11-8-0-download-archive)

2.安装cupy
```
pip install cupy-cuda11x
```

3.安装[CUDNN](https://developer.nvidia.com/downloads/compute/cudnn/secure/8.9.6/local_installers/11.x/cudnn-windows-x86_64-8.9.6.50_cuda11-archive.zip/)（需要Nvidia账户）

4.安装[TensorRT 8.6 GA](https://developer.nvidia.com/downloads/compute/machine-learning/tensorrt/secure/8.6.1/zip/TensorRT-8.6.1.6.Windows10.x86_64.cuda-11.8.zip).

5.将解压后的CUDNN和TensorRT里的文件全都复制到CUDA Toolkit文件夹里，默认路径在`C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8`

6.在Python中安装TensorRT（路径与本地文件存放位置保持一致）
```
   pip install "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\python\tensorrt-8.6.1-cp311-none-win_amd64.whl"
```

7.添加系统环境变量
- `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\lib`
- `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\libnvvp`
- `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\bin`

8.下载模型并导出为引擎

在[ultralytics官方仓库](https://github.com/ultralytics/yolov5/releases/tag/v7.0)下载预训练好的模型。在本项目中，推荐使用yolov5s.pt和yolov5m.pt模型。
运行以下命令导出模型，可能需要十几分钟的时间：
```
   python .\export.py --weights ./yolov5s.pt --include engine --half --imgsz 320 320 --device 0
```
修改`main_tensorrt.py`的第27行：
```
model = DetectMultiBackend('yolov5s.engine(替换为本地引擎的名字)', device=torch.device(
        'cuda'), dnn=False, data='', fp16=True)
    stride, names, pt = model.stride, model.names, model.pt
```

9.在`Anaconda Prompt`中运行以下命令：
```
python main_tensorrt.py
```
10.后续步骤同上。

## 五、设置选项

修改 `config.py`以适应需要。 

`screenShotHeight/Width` - 只检测屏幕中央320x320分辨率的区域

`cpsDisplay` - cps代表着Corrections per second，监测鼠标移动速度。理想状况下，如果是fps是60帧，cps也是60帧，意味着鼠标每一帧都在移动。设为False时不在终端显示实时cps数据。

`visuals` - 一个320x320的窗口，始终显示在屏幕最前端，用于显示AI图像识别的过程。如果觉得影响游戏体验，可以设为False。

`aaMovementAmp` - 鼠标移动放大器。数值越低越灵敏，推荐0.5-2，虽然视角会有晃动，但更像人在操作。

`confidence` - 置信度阈值，置信度大于这个值时就将物体识别为人并自动瞄准。

## 六、附加

添加了yolov8_live_overlay.py，需要安装pygame库。
仅作为目标检测的展示。
