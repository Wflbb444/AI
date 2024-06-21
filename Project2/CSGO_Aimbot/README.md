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

### 1.Pytorch

1.以1920x1080的分辨率运行CS2，并在游戏内的`视频设置`/`视频`/`显示模式`中选择`窗口`选项。

2.接着在`Anaconda Prompt`中运行以下命令：
```
python main.py
```
启动后会要求你输入窗口编号，输入游戏窗口的编号。

3.进入游戏，在需要的时候，按下**大写锁定**键开启自动瞄准。这个功能默认是关闭的。

4.需要结束的时候，就在命令行里输入`q`关闭程序。


### 2.Onnx

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
python main.py
```

4.后续步骤同上。

### 3.TensorRT

1.安装[CUDA Toolkit 11.8](https://developer.nvidia.com/cuda-11-8-0-download-archive)

2.安装cupy
```
pip install cupy-cuda11x
```

3.安装[CUDNN](https://developer.nvidia.com/downloads/compute/cudnn/secure/8.9.6/local_installers/11.x/cudnn-windows-x86_64-8.9.6.50_cuda11-archive.zip/)（需要Nvidia账户）

4.安装[`TensorRT 8.6 GA`](https://developer.nvidia.com/downloads/compute/machine-learning/tensorrt/secure/8.6.1/zip/TensorRT-8.6.1.6.Windows10.x86_64.cuda-11.8.zip).

5.将解压后的CUDNN和TensorRT里的文件全都复制到CUDA Toolkit文件夹里，默认路径在`C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8`

6.在Python中安装TensorRT（路径与本地文件存放位置保持一致）
```
   pip install "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\python\tensorrt-8.6.1-cp311-none-win_amd64.whl"
```

7.添加系统环境变量
- `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\lib`
- `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\libnvvp`
- `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\bin`

8.将模型导出为引擎


