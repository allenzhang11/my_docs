# FastRTPS 文档 _1.10.0 版_
**eProsima** 

## 目录
|章节|标题|页码|
|---:|---|---:|
|**1**|**需求**|3|
|1.1|通用依赖项|3|
|1.2|Windows 7 32 位和 64 位|3|
|**2**|**从二进制包安装**|5|
|2.1|Windows 7 32 位和 64 位|5|
|2.2|Linux|5|
|**3**|**从源代码安装**|7|
|3.1|依赖项|7|
|3.2|使用 Colcon 安装|7|
|3.3|手动安装|8|
|3.4|Fast-RTPS-gen|8|
|3.5|安全|8|
|**4**|**快速入门**|11|
|4.1|RTPS 协议简介|11|
|4.2|构建第一个应用程序|12|
|**5**|**库概述**|15|
|5.1|Fast RTPS 架构|16|
|**6**|**对象与数据结构**|17|
|6.1|发布者-订阅者模块|17|
|6.2|RTPS 模块|17|
|**7**|**发布者-订阅者层**|19|
|7.1|如何使用发布者-订阅者层|19|
|7.2|配置|21|
|7.3|其他概念|33|
|**8**|**写入者-读取者层**|35|
|8.1|与发布者-订阅者层的关系|35|
|8.2|如何使用写入者-读取者层|35|
|8.3|配置读取者和写入者|37|
|8.4|配置历史缓存|38|
|**9**|**高级功能**|39|
|9.1|话题与键|39|
|9.2|分区|40|
|9.3|进程内投递|43|
|9.4|传输|43|
|9.5|流控制器|57|
|9.6|发送大数据|58|
|9.7|发现|60|
|9.8|订阅发现话题|81|
|9.9|调优|83|
|9.10|其他服务质量选项|84|
|9.11|日志记录|84|
|**10**|**安全**|89|
|10.1|身份验证插件|89|
|10.2|访问控制插件|89|
|10.3|加密插件|90|
|10.4|内置插件|90|
|10.5|示例：配置 Participant|99|
|**11**|**实时行为**|105|
|11.1|调优内存分配|105|
|11.2|非阻塞调用|109|
|**12**|**动态话题类型**|111|
|12.1|概念|111|
|12.2|支持的类型|112|
|12.3|复杂示例|118|
|12.4|序列化|121|
|12.5|重要说明|122|
|12.6|动态类型发现与端点匹配|122|
|12.7|XML 动态类型|124|
|12.8|动态 HelloWorld 示例|124|
|**13**|**持久化**|127|
|13.1|配置|127|
|13.2|内置插件|128|
|**14**|**XML 配置文件**|131|
|14.1|创建 XML|131|
|14.2|库设置|132|
|14.3|传输描述符|133|
|14.4|XML 动态类型|136|
|14.5|Participant 配置|146|
|14.6|Publisher 配置|153|
|14.7|Subscriber 配置|155|
|14.8|通用配置|157|
|14.9|示例|163|
|**15**|**使用 fastrtpsgen 生成代码**|175|
|15.1|输出|175|
|15.2|在哪里找到 _fastrtpsgen_|176|
|**16**|**典型用例**|177|
|16.1|通过 WIFI 使用 Fast-RTPS|177|
|16.2|大规模部署|179|
|16.3|ROS 2 中的 Fast-RTPS|192|
|**17**|**简介**|195|
|17.1|编译|195|
|**18**|**执行与 IDL 定义**|197|
|18.1|构建 publisher/subscriber 代码|197|
|18.2|通过 IDL 定义数据类型|198|
|**19**|**1.10.0 版**|207|
|19.1|以前的版本|208|




![](fast-dds-docs-eprosima-com-en-v1.10.0_images/fast-dds-docs-eprosima-com-en-v1.10.0.pdf-0007-01.png)


_eProsima Fast RTPS_ 是 RTPS（Real Time Publish-Subscribe，实时发布-订阅）协议的 C++ 实现。该协议由对象管理组（Object Management Group，OMG）联盟定义和维护，可通过 UDP 等不可靠传输提供发布者-订阅者通信。RTPS 也是 OMG 为数据分发服务（Data Distribution Service，DDS）标准定义的线协议互操作规范。_eProsima Fast RTPS_ 的优势在于独立且保持更新，因为大多数厂商方案要么把 RTPS 仅作为实现 DDS 的工具，要么沿用规范的旧版本。

该库的部分主要特性如下：

- 可为实时应用配置尽力而为（best-effort）和可靠（reliable）的发布-订阅通信策略。

- 支持即插即用连接，网络中的其他成员能够自动发现任何新应用。

- 具备模块化和可扩展性，能够在网络中持续加入复杂设备和简单设备。

- 网络行为和传输层可配置、可替换：可为每种部署选择最合适的协议与系统输入/输出通道组合。

- 两个 API 层：一个注重易用性的高层 Publisher-Subscriber 层，以及一个可更精细地访问 RTPS 协议内部工作机制的低层 Writer-Reader 层。

eProsima Fast RTPS 已被多个行业的组织采用，其中包括以下重要案例：

- 机器人：ROS（Robotic Operating System，机器人操作系统）将其作为 ROS2 的默认中间件。

- 欧盟研发：FIWARE 孵化的 GE。

本文档分为以下部分：

- _安装手册_

- _用户手册_

- _FastRTPSGen 手册_

- _发行说明_

# 第 1 章：需求
_eProsima Fast RTPS_ 需要以下软件包才能正常工作。

## 1.1 通用依赖项
### 1.1.1 Gtest
从源代码构建时，需要使用 Gtest 编译测试。

### 1.1.2 Java & Gradle
使用内置代码生成工具 _fastrtpsgen_ 时需要 Java 和 Gradle（参见 _编译_）。

## 1.2 Windows 7 32 位和 64 位
### 1.2.1 Visual C++ 2015 或 2017 可再发行组件包
_eProsima Fast RTPS_ 需要与安装或编译期间所选 Visual Studio 版本对应的 Visual C++ 可再发行组件包。安装程序会提供下载并安装这些组件的选项。

# 第 2 章：从二进制包安装
你可以随时从公司网站下载 _eProsima Fast RTPS_ 的最新二进制发行版。

## 2.1 Windows 7 32 位和 64 位
运行安装程序并按照提示操作，在出现提示时选择所需的 Visual Studio 版本和体系结构。

### 2.1.1 环境变量
_eProsima Fast RTPS_ 需要按以下方式设置环境变量才能正常工作：

- FASTRTPSHOME：安装 _eProsima Fast RTPS_ 的根文件夹。

- PATH 的追加项：应将 /bin 文件夹以及所选 Visual Studio 版本对应的子文件夹追加到 PATH。

在安装过程中勾选相应复选框即可自动设置这些变量。

## 2.2 Linux
解压软件包内容。该包同时包含 _eProsima Fast RTPS_ 及其所需软件包 _eProsima Fast CDR_。你需要对这两个软件包执行相同步骤，并先从 _Fast CDR_ 开始。

配置编译：

$ ./configure --libdir=/usr/lib 

如果需要编译并包含调试符号（这也会启用详细模式）：

$ ./configure CXXFLAGS="-g -D__DEBUG" --libdir=/usr/lib 

配置项目后，编译并安装该库：

$ sudo make install 

# 第 3 章：从源代码安装
## 3.1 依赖项
### 3.1.1 Asio 和 TinyXML2 库
在 Linux 上，可以使用 Linux 发行版的包管理器安装这些库。例如，在 Ubuntu 上可使用其包管理器执行以下命令安装。

```bash
sudo apt install libasio-dev libtinyxml2-dev
```

在 Windows 上，可以使用 Chocolatey 安装这些库。首先从该 ROS2 Github 仓库下载以下 Chocolatey 软件包。

- asio.1.12.1.nupkg 

- tinyxml2.6.0.0.nupkg 

下载这些软件包后，打开管理员 shell 并执行以下命令：

```powershell
choco install -y -s <PATH\TO\DOWNLOADS\> asio tinyxml2
```

请将 `<PATH\TO\DOWNLOADS>` 替换为下载软件包的文件夹。

## 3.2 使用 Colcon 安装
colcon 是用于构建软件包集合的命令行工具。本节说明如何使用它轻松编译 Fast-RTPS 及其依赖项。首先安装 ROS2 开发工具（colcon 和 vcstool）：

```bash
pip install -U colcon-common-extensions vcstool
```

下载用于获取 Fast RTPS 及其依赖项的 repos 文件：

```bash
wget https://raw.githubusercontent.com/eProsima/Fast-RTPS/master/fastrtps.repos
mkdir src
vcs import src < fastrtps.repos
```

最后，使用 colcon 编译所有软件：

```bash
colcon build
```

## 3.3 手动安装
手动编译 Fast RTPS 之前，需要克隆以下依赖项并使用 CMake 编译它们。

- Fast CDR 

  ```bash
  git clone https://github.com/eProsima/Fast-CDR.git
  mkdir Fast-CDR/build
  cd Fast-CDR/build
  cmake ..
  cmake --build . --target install
  ```

- Foonathan memory 

  ```bash
  git clone https://github.com/eProsima/foonathan_memory_vendor.git
  cd foonathan_memory_vendor
  mkdir build
  cd build
  cmake ..
  cmake --build . --target install
  ```

安装所有依赖项后，即可编译并安装 Fast RTPS。

```bash
git clone https://github.com/eProsima/Fast-RTPS.git
mkdir Fast-RTPS/build
cd Fast-RTPS/build
cmake ..
cmake --build . --target install
```

如果需要编译示例，调用 CMake 时需要添加参数 `-DCOMPILE_EXAMPLES=ON`。

如果需要编译性能测试，调用 CMake 时需要添加参数 `-DPERFORMANCE_TESTS=ON`。

有关生成 _fastrtpsgen_ 的说明，请参见 _编译_。

## 3.4 Fast-RTPS-gen
如果需要编译 _fastrtpsgen_ Java 应用程序，需要从 Fast-RPTSGen 仓库下载其源代码，下载时使用 `--recursive` 选项，然后调用 `gradle assemble` 进行编译。更多详细信息请参见 _编译_。

## 3.5 安全
默认情况下，Fast RTPS 不编译安全支持。可以在 CMake 配置步骤中添加 `-DSECURITY=ON` 以启用该支持。有关 Fast RTPS 安全功能的更多信息，请参见 _安全_。

编译时启用安全功能后，Fast RTPS 会构建多个内置安全插件。其中一些插件依赖 OpenSSL 库。

### 3.5.1 在 Linux 上安装 OpenSSL
当然，可以使用 Linux 发行版的包管理器安装 OpenSSL。例如，在 Ubuntu 上可使用其包管理器执行以下命令安装 OpenSSL。

```bash
sudo apt install libssl-dev
```

### 3.5.2 在 Windows 上安装 OpenSSL
你可以从该网页下载适用于 Windows 的 OpenSSL 1.0.2。这是我们的团队测试过的 OpenSSL 版本。请下载并使用符合你需求的安装程序。安装后，添加环境变量 `OPENSSL_ROOT_DIR`，使其指向安装根目录。例如：

```bat
OPENSSL_ROOT_DIR=C:\OpenSSL-Win64
```

# 第 4 章：快速入门
## 4.1 RTPS 协议简介
RTPS 的最上层是域（Domain），它定义一个独立的通信平面。多个域可以同时独立共存。一个域包含任意数量的 Participant（参与者），这些元素能够发送和接收数据。为此，参与者使用其端点（Endpoint）：

- Reader：能够接收数据的端点。

- Writer：能够发送数据的端点。

一个 Participant 可以拥有任意数量的 writer 和 reader 端点。


![](fast-dds-docs-eprosima-com-en-v1.10.0_images/fast-dds-docs-eprosima-com-en-v1.10.0.pdf-0017-07.png)


通信围绕 Topic（话题）进行，Topic 定义所交换的数据。Topic 不属于任何特定参与者；相反，所有感兴趣的参与者会跟踪话题数据的变化，并确保彼此保持同步。通信单位称为 Change（变更），表示对某个 Topic 的一次更新。端点会将这些变更登记到其 History（历史缓存）中，该数据结构用作近期变更的缓存。通过 writer 端点发布变更时，后台会发生以下步骤：

- 该变更会被添加到 writer 的历史缓存中。

- writer 会通知其已知的所有 reader。

- 任何感兴趣（已订阅）的 reader 会请求该变更。

- 收到数据后，reader 会使用新变更更新其历史缓存。

通过选择服务质量（Quality of Service，QoS）策略，可以从多个方面影响这些历史缓存的管理方式，但通信环路保持不变。更多信息请参见 _配置_。

## 4.2 构建第一个应用程序
要构建一个最小应用程序，必须先定义 Topic。Fast-RTPS 提供两种定义 Topic 数据类型的方式：通过 _动态话题类型_ 动态定义，或通过接口定义语言（Interface Definition Language，IDL）静态定义。本示例将使用 IDL 静态定义数据类型；有关 IDL 的更多信息，请参见 _简介_。

编写一个包含所需定义的 IDL 文件。在本例中，单个字符串已经足够。

```idl
// HelloWorld.idl
struct HelloWorld {
  string msg;
};
```

接下来需要将该文件转换为 Fast RTPS 能够理解的形式。为此，我们提供了名为 fastrtpsgen 的代码生成工具（参见 _简介_），它可以完成两项工作：

- 为自定义 Topic 生成 C++ 定义。

- 可选地生成一个使用该 Topic 数据的可运行示例。

你可以查阅随库发行版提供的 fastrtpsgen 用户手册。不过，目前执行以下命令即可：

在 Linux 上：

```bash
fastrtpsgen -example CMake HelloWorld.idl
```

在 Windows 上：

```bat
fastrtpsgen.bat -example CMake HelloWorld.idl
```

`-example` 选项会创建一个示例应用程序及其构建所需文件。

在 Linux 上：

```bash
mkdir build
cd build
cmake ..
make
```

在 Windows 上：

```bat
mkdir build
cd build
cmake -G "Visual Studio 15 2017 Win64" ..
cmake --build .
```

构建出的应用程序可用于启动任意数量、与该 Topic 关联的 publisher 和 subscriber。在 Linux 上：

```bash
./HelloWorld publisher
./HelloWorld subscriber
```

在 Windows 上：

```bat
HelloWorld.exe publisher
HelloWorld.exe subscriber
```

为使 _eprosima Fast RTPS_ 在 Windows 上正常工作，你可能需要在防火墙中设置特殊规则。

每次在 Publisher 中按 `<Enter>` 时，都会生成一个新的数据报，通过网络发送，并由当前在线的 Subscriber 接收。如果有多个 subscriber 可用，可以看到所有正在监听的节点都会同样收到该消息。

发送前，可以修改由 IDL 生成的自定义数据类型中的任意值。

```cpp
HelloWorld sample; // Auto-generated container class for topic data from FastRTPSGen
sample.msg("Hello there!"); // Add contents to the message
publisher->write(&sample);  // Publish
```

可以查看 _examples/_ 文件夹，了解如何通过不同配置选项改进这个基础应用，并查找高级 Fast RTPS 功能的示例。

# 第 5 章：库概述
可以从两个不同层次与 Fast RTPS 交互：

- Publisher-Subscriber：RTPS 之上的简化抽象。

- Writer-Reader：直接控制 RTPS 端点。


![](fast-dds-docs-eprosima-com-en-v1.10.0_images/fast-dds-docs-eprosima-com-en-v1.10.0.pdf-0021-05.png)


图中红色表示的 Publisher-Subscriber 层为大多数用例提供了便利的抽象。它允许定义与某个 Topic 关联的 Publisher 和 Subscriber，并提供简单的方式来传输 Topic 数据。你可能还记得“快速入门”部分生成的示例：在该示例中，我们更新了 Topic 数据的本地副本，并对其调用了 `write()` 方法。图中蓝色表示的 Writer-Reader 层更接近 RTPS 标准定义的概念，可以实施更精细的控制，但要求你直接操作每个端点的历史缓存。

## 5.1 Fast RTPS 架构
### 5.1.1 线程
eProsima Fast RTPS 采用并发和事件驱动设计。每个 participant 都会创建一组线程来处理后台任务，例如日志记录、消息接收和异步通信。这不应影响你使用该库的方式：公共 API 是线程安全的，因此可以从不同线程中放心调用同一 participant 上的任意方法。不过，了解 Fast RTPS 的工作调度方式仍然很有用：

- 主线程：由应用程序管理。

- 事件线程：每个 participant 拥有一个事件线程，用于处理周期事件和触发事件。

- 异步写入线程：该线程管理所有 participant 的异步写入。即使是同步 writer，某些形式的通信也必须在后台发起。

- 接收线程：participant 为每个接收通道创建一个线程，而通道的概念取决于传输层（例如一个 UDP 端口）。

### 5.1.2 事件
Fast RTPS 提供一个事件系统，使其能够响应特定条件并调度周期性活动。由于大多数事件与 RTPS 元数据有关，用户可见的事件很少。不过，可以通过继承 `TimedEvent` 类来定义自己的周期事件。

# 第 6 章：对象与数据结构
为了充分利用 _eProsima Fast RTPS_，需要掌握库中包含的对象和数据结构。_eProsima Fast RTPS_ 的对象按模块分类，本节简要列出并说明这些模块。完整内容请参阅发行版附带的 API Reference 文档。

## 6.1 发布者-订阅者模块
该模块构成我们在“库概述”中看到的 Publisher-Subscriber 抽象。这里的各项概念比 RTPS 标准中的概念层次更高。

- Domain 用于创建、管理和销毁高层 Participant。

- Participant 包含 Publisher 和 Subscriber，并管理其配置。

   - ParticipantAttributes 创建 Participant 时使用的配置参数。

   - ParticipantListener 允许在 Participant 的作用域内实现回调。

- Publisher 以 Topic 变更的形式发送（发布）数据。

   - PublisherAttributes 构造 Publisher 时使用的配置参数。

   - PublisherListener 允许在 Publisher 的作用域内实现回调。

- Subscriber 接收其所订阅 Topic 的数据。

   - SubscriberAttributes 构造 Subscriber 时使用的配置参数。

   - SubscriberListener 允许在 Subscriber 的作用域内实现回调。

## 6.2 RTPS 模块
该模块直接映射 RTPS 标准中定义的概念，允许直接与 RTPS 实体交互。它由若干子模块组成：

### 6.2.1 RTPS 公共组件
- CacheChange_t 表示对 Topic 的一次变更，将存储在历史缓存中。

- Data 与缓存变更关联的负载。根据消息和变更类型，它可能为空。

- Message 定义 RTPS 消息的组织结构。

- Header 标准消息头，用于标识消息属于 RTPS 协议，并包含厂商 ID。

- Sub-Message Header RTPS 子消息的标识符。一个 RTPS 消息可以由多个子消息组成。

- MessageReceiver 反序列化并处理收到的 RTPS 消息。

- RTPSMessageCreator 组装 RTPS 消息。

### 6.2.2 RTPS 域
- RTPSDomain 用于创建、管理和销毁低层 RTPSParticipant。

- RTPSParticipant 包含 RTPS Writer 和 Reader，并管理其配置。

   - RTPSParticipantAttributes 创建 RTPS Participant 时使用的配置参数。

   - PDPSimple 使 participant 能够通过 Participant Discovery Protocol（参与者发现协议）感知网络中的其他 participant。

   - EDPSimple 使 Participant 能够通过 Endpoint Discovery Protocol（端点发现协议）感知网络中其他 Participant 内的端点（RTPS Writer 和 Reader）。

   - EDPStatic 从用户文件读取远程端点信息。

   - TimedEvent 周期性事件或定时事件的基类。

### 6.2.3 RTPS Reader
- RTPSReader reader 端点的基类。

   - ReaderAttributes 创建 RTPS Reader 时使用的配置参数。

   - ReaderHistory History 数据结构，用于存储近期的 Topic 变更。

   - ReaderListener 用于在 Reader 的作用域内定义回调。

### 6.2.4 RTPS Writer
- RTPSWriter writer 端点的基类。

   - WriterAttributes 创建 RTPS Writer 时使用的配置参数。

   - WriterHistory History 数据结构，用于存储待发送的 Topic 变更并调度发送。

# 第 7 章：发布者-订阅者层
_eProsima Fast RTPS_ 提供高层的发布者-订阅者层，它是对 RTPS 协议的易用抽象。使用该层时，你可以编写直接了当的应用程序，而由库负责低层配置。

## 7.1 如何使用发布者-订阅者层
我们将使用上一节构建的示例来说明该层的工作方式。

第一步是创建 Participant 实例，它将作为应用程序所需 Publisher 和 Subscriber 的容器。为此，我们使用 Domain，这是一个管理 RTPS 实体的静态类。还需要传入 Participant 的配置结构；目前可以保留其默认配置：

ParticipantAttributes participant_attr; _//Configuration structure_ Participant *participant = Domain::createParticipant(participant_attr); 

默认配置提供一组可用的基本选项以及预定义的通信端口。在本教程中，你将学习如何调优 _eProsima Fast RTPS_。

为了使用 Topic，必须在 Participant 中使用由 _fastrtpsgen_ 生成的代码注册它（参见 _简介_）。这同样通过 Domain 类完成：

HelloWorldPubSubType m_type; _//Auto-generated type from FastRTPSGen_ Domain::registerType(participant, &m_type); 

设置完成后，在 Participant 中实例化 Publisher：

PublisherAttributes publisher_attr; _//Configuration structure_ PubListener publisher_listener; _//Class that implements callbacks from the publisher_ Publisher *publisher = Domain::createPublisher(participant, publisher_attr, & publisher_listener); 

Publisher 可正常工作后，发布数据的过程很简单：

HelloWorld sample; _//Auto-generated container class for topic data from FastRTPSGen_ sample.msg("Hello there!"); _// Add contents to the message_ publisher->write(&sample); _//Publish_ 

Publisher 有一组可选的回调函数，会在事件发生时触发。例如，当某个 Subscriber 开始监听我们的 Topic 时。

要实现这些回调，我们创建 `PubListener` 类，它继承自基类 `PublisherListener`。创建 Publisher 时，将其实例传给构造函数。

**class PubListener** : **public** PublisherListener { **public** : PubListener() {} ~PubListener() {} **void** onPublicationmatched(Publisher* pub, MatchingInfo& info) { _//Callback implementation. This is called each time the Publisher finds a Subscriber on the network that listens to the same topic._ } }; 

Subscriber 的创建和实现与之对称。

SubscriberAttributes subscriber_attr; _//Configuration structure_ SubListener subscriber_listener; _//Class that implements callbacks from the Subscriber_ Subscriber *subscriber = Domain::createSubscriber(participant, subscriber_attr, & subscriber_listener); 

收到的消息会在新消息到达时调用的回调中处理：

**class SubListener** : **public** SubscriberListener { **public** : SubListener() {} ~SubListener() {} **void** onNewDataMessage(Subscriber * sub) { **if** (sub->takeNextData(( **void** *)&sample, &sample_info)) { **if** (sample_info.sampleKind == ALIVE) { std::cout << "New message: " << sample.msg() << std::endl; } } } HelloWorld sample; _//Storage for incoming messages_ SampleInfo_t sample_info; _//Auxiliary structure with meta-data on the message_ }; 

## 7.2 配置
_eProsima Fast RTPS_ 实体可以通过代码或 XML 配置文件进行配置。本节将展示这两种方式。

### 7.2.1 Participant 配置
可以通过 `ParticipantAttributes` 结构配置 Participant。`createParticipant` 函数接受该结构的实例。

ParticipantAttributes participant_attr; participant_attr.rtps.setName("my_participant"); participant_attr.rtps.builtin.domainId = 80; Participant *participant = Domain::createParticipant(participant_attr); 

也可以通过 XML 配置文件进行配置。`createParticipant` 函数接受 XML 配置文件的名称。

Participant *participant = Domain::createParticipant("participant_xml_profile"); 

有关 XML 配置文件的更多信息，请参见 _XML 配置文件_。以下是一个 participant XML 配置示例。

<participant profile_name="participant_xml_conf_profile" > <rtps> <name> my_participant </name> <builtin> <domainId> 80 </domainId> </builtin> </rtps> </participant> 

下面介绍最常见的配置选项。

- **Participant 名称：** Participant 的名称是 RTPS 协议元数据的一部分。

**C++** 

participant_attr.rtps.setName("my_participant"); 

**XML** 

<participant profile_name="participant_xml_conf_name_profile" > <rtps> <name> my_participant </name> </rtps> </participant> 

- **DomainId：** 仅当 Publisher 和 Subscriber 所属的 Participant 位于同一 DomainId 时，它们才能相互通信。

#### C++
participant_attr.rtps.builtin.domainId = 80; 

#### XML
<participant profile_name="participant_xml_conf_domain_profile" > <rtps> <builtin> <domainId> 80 </domainId> </builtin> </rtps> </participant> 

- **Mutation Tries：** reader 的物理端口可能已被占用。此时，Participant 使用 `mutation_tries` 属性确定失败前尝试多少个不同端口。这些发生变更的端口会修改 locator 信息。默认值为 _100_。

**C++** 

participant_attr.rtps.builtin.mutation_tries = 55; 

#### XML
<participant profile_name="participant_xml_conf_mutation_tries_profile" > <rtps> <builtin> <mutation_tries> 55 </mutation_tries> </builtin> </rtps> </participant> 

### 7.2.2 Publisher 和 Subscriber 配置
可以通过 `PublisherAttributes` 结构配置 Publisher，`createPublisher` 函数接受该结构的实例。可以通过 `SubscriberAttributes` 结构配置 Subscriber，`createSubscriber` 函数接受该结构的实例。

PublisherAttributes publisher_attr; Publisher *publisher = Domain::createPublisher(participant, publisher_attr); SubscriberAttributes subscriber_attr; Subscriber *subscriber = Domain::createSubscriber(participant, subscriber_attr); 

这些实体也可以通过 XML 配置文件进行配置。`createPublisher` 和 `createSubscriber` 函数接受 XML 配置文件的名称。

Publisher *publisher = Domain::createPublisher(participant, "publisher_xml_profile"); Subscriber *subscriber = Domain::createSubscriber(participant, "subscriber_xml_profile "); 

下面介绍最常见的配置选项。

#### Topic 信息
Topic 名称和数据类型用作元数据，以判断 Publisher 和 Subscriber 能否交换消息。

#### C++
publisher_attr.topic.topicDataType = "HelloWorldType"; publisher_attr.topic.topicName = "HelloWorldTopic"; subscriber_attr.topic.topicDataType = "HelloWorldType"; subscriber_attr.topic.topicName = "HelloWorldTopic"; **XML** 

<publisher profile_name="publisher_xml_conf_topic_profile" > <topic> <dataType> HelloWorldType </dataType> <name> HelloWorldTopic </name> </topic> </publisher> <subscriber profile_name="subscriber_xml_conf_topic_profile" > <topic> <dataType> HelloWorldType </dataType> <name> HelloWorldTopic </name> </topic> </subscriber> 

#### 可靠性
RTPS 标准定义了两种消息投递行为模式：

- Best-Effort（默认）：发送消息时不需要接收方（subscriber）确认到达。该模式速度快，但消息可能丢失。

- Reliable：发送方（publisher）期望接收方（subscriber）确认到达。该模式速度较慢，但可防止数据丢失。

#### C++
publisher_attr.qos.m_reliability.kind = RELIABLE_RELIABILITY_QOS; subscriber_attr.qos.m_reliability.kind = BEST_EFFORT_RELIABILITY_QOS; 

#### XML
<publisher profile_name="publisher_xml_conf_reliability_profile" > <qos> <reliability> <kind> RELIABLE </kind> </reliability> </qos> </publisher> <subscriber profile_name="subscriber_xml_conf_reliability_profile" > <qos> <reliability> <kind> BEST_EFFORT </kind> </reliability> </qos> </subscriber> 

某些可靠性组合会使 publisher 和 subscriber 不兼容，无法相互通信。下表列出了不兼容的组合。

|**Publisher \ Subscriber**|**Best Effort**|**Reliable**|
|---|---|---|
|**Best Effort**|✓||
|**Reliable**|✓|✓|



#### History
样本存储有两种策略：

- Keep-All：将所有样本存储在内存中。

- Keep-Last（默认）：最多存储由 `depth` 指定数量的样本。达到该限制后，旧样本会开始被覆盖。

#### C++
publisher_attr.topic.historyQos.kind = KEEP_ALL_HISTORY_QOS; subscriber_attr.topic.historyQos.kind = KEEP_LAST_HISTORY_QOS; subscriber_attr.topic.historyQos.depth = 5; 

#### XML
<publisher profile_name="publisher_xml_conf_history_profile" > <topic> <historyQos> <kind> KEEP_ALL </kind> </historyQos> </topic> </publisher> <subscriber profile_name="subscriber_xml_conf_history_profile" > <topic> <historyQos> <kind> KEEP_LAST </kind> <depth> 5 </depth> </historyQos> </topic> </subscriber> 

#### 持久性
端点的持久性配置定义其如何处理 subscriber 加入之前已存在于 Topic 上的样本。

- Volatile：忽略过去的样本；加入的 subscriber 只接收匹配时刻之后生成的样本。

- Transient Local（默认）：新 subscriber 加入时，其 History 会填入过去的样本。

- Transient：新 subscriber 加入时，其 History 会填入过去的样本，这些样本存储在持久化存储中（参见 _持久化_）。

#### C++
publisher_attr.qos.m_durability.kind = TRANSIENT_LOCAL_DURABILITY_QOS; subscriber_attr.qos.m_durability.kind = VOLATILE_DURABILITY_QOS; 

#### XML
<publisher profile_name="publisher_xml_conf_durability_profile" > <qos> <durability> <kind> TRANSIENT_LOCAL </kind> </durability> </qos> </publisher> <subscriber profile_name="subscriber_xml_conf_durability_profile" > <qos> <durability> <kind> VOLATILE </kind> </durability> </qos> </subscriber> 

#### Deadline
当新样本的频率低于特定阈值时，Deadline QoS 会发出警报。它适用于预期数据会周期性更新的情况。

在发布侧，Deadline QoS 定义应用应提供新样本的最大周期。在订阅侧，它定义应收到新样本的最大周期。publisher 和 subscriber 要匹配，提供的 deadline 周期必须小于或等于请求的 deadline 周期，否则这些实体将被视为不兼容。

对于带键的 Topic，该 QoS 按 key 应用。例如，假设正在发布车辆位置，并希望强制每辆车的位置都周期性发布。在这种情况下，可以将车辆 ID 设置为 Topic 的 key，并使用 Deadline QoS。


### C++
publisher_attr.qos.m_deadline.period = 1; subscriber_attr.qos.m_deadline.period = 1; **XML <publisher** profile_name="publisher_xml_conf_deadline_profile" **> <qos> <deadline> <period> <sec>** 1 **</sec> </period> </deadline> </qos> </publisher> <subscriber** profile_name="subscriber_xml_conf_deadline_profile" **> <qos> <deadline> <period> <sec>** 1 **</sec> </period> </deadline> </qos> </subscriber>** 

### Lifespan
指定 publisher 写入数据的最大有效时长。Lifespan 周期到期后，数据会从 History 中删除。

### C++
publisher_attr.qos.m_lifespan.duration = 1; subscriber_attr.qos.m_lifespan.duration = 1; 

**XML** 

<publisher profile_name="publisher_xml_conf_lifespan_profile" > <qos> <lifespan> <duration> <sec> 1 </sec> </duration> </lifespan> </qos> </publisher> <subscriber profile_name="subscriber_xml_conf_lifespan_profile" > <qos> <lifespan> <duration> <sec> 1 </sec> </duration> </lifespan> </qos> </subscriber> 

### Liveliness
Liveliness 是一种 QoS，可用于确保网络中的特定实体处于“存活”状态。通过不同设置，可以区分数据周期性更新的应用和数据偶尔变化的应用。它还可以根据 liveliness 机制应检测的故障类型定制应用行为。

AUTOMATIC 活跃性类型适用于只需检测远程应用是否仍在运行的应用。因此，只要运行 participant 的本地进程及其与远程 participant 之间的链路仍然存在，远程 participant 内的实体就会被视为存活。

两种手动设置要求发布侧周期性声明活跃性，才会认为远程实体存活。可以显式调用 publisher 上的 `assert_liveliness` 操作来声明活跃性，也可以通过写入数据隐式声明。MANUAL_BY_PARTICIPANT 设置只要求发布侧的一个实体声明活跃性，即可推断该 participant 内的所有其他实体也存活。MANUAL_BY_TOPIC 模式限制更严格，要求 publisher 内至少有一个实例被声明活跃，才会认为该 publisher 存活。

除 liveliness 类型外，还有两个附加参数可用于定义应用行为。下表列出了所有这些参数。

|名称|说明|值|默认<br>值|
|---|---|---|---|
|<kind>|指定如何管理活跃性。|AUTOMATIC、<br>MANUAL_BY_PARTICIPANT、<br>MANUAL_BY_TOPIC|AUTOMATIC|
|<lease_d|uration><br>自收到 writer 的最后一条消息起，经过多长时间后认为该 writer 不再存活。|_DurationType_|c_TimeInfinite|
|<announc|ement_period><br>publisher 发送的相邻活跃性消息之间的时间间隔。<br>仅用于 AUTOMATIC 和<br>MANUAL_BY_PARTICIPANT 活跃性类型。|_DurationType_|c_TimeInfinite|



### C++
publisher_attr.qos.m_liveliness.announcement_period = 0.5; publisher_attr.qos.m_liveliness.lease_duration = 1; publisher_attr.qos.m_liveliness.kind = AUTOMATIC_LIVELINESS_QOS; subscriber_attr.qos.m_liveliness.lease_duration = 1; subscriber_attr.qos.m_liveliness.kind = AUTOMATIC_LIVELINESS_QOS; 

### XML
<publisher profile_name="publisher_xml_conf_liveliness_profile" > <qos> <liveliness> <announcement_period> <sec> 0 </sec> <nanosec> 1000000 </nanosec> </announcement_period> <lease_duration> <sec> 1 </sec> </lease_duration> <kind> AUTOMATIC </kind> </liveliness> </qos> </publisher> <subscriber profile_name="subscriber_xml_conf_liveliness_profile" > <qos> <liveliness> <lease_duration> <sec> 1 </sec> </lease_duration> <kind> AUTOMATIC </kind> </liveliness> </qos> </subscriber> 

### 资源限制
用于控制 History 和其他资源的最大大小。

### C++
publisher_attr.topic.resourceLimitsQos.max_samples = 200; subscriber_attr.topic.resourceLimitsQos.max_samples = 200; 

### XML
<publisher profile_name="publisher_xml_conf_resource_limits_profile" > <topic> <resourceLimitsQos> <max_samples> 200 </max_samples> </resourceLimitsQos> </topic> </publisher> <subscriber profile_name="subscriber_xml_conf_resource_limits_profile" > <topic> <resourceLimitsQos> <max_samples> 200 </max_samples> </resourceLimitsQos> </topic> </subscriber> 

### 禁用正向确认
这是一项附加 QoS，可在不需要严格可靠通信且带宽有限时减少网络流量。它改变了 reader 向 writer 发送正向确认的默认行为。改为仅在 reader 缺少某个样本时发送负向确认，而 writer 会在足够的 `keep duration` 内保留数据，然后才视为已确认。如果 reader 使用该 QoS 而 writer 未使用，则二者不兼容（即不会匹配）。

### C++
publisher_attr.qos.m_disablePositiveACKs.enabled = true; publisher_attr.qos.m_disablePositiveACKs.duration = 1; subscriber_attr.qos.m_disablePositiveACKs.enabled = true; 

### XML
<publisher profile_name="publisher_xml_conf_disable_positive_acks_profile" > <qos> <disablePositiveAcks> <enabled> true </enabled> <duration> <sec> 1 </sec> </duration> </disablePositiveAcks> </qos> </publisher> <subscriber profile_name="subscriber_xml_conf_disable_positive_acks_profile" > <qos> <disablePositiveAcks> <enabled> true </enabled> </disablePositiveAcks> </qos> </subscriber> 

### 单播定位器
这些是实体接收数据的网络端点。有关网络的更多信息，请参见 _传输_。Publisher 和 Subscriber 从 participant 继承单播定位器。可以通过此属性设置另一组定位器。

### C++
Locator_t new_locator; new_locator.port = 7800; subscriber_attr.unicastLocatorList.push_back(new_locator); publisher_attr.unicastLocatorList.push_back(new_locator); 

### XML
<publisher profile_name="publisher_xml_conf_unicast_locators_profile" > <unicastLocatorList> <locator> <udpv4> <port> 7800 </port> </udpv4> </locator> </unicastLocatorList> </publisher> <subscriber profile_name="subscriber_xml_conf_unicast_locators_profile" > <unicastLocatorList> <locator> <udpv4> <port> 7800 </port> </udpv4> </locator> </unicastLocatorList> </subscriber> 

### 多播定位器
这些是实体接收数据的网络端点。有关网络配置的更多信息，请参见 _传输_。默认情况下，Publisher 和 Subscriber 不使用任何多播定位器。当实体数量很多并希望减少网络使用时，此属性很有用。

### C++
Locator_t new_locator; IPLocator::setIPv4(new_locator, "239.255.0.4"); new_locator.port = 7900; subscriber_attr.multicastLocatorList.push_back(new_locator); publisher_attr.multicastLocatorList.push_back(new_locator); 

### XML
<publisher profile_name="publisher_xml_conf_multicast_locators_profile" > <multicastLocatorList> <locator> <udpv4> <address> 239.255.0.4 </address> <port> 7900 </port> </udpv4> </locator> </multicastLocatorList> </publisher> <subscriber profile_name="subscriber_xml_conf_multicast_locators_profile" > <multicastLocatorList> <locator> <udpv4> <address> 239.255.0.4 </address> <port> 7900 </port> </udpv4> </locator> </multicastLocatorList> </subscriber> 

# 7.3 其他概念
## 7.3.1 使用消息元数据
从 Subscriber 取出消息时，还会返回一个辅助的 `SampleInfo_t` 结构实例。

### 静态类型
HelloWorld sample; SampleInfo_t sample_info; subscriber->takeNextData(( **void** *)&sample, &sample_info); 

### 动态类型
_// input_type is an instance of DynamicPubSubType of out current dynamic type_ DynamicPubSubType *pst = **dynamic_cast** <DynamicPubSubType*>(input_type); DynamicData *sample = DynamicDataFactory::get_instance()->create_data(pst-> GetDynamicType()); subscriber->takeNextData(sample, &sample_info); 

该 `SampleInfo_t` 结构包含传入消息的元数据：

- `sampleKind`：样本类型，由 RTPS 标准定义。来自 Topic 的正常消息始终为 ALIVE。

- `WriterGUID`：消息发送方（Publisher）的标识。

- `OwnershipStrength`：当多个发送方写入相同数据时，此字段可用于确定哪个数据更可靠。

- `SourceTimestamp`：发送方的时间戳，表示样本被封装并发送的时刻。

这些元数据可用于实现过滤器：

**if** ( (sample_info.sampleKind == ALIVE) & (sample_info.ownershipStrength > 25) ) { _//Process data_ } 

## 7.3.2 定义回调
如示例所示，Publisher 和 Subscriber 都有一组可在应用中使用的回调。这些回调应在派生自 `SubscriberListener` 或 `PublisherListener` 的类中实现。下表汇总了两种情况下可实现的各种回调：

|回调|Publisher|Subscriber|
|---|---|---|
|_onNewDataMessage_|N|Y|
|_onSubscriptionMatched_|N|Y|
|_onPublicationMatched_|Y|N|
|_on_offered_deadline_missed_|Y|N|
|_on_requested_deadline_missed_|N|Y|
|_on_liveliness_lost_|Y|N|
|_on_liveliness_changed_|N|Y|



# 第 8 章：写入者-读取者层
_eprosima Fast RTPS_ 的低层写入者-读取者层提供 RTPS 协议的原生实现。与发布者-订阅者层相比，它可以更深入地控制协议内部机制。高级用户可以直接使用该层，以便更精细地控制库的功能。

# 8.1 与发布者-订阅者层的关系
该层的元素与发布者-订阅者层的元素大多一一对应，仅有少量新增项。下表列出两层之间的名称对应关系：

|发布者-订阅者层|写入者-读取者层|
|---|---|
|Domain|RTPSDomain|
|Participant|RTPSParticipant|
|Publisher|RTPSWriter|
|Subscriber|RTPSReader|



# 8.2 如何使用写入者-读取者层
接下来，我们将像介绍 Publisher-Subscriber 层那样介绍 Writer-Reader 层的用法，并说明它提供的新功能。

建议在阅读本节时参考发行版附带的两个使用该层的示例，它们位于 _examples/RTPSTest_as_socket_ 和 _examples/RTPSTest_registered_。

## 8.2.1 管理 Participant
创建 RTPSParticipant 的过程与 Publisher-Subscriber 层所示过程非常相似。

RTPSParticipantAttributes participant_attr; participant_attr.setName("participant"); RTPSParticipant* participant = RTPSDomain::createParticipant(participant_attr); 

`RTPSParticipantAttributes` 结构等同于 Publisher-Subscriber 层中 `ParticipantAttributes` 的 `rtps` 成员，因此可以像之前一样配置 RTPSParticipant：

RTPSParticipantAttributes participant_attr; participant_attr.setName("my_participant"); _//etc._ 

## 8.2.2 管理 Writer 和 Reader
按照 RTPS 标准规定，Writer 和 Reader 始终与一个 History 元素关联。在 Publisher-Subscriber 层中，History 的创建和管理被隐藏；但在 Writer-Reader 层中，可以完全控制其创建和配置。

Writer 通过 `WriterAttributes` 结构配置。它们还需要一个用 `HistoryAttributes` 结构配置的 `WriterHistory`。

HistoryAttributes history_attr; WriterHistory* history = **new** WriterHistory(history_attr); WriterAttributes writer_attr; RTPSWriter* writer = RTPSDomain::createRTPSWriter(participant, writer_attr, history); 

Reader 的创建方式类似。请注意，在这种情况下，可以提供实现回调的 `ReaderListener` 实例：

**class MyReaderListener** : **public** ReaderListener{}; MyReaderListener listener; HistoryAttributes history_attr; ReaderHistory* history = **new** ReaderHistory(history_attr); ReaderAttributes reader_attr; RTPSReader* reader = RTPSDomain::createRTPSReader(participant, reader_attr, history, & listener); 

## 8.2.3 使用 History 发送和接收数据
在 RTPS 协议中，Reader 和 Writer 将 Topic 数据保存在其关联的 History 中。每项数据由一个 Change 表示，_eprosima Fast RTPS_ 将其实现为 `CacheChange_t`。Change 始终由 History 管理。作为用户，与 History 交互的流程始终相同：

1. 从 History 请求一个 `CacheChange_t`

2. 使用它

3. 释放它

可以与 Writer 的 History 交互来发送数据。需要提供一个返回最大负载字节数的回调：

_//Request a change from the history_ CacheChange_t* change = writer->new_change([]() -> **uint32_t** { **return** 255;}, ALIVE); _//Write serialized data into the change_ 


change->serializedPayload.length = sprintf(( **char** *) change->serializedPayload.data, "My example string %d", 2)+1; _//Insert change back into the history. The Writer takes care of the rest._ history->add_change(change); 

如果 Topic 数据类型包含多个字段，则必须提供函数，在 `CacheChange_t` 中序列化和反序列化数据。_FastRTPSGen_ 会为你完成这些工作。

可以像在 Publisher-Subscriber 层中那样，在 `ReaderListener` 回调方法中接收数据：

**class MyReaderListener** : **public** ReaderListener { **public** : MyReaderListener(){} ~MyReaderListener(){} **void** onNewCacheChangeAdded(RTPSReader* reader, **const** CacheChange_t* **const** change) { _// The incoming message is enclosed within the `change` in the function parameters_ printf("%s **\n** ",change->serializedPayload.data); _// Once done, remove the change_ reader->getHistory()->remove_change((CacheChange_t*)change); } }; 

# 8.3 配置 Reader 和 Writer
使用 Writer-Reader 层的优势之一是，它保留 Publisher-Subscriber 层的选项（参见 _配置_），同时提供新的配置可能性。例如，可以像之前一样将 Writer 或 Reader 设置为 Reliable 或 Best-Effort 端点：

writer_attr.endpoint.reliabilityKind = BEST_EFFORT; 

## 8.3.1 设置数据持久性类型
当新 Reader 匹配时，Durability 参数定义 Writer 对已发送样本的行为。_eProsima Fast RTPS_ 提供三种 Durability 选项：

- VOLATILE（默认）：消息发送后即被丢弃。如果新 Reader 在第 _n_ 条消息之后匹配，它将从第 _n+1_ 条消息开始接收。

- TRANSIENT_LOCAL：Writer 保存其最近发送的 _k_ 条消息记录。如果新 reader 在第 _n_ 条消息之后匹配，它将从第 _n-k_ 条消息开始接收。

- TRANSIENT：与 TRANSIENT_LOCAL 相同，但消息记录会保存到持久化存储中，因此即使 writer 被销毁并重新创建，或应用崩溃，这些记录仍然可用（参见 _持久化_）。

要选择所需选项：

writer_attr.endpoint.durabilityKind = TRANSIENT_LOCAL; 

由于在 Writer-Reader 层中可以控制 History，因此在 TRANSIENT_LOCAL 和 TRANSIENT 模式下，Writer 会发送你尚未从 History 中显式释放的所有变更。

# 8.4 配置 History
History 有自己的配置结构 `HistoryAttributes`。

## 8.4.1 更改负载的最大大小
可以选择可以放入 `CacheChange_t` 的 Payload 最大大小。请确保所选大小能够容纳可能出现的最大数据块：

history_attr.payloadMaxSize = 250; _//Defaults to 500 bytes_ 

## 8.4.2 更改 History 的大小
可以指定 History 能够容纳的最大变更数量以及初始分配的变更数量：

history_attr.initialReservedCaches = 250; _//Defaults to 500_ history_attr.maximumReservedCaches = 500; _//Defaults to 0 = Unlimited Changes_ 

当初始预留的变更数量低于最大值时，History 会根据需要分配更多变更，直到达到最大大小。

# 第 9 章：高级功能
本节介绍一些稍高级但很有用的功能，可增强你的实现。

# 9.1 Topic 与 Key
RTPS 标准允许使用 key 在单个 Topic 内定义多个数据源/数据汇。

可以通过三种方式在 Topic 中实现 key：

- 使用 FastRTPSGen 时，在 IDL 文件中定义 _@Key_ 字段（参见发行版附带的示例）。

- 手动实现并使用 `getKey()` 方法。

- 使用动态类型时，为成员及其父级添加 _Key_ 属性（参见 _动态话题类型_）。

使用带键 Topic 的 Publisher 和 Subscriber 必须配置为使用 key，否则 key 不会生效：

**C++** _// Publisher-Subscriber Layer configuration._ publisher_attr.topic.topicKind = WITH_KEY; **XML** 

<publisher profile_name="publisher_profile_qos_key" > <topic> <kind> WITH_KEY </kind> </topic> </publisher> 

RTPS 层要求在回调中手动调用 `getKey()` 方法。

可以根据当前配置调整 History，以容纳来自多个 key 的数据。这包括定义数据汇的最大数量以及每个数据汇的最大大小：

**C++** _// Set the subscriber to remember and store up to 3 different keys._ subscriber_attr.topic.resourceLimitsQos.max_instances = 3; _// Hold a maximum of 20 samples per key._ subscriber_attr.topic.resourceLimitsQos.max_samples_per_instance = 20; **XML <subscriber** profile_name="subscriber_profile_qos_resourcelimit" **> <topic> <resourceLimitsQos> <max_instances>** 3 **</max_instances> <max_samples_per_instance>** 20 **</max_samples_per_instance> </resourceLimitsQos> </topic> </subscriber>** 

请注意，History 必须足够大，以容纳每个 key 的最大样本数。如果 History 太小，eProsima Fast RTPS 会通知你。

# 9.2 分区
分区（Partition）在 Domain 提供的物理隔离内部引入逻辑实体隔离级别的概念。它们在 Domain 和 Topic 之外提供另一层 Publisher 与 Subscriber 隔离。Publisher 要与 Subscriber 通信，双方至少必须属于一个共同分区。从这个意义上说，分区是一种轻量机制，用于在端点之间隔离数据：

- 与 Domain 和 Topic 不同，Partition 可以在 Endpoint 生命周期内以很小的代价动态更改。具体来说，不会启动新线程，不会分配新内存，也不会影响变更历史。请注意，修改端点的 Partition 成员关系会触发新 QoS 配置的公告，并且根据新的 Partition 配置，可能发生新的 Endpoint 匹配。远程 Endpoint 的匹配可能导致内存分配和运行线程发生变化。

- 与 Domain 和 Topic 不同，一个 Endpoint 可以同时属于多个 Partition。要让特定数据在不同 Topic 之间共享，必须为每个 Topic 使用不同的 Publisher，且各自共享自己的变更历史。另一方面，单个 Publisher 可以通过一个 Topic 变更在不同 Partition 之间共享相同数据，从而减少网络负载。

可以在 `PublisherAttributes` 或 `SubscriberAttributes` 对象的 `qos.m_partitions` 属性中配置 Endpoint 的 Partition 成员关系。该属性保存 Partition 名称字符串列表。如果未为实体定义 Partition，该实体会自动加入默认的无名 Partition。因此，未指定 Partition 的 Publisher 和 Subscriber 仍可通过默认 Partition 通信。

**注意：** Partition 与 Endpoint 关联，而不是与变更关联。这意味着 Endpoint 的 History 不会感知 Partition 的修改。例如，如果 Publisher 切换 Partition 后需要再次重发某个较早的变更，它会把该变更投递到新的 Partition 集合，而不考虑创建该变更时定义了哪些 Partition。

这意味着后加入的 Subscriber 可能收到在另一组 Partition 处于活动状态时创建的变更。

## 9.2.1 Partition 中的通配符
Partition 名称条目可以使用通配符，命名约定由 POSIX `fnmatch` API 定义（1003.2-1992 第 B.6 节）。带通配符的条目可以匹配多个名称，使 Endpoint 能轻松加入多个 Partition。如果两个带通配符的 Partition 名称中任意一个能按 `fnmatch` 匹配另一个，则二者匹配。也就是说，会双向检查匹配。例如，考虑以下配置：

- 一个使用 Partition `part*` 的 publisher

- 一个使用 Partition `partition*` 的 subscriber

尽管 `partition*` 不匹配 `part*`，但由于 `part*` 匹配 `partition*`，该 publisher 和 subscriber 仍会相互通信。

请注意，名称为 `*` 的 Partition 会匹配任何其他 Partition，**但不会匹配默认 Partition**。

## 9.2.2 完整示例
假设系统采用以下 Partition 配置：

|Participant_1|Pub_11|{“Partition_1”,“Partition_2”}|
|---|---|---|
||Pub_12|{“*”}|
|Participant_2|Pub_21|{}|
||Pub_22|{“Partition*”}|
|Participant_3|Subs_31|{“Partition_1”}|
||Subs_32|{“Partition_2”}|
||Subs_33|{“Partition_3”}|
||Subs_34|{}|



这些端点最终会按下表所示的 Partition 进行匹配。请注意，`Pub_12` 不匹配默认 Partition。

||Participa|nt_1|Participa|nt_2|Participant|_3|||
|---|---|---|---|---|---|---|---|---|
||Pub_11|Pub_12|Pub_21|Pub_22|Subs_31|Subs_32|Subs_33|Subs_34|
|Partition_1|✓|✓||✓|✓||||
|Partition_2|✓|✓||✓||✓|||
|Partition_3||✓||✓|||✓||
|{default}|||✓|||||✓|



下表给出该示例的通信矩阵：

|||Participa|nt_1|Participa|nt_2|
|---|---|---|---|---|---|
|||Pub_11|Pub_12|Pub_21|Pub_22|
|Participant_3|Subs_31|✓|✓||✓|
||Subs_32|✓|✓||✓|
||Subs_33||✓||✓|
||Subs_34|||✓||



以下代码展示了本示例用例所需的一组参数。

### C++
PublisherAttributes pub_11_attr; pub_11_attr.qos.m_partition.push_back("Partition_1"); pub_11_attr.qos.m_partition.push_back("Partition_2"); PublisherAttributes pub_12_attr; pub_12_attr.qos.m_partition.push_back("*"); PublisherAttributes pub_21_attr; _//No partitions defined for pub_21_ PublisherAttributes pub_22_attr; pub_22_attr.qos.m_partition.push_back("Partition*"); SubscriberAttributes subs_31_attr; subs_31_attr.qos.m_partition.push_back("Partition_1"); SubscriberAttributes subs_32_attr; subs_32_attr.qos.m_partition.push_back("Partition_2"); SubscriberAttributes subs_33_attr; subs_33_attr.qos.m_partition.push_back("Partition_3"); SubscriberAttributes subs_34_attr; _//No partitions defined for subs_34_ **XML** 

<publisher profile_name="pub_11" > <topic> <name> TopicName </name> <dataType> TopicDataTypeName </dataType> </topic> <qos> <partition> <names> <name> Partition_1 </name> <name> Partition_2 </name> </names> </partition> </qos> </publisher> <publisher profile_name="pub_12" > <topic> <name> TopicName </name> <dataType> TopicDataTypeName </dataType> </topic> <qos> <partition> <names> <name> * </name> </names> </partition> </qos> </publisher> <publisher profile_name="pub_21" > <topic> 42 <name> TopicName </name> <dataType> TopicDataTypeName </dataType> </topic> </publisher> 

# 9.3 进程内投递
_eProsima Fast RTPS_ 通过避免传输层（UDP 或 TCP）涉及的复制或发送操作，加快同一进程内实体之间的通信。该功能默认启用，并可通过 _XML 配置文件_ 配置。目前提供以下选项：

- **INTRAPROCESS_OFF**：禁用该功能。

- **INTRAPROCESS_USER_DATA_ONLY**：发现元数据仍使用普通传输。

- **INTRAPROCESS_FULL**：默认值。用户数据和发现元数据都使用进程内投递。

### XML
<library_settings> <intraprocess_delivery> FULL </intraprocess_delivery> _<!-- OFF | USER_DATA_ ONLY | FULL -->_ </library_settings> 

# 9.4 传输
_eProsima Fast RTPS_ 实现可插拔传输架构。当前版本实现五种传输：UDPv4、UDPv6、TCPv4、TCPv6 和 SHM（共享内存）。默认情况下，创建 Participant 时会配置两种内置传输：

- 同一台机器上 participant 之间的所有通信都使用 SHM 传输。

- 跨机器通信使用 UDPv4。

可以使用 `rtps.userTransports` 属性添加自定义传输。

### C++
_//Create a descriptor for the new transport._ **auto** custom_transport = std::make_shared<UDPv4TransportDescriptor>(); custom_transport->sendBufferSize = 9216; custom_transport->receiveBufferSize = 9216; _//Disable the built-in Transport Layer._ participant_attr.rtps.useBuiltinTransports = false; _//Link the Transport Layer to the Participant._ participant_attr.rtps.userTransports.push_back(custom_transport); 

### XML
<transport_descriptors> <transport_descriptor> <transport_id> my_transport </transport_id> <type> UDPv4 </type> <sendBufferSize> 9216 </sendBufferSize> <receiveBufferSize> 9216 </receiveBufferSize> </transport_descriptor> </transport_descriptors> <participant profile_name="my_transport" > <rtps> <userTransports> <transport_id> my_transport </transport_id> </userTransports> <useBuiltinTransports> false </useBuiltinTransports> </rtps> </participant> 

所有传输配置选项见 _传输描述符_ 一节。

## 9.4.1 共享内存传输（SHM）
共享内存传输依赖宿主操作系统提供的共享内存机制，使同一处理单元/机器上运行的实体之间能够快速通信。

即使 UDP/TCP 使用环回接口，SHM 传输的性能也优于这些传输。主要原因如下：

- 支持大消息：网络协议必须对数据分片，以满足特定协议和网络栈的要求。SHM 传输允许复制完整消息，唯一的大小限制是机器的内存容量。

- 减少内存复制次数：将同一条消息发送到不同端点时，SHM 传输可以直接与所有目标端点共享同一内存缓冲区。其他协议则要求为每个端点复制一次消息。

- 降低操作系统开销：初始设置完成后，共享内存传输所需的系统调用远少于其他协议。因此，使用 SHM 可以提升性能并减少耗时。

当同一台机器上的两个 participant 都启用 SHM 传输时，它们之间的所有通信会自动仅通过 SHM 传输进行。这两个 participant 之间不会使用其他已启用的传输。


要更改 SHM 传输的默认参数，需要将 `SharedMemTransportDescriptor` 添加到 `rtps.userTransports` 属性（C++ 代码），或在 XML 文件中定义类型为 SHM 的 `transport_descriptor`。两种情况下都必须禁用 `rtps.useBuiltinTransports`（参见以下示例）。

### C++
_// Create a descriptor for the new transport._ std::shared_ptr<SharedMemTransportDescriptor> shm_transport = std::make_shared <SharedMemTransportDescriptor>(); _// Disable the built-in Transport Layer._ participant_attr.rtps.useBuiltinTransports = false; _// Link the Transport Layer to the Participant._ participant_attr.rtps.userTransports.push_back(shm_transport); **XML** 

<transport_descriptors> _<!-- Create a descriptor for the new transport -->_ <transport_descriptor> <transport_id> shm_transport </transport_id> <type> SHM </type> </transport_descriptor> </transport_descriptors> <participant profile_name="SHMParticipant" > <rtps> _<!-- Link the Transport Layer to the Participant -->_ <userTransports> <transport_id> shm_transport </transport_id> </userTransports> _<!-- Disable the built-in Transport Layer -->_ <useBuiltinTransports> false </useBuiltinTransports> </rtps> </participant> 

SHM 配置参数：

- `segment_size`：共享内存段的大小，单位为字节。每个 participant 都会创建一个共享内存段。participant 的 writer 将消息复制到该段中，并向目标 reader 发送消息引用。

- `port_queue_capacity`：每个启用 SHM 传输的 participant 都在一个队列（端口）上监听传入的 SHM 消息引用。此参数指定队列大小（以消息数为单位）。

- `healthy_check_timeout_ms`：使用 SHM 时，Reader 和 Writer 通过队列（称为 Port）交换消息。如果参与使用该端口的某个进程崩溃，该结构可能失效。因此，每次打开端口时都会执行健康检查。如果挂接的监听器未在 `healthy_check_timeout_ms` 毫秒内响应，该端口会被销毁并重新创建。

- `rtps_dump_file`：协议转储文件的完整路径（包括文件名）。当该字符串参数非空时，participant 的所有 SHM 流量（发送和接收）都会跟踪写入文件。输出文件格式为 _tcpdump_ 文本十六进制格式，可使用 Wireshark 等协议分析器读取。

## 9.4.2 TCP 传输
与 UDP 不同，TCP 传输是面向连接的，因此 Fast-RTPS 必须先建立 TCP 连接才能发送 RTPS 消息。因此，TCP 传输可以表现为两种行为：作为服务器（**TCP Server**）或作为客户端（**TCP Client**）。服务器打开 TCP 端口监听传入连接，客户端尝试连接服务器。服务器和客户端概念独立于 RTPS 概念 **Publisher**、**Subscriber**、**Writer** 和 **Reader**。其中任何实体都可以作为 **TCP Server** 或 **TCP Client** 运行，因为这些概念仅用于建立 TCP 连接，而 RTPS 协议在该连接之上工作。

使用 TCP 传输需要定义更多配置：

必须创建新的 TCP 传输描述符，例如 TCPv4。该描述符有一个名为 `listening_ports` 的字段，用于告知 Fast-RTPS participant 将在哪些物理 TCP 端口上监听传入连接。如果省略该字段，participant 将无法接收传入连接，但仍可连接到已配置监听端口的其他 participant。必须将该传输添加到 participant 属性的 `userTransports` 列表中。`wan_addr` 字段可用于允许在 WAN 环境或互联网中通过公网 IP 接受传入连接。有关如何配置 TCP 传输以允许或建立 WAN 连接的更多信息，请参见 _基于 TCP/IPv4 的 WAN 或互联网通信_。

**C++** 

_//Create a descriptor for the new transport._ **auto** tcp_transport = std::make_shared<TCPv4TransportDescriptor>(); tcp_transport->add_listener_port(5100); tcp_transport->set_WAN_address("80.80.99.45"); _//Disable the built-in Transport Layer._ participant_attr.rtps.useBuiltinTransports = false; _//Link the Transport Layer to the Participant._ participant_attr.rtps.userTransports.push_back(tcp_transport); 

**XML** 

<transport_descriptors> <transport_descriptor> <transport_id> tcp_transport </transport_id> <type> TCPv4 </type> <listening_ports> <port> 5100 </port> </listening_ports> <wan_addr> 80.80.99.45 </wan_addr> </transport_descriptor> </transport_descriptors> <participant profile_name="TCPParticipant" > <rtps> <userTransports> <transport_id> tcp_transport </transport_id> </userTransports> <useBuiltinTransports> false </useBuiltinTransports> </rtps> </participant> 

要将 participant 配置为通过 TCP 连接另一个节点，必须配置一个 Locator 并将其添加到 `initialPeersList`，该 Locator 指向远程 _监听端口_。

### C++
**auto** tcp2_transport = std::make_shared<TCPv4TransportDescriptor>(); _//Disable the built-in Transport Layer._ participant_attr.rtps.useBuiltinTransports = false; _//Set initial peers._ Locator_t initial_peer_locator; initial_peer_locator.kind = LOCATOR_KIND_TCPv4; IPLocator::setIPv4(initial_peer_locator, "80.80.99.45"); initial_peer_locator.port = 5100; participant_attr.rtps.builtin.initialPeersList.push_back(initial_peer_locator); _//Link the Transport Layer to the Participant._ participant_attr.rtps.userTransports.push_back(tcp2_transport); **XML** 

<transport_descriptors> <transport_descriptor> <transport_id> tcp2_transport </transport_id> <type> TCPv4 </type> </transport_descriptor> </transport_descriptors> <participant profile_name="TCP2Participant" > <rtps> <userTransports> <transport_id> tcp2_transport </transport_id> </userTransports> <builtin> <initialPeersList> <locator> <tcpv4> <address> 80.80.99.45 </address> <physical_port> 5100 </physical_port> </tcpv4> </locator> </initialPeersList> </builtin> <useBuiltinTransports> false </useBuiltinTransports> </rtps> </participant> 

可在此链接找到 HelloWorld 示例的 TCP 版本。

### 基于 TCP/IPv4 的 WAN 或互联网通信
配置正确后，Fast-RTPS 可以通过互联网或其他 WAN 网络连接。要实现此类场景，路由器、防火墙等相关网络设备应添加允许通信的规则。

例如，要通过 NAT 接受传入连接，必须将 Fast-RTPS 配置为监听传入 TCP 连接的 **TCP Server**。要通过 WAN 接受传入连接，关联的 TCP 描述符

必须通过 `wan_addr` 字段指明其公网 IP。

### C++
_//Create a descriptor for the new transport._ **auto** tcp_transport = std::make_shared<TCPv4TransportDescriptor>(); tcp_transport->add_listener_port(5100); tcp_transport->set_WAN_address("80.80.99.45"); _//Disable the built-in Transport Layer._ participant_attr.rtps.useBuiltinTransports = false; _//Link the Transport Layer to the Participant._ participant_attr.rtps.userTransports.push_back(tcp_transport); 

**XML** 

<transport_descriptors> <transport_descriptor> <transport_id> tcp_transport </transport_id> <type> TCPv4 </type> <listening_ports> <port> 5100 </port> </listening_ports> <wan_addr> 80.80.99.45 </wan_addr> </transport_descriptor> </transport_descriptors> <participant profile_name="TCPParticipant" > <rtps> <userTransports> <transport_id> tcp_transport </transport_id> </userTransports> <useBuiltinTransports> false </useBuiltinTransports> </rtps> </participant> 

在这种情况下，必须配置路由器（其公网 IP 为 80.80.99.45），使传入流量能够到达 **TCP Server**。通常只需将 `listening_port` 5100 通过 NAT 路由到我们的机器。还应配置现有防火墙。

在客户端，需要将 **TCP Server** 的公网 IP 及其 `listening_port` 指定为 initial peer。

### C++
**auto** tcp2_transport = std::make_shared<TCPv4TransportDescriptor>(); _//Disable the built-in Transport Layer._ participant_attr.rtps.useBuiltinTransports = false; _//Set initial peers._ Locator_t initial_peer_locator; initial_peer_locator.kind = LOCATOR_KIND_TCPv4; IPLocator::setIPv4(initial_peer_locator, "80.80.99.45"); initial_peer_locator.port = 5100; participant_attr.rtps.builtin.initialPeersList.push_back(initial_peer_locator); _//Link the Transport Layer to the Participant._ participant_attr.rtps.userTransports.push_back(tcp2_transport); **XML** 

<transport_descriptors> <transport_descriptor> <transport_id> tcp2_transport </transport_id> <type> TCPv4 </type> </transport_descriptor> </transport_descriptors> <participant profile_name="TCP2Participant" > <rtps> <userTransports> <transport_id> tcp2_transport </transport_id> </userTransports> <builtin> <initialPeersList> <locator> <tcpv4> <address> 80.80.99.45 </address> <physical_port> 5100 </physical_port> </tcpv4> </locator> </initialPeersList> </builtin> <useBuiltinTransports> false </useBuiltinTransports> </rtps> </participant> 

在 **TCP Server** 和 **TCP Client** 中组合上述配置，可以实现下图所示的场景。


![](fast-dds-docs-eprosima-com-en-v1.10.0_images/fast-dds-docs-eprosima-com-en-v1.10.0.pdf-0056-01.png)


### IPLocator
`IPLocator` 是一个辅助静态类，提供便于管理基于 IP 的定位器（如 UDP 或 TCP 定位器）的方法。在 TCP 中，定位器的 port 字段分为物理端口和逻辑端口。物理端口是网络设备使用的端口，也是操作系统理解的真实端口。逻辑端口可视为 RTPS 端口，或 UDP 的等价端口（UDP 的物理端口在 TCP 中属于逻辑端口）。逻辑端口通常不需要显式管理，但可以通过 `IPLocator` 类进行管理。相反，要明确使用特定端口时（例如通过 NAT 通信），必须设置物理端口。

Locator_t locator; _// Get & Set Physical Port_ **uint16_t** physical_port = IPLocator::getPhysicalPort(locator); IPLocator::setPhysicalPort(locator, 5555); _// Get & Set Logical Port_ **uint16_t** logical_port = IPLocator::getLogicalPort(locator); IPLocator::setLogicalPort(locator, 7400); _// Set WAN Address_ IPLocator::setWan(locator, "80.88.75.55"); 

### 注意
TCP 不支多播场景，因此必须仔细规划网络架构。

### 基于 TCP 的 TLS
Fast-RTPS 允许通过正确设置 **TCP Server** 和 **TCP Client**，将 TCP 传输配置为使用 TLS（Transport Layer Security，传输层安全协议）。

### TCP Server
### C++
**auto** tls_transport = std::make_shared<TCPv4TransportDescriptor>(); **using** TLSOptions = TCPTransportDescriptor::TLSConfig::TLSOptions; tls_transport->apply_security = true; tls_transport->tls_config.password = "test"; tls_transport->tls_config.cert_chain_file = "server.pem"; tls_transport->tls_config.private_key_file = "serverkey.pem"; tls_transport->tls_config.tmp_dh_file = "dh2048.pem"; tls_transport->tls_config.add_option(TLSOptions::DEFAULT_WORKAROUNDS); tls_transport->tls_config.add_option(TLSOptions::SINGLE_DH_USE); tls_transport->tls_config.add_option(TLSOptions::NO_SSLV2); 

### XML
<transport_descriptors> <transport_descriptor> <transport_id> tls_transport_server </transport_id> <type> TCPv4 </type> <tls> <password> test </password> <private_key_file> serverkey.pem </private_key_file> <cert_chain_file> server.pem </cert_chain_file> <tmp_dh_file> dh2048.pem </tmp_dh_file> <options> <option> DEFAULT_WORKAROUNDS </option> <option> SINGLE_DH_USE </option> <option> NO_SSLV2 </option> </options> </tls> </transport_descriptor> </transport_descriptors> 

### TCP Client
### C++
**auto** tls_transport = std::make_shared<TCPv4TransportDescriptor>(); **using** TLSOptions = TCPTransportDescriptor::TLSConfig::TLSOptions; **using** TLSVerifyMode = TCPTransportDescriptor::TLSConfig::TLSVerifyMode; tls_transport->apply_security = true; tls_transport->tls_config.verify_file = "ca.pem"; tls_transport->tls_config.verify_mode = TLSVerifyMode::VERIFY_PEER; tls_transport->tls_config.add_option(TLSOptions::DEFAULT_WORKAROUNDS); tls_transport->tls_config.add_option(TLSOptions::SINGLE_DH_USE); tls_transport->tls_config.add_option(TLSOptions::NO_SSLV2); **XML** 

<transport_descriptors> <transport_descriptor> <transport_id> tls_transport_client </transport_id> <type> TCPv4 </type> <tls> <verify_file> ca.pem </verify_file> <verify_mode> <verify> VERIFY_PEER </verify> </verify_mode> <options> <option> DEFAULT_WORKAROUNDS </option> <option> SINGLE_DH_USE </option> <option> NO_SSLV2 </option> </options> </tls> </transport_descriptor> </transport_descriptors> 

更多 TLS 相关选项见 _传输描述符_ 一节。

## 9.4.3 监听定位器
_eProsima Fast RTPS_ 将监听定位器分为四类：

- 元流量多播定位器：这些定位器用于通过多播接收元流量信息。它们通常供内置端点使用，例如发现内置端点。可以使用 `rtps.builtin.metatrafficMulticastLocatorList` 属性设置自己的定位器。

_// This locator will open a socket to listen network messages on UDPv4 port 22222 over multicast address 239.255.0.1_ eprosima::fastrtps::rtps::Locator_t locator; IPLocator::setIPv4(locator, 239, 255, 0 , 1); locator.port = 22222; participant_attr.rtps.builtin.metatrafficMulticastLocatorList.push_back(locator); 

- 元流量单播定位器：这些定位器用于通过单播接收元流量信息。它们通常供内置端点使用，例如发现内置端点。可以使用 `rtps.builtin.metatrafficUnicastLocatorList` 属性设置自己的定位器。

_// This locator will open a socket to listen network messages on UDPv4 port 22223 over network interface 192.168.0.1_ eprosima::fastrtps::rtps::Locator_t locator; IPLocator::setIPv4(locator, 192, 168, 0 , 1); locator.port = 22223; participant_attr.rtps.builtin.metatrafficUnicastLocatorList.push_back(locator); 

- 用户多播定位器：这些定位器用于通过多播接收用户信息，供用户端点使用。可以使用 `rtps.defaultMulticastLocatorList` 属性设置自己的定位器。

_// This locator will open a socket to listen network messages on UDPv4 port 22224 over multicast address 239.255.0.1_ eprosima::fastrtps::rtps::Locator_t locator; IPLocator::setIPv4(locator, 239, 255, 0 , 1); locator.port = 22224; 

participant_attr.rtps.defaultMulticastLocatorList.push_back(locator); 

- 用户单播定位器：这些定位器用于通过单播接收用户信息，供用户端点使用。可以使用 `rtps.defaultUnicastLocatorList` 属性设置自己的定位器。

_// This locator will open a socket to listen network messages on UDPv4 port 22225 over network interface 192.168.0.1_ eprosima::fastrtps::rtps::Locator_t locator; IPLocator::setIPv4(locator, 192, 168, 0 , 1); locator.port = 22225; participant_attr.rtps.defaultUnicastLocatorList.push_back(locator); 

默认情况下，_eProsima Fast RTPS_ 使用众所周知端口为内置 UDPv4 网络传输计算监听定位器。这些众所周知端口按以下预定义规则计算：

表 1：使用的端口

|流量类型|众所周知端口表达式|
|---|---|
|Metatraffic multicast|PB + DG *_domainId_+ offsetd0|
|Metatraffic unicast|PB + DG *_domainId_+ offsetd1 + PG * _participantId_|
|User multicast|PB + DG *_domainId_+ offsetd2|
|User unicast|PB + DG *_domainId_+ offsetd3 + PG * _participantId_|



这些预定义规则使用以下值：

- DG：DomainId Gain。可以使用 `rtps.port.domainIDGain` 属性设置该值。

- PG：ParticipantId Gain。可以使用 `rtps.port.participantIDGain` 属性设置该值。默认值为 2。

- PB：端口基数。可以使用 `rtps.port.portBase` 属性设置该值。默认值为 7400。

- offsetd0、offsetd1、offsetd2、offsetd3：附加偏移量。可以使用 `rtps.port.offsetdN` 属性设置这些值。默认值为：offsetd0 = 0、offsetd1 = 10、offsetd2 = 1、offsetd3 = 11。

UDP 和 TCP 单播定位器都支持空地址。此时，_eProsima Fast RTPS_ 会获取并使用本地网络地址。

UDP 和 TCP 定位器都支持端口为零。此时，_eProsima Fast RTPS_ 会为该类流量计算众所周知端口。

## 9.4.4 初始对等节点
根据 RTPS 标准（第 9.6.1.1 节），每个 participant 必须在两个不同端口上监听传入的 Participant Discovery Protocol（PDP）发现元流量，其中一个端口关联多播地址，另一个关联单播地址（参见 _发现_）。Fast-RTPS 允许配置初始对等节点列表，其中包含一个或多个与远程 participant 的 PDP 发现监听资源对应的地址-端口对。这样，本地 participant 不仅会将 PDP 流量发送到其域指定的默认多播地址-端口，还会发送到初始对等节点列表中指定的所有地址-端口对。

participant 的初始对等节点列表包含其将与之通信的所有其他 participant 的地址-端口对。该列表包含 participant 在单播发现机制中使用的地址，可与多播发现一起使用，也可作为其替代方案。因此，该方法也适用于无法使用多播功能的场景。

根据 RTPS 标准（第 9.6.1.1 节），participant 发现流量的单播监听端口按以下公式计算：7400 + 250 * _domainID_ + 10 + 2 * _participantID_。因此，例如 participant 在 Domain 0（默认域）中运行且 ID 为 1，其发现流量的单播监听端口为：7400 + 250 * 0 + 10 + 2 * 1 = 7412。默认情况下，_eProsima Fast RTPS_ 使用元流量多播定位器作为初始对等节点。

以下示例配置了一个初始对等节点列表，其中包含域 0 中主机 192.168.10.13 上 participant ID 为 1 的对等节点。

### C++
Locator_t initial_peers_locator; IPLocator::setIPv4(initial_peers_locator, "192.168.10.13"); initial_peers_locator.port = 7412; participant_attr.rtps.builtin.initialPeersList.push_back(initial_peers_locator); 

### XML
<participant profile_name="initial_peers_example_profile" is_default_profile="true" > <rtps> <builtin> <initialPeersList> <locator> <udpv4> <address> 192.168.10.13 </address> <port> 7412 </port> </udpv4> </locator> </initialPeersList> </builtin> </rtps> </participant> 

## 9.4.5 接口白名单
有时可能希望阻止某些网络接口，以避免通过这些接口建立连接或发送数据。可以使用传输描述符中的 _interface whitelist_ 字段管理此项功能，借此

设置希望用于发送或接收数据包的接口。此列表中的值应与机器在相应网络中的 IP 匹配。例如：

**C++** UDPv4TransportDescriptor descriptor; descriptor.interfaceWhiteList.emplace_back("127.0.0.1"); **XML** 

<transport_descriptors> <transport_descriptor> <transport_id> CustomTransport </transport_id> <type> UDPv4 </type> <interfaceWhiteList> <address> 127.0.0.1 </address> </interfaceWhiteList> </transport_descriptor> <transport_descriptor> 

## 9.4.6 提示
**禁用所有多播流量**

### C++
_// Metatraffic Multicast Locator List will be empty. // Metatraffic Unicast Locator List will contain one locator, with null address and null port. // Then eProsima Fast RTPS will use all network interfaces to receive network messages using a well-known port._ Locator_t default_unicast_locator; participant_attr.rtps.builtin.metatrafficUnicastLocatorList.push_back(default unicast_locator); 

_// Initial peer will be UDPv4 addresss 192.168.0.1. The port will be a well-known port. // Initial discovery network messages will be sent to this UDPv4 address._ Locator_t initial_peer; IPLocator::setIPv4(initial_peer, 192, 168, 0, 1); participant_attr.rtps.builtin.initialPeersList.push_back(initial_peer); 

### XML
<participant profile_name="disable_multicast" is_default_profile="true" > <rtps> <builtin> <metatrafficUnicastLocatorList> <locator/> </metatrafficUnicastLocatorList> <initialPeersList> <locator> <udpv4> <address> 192.168.0.1 </address> </udpv4> </locator> </initialPeersList> </builtin> </rtps> </participant> 

### 套接字上的非阻塞写入
对于 UDP 传输，可以配置套接字是否使用非阻塞写入调用。

### C++
_//Create a descriptor for the new transport._ **auto** non_blocking_UDP_transport = std::make_shared<UDPv4TransportDescriptor>(); non_blocking_UDP_transport->non_blocking_send = false; _//Disable the built-in Transport Layer._ participant_attr.rtps.useBuiltinTransports = false; _//Link the Transport Layer to the Participant._ participant_attr.rtps.userTransports.push_back(non_blocking_UDP_transport); 

### XML
<transport_descriptors> <transport_descriptor> <transport_id> non_blocking_transport </transport_id> <type> UDPv4 </type> <non_blocking_send> false </non_blocking_send> </transport_descriptor> </transport_descriptors> <participant profile_name="non_blocking_transport" > <rtps> <userTransports> <transport_id> non_blocking_transport </transport_id> </userTransports> <useBuiltinTransports> false </useBuiltinTransports> </rtps> </participant> 

### XML 配置
_XML 配置文件_ 一节完整说明了如何通过 _XML 文件_ 设置 _Fast RTPS_。

# 9.5 流控制器
_eProsima Fast RTPS_ 支持在 Publisher 和 Participant 级别配置用户流控制器。根据所实现的控制器类型，这些控制器可用于在特定条件下限制要发送的数据量。

当前发行版实现吞吐量控制器，可用于限制每个时间单位通过网络发送的总消息吞吐量。要使用它们，必须将描述符传入 Participant 或 Publisher 属性。

### C++
_// Limit to 300kb per second._ ThroughputControllerDescriptor slowPublisherThroughputController{300000, 1000}; publisher_attr.throughputController = slowPublisherThroughputController; **XML** 

<publisher profile_name="publisher_profile_qos_flowcontroller" > <throughputController> <bytesPerPeriod> 300000 </bytesPerPeriod> <periodMillisecs> 1000 </periodMillisecs> </throughputController> </publisher> 

在 Writer-Reader 层中，吞吐量控制器是内置的，描述符默认使用无限吞吐量。要更改这些值：

WriterAttributes writer_attr; writer_attr.throughputController.bytesPerPeriod = 300000; _//300kb_ writer_attr.throughputController.periodMillisecs = 1000; _//1000ms //CONF-QOS-PUBLISHMODE // Allows fragmentation._ publisher_attr.qos.m_publishMode.kind = ASYNCHRONOUS_PUBLISH_MODE; 

请注意，如果指定的吞吐量控制器大小小于套接字大小，消息可能始终无法发送。

# 9.6 发送大数据
_eProsima Fast RTPS_ 使用的默认消息大小是较保守的 65Kb。如果 Topic 数据更大，则必须对其进行分片。

分片消息会按特定传输层可理解的方式通过多个数据包发送。为此，必须将 Publisher 配置为异步模式。

### C++
_// Allows fragmentation._ publisher_attr.qos.m_publishMode.kind = ASYNCHRONOUS_PUBLISH_MODE; 

### XML
<publisher profile_name="publisher_profile_qos_publishmode" > <qos> <publishMode> <kind> ASYNCHRONOUS </kind> </publishMode> </qos> </publisher>


在 Writer-Subscriber 层中，必须配置 Writer：

WriterAttributes write_attr; write_attr.mode = ASYNCHRONOUS_WRITER; _// Allows fragmentation_ 

请注意，在 best-effort 模式下，如果发送大数据过快且缓冲区填满速度超过客户端处理消息的速度，消息可能丢失。另一方面，在 reliable 模式下，大量数据分片可能降低消息接收频率。如果出现这种情况，可以按照 _增大套接字缓冲区大小_ 中所述，通过增大套接字缓冲区大小来解决。按照 _调优 Reliable 模式_ 中所述，在 reliable 模式下设置更短的 Heartbeat 周期也可能有帮助。

发送大数据时，宜设置流控制器，以避免网络中出现消息突发并提升性能。参见 _流控制器_。

## 9.6.1 示例：发送单个大文件
以下示例说明如何配置应用以获得最佳性能。为使示例更具体，假设文件大小为 9.9MB，publisher 和 subscriber 所在网络的带宽为 100MB/s。

首先，必须在 publisher 参数中启用异步模式。然后，必须选择合适的可靠性模式。在本例中，确保收到消息的所有分片很重要。丢失一个分片就意味着丢失整条消息，因此最好选择 reliable 模式。

使用 UDPv4 传输时，这些分片的默认消息大小为 65Kb（包括为数据和消息头预留的空间）。这意味着 publisher 至少要写入约 1100 个分片。

如此多的分片可能拖慢传输，因此可以考虑缩短 heartbeat 周期，以提高 publisher 的响应速度。

另一个重要考虑因素是添加流控制器。如果没有流控制器，publisher 可能占用全部带宽。对于此应用，合理的流控制器限制可以是 5MB/s，仅占总带宽的 5%。不过，这些值高度依赖于具体应用及其期望行为。

最后还有一个细节需要注意：检查系统 UDP 缓冲区大小至关重要。在 Linux 中，可以使用以下命令增大缓冲区：

sysctl -w net.ipv4.udp_mem="102400 873800 16777216" sysctl -w net.core.netdev_max_backlog="30000" sysctl -w net.core.rmem_max="16777216" sysctl -w net.core.wmem_max="16777216" 

## 9.6.2 示例：视频流
在本示例中，目标应用在 publisher 和 subscriber 之间传输视频。该视频的分辨率为 640x480，帧率为 50fps。

与上一示例相同，由于应用发送的数据需要分片，必须在 publisher 参数中启用异步模式。

在音频或视频传输中，稳定且高数据率的传输有时比 100% 无损通信更合适。以 50Hz 频率工作时，每秒丢失一两个样本影响不大。因此，为了获得更高性能，可以将可靠性模式配置为 best-effort。

# 9.7 发现
作为 DDS 实现，Fast-RTPS 提供发现机制，可自动跨 participant 查找并匹配 publisher 和 subscriber，使它们能够开始共享数据。无论使用哪种机制，发现过程都分为两个阶段。

## 9.7.1 发现阶段
1. **参与者发现阶段（Participant Discovery Phase，PDP）**：在此阶段，participant 确认彼此的存在。为此，每个 participant 都会发送周期性公告消息，其中指定其监听传入元流量和用户数据的单播地址（IP 和端口）等信息。两个 participant 位于同一域时会相互匹配。默认情况下，公告消息使用众所周知的多播地址和端口（根据域计算）发送。此外，可以指定地址列表以通过单播发送公告（参见 _初始对等节点_）。还可以配置此类公告的周期（参见 _发现配置_）。

2. **端点发现阶段（Endpoint Discovery Phase，EDP）**：在此阶段，publisher 和 subscriber 确认彼此。为此，participant 使用 PDP 期间建立的通信通道相互共享其 publisher 和 subscriber 的信息。该信息包括 Topic 和数据类型等。两个端点要匹配，其 Topic 和数据类型必须一致。publisher 和 subscriber 匹配后，即可发送/接收用户数据流量。

## 9.7.2 发现机制
Fast-RTPS 提供以下发现机制：

- _简单发现（Simple Discovery）_：这是默认机制。它遵循 RTPS 标准中的 PDP 和 EDP 阶段，因此可与任何其他 DDS 和 RTPS 实现兼容。

- _静态发现（Static Discovery）_：该机制在 PDP 阶段使用 Simple Participant Discovery Protocol（SPDP，如 RTPS 标准所规定），但当所有 publisher 和 subscriber 的地址、端口、数据类型和 Topic 都已知时，可以跳过 Simple Endpoint Discovery Protocol（SEDP）阶段。

- _服务器-客户端发现（Server-Client Discovery）_：该发现机制使用集中式发现架构，服务器充当发现元流量的枢纽。

- **手动发现（Manual Discovery）**：该机制仅与 RTPSDomain 层兼容。它禁用 PDP 发现阶段，允许用户使用自行选择的外部元信息通道手动匹配和取消匹配 RTPS participant、reader 和 writer。

## 9.7.3 通用发现设置
部分发现设置由不同发现机制共享：

|名称|说明|类型|默认值|
|---|---|---|---|
|_Discovery_<br>_Protocol_|要使用的发现协议（参见 _发现机制_）|DiscoveryProtocol|_t<br>SIMPLE|
|_Ignore_<br>_Participant_<br>_flags_|筛选同一进程、不同进程或不同主机中 participant 的发现流量|ParticipantFilter|ingFlags_t<br>NO_FILTER|
|_Lease_<br>_Duration_|指示远程 participant 应在多长时间内认为本地 participant 存活。|Duration_t|20 s|
|_Announce-_<br>_ment Period_|participant 发送 PDP 公告的周期。|Duration_t|3 s|



### 发现协议
指定要使用的发现协议（参见 _发现机制_）。可选值如下：

|发现<br>机制|可选<br>值|说明|
|---|---|---|
|Simple|SIMPLE|RTPS 标准规定的简单发现协议|
|Static|STATIC|使用 SPDP，并由 XML 文件手动指定 EDP|
|服务器-<br>客户端|SERVER|participant 充当发现流量的枢纽，接收并分发发现信息。|
||CLIENT|participant 充当发现流量的客户端。它将自己的发现信息发送到服务器，并从服务器接收所有其他发现信息。|
||BACKUP|创建带有持久化 SQLite 数据库的 SERVER participant。BACKUP 服务器可以在启动时加载数据库。此类服务器使服务器-客户端架构能够抵御服务器销毁。|
|Manual|NONE|禁用 PDP 阶段，因此也不存在 EDP 阶段。所有匹配都必须通过 `addReaderLocator`、`addReaderProxy` 和 `addWriterProxy` 方法手动完成。|



### C++
participant_attr.rtps.builtin.discovery_config.discoveryProtocol = DiscoveryProtocol_t::SIMPLE; 

### XML
<participant profile_name="participant_discovery_protocol" > <rtps> <builtin> <discovery_config> <discoveryProtocol> SIMPLE </discoveryProtocol> </discovery_config> </builtin> </rtps> </participant> 

### 忽略 Participant 标志
定义在收到发现流量时忽略其中一部分的过滤器。这有助于增加一层 participant 隔离。可选值如下：

|可选值|说明|
|---|---|
|NO_FILTER|处理所有发现流量。|
|FILTER_DIFFERENT_HOST|丢弃来自其他主机的发现流量。|
|FILTER_DIFFERENT_PROCESS|丢弃来自同一主机上其他进程的发现流量。|
|FILTER_SAME_PROCESS|丢弃来自 participant 自身进程的发现流量。|
|FILTER_DIFFERENT_PROCESS |<br>FILTER_SAME_PROCESS|丢弃来自 participant 自身主机的发现流量。|



### C++
participant_attr.rtps.builtin.discovery_config.ignoreParticipantFlags = **static_cast** <ParticipantFilteringFlags_t>( ParticipantFilteringFlags_t::FILTER_DIFFERENT_PROCESS | ParticipantFilteringFlags_t::FILTER_SAME_PROCESS); 

### XML
<participant profile_name="participant_discovery_ignore_flags" > <rtps> <builtin> <discovery_config> <ignoreParticipantFlags> FILTER_DIFFERENT_PROCESS | FILTER_SAME PROCESS </ignoreParticipantFlags> </discovery_config> </builtin> </rtps> </participant> 

### 租约时长
指示远程 participant 应在多长时间内认为本地 participant 存活。如果本地 participant 未在该时间内声明活跃性，远程 participant 会认为本地 participant 已失效，并销毁有关该本地 participant 及其所有端点的全部信息。

只要远程 participant 收到来自本地 participant 的任何类型流量，就会在远程 participant 处声明本地 participant 活跃。

租约时长使用 `Duration_t` 指定，以秒和纳秒表示。

### C++
participant_attr.rtps.builtin.discovery_config.leaseDuration = Duration_t(10, 20); 

### XML
<participant profile_name="participant_discovery_lease_duration" > <rtps> <builtin> <discovery_config> <leaseDuration> <sec> 10 </sec> <nanosec> 20 </nanosec> </leaseDuration> </discovery_config> </builtin> </rtps> </participant> 

### 公告周期
该参数指定 participant PDP 公告的周期。为保证活跃性，建议公告周期短于租约时长，以便即使没有数据流量也能声明 participant 活跃。请注意，设置公告周期存在权衡：公告过于频繁会使网络中充斥元流量，而公告过于稀疏会延迟后加入者的发现。

Participant 的公告周期使用 `Duration_t` 指定，以秒和纳秒表示。

### C++
participant_attr.rtps.builtin.discovery_config.leaseDuration_announcementperiod = Duration_t(1, 2); 

### XML
<participant profile_name="participant_discovery_lease_announcement" > <rtps> <builtin> <discovery_config> <leaseAnnouncement> <sec> 1 </sec> <nanosec> 2 </nanosec> </leaseAnnouncement> </discovery_config> </builtin> </rtps> </participant> 

## 9.7.4 SIMPLE 发现设置
SIMPLE 发现协议负责通过 RTPS 协议通信的各类 RTPS 实体之间建立端到端连接。Fast-RTPS 实现 SIMPLE 发现协议，以提供与 RTPS 标准的兼容性。规范将 SIMPLE 发现协议拆分为两个独立协议：

- **Simple Participant Discovery Protocol（SPDP，简单参与者发现协议）：** 规定 Participant 如何在网络中相互发现；它公告并检测域中 participant 的存在。

- **Simple Endpoint Discovery Protocol（SEDP，简单端点发现协议）：** 定义已发现 participant 为发现彼此包含的 RTPS 实体（即 writer 和 reader 端点）而交换信息时采用的协议。

|名称|说明|
|---|---|
|_Initial Announcements_|定义 RTPSParticipant 初始公告的行为。|
|_Simple EDP Attributes_|定义将 SIMPLE 协议用作发现协议。|
|_Initial Peers_|SPDP 公告发送到的端点列表。|



### 初始公告
RTPS 标准的简单发现机制要求 participant 发送公告。这些公告不以保证可靠的方式投递，可能会被网络丢弃。为避免消息丢弃造成发现延迟，可以将初始公告设置为多次发送，以提高被正确接收的概率。

初始公告仅在创建 participant 时进行。该阶段结束后，只强制发送基于 `leaseDuration_announcementperiod` 周期的标准公告（而不是 `initial_announcements.period`）。

|名称|说明|类型|默认值|
|---|---|---|---|
|count|定义启动时发送的公告数量。|uint32|5|
|period|定义初始公告的周期。|Duration_t|100ms|



### C++
participant_attr.rtps.builtin.discovery_config.initial_announcements.count = 5; participant_attr.rtps.builtin.discovery_config.initial_announcements.period = Duration_t(0,100000000u); 


![](fast-dds-docs-eprosima-com-en-v1.10.0_images/fast-dds-docs-eprosima-com-en-v1.10.0.pdf-0071-03.png)


<!-- Start of picture text -->
XML<br><participant profile_name="participant_profile_simple_discovery" ><br><rtps><br><builtin><br><discovery_config><br><initialAnnouncements><br><count> 5 </count><br><period><br><sec> 0 </sec><br><nanosec> 100000000 </nanosec><br></period><br></initialAnnouncements><br></discovery_config><br></builtin><br></rtps><br></participant><br><!-- End of picture text -->

### Simple EDP 属性
|名称|说明|类型|默认<br>值|
|---|---|---|---|
|SIMPLE EDP|定义将 SIMPLE 协议用作 EDP 阶段的发现协议。Participant 可以创建 publisher、subscriber、二者或无。|bool|true|
|Publication writer<br>and<br>Subscription<br>reader|适用于只实现一个或多个 publisher、即不实现 subscriber 的 participant。它允许仅创建与 subscriber 发现相关的 EDP 端点。|bool|true|
|Publication reader<br>and<br>Subscription<br>writer|适用于只实现一个或多个 subscriber、即不实现 publisher 的 participant。它允许仅创建与 publisher 发现相关的 EDP 端点。|bool|true|



### C++
participant_attr.rtps.builtin.discovery_config.use_SIMPLE_EndpointDiscoveryProtocol = true; participant_attr.rtps.builtin.discovery_config.m_simpleEDP.use PublicationWriterANDSubscriptionReader = true; participant_attr.rtps.builtin.discovery_config.m_simpleEDP.use PublicationReaderANDSubscriptionWriter = false; 

### XML
<participant profile_name="participant_profile_qos_discovery_edp" > <rtps> <builtin> <discovery_config> <EDP> SIMPLE </EDP> <simpleEDP> <PUBWRITER_SUBREADER> true </PUBWRITER_SUBREADER> <PUBREADER_SUBWRITER> false </PUBREADER_SUBWRITER> </simpleEDP> </discovery_config> </builtin> </rtps> </participant> 

### 初始对等节点
默认情况下，SPDP 协议在 participant 发现阶段使用众所周知的组播地址。使用 FastRTPS 时，可以按照 _初始对等节点_ 中的说明配置初始对等节点列表，从而扩展 participant 公告发送到的端点列表。

## 9.7.5 STATIC 端点发现设置
Fast-RTPS 允许在 EDP 阶段用静态版本替代 SEDP 协议，从而完全消除 EDP 元流量。当网络带宽有限且 publisher 和 subscriber 的模式已知时，这很有用。如果所有 publisher 和 subscriber 及其 Topic 和数据类型都已知，则可以用静态对等节点配置替代 EDP 阶段。请注意，这样做不会生成 EDP 发现元流量，并且只有配置中定义的对等节点能够通信。与 STATIC 端点发现相关的设置如下：

|名称|说明|
|---|---|
|_STATIC EDP_|启用 STATIC 端点发现协议。|
|_STATIC EDP XML 文件规范_|指定包含远程端点描述的 XML 文件。|
|_Initial Announcements_|定义 RTPSParticipant 初始公告的行为（PDP 阶段）。|



### STATIC EDP
要启用 STATIC EDP，必须在 participant 属性中禁用 SEDP。可以通过代码或 XML 配置文件完成：

### C++
participant_attr.rtps.builtin.discovery_config.use_SIMPLE_EndpointDiscoveryProtocol = false; participant_attr.rtps.builtin.discovery_config.use_STATIC_EndpointDiscoveryProtocol = true; 

### XML
<participant profile_name="participant_profile_static_edp" > <rtps> <builtin> <discovery_config> <EDP> STATIC </EDP> </discovery_config> </builtin> </rtps> </participant> 

### STATIC EDP XML 文件规范
由于启用 STATIC EDP 会抑制所有 EDP 元流量，必须使用专用 XML 文件静态指定远程实体（publisher 和 subscriber）的信息。一个 participant 可以加载多个此类配置文件，因此不同端点的信息既可以放在一个文件中，也可以拆分到多个文件中以保持条理。Fast-RTPS 提供实现该 EDP 发现协议的 Static Endpoint Discovery 示例。

下表说明 STATIC EDP XML 配置文件的所有可能属性。完整示例见 _STATIC EDP XML 示例_。

|名称|说明|值|默认值|
|---|---|---|---|
|<userId>|必填。唯一标识端点。|uint16_t|0|
|<entityID>|端点的 EntityId。|uint16_t|0|
|<expectsI|nlineQos>|指示是否要求内联 QoS（仅限 **reader**）。|bool|false|
|<topicNam|e>|必填。<br>远程端点的 Topic。<br>应与本地 participant 的某个 Topic 匹配。|string_255||
|<topicDat|aType>|必填。Topic 的数据类型。|string_255||
|<topicKin|d>|Topic 类型。|NO_KEY<br>WITH_KEY|NO_KEY|
|<partitio|nQos>|远程对等节点的一个 Partition 名称。重复设置可配置多个 Partition。|string||
|<unicastL|ocator>|participant 的单播定位器。参见 _定位器定义_。|||
|<multicas|tLocator>|participant 的多播定位器。参见 _定位器定义_。|||
|<reliabil|ityQos>|参见 _可靠性_ 一节。|BEST_EFFORT_REL<br>RELIABLE_RELIAB|IABILITY_QOS<br>BEST_EFFORT_RELIABILITY_QOS<br>ILITY_QOS|
|<durabili|tyQos>|参见 _设置数据持久性类型_ 一节。|VOLATILE_DURABI<br>TRANSIENT_LOCAL<br>TRANSIENT_DURAB|LITY_QOS<br>VOLATILE_DURABILITY_QOS<br>_DURABILITY_QOS<br>ILITY_QOS|
|<ownershi|pQos>|参见 _Ownership QoS_。|||
|<liveline|ssQos>|定义远程对等节点的活跃性。参见 _Liveliness QoS_。|||



### 定位器定义
远程对等节点的定位器使用 `<unicastLocator>` 和 `<multicastLocator>` 标签配置。这些标签不取值，定位器通过标签属性定义。使用 `<unicastLocator>` 和 `<multicastLocator>` 定义的定位器会累积，因此可以重复使用它们，为同一个对等节点指定多个远程端点定位器。

- `address`：必填字符串，表示定位器地址。

- `port`：可选的 `uint16_t`，表示该地址上的端口。

### Ownership QoS
Topic 的所有权可以使用 `<ownershipQos>` 标签配置。该标签不取值，配置通过标签属性完成：

- `kind`：可为 `SHARED_OWNERSHIP_QOS` 或 `EXCLUSIVE_OWNERSHIP_QOS`。该属性在标签内为必填项。

- `strength`：可选的 `uint32_t`，指定远程 participant 拥有该 Topic 的强度。该属性**只能**在 writer 上设置。如果未指定，默认值为零。

### Liveliness QoS
远程对等节点的 _Liveliness_ 使用 `<livelinessQos>` 标签配置。该标签不取值，配置通过标签属性完成：

- `kind`：可为 `AUTOMATIC_LIVELINESS_QOS`、`MANUAL_BY_PARTICIPANT_LIVELINESS_QOS` 或 `MANUAL_BY_TOPIC_LIVELINESS_QOS`。该属性在标签内为必填项。

- `leaseDuration_ms`：可选的 `UInt32`，指定远程对等节点的租约时长。特殊值 `INF` 可用于表示无限租约时长。如果未指定，默认值为 `INF`。

### STATIC EDP XML 示例
以下是两个远程 participant（一个 publisher 和一个 subscriber）的完整配置 XML 文件示例。此配置**必须**与创建远程端点时使用的配置一致，否则端点之间的通信可能受到影响。如果缺少任何非必需元素，将采用默认值。通常，远程端点创建时指定的所有元素都应在此配置。

### XML
<staticdiscovery> <participant> <name> HelloWorldSubscriber </name> <reader> <userId> 3 </userId> <entityId> 4 </entityId> <expectsInlineQos> true </expectsInlineQos> <topicName> HelloWorldTopic </topicName> <topicDataType> HelloWorld </topicDataType> <topicKind> WITH_KEY </topicKind> <partitionQos> HelloPartition </partitionQos> <partitionQos> WorldPartition </partitionQos> <unicastLocator address="192.168.0.128" port="5000" /> <unicastLocator address="10.47.8.30" port="6000" /> <multicastLocator address="239.255.1.1" port="7000" /> <reliabilityQos> BEST_EFFORT_RELIABILITY_QOS </reliabilityQos> <durabilityQos> VOLATILE_DURABILITY_QOS </durabilityQos> <ownershipQos kind="SHARED_OWNERSHIP_QOS" /> <livelinessQos kind="AUTOMATIC_LIVELINESS_QOS" leaseDuration_ms="1000" /> </reader> </participant> <participant> <name> HelloWorldPublisher </name> <writer> <unicastLocator address="192.168.0.120" port="9000" /> <unicastLocator address="10.47.8.31" port="8000" /> <multicastLocator address="239.255.1.1" port="7000" /> <userId> 5 </userId> <entityId> 6 </entityId> <topicName> HelloWorldTopic </topicName> <topicDataType> HelloWorld </topicDataType> <topicKind> WITH_KEY </topicKind> <partitionQos> HelloPartition </partitionQos> <partitionQos> WorldPartition </partitionQos> <reliabilityQos> BEST_EFFORT_RELIABILITY_QOS </reliabilityQos> <durabilityQos> VOLATILE_DURABILITY_QOS </durabilityQos> <ownershipQos kind="SHARED_OWNERSHIP_QOS" strength="50" /> <livelinessQos kind="AUTOMATIC_LIVELINESS_QOS" leaseDuration_ms="1000" /> </writer> </participant> </staticdiscovery> 

### 加载 STATIC EDP XML 文件
静态发现的远程端点**必须**在其配置文件中定义唯一的 `userID`，该值**必须**与发现配置 XML 中指定的值一致。这通过设置实体属性上的用户 ID 完成：

### C++
SubscriberAttributes sub_attr; sub_attr.setUserDefinedID(3); PublisherAttributes pub_attr; pub_attr.setUserDefinedID(5); 

### XML
<publisher profile_name="publisher_xml_conf_static_discovery" > <userDefinedID> 3 </userDefinedID> </publisher> <subscriber profile_name="subscriber_xml_conf_static_discovery" > <userDefinedID> 5 </userDefinedID> </subscriber> 

在本地 participant 上，通过以下方式加载 STATIC EDP 配置文件：

### C++
participant_attr.rtps.builtin.discovery_config.setStaticEndpointXMLFilename( "RemotePublisher.xml"); participant_attr.rtps.builtin.discovery_config.setStaticEndpointXMLFilename( "RemoteSubscriber.xml"); 

### XML
<participant profile_name="participant_profile_static_load_xml" > <rtps> <builtin> <discovery_config> <staticEndpointXMLFilename> RemotePublisher.xml </ staticEndpointXMLFilename> <staticEndpointXMLFilename> RemoteSubscriber.xml </ staticEndpointXMLFilename> </discovery_config> </builtin> </rtps> </participant> 

## 9.7.6 服务器-客户端发现
该机制基于客户端-服务器发现范式，即由一个或多个服务器 participant 管理元流量（participant 之间为识别彼此而交换的消息）（左图）；与之相对，简单发现（右图）使用 IP 多播协议等消息广播机制交换元流量。


![](fast-dds-docs-eprosima-com-en-v1.10.0_images/fast-dds-docs-eprosima-com-en-v1.10.0.pdf-0077-01.png)


### 关键概念
在该架构中，需要理解以下关键概念：

- 服务器-客户端发现机制复用 RTPS 发现消息结构以及标准 RTPS writer 和 reader。

- 发现服务器 participant 可以是 _client_ 或 _server_。它们之间的唯一区别是处理元流量的方式。用户流量（即它们创建的 publisher 和 subscriber 之间的流量）与角色无关。

- 所有 _server_ 和 _client_ 的发现信息都会与关联的 _client_ 共享；这些信息还会与其关联的 _server_ 共享。请注意，一个 _server_ 可以作为其他 _server_ 的 _client_。

- _Client_ 需要预先了解其要连接的 _server_。这基本上归结为 _server_ 身份（下文称为 GuidPrefix）以及 _server_ 监听的一组定位器。这些定位器还定义 client 联系 _server_ 时使用的传输协议（UDP 或 TCP）。

   - GuidPrefix 是 RTPS 标准中的 participant 唯一标识符，是一个 12 字节链。由于每条标准 RTPS 消息都包含该信息，客户端可据此判断消息是否来自正确的服务器。

   - 使用 GuidPrefix 是因为服务器的 IP 地址可能不足以可靠标识服务器：同一台机器上可以托管多个服务器，因此它们可能具有相同 IP；此外，多播地址也可以作为有效地址。

- _Server_ 不需要预先了解其 _client_，但其 GuidPrefix 和定位器列表（即监听位置）必须与提供给 _client_ 的值一致。

为收集 _client_ 发现信息，采用以下握手策略：

- _Client_ 按固定间隔（ping 周期）向 _server_ 发送呼叫消息，直到收到消息接收确认。

- _Server_ 收到呼叫消息后，不会立即与新加入者共享 publisher 或 subscriber 信息，而是仅按固定间隔（匹配周期）触发此过程。调整该周期可以捆绑发现信息，从而更高效地投递。

为说明在编译时（源代码）或运行时（XML 文件）如何配置此发现机制，我们将其分为两节：一节聚焦主要概念（_按概念配置_），另一节聚焦主要属性结构和 XML 标签（_按属性配置_）。

### 按概念配置服务器-客户端
|概念|说明|
|---|---|
|_发现协议_|如何使 participant 成为 _client_ 或 _server_。|
|_服务器唯一 ID_|如何将 _clients_ 关联到 _servers_。|
|_设置传输_|如何指定要使用的传输并使 _servers_ 可访问。|
|_Ping 周期_|如何微调服务器-客户端握手。|
|_匹配周期_|如何微调服务器投递效率。|



### 在客户端和服务器之间选择
这由通用属性 _Discovery Protocol_ 设置。一个 participant 只能扮演一个角色（尽管 _server_ 可以作为其他服务器的 _client_）。由于该值默认为 _simple_，因此必须填写。与服务器-客户端发现关联的值在 _发现设置_ 一节中说明。以下示例展示如何管理相应枚举属性和 XML 标签：

ParticipantAttributes.rtps.builtin.discovery_config.discoveryProtocol 

dds>profiles>participant>rtps>builtin>discovery_config>discoveryProtocol 

### C++
DiscoverySettings & ds = participant_attr.rtps.builtin.discovery_config; ds.discoveryProtocol = DiscoveryProtocol_t::CLIENT; ds.discoveryProtocol = DiscoveryProtocol_t::SERVER; ds.discoveryProtocol = DiscoveryProtocol_t::BACKUP; 

### XML
<participant profile_name="participant_discovery_protocol_alt" > <rtps> <builtin> <discovery_config> <discoveryProtocol> CLIENT </discoveryProtocol> _<!-- alternatives <discoveryProtocol>SERVER</discoveryProtocol> <discoveryProtocol>BACKUP</discoveryProtocol> -->_ </discovery_config> </builtin> </rtps> </participant> 

**服务器唯一标识符 GuidPrefix**

该标识符属于 RTPS 规范，唯一标识每个 DDS participant。它由 12 个字节组成，是 DDS 域中的 key。在服务器-客户端发现中，其作用是将 _server_ 与其 _clients_ 关联起来。请注意，辅助方法 **ReadguidPrefix** 可使用字符串填充 GuidPrefix。必须在 _server 侧_ 和 _client 侧_ 设置中指定该值。

### 服务器侧设置
以下示例展示如何管理相应枚举属性和 XML 标签：

ParticipantAttributes.rtps.prefix 

dds>profiles>participant>rtps>prefix 

### C++
participant_attr.rtps.ReadguidPrefix("4D.49.47.55.45.4c.5f.42.41.52.52.4f"); 

### XML
<participant profile_name="participant_server_guidprefix" > <rtps> <prefix> 4D.49.47.55.45.4c.5f.42.41.52.52.4f </prefix> </rtps> </participant> 

请注意，一个 _server_ 可以作为其他 _servers_ 的 _client_。因此，下一节也可能适用。

### 客户端侧设置
每个 _client_ 必须维护其要关联的 _servers_ 列表。每个元素表示一个单独的服务器，并且必须提供 GuidPrefix。_server_ 列表对应以下属性：

ParticipantAttributes.rtps.builtin.discovery_config.m_DiscoveryServers 

并且必须使用具有有效 `guidPrefix` 成员的 `RemoteServerAttributes` 对象填充。在 XML 中，服务器列表及其元素会同时指定。请注意，prefix 是 `RemoteServer` 标签的属性。

dds>profiles>participant>rtps>builtin>discovery_config>discoveryServerList> RemoteServer@prefix 

### C++
RemoteServerAttributes server; server.ReadguidPrefix("4D.49.47.55.45.4c.5f.42.41.52.52.4f"); DiscoverySettings & ds = participant_attr.rtps.builtin.discovery_config; ds.m_DiscoveryServers.push_back(server); 

### XML
<participant profile_name="participant_profile_discovery_client_prefix" > <rtps> <builtin> <discovery_config> <discoveryServersList> <RemoteServer prefix="4D.49.47.55.45.4c.5f.42.41.52.52.4f" > <metatrafficUnicastLocatorList> <locator/> </metatrafficUnicastLocatorList> </RemoteServer> </discoveryServersList> </discovery_config> </builtin> </rtps> </participant> 

### 服务器定位器列表
每个 _server_ 必须指定可访问它的有效定位器。必须为任何 _client_ 提供适当的定位器，以便访问其每个 _server_。与上一节相同，这里也分为 _server_ 侧和 _client_ 侧设置。

### 服务器侧设置
以下示例展示如何设置定位器列表属性（注意发现策略只处理元流量属性）和 XML 标签：

ParticipantAttributes.rtps.builtin. (metatrafficMulticastLocatorList|metatrafficUnicastLocatorList) 

dds>profiles>participant>rtps>builtin> (metatrafficMulticastLocatorList|metatrafficUnicastLocatorList) 

### C++
eprosima::fastrtps::rtps::Locator_t locator; IPLocator::setIPv4(locator, 192, 168, 1 , 133); locator.port = 64863; 

LocatorList_t & ull = participant_attr.rtps.builtin.metatrafficUnicastLocatorList; ull.push_back(locator); 

### XML
<participant profile_name="participant_profile_discovery_server_server_metatraffic" > <rtps> <builtin> <metatrafficUnicastLocatorList> <locator> <udpv4> _<!-- placeholder server UDP address -->_ <address> 192.168.1.113 </address> <port> 64863 </port> </udpv4> </locator> </metatrafficUnicastLocatorList> </builtin> </rtps> </participant> 

请注意，一个 _server_ 可以作为其他 _servers_ 的 client，因此下一节也可能适用。

### 客户端侧设置
每个 _client_ 必须维护与其要关联的 _servers_ 对应的定位器列表。每个 _server_ 指定自己的定位器。定位器列表对应以下属性：

ParticipantAttributes.rtps.builtin.discovery_config.m_DiscoveryServers 

并且必须使用具有有效 `metatrafficUnicastLocatorList` 或 `metatrafficMulticastLocatorList` 成员的 `RemoteServerAttributes` 对象填充。在 XML 中，服务器列表及其元素会同时指定。请注意 `RemoteServer` 标签的 `metatrafficUnicastLocatorList` 或 `metatrafficMulticastLocatorList` 属性。

dds>profiles>participant>rtps>builtin>discovery_config>discoveryServerList> RemoteServer@metatrafficUnicastLocatorList dds>profiles>participant>rtps>builtin>discovery_config>discoveryServerList> RemoteServer@metatrafficMulticastLocatorList 

### C++
eprosima::fastrtps::rtps::Locator_t locator; IPLocator::setIPv4(locator, 192, 168, 1 , 133); locator.port = 64863; RemoteServerAttributes server; server.metatrafficUnicastLocatorList.push_back(locator); 

DiscoverySettings & ds = participant_attr.rtps.builtin.discovery_config; ds.m_DiscoveryServers.push_back(server); 

### XML
<participant profile_name="participant_profile_discovery_server_client_metatraffic" > <rtps> <builtin> <discovery_config> <discoveryServersList> <RemoteServer prefix="4D.49.47.55.45.4c.5f.42.41.52.52.4f" > <metatrafficUnicastLocatorList> <locator> <udpv4> _<!-- placeholder server UDP address -->_ <address> 192.168.1.113 </address> <port> 64863 </port> </udpv4> </locator> </metatrafficUnicastLocatorList> </RemoteServer> </discoveryServersList> </discovery_config> </builtin> </rtps> </participant> 

### 客户端 ping 周期
如 _上文_ 所述，_clients_ 按固定间隔（ping 周期）向 _servers_ 发送呼叫消息，直到收到消息接收确认。该周期由以下成员指定：

ParticipantAttributes.rtps.builtin.discovery_config.discoveryServer_client_syncperiod 

或由以下 XML 标签指定：

dds>profiles>participant>rtps>builtin>discovery_config>clientAnnouncementPeriod 

### C++
DiscoverySettings & ds = participant_attr.rtps.builtin.discovery_config; ds.discoveryServer_client_syncperiod = Duration_t(0,250000000); 

### XML
<participant profile_name="participant_profile_client_ping" > <rtps> <builtin> <discovery_config> <clientAnnouncementPeriod> _<!-- change default to 250 ms -->_ <nanosec> 250000000 </nanosec> </clientAnnouncementPeriod> </discovery_config> </builtin> </rtps> </participant> 

### 服务器匹配周期
如 _上文_ 所述，_Servers_ 会收到呼叫消息，但不会立即与新加入者共享 publisher 或 subscriber 信息，而是仅按固定间隔（匹配周期）触发此过程。请注意，该成员与 _client_ 设置共用，但其名称仅指 _client_ 功能。该周期由以下成员指定：

ParticipantAttributes.rtps.builtin.discovery_config.discoveryServer_client_syncperiod 

或由以下 XML 标签指定：

dds>profiles>participant>rtps>builtin>discovery_config>clientAnnouncementPeriod 

### C++
DiscoverySettings & ds = participant_attr.rtps.builtin.discovery_config; ds.discoveryServer_client_syncperiod = Duration_t(0,250000000); 

### XML
<participant profile_name="participant_profile_server_ping" > <rtps> <builtin> <discovery_config> <clientAnnouncementPeriod> _<!-- change default to 250 ms -->_ <nanosec> 250000000 </nanosec> </clientAnnouncementPeriod> </discovery_config> </builtin> </rtps> </participant> 

### 按属性配置服务器-客户端
与服务器-客户端发现相关的设置如下：

|名称|说明|
|---|---|
|_RTPSParticipantAt_|_tributes_<br>指定 participant 的通用设置。为了正确配置 Server（例如 GuidPrefix），其中某些设置必须修改。|
|_BuiltinAttributes_|上述 _RTPSParticipantAttributes_ 结构的成员。用于指定一些必需的服务器发现设置，例如服务器监听客户端发现信息的地址。|
|_DiscoverySettings_|上述 _BuiltinAttributes_ 结构的成员。用于指定必需的客户端设置和可选的服务器设置，例如它作为客户端还是服务器、关联的服务器列表，或 client-ping 与 server-match 频率。|



### RTPSParticipantAttributes
`GuidPrefix_t guidPrefix` 成员指定服务器的身份。仅当 `discovery_config.discoveryProtocol` 为 **SERVER** 或 **BACKUP** 时，该成员才有意义。可以使用 `ReadguidPrefix` 方法，从格式类似 "4D.49.47.55.45.4c.5f.42.41.52.52.4f" 的字符串轻松填充该成员（注意每个字节都必须是有效的十六进制数）。

### C++
participant_attr.rtps.ReadguidPrefix("4D.49.47.55.45.4c.5f.42.41.52.52.4f"); 

### XML
<participant profile_name="participant_profile_discovery_client_prefix" > <rtps> <builtin> <discovery_config> <discoveryServersList> <RemoteServer prefix="4D.49.47.55.45.4c.5f.42.41.52.52.4f" > <metatrafficUnicastLocatorList> <locator/> </metatrafficUnicastLocatorList> </RemoteServer> </discoveryServersList> </discovery_config> </builtin> </rtps> </participant> 

### BuiltinAttributes
所有与发现相关的信息都汇集在 _DiscoverySettings_ `discovery_config` 成员中。

为了接收客户端元流量，必须使用提供给客户端的地址填充 `metatrafficUnicastLocatorList` 或 `metatrafficMulticastLocatorList`。

### C++
eprosima::fastrtps::rtps::Locator_t locator; IPLocator::setIPv4(locator, 192, 168, 1 , 133); locator.port = 64863; participant_attr.rtps.builtin.metatrafficUnicastLocatorList.push_back(locator); 

### XML
<participant profile_name="participant_profile_discovery_server_metatraffic" > <rtps> <builtin> <discovery_config> <discoveryProtocol> SERVER </discoveryProtocol> </discovery_config> <metatrafficUnicastLocatorList> <locator> <udpv4> _<!-- placeholder server UDP address -->_ <address> 192.168.1.113 </address> <port> 64863 </port> </udpv4> </locator> </metatrafficUnicastLocatorList> </builtin> </rtps> </participant> 

### DiscoverySettings
_discovery_protocol_ `discoveryProtocol` 成员指定 participant 的发现类型。如前所述，配置服务器-客户端发现时，该成员可为：

|枚举<br>值|说明|
|---|---|
|CLIENT|生成客户端 participant，它依赖一个或多个服务器获知其他客户端的存在。<br>该 participant 可以像普通 participant 一样，为任意 Topic（静态或动态）创建 publisher 和 subscriber。|
|SERVER|生成服务器 participant，它接收、管理并传播所关联客户端的元流量，确保各客户端都能获知其他客户端。该 participant 可以像普通 participant 一样，为任意 Topic（静态或动态）创建 publisher 和 subscriber。<br>服务器可以关联其他服务器，以共享其客户端信息。|
|BACKUP|生成在 **SERVER** 基础上增加功能的服务器 participant。具体而言，它使用数据库备份客户端信息，因此无论因何原因消失，都可以自动恢复，并继续向后来加入者传播元流量。相同场景中的 **SERVER** 需要重新收集客户端信息，从而引入恢复延迟。|



`RemoteServerList_t m_DiscoveryServers` 列出与客户端 participant 关联的服务器。仅当 _discovery_protocol_ 为 **CLIENT**、**SERVER** 或 **BACKUP** 时，该成员才有意义。其元素是 `RemoteServerAttributes` 对象，用于标识每个服务器并报告其可访问位置：

|属性|说明|
|---|---|
|GuidPrefix_t<br>guidPrefix|要关联的服务器 participant 的 RTPS 唯一标识符。<br>可以使用 `ReadguidPrefix` 方法，从格式类似 "4D.49.47.55.45.4c.<br>5f.42.41.52.52.4f" 的字符串轻松填充该成员。<br>（注意每个八位组都必须是有效的十六进制数）。|
|metatrafficU<br>和<br>metatrafficM|nicastLocatorList<br>ulticastLocatorList<br>是普通 `LocatorList_t`（参见 _LocatorListType_），必须用于指定服务器的定位器。至少应填充其中一个。|
|Duration_t<br>discoverySer|ver_client_syncperiod<br>仅当 _discovery_protocol_ 为 **CLIENT**、**SERVER** 或 **BACKUP** 时才有意义。<br>对于 _client_，它按 _关键概念_ 中所述指定 ping 周期。<br>当客户端尚未与服务器建立可靠连接时，它会持续 _ping_，直到服务器注意到它并建立连接。<br>对于 _server_，它按 _关键概念_ 中所述指定匹配周期。<br>当 _server_ 发现新的 _client_ 时，仅按固定间隔开始与其交换信息，以捆绑发现信息并优化投递。<br>默认值为半秒。|



### C++
RemoteServerAttributes server; server.ReadguidPrefix("4D.49.47.55.45.4c.5f.42.41.52.52.4f"); eprosima::fastrtps::rtps::Locator_t locator; IPLocator::setIPv4(locator, 192, 168, 1 , 133); locator.port = 64863; server.metatrafficUnicastLocatorList.push_back(locator); DiscoverySettings & ds = participant_attr.rtps.builtin.discovery_config; ds.discoveryProtocol = DiscoveryProtocol_t::CLIENT; ds.m_DiscoveryServers.push_back(server); ds.discoveryServer_client_syncperiod = Duration_t(0,250000000); 

### XML
<participant profile_name="participant_profile_client" > <rtps> <builtin> <discovery_config> <discoveryProtocol> CLIENT </discoveryProtocol> <discoveryServersList> <RemoteServer prefix="4D.49.47.55.45.4c.5f.42.41.52.52.4f" > <metatrafficUnicastLocatorList> <locator> <udpv4> _<!-- placeholder server UDP address -->_ <address> 192.168.1.113 </address> <port> 64863 </port> </udpv4> </locator> </metatrafficUnicastLocatorList> </RemoteServer> </discoveryServersList> <clientAnnouncementPeriod> _<!-- change default to 250 ms -->_ <nanosec> 250000000 </nanosec> </clientAnnouncementPeriod> </discovery_config> </builtin> </rtps> </participant> 

# 9.8 订阅发现话题
如 _发现_ 一节所述，Participant 或 RTPS Participant 在发现过程中使用一系列元数据端点。participant 监听器接口包含每次发现 Publisher 或 Subscriber 时调用的方法。这允许你创建自己的网络分析工具。

### 自定义监听器的实现
**class CustomParticipantListener** : **public** eprosima::fastrtps::ParticipantListener { _/* Custom Listener onSubscriberDiscovery */_ **void** onSubscriberDiscovery( eprosima::fastrtps::Participant * participant, eprosima::fastrtps::rtps::ReaderDiscoveryInfo && info) **override** { ( **void** )participant; **switch** (info.status) { **case** eprosima::fastrtps::rtps::ReaderDiscoveryInfo:: **DISCOVERED_READER** : _/* Process the case when a new subscriber was found in the domain */_ cout << "New subscriber for topic '" << info.info.topicName() << "' of type '" << info.info.typeName() << "' discovered"; **break** ; **case** eprosima::fastrtps::rtps::ReaderDiscoveryInfo:: **CHANGED_QOS_READER** : _/* Process the case when a subscriber changed its QOS */_ **break** ; **case** eprosima::fastrtps::rtps::ReaderDiscoveryInfo:: **REMOVED_READER** : _/* Process the case when a subscriber was removed from the domain */_ cout << "Subscriber for topic '" << info.info.topicName() << "' of type '" << info.info.typeName() << "' left the domain."; **break** ; } } _/* Custom Listener onPublisherDiscovery */_ **void** onPublisherDiscovery( eprosima::fastrtps::Participant * participant, eprosima::fastrtps::rtps::WriterDiscoveryInfo && info) **override** { ( **void** )participant; **switch** (info.status) { **case** eprosima::fastrtps::rtps::WriterDiscoveryInfo :: **DISCOVERED_WRITER** : _/* Process the case when a new publisher was found in the domain */_ cout << "New publisher for topic '" << info.info.topicName() << "' of type '" << info.info.typeName() << "' discovered"; **break** ; **case** eprosima::fastrtps::rtps::WriterDiscoveryInfo :: **CHANGED_QOS_WRITER** : _/* Process the case when a publisher changed its QOS */_ **break** ; **case** eprosima::fastrtps::rtps::WriterDiscoveryInfo :: **REMOVED_WRITER** : _/* Process the case when a publisher was removed from the domain */_ cout << "publisher for topic '" << info.info.topicName() << "' of type '" << info.info.typeName() << "' left the domain."; **break** ; } } }; **Setting the custom listener** _// Create Custom user ParticipantListener (should inherit from eprosima::fastrtps::ParticipantListener._ CustomParticipantListener *listener = **new** CustomParticipantListener(); _// Pass the listener on participant creation._ Participant* participant = Domain::createParticipant(participant_attr, listener); 

挂接到 EDP 的 `ReaderListener` 中定义的回调，会在内置协议处理完每条数据消息后执行。

# 9.9 调优
## 9.9.1 利用多播
对于有多个 subscriber 的 Topic，建议将其配置为使用多播而不是单播。这样，每个样本只发送一个网络数据包，可改善 CPU 和网络使用情况。多播配置见 _多播定位器_。

## 9.9.2 增大套接字缓冲区大小
在高数据率或大数据场景中，瓶颈可能是套接字缓冲区大小。由于套接字缓冲区没有空间，网络数据包可能被丢弃。使用 Reliable _Reliability_ 时，Fast RTPS 会尝试恢复丢失的样本，但需要付出重传代价。使用 Best-Effort _Reliability_ 时，样本将确定丢失。

默认情况下，_eProsima Fast RTPS_ 使用系统默认大小创建套接字缓冲区，但可以修改。`sendSocketBufferSize` 属性用于增大发送数据所用的套接字缓冲区。`listenSocketBufferSize` 属性用于增大读取数据所用的套接字缓冲区。

### C++
participant_attr.rtps.sendSocketBufferSize = 1048576; participant_attr.rtps.listenSocketBufferSize = 4194304; 

### XML
<participant profile_name="participant_xml_profile_qos_socketbuffers" > <rtps> <sendSocketBufferSize> 1048576 </sendSocketBufferSize> <listenSocketBufferSize> 4194304 </listenSocketBufferSize> </rtps> </participant> 

### 查明系统最大值
Linux 操作系统会设置套接字缓冲区的最大值。在 _Fast RTPS_ 中设置套接字缓冲区大小时，所设值不能超过系统最大值。

可以使用 `sysctl` 命令获取这些值。发送数据所用套接字缓冲区的最大大小可通过以下命令获取：

$> sudo sysctl -a | grep net.core.wmem_max net.core.wmem_max = 1048576 

用于接收数据的套接字缓冲区可通过以下命令查询：

$> sudo sysctl -a | grep net.core.rmem_max net.core.rmem_max = 4194304 

如果这些默认最大值不够用，也可以增大它们。

$> echo 'net.core.wmem_max=12582912' >> /etc/sysctl.conf $> echo 'net.core.rmem_max=12582912' >> /etc/sysctl.conf 

## 9.9.3 调优 Reliable 模式
RTPS 协议可以使用特殊消息（Heartbeat 和 Ack/Nack 消息）维持可靠通信。RTPS 协议能够检测哪些样本丢失并重新发送。

可以通过指定自定义 heartbeat 周期来修改这些特殊子消息的交换频率。Publisher-Subscriber 层的 heartbeat 周期作为 `ParticipantAttributes` 的一部分配置：

publisher_attr.times.heartbeatPeriod.seconds = 0; publisher_attr.times.heartbeatPeriod.nanosec = 500000000; _//500 ms_ 

在 Writer-Reader 层中，该配置属于 `WriterAttributes`：

writer_attr.times.heartbeatPeriod.seconds = 0; writer_attr.times.heartbeatPeriod.nanosec = 500000000; _//500 ms_ 

较小的 heartbeat 周期会增加网络中的开销消息数量，但能在数据丢失时加快系统响应。

### 非严格可靠性
使用严格可靠性并将 _History_ 类型配置为 KEEP_ALL 时，所有 subscriber 都必须收到所有样本。如果丢弃大量样本，这会导致性能下降。如果不需要如此严格，请使用非严格可靠性，即将 _History_ 类型配置为 KEEP_LAST。

## 9.9.4 降低样本速率
有时 publisher 向 subscriber 发送数据的速率可能过高，最终导致样本被丢弃。为避免这种情况，可以使用 _流控制器_ 降低速率。

# 9.10 其他服务质量选项
你可以在应用中实现自己的服务质量（QoS）限制。_eProsima Fast RTPS_ 随附一组示例，说明如何实现常见的客户端 QoS 设置：

- Ownership Strength：多个数据源上线时，通过关注优先级更高的数据源来过滤重复数据。

- 过滤：根据内容、时间或二者兼有来过滤传入消息。

这些示例附有各自的 _Readme.txt_，说明其实现方式。

# 9.11 日志记录
Fast RTPS 包含可扩展的日志系统，其类层次结构如下：


![](fast-dds-docs-eprosima-com-en-v1.10.0_images/fast-dds-docs-eprosima-com-en-v1.10.0.pdf-0091-01.png)


Log 是日志系统的入口，公开三个宏定义以简化使用：

logInfo(INFO_MSG, "This is an info message"); logWarning(WARN_MSG, "This is a warning message"); logError(ERROR_MSG, "This is an error message"); 

在所有情况下，INFO_MSG、WARN_MSG 和 ERROR_MSG 都会作为预处理器字符串用作日志条目的类别，因此可以内联定义任意类别。

logInfo(NEW_CATEGORY, "This log message belong to NEW_CATEGORY category."); 

可以控制日志系统的详细程度并按类别过滤：

Log::SetVerbosity(Log::Kind::Warning); std::regex my_regex("NEW_CATEGORY"); Log::SetCategoryFilter(my_regex); 

可能的详细级别为 `Log::Kind::Info`、`Log::Kind::Warning` 和 `Log::Kind::Error`。

选择其中一个级别时，也会同时选择优先级更高的级别。

- 选择 `Log::Kind::Error` 时，只会收到错误消息。

- 选择 `Log::Kind::Warning` 时，也会选择 `Log::Kind::Error`。

- 选择 `Log::Kind::Info` 时，将选择所有级别。

要按类别过滤，必须提供有效的 `std::regex` 表达式，该表达式将应用于类别。与表达式匹配的类别会被记录。

默认情况下，详细级别设置为 `Log::Kind::Error`，且不进行类别过滤。

还有其他一些可配置参数：

_//! Enables the reporting of filenames in log entries. Disabled by default._ RTPS_DllAPI **static void** ReportFilenames( **bool** ); _//! Enables the reporting of function names in log entries. Enabled by default when supported._ 



RTPS_DllAPI **static void** ReportFunctions( **bool** ); _//! Sets the verbosity level, allowing for messages equal or under that priority to be logged._ RTPS_DllAPI **static void** SetVerbosity(Log::Kind); _//! Returns the current verbosity level._ RTPS_DllAPI **static** Log::Kind GetVerbosity(); _//! Sets a filter that will pattern-match against log categories, dropping any unmatched categories._ RTPS_DllAPI **static void** SetCategoryFilter ( **const** std::regex&); _//! Sets a filter that will pattern-match against filenames, dropping any unmatched categories._ RTPS_DllAPI **static void** SetFilenameFilter ( **const** std::regex&); _//! Sets a filter that will pattern-match against the provided error string, dropping any unmatched categories._ RTPS_DllAPI **static void** SetErrorStringFilter ( **const** std::regex&); 

## 9.11.1 LogConsumer
LogConsumer 是实现日志信息管理方式的类。必须将它们注册到 Log 系统中，才能在过滤后接收日志消息。

目前有两种 LogConsumer 实现：

- **StdoutConsumer：** 默认消费者，将日志消息输出到标准输出，没有可配置项。

- **FileConsumer：** 将日志消息输出到文件。它有两个配置参数：

   - `filename` 定义消费者写入日志消息的文件。

   - `append` 指示消费者是否以追加新内容的方式打开输出文件。

默认情况下，`filename` 为 **output.log**，`append` 等于 **false**。

如果要添加消费者来管理日志，必须调用 Log 的 `RegisterConsumer` 方法。要移除所有消费者（包括默认消费者），应调用 `ClearConsumers` 方法。要将 Log 配置重置为默认值（包括恢复默认消费者），可以调用其 `Reset` 方法。

Log::ClearConsumers(); _// Deactivate StdoutConsumer // Add FileConsumer consumer_ std::unique_ptr<FileConsumer> fileConsumer( **new** FileConsumer("append.log", true)); Log::RegisterConsumer(std::move(fileConsumer)); 

_// Back to its defaults: StdoutConsumer will be enable and FileConsumer removed._ Log::Reset(); 

## 9.11.2 XML 日志配置
可以通过 XML 配置日志系统：将 `<log>` 标签放在 `<dds>` 标签下，也可以作为独立文件使用（不使用 `<dds>` 标签，仅以 `<log>` 作为根元素）。可以设置 `<use_default>` 和一组 `<consumer>`。每个 `<consumer>` 由 `<class>` 和一组 `<property>` 定义。

<log> <use_default> FALSE </use_default> 



<consumer> <class> FileConsumer </class> <property> <name> filename </name> <value> test1.log </value> </property> <property> <name> append </name> <value> TRUE </value> </property> </consumer> </log> 

`<use_default>` 指示是否使用默认消费者 `StdoutConsumer`。

每个 `<consumer>` 定义一个消费者，并将其添加到 Log 的消费者列表。`<class>` 指示要实例化的消费者类，一组 `<property>` 对其进行配置。`StdoutConsumer` 没有可配置属性，而 `FileConsumer` 有 `filename` 和 `append`。

本文档到此结束。建议查阅 Doxygen API Reference 以及发行版附带的内嵌示例。如需更多帮助，请发送电子邮件至 _support@eprosima.com_。

# 第 10 章：安全
Fast RTPS 可以配置为提供安全通信。为此，Fast RTPS 在三个层面实现可插拔安全：远程 participant 身份验证、实体访问控制和数据加密。

默认情况下，Fast RTPS 不编译安全支持。可以在 CMake 配置步骤中添加 `-DSECURITY=ON` 以启用。有关 Fast RTPS 编译的更多信息，请参见 _从源代码安装_。

可以通过 `eprosima::fastrtps::Participant` 属性使用 properties 激活和配置安全插件。`eprosima::fastrtps::rtps::Property` 由其名称（`std::string`）和值（`std::string`）定义。本页的表格展示每个安全插件使用的属性。

# 10.1 身份验证插件
这些插件在发现远程 participant 时提供身份验证。检测到远程 participant 后，Fast RTPS 会尝试使用已激活的身份验证插件进行认证。如果认证过程成功，两个 participant 会匹配，发现协议继续。如果失败，远程 participant 会被拒绝。

可以使用 Participant 属性 `dds.sec.auth.plugin` 激活身份验证插件。Fast RTPS 提供内置身份验证插件。更多信息请参见 _Auth:PKI-DH_。

# 10.2 访问控制插件
这些插件提供实体权限验证。远程 participant 通过身份验证后，需要验证并强制执行其权限。

文中描述每个实体对资源拥有的访问权限。主要实体是 Participant，用于访问或生成域中的信息；因此必须允许 Participant 在特定域中运行。此外，Participant 负责创建通过特定 Topic 通信的 Publisher 和 Subscriber。因此，Participant 必须具备创建 Topic、通过其 Publisher 发布特定 Topic，以及通过其 Subscriber 订阅特定 Topic 所需的权限。访问控制插件可以配置加密插件，因为加密插件的使用基于 Participant 的权限。

可以使用 Participant 属性 `dds.sec.access.plugin` 激活访问控制插件。Fast RTPS 提供内置访问控制插件。更多信息请参见 _Access:Permissions_。

# 10.3 加密插件
这些插件提供加密支持。加密可应用于 RTPS 协议的三个不同层次。加密插件可以加密整个 RTPS 消息、特定实体（Writer 或 Reader）的 RTPS 子消息，或特定 Writer 的负载（用户数据）。这些方式可以组合使用。

可以使用 Participant 属性 `dds.sec.crypto.plugin` 激活加密插件。Fast RTPS 提供内置加密插件。更多信息请参见 _Crypto:AES-GCM-GMAC_。

加密插件由访问控制插件配置。如果不使用访问控制，可以使用以下属性手动配置加密插件：

### 加密整个 RTPS 消息
可以使用 Participant 属性 `rtps.participant.rtps_protection_kind`（值为 `ENCRYPT`）配置 Participant 加密所有 RTPS 消息。

### 加密特定实体的 RTPS 子消息
可以使用实体属性 `rtps.endpoint.submessage_protection_kind`（值为 `ENCRYPT`）配置实体（Writer 或 Reader）加密其 RTPS 子消息。

### 加密特定 Writer 的负载
可以使用 Writer 属性 `rtps.endpoint.payload_protection_kind`（值为 `ENCRYPT`）配置 Writer 加密其负载。

# 10.4 内置插件
当前版本附带三个内置安全插件：

- _Auth:PKI-DH_：该插件使用受信任的 _Certificate Authority_（CA，证书颁发机构）提供身份验证。

- _Access:Permissions_：该插件在 Domain 和 Topic 层面为 Participant 提供访问控制。

- _Crypto:AES-GCM-GMAC_：该插件使用 Galois Counter Mode（AES-GCM）中的高级加密标准（AES）提供认证加密。

## 10.4.1 Auth:PKI-DH
该内置插件在已发现的 participant 之间提供身份验证。它由受信任的 _Certificate Authority_（CA）提供支持，并使用 ECDSA 数字签名算法执行双向认证。它还使用椭圆曲线 Diffie-Hellman（ECDH）密钥协商方法建立共享密钥。该共享密钥可供 _Crypto:AES-GCM-GMAC_ 等其他安全插件使用。

可以使用 Participant 属性 `dds.sec.auth.plugin`（值为 `builtin.PKI-DH`）激活该插件。下表列出该安全插件使用的 Participant 属性。


表 1：**配置 Auth:PKI-DH 的属性**

|属性名（所有属性均带<br>“dds.sec.auth.builtin.PKI-DH.”<br>前缀）|属性值|
|---|---|
|identity_ca|Identity CA 的 X509 证书 URI。支持的 URI 方案：<br>file。**file** 方案应指向 PEM 格式的 X.509 v3 证书。|
|identity_certificate|由 Identity CA 签署的 PEM 格式 X509 证书 URI，其中包含 Participant 的已签名公钥。支持的 URI 方案：<br>file。|
|identity_crl_（可选）|X509 证书吊销列表（CRL）的 URI。支持的 URI<br>方案：file。|
|private_key|用于访问 Participant 私钥的 URI。支持的 URI<br>方案：file。|
|password _（可选）_|用于解密 `private_key` 的密码。|



### 生成 x509 证书
可以使用 OpenSSL 应用程序生成自己的 x509 证书。本节说明如何操作。

### 为 CA 生成证书
要创建自己的 CA 证书，首先必须编写包含 CA 信息的配置文件。

_# File: maincaconf.cnf # OpenSSL example Certificate Authority configuration file ####################################################################_ **[ ca ]** default_ca = CA_default # The default ca section _####################################################################_ **[ CA_default ]** dir = . # Where everything is kept certs = $dir/certs # Where the issued certs are kept crl_dir = $dir/crl # Where the issued crl are kept database = $dir/index.txt # database index file. unique_subject = no # Set to 'no' to allow creation of # several ctificates with same subject. new_certs_dir = $dir certificate = $dir/maincacert.pem # The CA certificate serial = $dir/serial # The current serial number crlnumber = $dir/crlnumber # the current crl number # must be commented out to leave a V1 CRL crl = $dir/crl.pem # The current CRL private_key = $dir/maincakey.pem # The private key RANDFILE = $dir/private/.rand # private random number file name_opt = ca_default # Subject Name options cert_opt = ca_default # Certificate field options default_days= 1825 # how long to certify for default_crl_days = 30 # how long before next CRL default_md = sha256 # which md to use. 



preserve = no # keep passed DN ordering policy = policy_match _# For the CA policy_ **[ policy_match ]** countryName = match stateOrProvinceName = match organizationName = match organizationalUnitName = optional commonName = supplied emailAddress = optional _# For the 'anything' policy # At this point in time, you must list all acceptable 'object' # types._ **[ policy_anything ]** countryName = optional stateOrProvinceName = optional localityName = optional organizationName = optional organizationalUnitName = optional commonName = supplied emailAddress = optional **[ req ]** prompt = no _#default_bits = 1024 #default_keyfile = privkey.pem_ distinguished_name= req_distinguished_name _#attributes = req_attributes #x509_extensions = v3_ca # The extentions to add to the self signed cert_ string_mask = utf8only **[ req_distinguished_name ]** countryName = ES stateOrProvinceName = MA localityName = Tres Cantos 0.organizationName = eProsima commonName = eProsima Main Test CA emailAddress = mainca@eprosima.com 

编写配置文件后，以下命令使用 ECDSA 生成证书。

openssl ecparam -name prime256v1 > ecdsaparam openssl req -nodes -x509 -days 3650 -newkey ec:ecdsaparam -keyout maincakey.pem -out maincacert.pem -config maincaconf.cnf 

### 为 Participant 生成证书
要为 Participant 创建自己的证书，首先必须编写配置文件。

_# File: appconf.cnf_ prompt = no string_mask = utf8only 



distinguished_name = req_distinguished_name **[ req_distinguished_name ]** countryName = ES stateOrProvinceName = MA localityName = Tres Cantos organizationName = eProsima emailAddress = example@eprosima.com commonName = AppName 

编写配置文件后，以下命令使用 ECDSA 为 Participant 生成证书。

openssl ecparam -name prime256v1 > ecdsaparam 

openssl req -nodes -new -newkey ec:ecdsaparam -config appconf.cnf -keyout appkey.pem - out appreq.pem 

openssl ca -batch -create_serial -config maincaconf.cnf -days 3650 -in appreq.pem - out appcert.pem 

## 10.4.2 Access:Permissions
该内置插件使用由共享 _Certificate Authority_ 签署的 permissions 文档提供访问控制。它通过三个文档配置：

可以使用 Participant 属性 `dds.sec.access.plugin`（值为 `builtin.Access-Permissions`）激活该插件。下表列出该安全插件使用的 Participant 属性。

表 2：**配置 Access:Permissions 的属性**

|属性名（所有属性均带<br>“dds.sec.access.builtin.Access-<br>Permissions.”前缀）|属性值|
|---|---|
|permissions_ca|Permissions CA 的 X509 证书 URI。支持的 URI<br>方案：file。**file** 方案应指向 PEM 格式的 X.509 v3 证书。|
|governance|由 Permissions CA 以 S/MIME 格式签署的共享 Governance 文档 URI。支持的 URI 方案：file。|
|permissions|由 Permissions CA 以 S/MIME 格式签署的 Participant permissions 文档 URI。支持的 URI 方案：file。|



### Permissions CA 证书
这是一个 X.509 证书，包含用于签署 Domain Governance 和 Domain Permissions 文档的 CA 公钥。

### 域治理文档（Domain Governance Document）
Domain Governance 文档是一个 XML 文档，规定域应如何受安全保护。该文档应由 Permissions CA 以 S/MIME 格式签署。

该文档的格式由此 Governance XSD 文件定义。还可以找到通用 Governance XML 示例。

### 域规则（Domain Rules）
每个域规则由 `<domain_rule>` XML 元素标签分隔。每个域规则包含以下元素和节：

- Domains 元素

- Allow Unauthenticated Participants 元素

- Enable Join Access Control 元素

- Discovery Protection Kind 元素

- Liveliness Protection Kind 元素

- RTPS Protection Kind 元素

- Topic Access Rules 节

域规则按其在文档中出现的顺序求值。仅当规则的 domain 节与 Participant 所属域匹配时，规则才应用于该 Participant。如果多条规则匹配，只有第一条匹配的规则适用。

### Domains 元素
该元素由 XML 元素 `<domains>` 分隔。其中的值标识该规则适用的 Domain 值集合。

`<domains>` 元素可以包含单个域标识符，例如：

<domains> <id> 1 </id> </domains> 

也可以包含域标识符范围，例如：

<domains> <id_range> <min> 1 </min> <max> 10 </max> </id_range> </domains> 

还可以同时包含域标识符列表和域标识符范围。

### 允许未认证 Participant 元素（Allow Unauthenticated Participants）
该元素由 XML 元素 `<allow_unauthenticated_participants>` 分隔。它指示 Participant 与远程 Participant 匹配时是否要求身份验证。如果值为 false，Participant 必须强制认证远程 Participant，并禁止与无法成功认证的 Participant 匹配。如果值为 true，只要尚未与同一 Participant GUID 建立有效认证，Participant 就应允许与其他 Participant 匹配（即使远程 Participant 无法认证）。

### 启用加入访问控制元素（Enable Join Access Control）
该元素由 XML 元素 `<enable_join_access_control>` 分隔。它指示 participant 与远程 Participant 匹配时是否需要访问控制插件授权。如果值为 false，Participant 不应检查已认证远程 Participant 的权限。如果值为 true，Participant 应检查已认证远程 Participant 的权限。

### 发现保护类型元素（Discovery Protection Kind）
该元素由 XML 元素 `<discovery_protection_kind>` 分隔。它指示端点发现阶段的安全通道是否需要加密。如果值为 SIGN 或 ENCRYPT，安全通道应加密；如果值为 NONE，则不应加密。

### 活跃性保护类型元素（Liveliness Protection Kind）
该元素由 XML 元素 `<liveliness_protection_kind>` 分隔。它指示活跃性机制的安全通道是否需要加密。如果值为 SIGN 或 ENCRYPT，安全通道应加密；如果值为 NONE，则不应加密。

### RTPS 保护类型元素（RTPS Protection Kind）
该元素由 XML 元素 `<rtps_protection_kind>` 分隔。它指示整个 RTPS 消息是否需要加密。如果值为 SIGN 或 ENCRYPT，整个 RTPS 消息应加密；如果值为 NONE，则不应加密。

### Topic 规则节
该元素由 XML 元素 `<topic_rule>` 分隔，并出现在 XML 元素为 `<topic_access_rules>` 的 Topic Access Rules 节内。

每个元素包含以下内容：

- Topic 表达式

- Enable Discovery protection

- Enable Liveliness protection

- Enable Read Access Control 元素

- Enable Write Access Control 元素

- Metadata protection Kind

- Data protection Kind

Topic 表达式选择一组 Topic 名称。该规则应用于任何关联 Topic 的 Publisher 或 Subscriber，只要该 Topic 名称匹配 Topic 表达式名称。

Topic 访问规则按其在 `<topic_access_rules>` 节中出现的顺序求值。如果多条规则匹配，只有第一条匹配的规则适用。

### Topic 表达式元素
该元素由 XML 元素 `<topic_expression>` 分隔。其中的值标识规则适用的 Topic 名称集合。该规则将应用于任何关联 Topic 的 Publisher 和 Subscriber，只要该 Topic 名称匹配该值。

Topic 名称表达式的语法和匹配必须使用 _POSIX 1003.2-1992 第 B.6 节_ 规定的 POSIX `fnmatch()` 函数语法和规则。

### 启用发现保护元素（Enable Discovery protection）
该元素由 XML 元素 `<enable_discovery_protection>` 分隔。它指示实体相关发现信息是否应通过端点发现阶段的安全通道。如果值为 false，实体发现信息应通过不安全的发现通道发送。如果值为 true，信息应通过安全通道发送。

### 启用活跃性保护元素（Enable Liveliness Protection）
该元素由 XML 元素 `<enable_liveliness_protection>` 分隔。它指示实体相关活跃性信息是否应通过活跃性机制的安全通道。如果值为 false，实体活跃性信息应通过不安全的活跃性通道发送。如果值为 true，信息应通过安全通道发送。

### 启用读取访问控制元素（Enable Read Access Control）
该元素由 XML 元素 `<enable_read_access_control>` 分隔。它指示 Topic 的读取访问是否受保护。如果值为 false，本地 Subscriber 创建和远程 Subscriber 匹配可以在不施加额外访问控制机制的情况下进行。如果值为 true，应使用访问控制插件进行检查。

### 启用写入访问控制元素（Enable Write Access Control）
该元素由 XML 元素 `<enable_write_access_control>` 分隔。它指示 Topic 的写入访问是否受保护。如果值为 false，本地 Publisher 创建和远程 Publisher 匹配可以在不施加额外访问控制机制的情况下进行。如果值为 true，应使用访问控制插件进行检查。

### 元数据保护类型元素（Metadata Protection Kind）
该元素由 XML 元素 `<metadata_protection_kind>` 分隔。它指示实体的 RTPS 子消息是否应由加密插件加密。如果值为 true，RTPS 子消息应加密；如果值为 false，则不应加密。

### 数据保护类型元素（Data Protection Kind）
该元素由 XML 元素 `<data_protection_kind>` 分隔。它指示数据负载是否应由加密插件加密。如果值为 true，数据负载应加密；如果值为 false，则不应加密。

### Participant 权限文档（Permissions Document）
permissions 文档是一个 XML 文档，包含 Participant 的权限并将其绑定到其可分辨名称。该 permissions 文档应由 Permissions CA 以 S/MIME 格式签署。

该文档的格式由此 Permissions XSD 文件定义。还可以找到通用 Permissions XML 示例。

### Grant 节
本节由 `<grant>` XML 元素标签分隔。每个 grant 节包含三个部分：

- Subject 名称

- 有效期

- 规则

### Subject 名称
本节由 XML 元素 `<subject_name>` 分隔。Subject 名称标识权限适用的 Participant。每个 Subject 名称在 XML Permissions 文档中只能出现在一个 `<permissions>` 节内。Subject 名称元素的内容必须是 Authorization Certificate 中给出的 Participant x.509 Subject 名称。

### 有效期
本节由 XML 元素 `<validity>` 分隔，表示权限的有效日期。

### 规则
本节包含分配给 Participant 的权限。规则按其在文档中出现的顺序应用。如果规则条件匹配正在尝试的 Domain 加入和/或发布、订阅操作，则应用允许或拒绝决定。如果规则条件不匹配正在尝试的操作，应继续评估下一条规则。如果检查完所有规则都未匹配，则应用 `<default>` 规则指定的决定。默认规则如果存在，必须位于所有 allow 和 deny 规则之后。如果不存在默认规则，则隐含的默认决定为 DENY。

要使 grant 匹配，必须同时满足 topics 和 partitions 条件。

Allow 规则由 XML 元素 `<allow_rule>` 分隔。Deny 规则由 XML 元素 `<deny_rule>` 分隔。二者包含相同的子元素。

### Domains 节
本节由 XML 元素 `<domains>` 分隔。其中的值标识规则适用的 Domain 值集合。语法与 Governance 文档的 _Domains 元素_ 相同。

### 允许/拒绝操作节的格式
三类操作对应的节格式相似，唯一区别是用于分隔操作的 XML 元素名称：

- Allow/Deny Publish Action 由 `<publish>` XML 元素分隔。

- Allow/Deny Subscribe Action 由 `<subscribe>` XML 元素分隔。

- Allow/Deny Relay Action 由 `<relay>` XML 元素分隔。

每类操作包含两个条件。

- 允许/拒绝的 Topics 条件

- 允许/拒绝的 Partitions 条件

### Topic 条件
本节由 `<topics>` XML 元素分隔。它定义允许/拒绝规则生效时必须匹配的 Topic 名称。Topic 名称可以显式给出，也可以通过 Topic 名称表达式给出。Topic 名称表达式中的每个 Topic 名称分别出现在 `<topics>` 元素内的 `<topic>` 子元素中。

Topic 名称表达式的语法和匹配必须使用 _POSIX 1003.1-1992 第 B.6 节_ 规定的 POSIX `fnmatch()` 函数语法和规则。

<topics> <topic> Plane </topic> <topic> Hel* </topic> </topics> 

### Partition 条件
本节由 `<partitions>` XML 元素分隔。它限制规则生效时（publish、subscribe、relay）操作可关联的 Partition 名称集合。Partition 名称表达式的语法和匹配必须使用 _POSIX 1003.2-1992 第 B.6 节_ 规定的 POSIX `fnmatch()` 函数语法和规则。如果规则中没有 `<partitions>` 节，则假定使用默认的“空字符串”Partition。

<partitions> <partition> A </partition> <partition> B* </partition> </partitions> 

### 使用 x509 证书签署文档
Governance 文档和 Permissions 文档必须由 X509 证书签署。X509 证书的生成在 _生成 x509 证书_ 中说明。以下命令为 Access:Permissions 插件签署所需文档。

_# Governance document: governance.xml_ openssl smime -sign -in governance.xml -text -out governance.smime -signer maincacert. pem -inkey maincakey.pem 

_# Permissions document: permissions.xml_ openssl smime -sign -in permissions.xml -text -out permissions.smime -signer maincacert.pem -inkey maincakey.pem 



## 10.4.3 Crypto:AES-GCM-GMAC
该内置插件使用 Galois Counter Mode 中的 AES（AES-GCM）提供认证加密。它还使用 Galois MAC（AES-GMAC）提供额外的 reader 专用消息认证码（MAC）。该插件需要激活安全插件 _Auth:PKI-DH_。

可以使用 Participant 属性 `dds.sec.crypto.plugin`（值为 `builtin.AES-GCM-GMAC`）激活该插件。

# 10.5 示例：配置 Participant
本示例说明如何配置 Participant 以激活和配置 _Auth:PKI-DH_、_Access:Permissions_ 和 _Crypto:AES-GCM-GMAC_ 插件。

### Participant 属性
### C++
eprosima::fastrtps::ParticipantAttributes part_attr; _// Activate Auth:PKI-DH plugin_ part_attr.rtps.properties.properties().emplace_back("dds.sec.auth.plugin", "builtin. PKI-DH"); _// Configure Auth:PKI-DH plugin_ part_attr.rtps.properties.properties().emplace_back("dds.sec.auth.builtin.PKI-DH. identity_ca", "file://maincacert.pem"); part_attr.rtps.properties.properties().emplace_back("dds.sec.auth.builtin.PKI-DH. identity_certificate", "file://appcert.pem"); part_attr.rtps.properties.properties().emplace_back("dds.sec.auth.builtin.PKI-DH. private_key", "file://appkey.pem"); _// Activate Access:Permissions plugin_ part_attr.rtps.properties.properties().emplace_back("dds.sec.access.plugin", "builtin.Access-Permissions"); _// Configure Access:Permissions plugin_ part_attr.rtps.properties.properties().emplace_back("dds.sec.access.builtin.Access- Permissions.permissions_ca", "file://maincacet.pem"); part_attr.rtps.properties.properties().emplace_back("dds.sec.access.builtin.Access- Permissions.governance", "file://governance.smime"); part_attr.rtps.properties.properties().emplace_back("dds.sec.access.builtin.Access- Permissions.permissions", "file://permissions.smime"); _// Activate Crypto:AES-GCM-GMAC plugin_ part_attr.rtps.properties.properties().emplace_back("dds.sec.crypto.plugin", "builtin.AES-GCM-GMAC"); 

### XML
<participant profile_name="secure_participant_conf_all_plugin_xml_profile" > <rtps> <propertiesPolicy> <properties> _<!-- Activate Auth:PKI-DH plugin -->_ <property> <name> dds.sec.auth.plugin </name> <value> builtin.PKI-DH </value> </property> _<!-- Configure Auth:PKI-DH plugin -->_ <property> <name> dds.sec.auth.builtin.PKI-DH.identity_ca </name> <value> file://maincacert.pem </value> </property> <property> <name> dds.sec.auth.builtin.PKI-DH.identity_certificate </name> <value> file://appcert.pem </value> </property> <property> <name> dds.sec.auth.builtin.PKI-DH.private_key </name> <value> file://appkey.pem </value> </property> _<!-- Activate Access:Permissions plugin -->_ <property> <name> dds.sec.access.plugin </name> <value> builtin.Access-Permissions </value> 


本示例说明如何在不使用访问控制插件的情况下，配置 Participant 以激活和配置 _Auth:PKI-DH_ 与 _Crypto:AESGCM-GMAC_ 插件。它还配置 Participant 加密其 RTPS 消息，配置 Writer 和 Reader 加密其 RTPS 子消息，并配置 writer 加密负载（用户数据）。

### Participant 属性
### C++
eprosima::fastrtps::ParticipantAttributes part_attr; _// Activate Auth:PKI-DH plugin_ part_attr.rtps.properties.properties().emplace_back("dds.sec.auth.plugin", "builtin. PKI-DH"); _// Configure Auth:PKI-DH plugin_ part_attr.rtps.properties.properties().emplace_back("dds.sec.auth.builtin.PKI-DH. identity_ca", "file://maincacert.pem"); part_attr.rtps.properties.properties().emplace_back("dds.sec.auth.builtin.PKI-DH. identity_certificate", "file://appcert.pem"); part_attr.rtps.properties.properties().emplace_back("dds.sec.auth.builtin.PKI-DH. private_key", "file://appkey.pem"); _// Activate Crypto:AES-GCM-GMAC plugin_ part_attr.rtps.properties.properties().emplace_back("dds.sec.crypto.plugin", "builtin.AES-GCM-GMAC"); _// Encrypt all RTPS submessages_ part_attr.rtps.properties.properties().emplace_back("rtps.participant.rtps protection_kind", "ENCRYPT"); 

### XML
<participant profile_name="secure_participant_conf_no_access_control_xml_profile" > <rtps> <propertiesPolicy> <properties> _<!-- Activate Auth:PKI-DH plugin -->_ <property> <name> dds.sec.auth.plugin </name> <value> builtin.PKI-DH </value> </property> _<!-- Configure Auth:PKI-DH plugin -->_ <property> <name> dds.sec.auth.builtin.PKI-DH.identity_ca </name> <value> file://maincacert.pem </value> </property> <property> <name> dds.sec.auth.builtin.PKI-DH.identity_certificate </name> <value> file://appcert.pem </value> </property> <property> <name> dds.sec.auth.builtin.PKI-DH.private_key </name> <value> file://appkey.pem </value> </property> _<!-- Activate Crypto:AES-GCM-GMAC plugin -->_ <property> <name> dds.sec.crypto.plugin </name> <value> builtin.AES-GCM-GMAC </value> </property> _<!-- Encrypt all RTPS submessages -->_ <property> <name> rtps.participant.rtps_protection_kind </name> <value> ENCRYPT </value> </property> </properties> </propertiesPolicy> </rtps> </participant> 


### Publisher 属性
### C++
eprosima::fastrtps::PublisherAttributes pub_attr; 

_// Encrypt RTPS submessages_ pub_attr.properties.properties().emplace_back("rtps.endpoint.submessage_protection kind", "ENCRYPT"); _// Encrypt payload_ pub_attr.properties.properties().emplace_back("rtps.endpoint.payload_protection_kind ", "ENCRYPT"); 

### XML
<publisher profile_name="secure_publisher_xml_profile" > <propertiesPolicy> <properties> _<!-- Encrypt RTPS submessages -->_ <property> <name> rtps.endpoint.submessage_protection_kind </name> <value> ENCRYPT </value> </property> _<!-- Encrypt payload -->_ <property> <name> rtps.endpoint.payload_protection_kind </name> <value> ENCRYPT </value> </property> </properties> </propertiesPolicy> </publisher> 

### Subscriber 属性
### C++
eprosima::fastrtps::SubscriberAttributes sub_attr; _// Encrypt RTPS submessages_ sub_attr.properties.properties().emplace_back("rtps.endpoint.submessage_protection kind", "ENCRYPT"); 

### XML
<subscriber profile_name="secure_publisher_xml_profile" > <propertiesPolicy> <properties> _<!-- Encrypt RTPS submessages -->_ <property> <name> rtps.endpoint.submessage_protection_kind </name> <value> ENCRYPT </value> </property> </properties> </propertiesPolicy> </subscriber> 

# 第 11 章：实时行为
Fast RTPS 可以配置为提供实时功能。这些功能保证 Fast RTPS 在指定时间约束内作出响应。为维持这一保证，Fast RTPS 可以表现出以下行为：

- 在 Fast RTPS 实体初始化后不再分配内存。

- 多个方法最多阻塞有限的一段时间。

本节说明如何配置 Fast RTPS 以实现这些行为。为便于理解，本节分为两个小节：

- _调优内存分配_：配置为初始化后避免内存分配。

- _非阻塞调用_：使用非阻塞方法实现实时行为。

# 11.1 调优内存分配
内存分配和释放是重要的非确定性操作系统调用。大多数实时系统都需要在应用启动时分配所有动态内存，并避免在主循环中调用内存管理 API。

Fast-RTPS 提供一些配置参数来满足这些要求，使内部数据集合的元素能够预分配。为选择正确的参数值，用户应了解整个域的拓扑，因此设置这些参数时应已知 participant 和端点的数量。

## 11.1.1 Participant 参数
Participant 上所有与分配相关的参数都集中在 `ParticipantAttributes` 结构的 `rtps.allocation` 字段中。

### 限制已发现 participant 的数量
Fast-RTPS 中的每个 participant 都持有一个 `ParticipantProxyData` 对象内部集合，包含本地和远程 participant 的信息。`RTPSParticipantAllocationAttributes` 中的 `participants` 字段允许配置该集合的分配行为。用户可以指定初始预分配元素数、允许的最大元素数以及分配增量。默认使用完全动态行为。

### 限制已发现端点的数量
每个 `ParticipantProxyData` 对象都持有包含 `ReaderProxyData` 和 `WriterProxyData` 对象的内部集合，其中包含 participant 的 reader 和 writer 信息。与 `participants` 字段类似，`RTPSParticipantAllocationAttributes` 具有 `readers` 和 `writers` 字段，用于配置这些集合的分配行为。用户可以指定初始预分配元素数、允许的最大元素数以及分配增量。默认使用完全动态行为。

### 限制参数大小
为 participant 和端点保存的大多数信息都有确定的大小限制，因此已知为每个本地和远程对等节点分配多少内存。对于大小不受限制的参数，可以使用 `RTPSParticipantAllocationAttributes::data_limits` 配置最大大小，其属性如下：

- `max_partitions` 将分区数据大小限制为指定的八位组数。

- `max_user_data` 将用户数据大小限制为指定的八位组数。

- `max_properties` 将 participant 属性数据大小限制为指定的八位组数。

值为零表示不限制大小。如果这些大小配置为非零值，将为每个 participant 和端点分配足够的内存。如果这些大小不受限制，则按需动态分配内存。默认使用完全动态行为。

## 11.1.2 Publisher 参数
每个 publisher 都持有一个集合，其中包含与其匹配的 subscriber 的部分信息。`PublisherAttributes` 中的 `matched_subscriber_allocation` 字段允许配置该集合的分配行为。用户可以指定初始预分配元素数、允许的最大元素数以及分配增量。默认使用完全动态行为。

## 11.1.3 Subscriber 参数
每个 subscriber 都持有一个集合，其中包含与其匹配的 publisher 的部分信息。`SubscriberAttributes` 中的 `matched_publisher_allocation` 字段允许配置该集合的分配行为。用户可以指定初始预分配元素数、允许的最大元素数以及分配增量。默认使用完全动态行为。

## 11.1.4 完整示例
假设系统采用以下拓扑：

表 1：**分配调优示例拓扑**

|Participant P1|Participant P2|Participant P3|
|---|---|---|
|Topic 1 publisher|Topic 1 subscriber|Topic 2 subscriber|
|Topic 1 subscriber||Topic 2 publisher|
|Topic 1 subscriber||Topic 2 subscriber|



- 所有 subscriber 都恰好与 1 个 publisher 匹配。

- Topic 1 的 publisher 与 3 个 subscriber 匹配，Topic 2 的 publisher 与 2 个 subscriber 匹配。

- 每个 participant 的 publisher 最大数量为 1，subscriber 最大数量为 2。

- participant 总数为 3。

我们还会限制参数大小：

- 最大分区数据大小：256

- 最大用户数据大小：256

- 最大 properties 数据大小：512

以下代码展示本示例用例所需的一组参数。

### C++
_// Before creating a participant: // We know we have 3 participants on the domain_ participant_attr.rtps.allocation.participants = eprosima::fastrtps::ResourceLimitedContainerConfig::fixed_size_configuration(3u); _// We know we have at most 2 readers on each participant_ participant_attr.rtps.allocation.readers = 

 eprosima::fastrtps::ResourceLimitedContainerConfig::fixed_size_configuration(2u); _// We know we have at most 1 writer on each participant_ participant_attr.rtps.allocation.writers = 

 eprosima::fastrtps::ResourceLimitedContainerConfig::fixed_size_configuration(1u); _// We know the maximum size of partition data_ participant_attr.rtps.allocation.data_limits.max_partitions = 256u; _// We know the maximum size of user data_ participant_attr.rtps.allocation.data_limits.max_user_data = 256u; _// We know the maximum size of properties data_ participant_attr.rtps.allocation.data_limits.max_properties = 512u; _// Before creating the publisher for topic 1: // we know we will only have three matching subscribers_ publisher_attr.matched_subscriber_allocation = eprosima::fastrtps::ResourceLimitedContainerConfig::fixed_size_configuration(3u); 

_// Before creating the publisher for topic 2: // we know we will only have two matching subscribers_ publisher_attr.matched_subscriber_allocation = 

 eprosima::fastrtps::ResourceLimitedContainerConfig::fixed_size_configuration(2u); 

_// Before creating a subscriber: // we know we will only have one matching publisher_ subscriber_attr.matched_publisher_allocation = 

 eprosima::fastrtps::ResourceLimitedContainerConfig::fixed_size_configuration(1u); 

### XML
<participant profile_name="participant_alloc_qos_example" > <rtps> <allocation> _<!-- We know we have 3 participants on the domain -->_ <total_participants> <initial> 3 </initial> <maximum> 3 </maximum> <increment> 0 </increment> </total_participants> _<!-- We know we have at most 2 readers on each participant -->_ <total_readers> <initial> 2 </initial> <maximum> 2 </maximum> <increment> 0 </increment> </total_readers> _<!-- We know we have at most 1 writer on each participant -->_ <total_writers> <initial> 1 </initial> <maximum> 1 </maximum> <increment> 0 </increment> </total_writers> <max_partitions> 256 </max_partitions> <max_user_data> 256 </max_user_data> <max_properties> 512 </max_properties></allocation> </rtps> </participant> <publisher profile_name="alloc_qos_example_pub_for_topic_1" > 

# 11.2 非阻塞调用
**注意：** 此功能在 OSX 上未得到完全支持。OSX 不支持必要的 POSIX 实时功能。该功能受 _std::timed_mutex_ 和 _std::condition_variable_any_ 实现的限制。

为实现实时性，方法不能无限期阻塞，而只能阻塞最长一段时间。Fast-RTPS API 中有多个方法允许设置该行为。但首先应使用 CMake 选项 `-DSTRICT_REALTIME=ON` 配置 Fast-RTPS。下表列出这些函数。

表 2：**Fast RTPS 非阻塞 API**

|方法|说明|
|---|---|
|Publisher::write()|这些方法会阻塞一段时间。_PublisherAttributes_ 上的 _ReliabilityQosPolicy.max_blocking_time_ 定义该时间段。默认值为 100 毫秒。|
|Sub-<br>scriber::takeNextDat|a()<br>此方法会阻塞一段时间。_SubscriberAttributes_ 上的 _ReliabilityQosPolicy.max_blocking_time_ 定义该时间段。默认值为 100 毫秒。|
|Sub-|此方法会阻塞一段时间。_ReliabilityQosPolicy.max_blocking_time_ 定义于|
|scriber::readNextDat|a()<br>_SubscriberAttributes_，用于定义该时间段。默认值为 100 毫秒。|
|Sub-<br>scriber::wait_for_un|read_samples()<br>接受一个参数，用于指定该方法可以阻塞多长时间。|



# 第 12 章：动态话题类型
_eProsima Fast RTPS_ 提供动态定义和使用 Topic 类型及 Topic 数据的方式。我们的实现遵循 _OMG Extensible and Dynamic Topic Types for DDS interface_。更多信息可阅读该链接中的文档（DDS-XTypes V1.2）。

动态 Topic 类型使开发者可以在不受 IDL 相关限制的情况下使用 RTPS。用户可以声明所需的不同类型并直接管理信息，从而避免更新 IDL 文件和生成 _C++_ 类等额外步骤。

动态类型的管理分为两大类：第一类管理类型声明、构建和配置；第二类负责数据实例及其信息。

# 12.1 概念
### 类型描述符（Type Descriptor）
存储某一类型及其关系和限制的信息。它是生成动态类型所需的最小类；对于复杂类型，它还存储子类型或父类型的信息。

### 成员描述符（Member Descriptor）
多种复杂类型需要使用成员描述符声明类型之间的关系。该类的信息包括成员名称、唯一 ID、要创建的类型以及创建后的默认值。Union 类型有特殊字段，以标签标识每个成员。

### 动态类型构建器工厂（Dynamic Type Builder Factory）
负责创建和管理所有 DynamicType 与 DynamicTypeBuilder 的 _Singleton_ 类。它声明用于创建各类支持类型的方法，使描述符管理更容易。工厂创建的每个对象都必须调用 `delete_type` 方法删除。

### 动态类型构建器（Dynamic Type Builder）
用于配置和创建 DynamicType 的中间类。按设计，动态类型不可修改，因此创建新类型前需要先创建 builder 并应用用户所需设置。用户可以使用同一 builder 创建

多种类型，但对 builder 应用的更改不会影响先前创建的类型。builder 创建的每个对象都必须调用 Dynamic Type Builder Factory 的 `delete_type` 方法删除。

### 动态类型（Dynamic Type）
动态类型声明中的基类，存储其类型及所有关联成员的信息。创建时它会复制描述符，并且为保持一致而不能更改。

### 动态类型成员（Dynamic Type Member）
用于在成员描述符与其父类型之间建立关系的类。对于添加到动态类型中的每个子成员，动态类型都有一个 Dynamic Type Member。

### 动态数据工厂（Dynamic Data Factory）
负责创建和管理所有 DynamicData 的 _Singleton_ 类。它使用给定 DynamicType 及其设置创建 DynamicData。工厂创建的每个数据对象都必须调用 `delete_type` 方法删除。它还允许根据 TypeDescriptor 创建 TypeIdentifier 以及（Minimal 和 Complete）TypeObject。

### 动态数据（Dynamic Data）
用于管理动态类型数据的类，存储发送和接收的信息。使用 DynamicData 有两种方式：第一种最安全，激活 `DYNAMIC_TYPES_CHECKING` 宏后，会为每种基本类型创建变量以帮助调试。第二种仅使用最小数据来减小 DynamicData 类的大小，但会增加调试难度。

### 动态 PubSubType
继承自 `TopicDataType` 的类，在 RTPS Domain 与动态类型之间充当中间层。当 participant 需要将任意传输收到的信息转换为已注册的动态类型时，它实现创建、序列化、反序列化和删除 DynamicData 实例所需的方法。

# 12.2 支持的类型
## 12.2.1 基本类型
本节包括所有简单类型：

|BOOLEAN|INT64|
|---|---|
|BYTE|UINT16|
|CHAR8|UINT32|
|CHAR16|UINT64|
|INT16|FLOAT32|
|INT32|FLOAT64|
|FLOAT128||



创建基本类型不需要特定配置。因此，`DynamicTypeBuilderFactory` 公开了多个方法，使用户可以跳过 `DynamicTypeBuilder` 步骤直接创建动态类型。下面的示例展示创建基本类型动态数据的两种方式。`DynamicData` 类为列表中的每种基本类型都提供特定的 get 和 set 方法。

_// Using Builders_ DynamicTypeBuilder_ptr created_builder = DynamicTypeBuilderFactory::get_instance()-> create_int32_builder(); DynamicType_ptr created_type = DynamicTypeBuilderFactory::get_instance()->create type(created_builder.get()); DynamicData* data = DynamicDataFactory::get_instance()->create_data(created_type); data->set_int32_value(1); _// Creating directly the Dynamic Type_ DynamicType_ptr pType = DynamicTypeBuilderFactory::get_instance()->create_int32 type(); DynamicData* data2 = DynamicDataFactory::get_instance()->create_data(pType); data2->set_int32_value(1); 

## 12.2.2 String 与 WString
字符串与基本类型非常相似，但有一个例外：需要设置其可管理缓冲区的大小。为此，`DynamicTypeBuilderFactory` 公开 `create_string_type` 和 `create_wstring_type` 方法。默认大小设置为 255 个字符。

_// Using Builders_ DynamicTypeBuilder_ptr created_builder = DynamicTypeBuilderFactory::get_instance()-> create_string_builder(100); DynamicType_ptr created_type = DynamicTypeBuilderFactory::get_instance()->create type(created_builder.get()); DynamicData* data = DynamicDataFactory::get_instance()->create_data(created_type); data->set_string_value("Dynamic String"); _// Creating directly the Dynamic Type_ DynamicType_ptr pType = DynamicTypeBuilderFactory::get_instance()->create_string type(100); DynamicData* data2 = DynamicDataFactory::get_instance()->create_data(pType); data2->set_string_value("Dynamic String"); 

## 12.2.3 别名
别名类型用于重命名现有类型，同时保留给定类型的其余属性。`DynamicTypeBuilderFactory` 公开 `create_alias_type` 方法，接收基础类型和别名要设置的新名称来创建别名类型。创建 DynamicData 后，用户可以像操作基础类型一样访问其信息。

_// Using Builders_ DynamicTypeBuilder_ptr base_builder = DynamicTypeBuilderFactory::get_instance()-> create_string_builder(100); DynamicType_ptr created_type = DynamicTypeBuilderFactory::get_instance()->create type(base_builder.get()); DynamicTypeBuilder_ptr builder = DynamicTypeBuilderFactory::get_instance()->create alias_builder(created_type, "alias"); DynamicData* data = DynamicDataFactory::get_instance()->create_data(builder.get()); data->set_string_value("Dynamic Alias String"); _// Creating directly the Dynamic Type_ DynamicType_ptr pType = DynamicTypeBuilderFactory::get_instance()->create_string type(100); 



DynamicType_ptr pAliasType = DynamicTypeBuilderFactory::get_instance()->create_alias type(pType, "alias"); DynamicData* data2 = DynamicDataFactory::get_instance()->create_data(pAliasType); data2->set_string_value("Dynamic Alias String"); 

## 12.2.4 枚举
动态类型中的 enum 类型按复杂类型管理，因为它允许添加成员来设置枚举管理的不同值。内部使用 `UINT32` 存储所选值。

要使用枚举，用户必须调用 `create_enum_type` 创建 Dynamic Type builder，然后调用 `add_member`，传入索引和枚举要支持的各个值名称。

_DynamicData_ 类提供 `get_enum_value` 和 `set_enum_value` 方法，可使用 `UINT32` 或 builder 中添加的成员名称字符串进行操作。

DynamicTypeBuilder_ptr builder = DynamicTypeBuilderFactory::get_instance()->create enum_builder(); builder->add_empty_member(0, "DEFAULT"); builder->add_empty_member(1, "FIRST"); builder->add_empty_member(2, "SECOND"); DynamicType_ptr pType = DynamicTypeBuilderFactory::get_instance()->create type(builder.get()); DynamicData* data = DynamicDataFactory::get_instance()->create_data(pType); std::string sValue = "SECOND"; data->set_enum_value(sValue); **uint32_t** uValue = 2; data->set_enum_value(uValue); 

## 12.2.5 位集
位集（Bitset）类型与 _结构体_ 类型相似，但其成员只能是 _位字段_，并且会以优化方式存储。在静态位集中，每个位在内存中只占一位（受平台限制），不考虑对齐。位字段可以匿名（无法寻址），以跳过位集中未使用的位。位集中的每个位字段都可以通过其所需的最小基本类型表示来修改。

|位数|基本类型|
|---|---|
|1|BOOLEAN|
|2-8|UINT8|
|9-16|UINT16|
|17-32|UINT32|
|33-64|UINT64|



每个位字段（或成员）的工作方式都与其基本类型相同，唯一区别是内部存储只修改相关位，而不是整个基本类型的值。

可以使用注解设置位字段的 `bit_bound` 和位置（在静态位集与动态位集之间转换时很有用）。

> _// Create bitfields_ 

> DynamicTypeBuilder_ptr base_type_builder = DynamicTypeBuilderFactory::get_instance()-> create_byte_builder(); 



**auto** base_type = base_type_builder->build(); 

DynamicTypeBuilder_ptr base_type_builder2 = DynamicTypeBuilderFactory::get_instance()- >create_uint32_builder(); **auto** base_type2 = base_type_builder2->build(); DynamicTypeBuilder_ptr builder = DynamicTypeBuilderFactory::get_instance()->create bitset_builder(); builder->add_member(0, "int2", base_type); builder->add_member(1, "int20", base_type2); _// Apply members' annotations_ builder->apply_annotation_to_member(0, ANNOTATION_BIT_BOUND_ID, "value", "2"); builder->apply_annotation_to_member(0, ANNOTATION_POSITION_ID, "value", "0"); builder->apply_annotation_to_member(1, ANNOTATION_BIT_BOUND_ID, "value", "20"); builder->apply_annotation_to_member(1, ANNOTATION_POSITION_ID, "value", "10"); _// 8 bits empty_ DynamicType_ptr pType(DynamicTypeBuilderFactory::get_instance()->create_type(builder. get())); DynamicData_ptr data(DynamicDataFactory::get_instance()->create_data(pType)); data->set_byte_value(234, 0); data->set_uint32_value(2340, 1); octet bValue; **uint32_t** uValue; data->get_byte_value(bValue, 0); data->get_uint32_value(uValue, 1); 

位集支持继承，含义与面向对象编程完全相同。要从另一个位集继承，必须调用工厂的 `create_child_struct_builder` 来创建位集。该方法与结构体共用，并会根据父类型推断当前类型。

DynamicTypeBuilder_ptr child_builder = DynamicTypeBuilderFactory::get_instance()->create_child_struct_builder(builder. get()); 

## 12.2.6 位掩码
位掩码（Bitmask）与 _枚举_ 类型相似，但其成员作为可单独打开和关闭的位标志工作。测试或设置位掩码值时可以应用位运算。`DynamicData` 提供特殊方法 `get_bitmask_value` 和 `set_bitmask_value`，可检索或修改完整值，而不必访问每一位。

位掩码最多可绑定 64 位。

**uint32_t** limit = 5; _// Stores as "octet" // Using Builders_ DynamicTypeBuilder_ptr builder = DynamicTypeBuilderFactory::get_instance()->create bitmask_builder(limit); builder->add_empty_member(0, "FIRST"); builder->add_empty_member(1, "SECOND"); DynamicType_ptr pType(DynamicTypeBuilderFactory::get_instance()->create_type(builder. get())); DynamicData_ptr data(DynamicDataFactory::get_instance()->create_data(pType)); data->set_bool_value(true, 2); **bool** bValue; 



data->get_bool_value(bValue, 0); **uint64_t** fullValue; data->get_bitmask_value(fullValue); 

## 12.2.7 结构体
结构体是常见的复杂类型，允许在其中添加任意类型的成员。结构体本身没有值，只用于包含其他类型。

要管理结构体中的类型，用户可以按照内部类型种类及其 ID 调用相应的 get 和 set 方法。如果结构体包含复杂值，应使用 `loan_value` 访问它，并使用 `return_loaned_value` 释放该指针。`DynamicData` 管理借出值计数，用户不能在未先调用 `return_loaned_value` 的情况下再次借出已借出的值。

ID 必须从零开始连续编号；如果 ID 与下一个值不匹配，`DynamicType` 会修改该 ID。如果两个成员具有相同 ID，添加第二个成员后，前一个成员的 ID 会改为下一个值。要按名称获取成员 ID，`DynamicData` 提供 `get_member_id_by_name` 方法。

DynamicTypeBuilder_ptr builder = DynamicTypeBuilderFactory::get_instance()->create struct_builder(); builder->add_member(0, "first", DynamicTypeBuilderFactory::get_instance()->create int32_type()); builder->add_member(1, "other", DynamicTypeBuilderFactory::get_instance()->create uint64_type()); 

DynamicType_ptr struct_type(builder->build()); DynamicData_ptr data(DynamicDataFactory::get_instance()->create_data(struct_type)); data->set_int32_value(5, 0); data->set_uint64_value(13, 1); 

结构体支持继承，含义与面向对象编程完全相同。要从另一个结构体继承，必须调用工厂的 `create_child_struct_builder` 来创建结构体。该方法与位集共用，并会根据父类型推断当前类型。

DynamicTypeBuilder_ptr child_builder = DynamicTypeBuilderFactory::get_instance()->create_child_struct_builder(builder. get()); 

## 12.2.8 Union
Union 是一种特殊结构体，同一时间只有一个成员处于活动状态。为控制这些成员，用户必须调用 `create_union_type` 方法设置用于选择当前成员的 discriminator 类型。创建动态类型后，每个要添加的成员至少需要一个 `union_case_index`，以设定其选择方式，并可选择将其设为 Union 的默认值。

DynamicType_ptr discriminator = DynamicTypeBuilderFactory::get_instance()->create int32_type(); DynamicTypeBuilder_ptr builder = DynamicTypeBuilderFactory::get_instance()->create union_builder(discriminator); 

builder->add_member(0, "first", DynamicTypeBuilderFactory::get_instance()->create_ _~~ ~~_ ~~int32_type(), "", { 0 }, true);~~ 



builder->add_member(0, "second", DynamicTypeBuilderFactory::get_instance()->create int64_type(), "", { 1 }, false); DynamicType_ptr union_type = builder->build(); DynamicData_ptr data(DynamicDataFactory::get_instance()->create_data(union_type)); data->set_int32_value(9, 0); data->set_int64_value(13, 1); **uint64_t** unionLabel; data->get_union_label(unionLabel); 

## 12.2.9 序列
序列是一种复杂类型，将其成员作为项目列表管理，允许用户插入、移除或访问列表成员。创建该类型时，用户需要指定其存储类型，并可选指定列表大小限制。为简化此类内存管理，`DynamicData` 提供以下方法：- `insert_sequence_data`：在列表末尾创建新元素并返回新元素 ID。- `remove_sequence_data`：移除给定索引处的元素并刷新 ID，以保持列表一致性。- `clear_data`：移除列表中的所有元素。

**uint32_t** length = 2; DynamicType_ptr base_type = DynamicTypeBuilderFactory::get_instance()->create_int32 type(); DynamicTypeBuilder_ptr builder = DynamicTypeBuilderFactory::get_instance()->create sequence_builder(base_type, length); DynamicType_ptr sequence_type = builder->build(); DynamicData_ptr data(DynamicDataFactory::get_instance()->create_data(sequence_type)); MemberId newId, newId2; data->insert_int32_value(10, newId); data->insert_int32_value(12, newId2); data->remove_sequence_data(newId); 

## 12.2.10 数组
数组与序列非常相似，但有两个主要区别：第一，数组可以具有多个维度；第二，数组元素不必连续存储。创建数组的方法需要一组维度大小，以设置要管理的维度数；如果不希望设置限制，可以将每个维度的值设为零，此时应用默认值（100）。为简化数组管理，`DynamicData` 类中的每个 set 方法都会在给定 ID 处没有项目时创建该项目。数组也具有与序列类似的元素创建和删除方法：`insert_array_data`、`remove_array_data` 和 `clear_data`。此外，还有一个特殊方法 `get_array_index`，它通过为数组支持的每个维度提供一组索引来返回位置 ID，这在多维数组中很有用。

std::vector< **uint32_t** > lengths = { 2, 2 }; 

DynamicType_ptr base_type = DynamicTypeBuilderFactory::get_instance()->create_int32 type(); DynamicTypeBuilder_ptr builder = DynamicTypeBuilderFactory::get_instance()->create array_builder(base_type, lengths); DynamicType_ptr array_type = builder->build(); DynamicData_ptr data(DynamicDataFactory::get_instance()->create_data(array_type)); 



MemberId pos = data->get_array_index({1, 0}); data->set_int32_value(11, pos); data->set_int32_value(27, pos + 1); data->clear_array_data(pos); 

## 12.2.11 映射
映射（Map）包含一组“键-值”类型对，允许用户插入、移除或修改映射中的元素类型。与序列的主要区别是，映射以元素对工作，并会创建键元素的副本，以阻止直接访问这些元素。

要创建映射，用户必须设置键元素和值元素的类型，并可选设置映射大小限制。要向映射添加新元素，`DynamicData` 提供 `insert_map_data` 方法，返回映射内键元素和值元素的 ID。要从映射移除元素，可使用 `remove_map_data` 方法；该方法使用给定 ID 查找键元素，并从映射中移除键和值元素。`clear_data` 方法会移除映射中的所有元素。

**uint32_t** length = 2; DynamicType_ptr base = DynamicTypeBuilderFactory::get_instance()->create_int32_type(); DynamicTypeBuilder_ptr builder = DynamicTypeBuilderFactory::get_instance()->create map_builder(base, base, length); DynamicType_ptr map_type = builder->build(); DynamicData_ptr data(DynamicDataFactory::get_instance()->create_data(map_type)); DynamicData_ptr key(DynamicDataFactory::get_instance()->create_data(base)); MemberId keyId; MemberId valueId; data->insert_map_data(key.get(), keyId, valueId); MemberId keyId2; MemberId valueId2; key->set_int32_value(2); data->insert_map_data(key.get(), keyId2, valueId2); data->set_int32_value(53, valueId2); data->remove_map_data(keyId); data->remove_map_data(keyId2); 

# 12.3 复杂示例
## 12.3.1 嵌套结构体
结构体允许在其中添加其他结构体，但用户必须注意：访问这些成员需要调用 `loan_value` 获取数据指针，并调用 `return_loaned_value` 释放。DynamicData 管理借出值计数，用户不能在未先调用 `return_loaned_value` 的情况下再次借出已借出的值。

DynamicTypeBuilder_ptr builder = DynamicTypeBuilderFactory::get_instance()->create struct_builder(); builder->add_member(0, "first", DynamicTypeBuilderFactory::get_instance()->create int32_type()); builder->add_member(1, "other", DynamicTypeBuilderFactory::get_instance()->create uint64_type()); DynamicType_ptr struct_type = builder->build(); DynamicTypeBuilder_ptr parent_builder = DynamicTypeBuilderFactory::get_instance()-> create_struct_builder(); parent_builder->add_member(0, "child_struct", struct_type); parent_builder->add_member(1, "second", DynamicTypeBuilderFactory::get_instance()-> create_int32_type()); DynamicData_ptr data(DynamicDataFactory::get_instance()->create_data(parent_builder. get())); DynamicData* child_data = data->loan_value(0); child_data->set_int32_value(5, 0); child_data->set_uint64_value(13, 1); data->return_loaned_value(child_data); 

## 12.3.2 结构体继承
结构体可以从其他结构体继承。为此，`DynamicTypeBuilderFactory` 提供 `create_child_struct_type` 方法，将给定结构体类型与新类型关联。结果类型包含基类的成员以及用户添加的成员。

结构体支持多级继承，会递归创建结构体层次结构中所有类型的成员。

DynamicTypeBuilder_ptr builder = DynamicTypeBuilderFactory::get_instance()->create struct_builder(); builder->add_member(0, "first", DynamicTypeBuilderFactory::get_instance()->create int32_type()); builder->add_member(1, "other", DynamicTypeBuilderFactory::get_instance()->create uint64_type()); DynamicTypeBuilder_ptr child_builder = DynamicTypeBuilderFactory::get_instance()-> create_child_struct_builder(builder.get()); builder->add_member(2, "third", DynamicTypeBuilderFactory::get_instance()->create uint64_type()); DynamicType_ptr struct_type = child_builder->build(); DynamicData_ptr data(DynamicDataFactory::get_instance()->create_data(struct_type)); data->set_int32_value(5, 0); data->set_uint64_value(13, 1); data->set_uint64_value(47, 2); 

## 12.3.3 别名的别名
别名类型支持递归，因此如果用户需要创建另一个别名的别名，可以调用 `create_alias_type` 方法，并将该别名作为基础类型。

_// Using Builders_ DynamicTypeBuilder_ptr created_builder = DynamicTypeBuilderFactory::get_instance()-> create_string_builder(100); DynamicType_ptr created_type = DynamicTypeBuilderFactory::get_instance()->create type(created_builder.get()); DynamicTypeBuilder_ptr builder = DynamicTypeBuilderFactory::get_instance()->create alias_builder(created_builder.get(), "alias"); DynamicTypeBuilder_ptr builder2 = DynamicTypeBuilderFactory::get_instance()->create alias_builder(builder.get(), "alias2"); DynamicData* data(DynamicDataFactory::get_instance()->create_data(builder2->build())); data->set_string_value("Dynamic Alias 2 String"); 

_// Creating directly the Dynamic Type_ DynamicType_ptr pType = DynamicTypeBuilderFactory::get_instance()->create_string type(100); DynamicType_ptr pAliasType = DynamicTypeBuilderFactory::get_instance()->create_alias type(pType, "alias"); DynamicType_ptr pAliasType2 = DynamicTypeBuilderFactory::get_instance()->create_alias type(pAliasType, "alias2"); DynamicData* data2(DynamicDataFactory::get_instance()->create_data(pAliasType)); data2->set_string_value("Dynamic Alias 2 String"); 

## 12.3.4 包含复杂类型的 Union
Union 支持复杂类型，访问它们的可用接口是调用 `loan_value` 获取数据指针并将该字段设为活动字段，然后调用 `return_loaned_value` 释放。

DynamicType_ptr discriminator = DynamicTypeBuilderFactory::get_instance()->create int32_type(); DynamicTypeBuilder_ptr builder = DynamicTypeBuilderFactory::get_instance()->create union_builder(discriminator); builder->add_member(0, "first", DynamicTypeBuilderFactory::get_instance()->create int32_type(), "", { 0 }, true); DynamicTypeBuilder_ptr struct_builder = DynamicTypeBuilderFactory::get_instance()-> create_struct_builder(); struct_builder->add_member(0, "first", DynamicTypeBuilderFactory::get_instance()-> create_int32_type()); struct_builder->add_member(1, "other", DynamicTypeBuilderFactory::get_instance()-> create_uint64_type()); builder->add_member(1, "first", struct_builder.get(), "", { 1 }, false); DynamicType_ptr union_type = builder->build(); DynamicData_ptr data(DynamicDataFactory::get_instance()->create_data(union_type)); DynamicData* child_data = data->loan_value(1); child_data->set_int32_value(9, 0); child_data->set_int64_value(13, 1); data->return_loaned_value(child_data); 

## 12.3.5 注解
`DynamicTypeBuilder` 允许使用以下方法对当前类型和内部成员应用注解：

- `apply_annotation`

• `apply_annotation_to_member`

`apply_annotation_to_member` 接收要应用注解的 `MemberId`，以及与 `apply_annotation` 相同的参数。常用参数包括注解名称、键和值。

例如，如果定义如下注解：

@annotation MyAnnotation { long value; string name; }; 

然后通过 IDL 将其应用到结构体：

@MyAnnotation(5, "length") struct MyStruct { ... 

使用 DynamicTypes 的等价代码如下：

_// Apply the annotation_ DynamicTypeBuilder_ptr builder = DynamicTypeBuilderFactory::get_instance()->create struct_builder(); _//..._ builder->apply_annotation("MyAnnotation", "value", "5"); builder->apply_annotation("MyAnnotation", "name", "length"); 

### 内置注解
以下注解可修改 DynamicTypes 的行为：

- `@position`：应用于 _Bitmask_ 时，按 IDL 注解的预期设置标志位置。应用于 _Bitset_ 时，设置位字段的基准位置，可用于识别未分配的位。

- `@bit_bound`：应用于 _Bitset_，设置位字段的位数。

- `@key`：`@Key` 的别名。更多详情见 _Topic 与 Key_ 一节。

- `@default`：设置成员默认值。

- `@non_serialized`：将成员排除在序列化之外。

# 12.4 序列化
动态类型像任何由 IDL 生成的类一样拥有自己的 pubsub 类型，其管理方式也非常相似。

DynamicType_ptr pType = DynamicTypeBuilderFactory::get_instance()->create_int32 type(); DynamicPubSubType pubsubType(pType); 

_// SERIALIZATION EXAMPLE_ DynamicData* pData = DynamicDataFactory::get_instance()->create_data(pType); **uint32_t** payloadSize = **static_cast** < **uint32_t** >(pubsubType. getSerializedSizeProvider(data)()); 



SerializedPayload_t payload(payloadSize); pubsubType.serialize(data, &payload); _// DESERIALIZATION EXAMPLE_ types::DynamicData* data2 = DynamicDataFactory::get_instance()->create_data(pType); pubsubType.deserialize(&payload, data2); 

可以使用 `@non_serialized` 注解将成员标记为序列化时忽略。

# 12.5 重要说明
动态类型最重要的部分是内存管理，因为每个动态类型和动态数据都由指针管理。存储在另一个动态对象内部的每个对象都由其所有者管理，因此用户只需管理通过调用工厂创建的对象。两个工厂负责管理这些对象，并且必须创建和删除每个对象。

DynamicTypeBuilder* pBuilder = DynamicTypeBuilderFactory::get_instance()->create uint32_builder(); DynamicType_ptr pType = DynamicTypeBuilderFactory::get_instance()->create_int32 type(); DynamicData* pData = DynamicDataFactory::get_instance()->create_data(pType); DynamicTypeBuilderFactory::get_instance()->delete_builder(pBuilder); DynamicDataFactory::get_instance()->delete_data(pData); 

为简化这项管理，库引入一种特殊共享指针（`DynamicTypeBuilder_ptr` 和 `DynamicData_ptr`），可直接调用工厂删除对象。使用这类指针的唯一限制是 `loan_value` 和 `return_loaned_value` 方法，因为它们返回的指针指向已由库管理的对象，将 `DynamicData_ptr` 与它们一起使用会导致崩溃。DynamicType 始终以 `DynamicType_ptr` 返回，因为其内存没有内部管理。

DynamicTypeBuilder_ptr pBuilder = DynamicTypeBuilderFactory::get_instance()->create uint32_builder(); DynamicType_ptr pType = DynamicTypeBuilderFactory::get_instance()->create_int32 type(); DynamicData_ptr pData(DynamicDataFactory::get_instance()->create_data(pType)); 

# 12.6 动态类型发现与端点匹配
使用动态类型支持时，_Fast RTPS_ 会使用可选的 TypeObjectV1 和 TypeIdV1。当前状态下，匹配只验证两个端点是否使用相同的 Topic 类型，但不会就此进行协商。

此验证依次使用 TypeIdentifier、MinimalTypeObject，最后使用 CompleteTypeObject。

如果某个端点改为使用 CompleteTypeObject，则可以实现 _发现时数据定型（Discovery-Time Data Typing）_。


## 12.6.1 TypeObject（TypeObjectV1）
TypeObject 有两种：MinimalTypeObject 和 CompleteTypeObject。

- MinimalTypeObject 用于检查类型之间的兼容性。

- CompleteTypeObject 完整描述类型。

二者都定义在 DDS-XTypes V1.2 文档的附录中，因此本文档不介绍其细节。

- TypeObject 是包含 _Minimal_ 和 _Complete_ 两种表示的 IDL union。

## 12.6.2 TypeIdentifier（TypeIdV1）
TypeIdentifier 也在 _DDS-XTypes V1.2 文档_ 的附录中描述。它表示基本类型的完整描述，并为复杂类型提供 EquivalenceKind。EquivalenceKind 是 14 个八位组的哈希码，具体如 _DDS-XTypes V1.2 文档_ 所述。

## 12.6.3 TypeObjectFactory
负责管理所有已注册 TypeObject 和 TypeIdentifier 的创建与访问的 _Singleton_ 类。它可以根据基本 TypeIdentifier（即 discriminator 不是 `EK_MINIMAL` 或 `EK_COMPLETE` 的 TypeIdentifier）生成完整的 DynamicType。

## 12.6.4 Fastrtpsgen
_FastRTPSGen_ 已升级为生成 `XXXTypeObject.h` 和 `XXXTypeObject.cxx` 文件，其中 XXX 为 IDL 类型。这些文件为类型 XXX 提供一个小型 Type Factory。通常不会直接使用这些文件，因为类型 XXX 现在会在构造函数中通过其工厂向 TypeObjectFactory 注册，从而非常容易地将静态类型与动态类型一起使用。

## 12.6.5 发现时数据定型
使用 fastdds API 时，如果 participant 发现某个端点发送了描述未知类型的完整 TypeObject 或简单 TypeIdentifier，_Fast RTPS_ 会调用 participant 监听器的 `on_type_discovery` 方法，并传入所提供的 TypeObject、TypeIdentifier，以及（在可能时）可直接使用的 `DynamicType_ptr`。发现时数据定型允许发现简单的 DynamicType。依赖其他 TypeObject 的 TypeObject 不能通过发现时数据定型在本地构建，而应改用 _TypeLookup Service_。

为便于共享发现时数据定型所用的 TypeObject 和 TypeIdentifier，`TopicAttributes` 中有一个名为 `auto_fill_type_object` 的属性。如果设为 true，本地 participant 在发现时会尝试填充相应 `ReaderProxyData` 或 `WriterProxyData` 中的 `type` 和 `type_id` 字段，以发送给远程端点。

## 12.6.6 TypeLookup Service
使用 fastdds API 时，如果 participant 发现某个端点发送了描述未知类型的 TypeInformation，_Fast RTPS_ 会调用 participant 监听器的 `on_type_information_received` 方法并传入该 TypeInformation。随后，用户可以使用 TypeLookup Service 尝试获取完整 TypeObject 层次结构，以便在本地构建远程类型。

要启用此内置 TypeLookup Service，用户必须在 Participant 的 RTPS 内置属性中启用它：

participant_attr.rtps.builtin.typelookup_config.use_client = true; participant_attr.rtps.builtin.typelookup_config.use_server = true; 

Participant 可以配置为 TypeLookup 服务器、客户端或二者兼有。

为便于在收到远程端点的 TypeInformation 后恢复并注册远程类型，DomainParticipant 提供 `register_remote_type` 函数，其内部使用 TypeLookup Service。

成功时，该函数会调用作为参数传入的函数，其签名如下：

**void** (std::string& type_name, **const** DynamicType_ptr type) 

- `type_name`：传给 `register_remote_type` 函数的类型名称，用于允许使用同一函数进行多次调用。

- `type`：在可能时，函数会以已构建的 DynamicType 调用。如果无法构建，则为

`nullptr`。在这种情况下，用户可以尝试自行使用工厂构建类型，但构建过程很可能会失败。

为便于共享 TypeLookup Service 使用的 TypeInformation，`TopicAttributes` 中有一个名为 `auto_fill_type_information` 的属性。如果设为 true，本地 participant 在发现时会尝试填充相应 `ReaderProxyData` 或 `WriterProxyData` 中的 `type_information` 字段，以发送给远程端点。

# 12.7 XML 动态类型
_XML 动态类型_ 允许 _eProsima Fast RTPS_ 通过 XML 直接定义并创建动态类型。这使任何应用都能更改 `TopicDataType`，而无需修改源代码。

# 12.8 动态 HelloWorld 示例
## 12.8.1 DynamicHelloWorldExample
利用本文档中描述的部分功能，_examples/C++/DynamicHelloWorldExample_ 文件夹中有一个名为 DynamicHelloWorldExample 的示例，它使用 DynamicType 生成来提供 `TopicDataType`。

该示例与经典 HelloWorldExample 兼容。

下面简要展示如何使用 DynamicTypes 创建 HelloWorld 类型：

_// In HelloWorldPublisher.h // Dynamic Types_ eprosima::fastrtps::types::DynamicData* m_DynHello; eprosima::fastrtps::types::DynamicPubSubType m_DynType; _// In HelloWorldPublisher.cpp // Create basic builders_ DynamicTypeBuilder_ptr struct_type_builder(DynamicTypeBuilderFactory::get_instance()-> create_struct_builder()); 



_// Add members to the struct._ struct_type_builder->add_member(0, "index", DynamicTypeBuilderFactory::get_instance()- >create_uint32_type()); struct_type_builder->add_member(1, "message", DynamicTypeBuilderFactory::get instance()->create_string_type()); struct_type_builder->set_name("HelloWorld"); DynamicType_ptr dynType = struct_type_builder->build(); m_DynType.SetDynamicType(dynType); m_DynHello = DynamicDataFactory::get_instance()->create_data(dynType); m_DynHello->set_uint32_value(0, 0); m_DynHello->set_string_value("HelloWorld", 1); 

## 12.8.2 DDSDynamicHelloWorldExample
_examples/C++/DDS/DynamicHelloWorldExample_ 文件夹中的另一个示例展示了一个 shared 类型从 XML 文件加载的 publisher，以及一个使用 _发现时数据定型_ 发现该类型的 subscriber；该 subscriber 在检查类型后显示收到的数据。

## 12.8.3 TypeLookupService
最后，_examples/C++/DDS/TypeLookupService_ 文件夹中有一个使用 TypeLookup Service 的示例。它与 DDSDynamicHelloWorldExample 非常相似，但共享类型足够复杂，由于依赖内部结构体类型而需要使用 TypeLookup Service。

# 第 13 章：持久化
默认情况下，writer 的 History 在整个 writer 生命周期内可供远程 reader 使用。可以将 Fast RTPS 配置为在多次应用执行之间提供持久化。writer 再次创建时，将保留先前的 History，新的远程 reader 会收到该 writer 生命周期内发送的所有样本。

reader 会保存每个匹配 writer 最近通知用户的变更信息。持久化该信息可以节省带宽，因为 reader 不会向 writer 请求已通知的变更。

总之，启用该功能可以保护端点状态免受意外故障影响：端点重启后会像只是与网络断开一样继续通信。

例如，假设某个设置为保留最近 100 个样本的 writer 的 History 已满，而其运行机器发生断电。writer 再次启动后，如果创建新的 reader，它将无法收到 writer History 中原有的 100 个样本。启用持久化后，writer History 中的变更会写入磁盘，并在 writer 重启时重新读取。

对于 reader，写入磁盘的信息有所不同：仅保存最近一次通知用户的变更信息。持久化 reader 重启时会加载该信息，并且只要求匹配的 writer 重发尚未通知上层的那部分变更。

### persistence_guid
每当创建端点（reader 或 writer）时，都会生成唯一标识符（GUID）。如果端点重启，将生成新的 GUID，其他端点无法知道它仍是同一个端点。因此，应在 `eprosima::fastrtps::rtps::EndpointAttributes` 上配置特定参数 `persistence_guid`。该参数将用作磁盘保存数据的主键，也用于在 DDS 域中标识该端点。

# 13.1 配置
建议在阅读本节时参考发行版附带的该功能使用示例，其位置为 _examples/RTPSTest_persistent_。

为使持久化功能正常工作，应设置以下特定 `eprosima::fastrtps::rtps::Writer` 或 `eprosima::fastrtps::rtps::Reader` 属性：

- `durabilityKind` 应设置为 `TRANSIENT`。

- `persistence_guid` 不应全为零。

- 应在 `eprosima::fastrtps::rtps::Writer`、`eprosima::fastrtps::rtps::Reader` 或 `eprosima::fastrtps::rtps::RTPSParticipant` 上配置持久化插件。

可以通过 `eprosima::fastrtps::rtps::RTPSParticipant` 属性使用 properties 选择并配置持久化插件。`eprosima::fastrtps::rtps::Property` 由其名称（`std::string`）和值（`std::string`）定义。本页表格展示每个持久化插件使用的属性。

# 13.2 内置插件
当前版本附带一个内置持久化插件：

- **SQLITE3**：该插件使用 SQLite3 API 在本地文件中提供持久化。

## 13.2.1 PERSISTENCE:SQLITE3
该内置插件使用 SQLite3 API 在本地文件中提供持久化。

可以使用 RTPSParticipant、Reader 或 Writer 属性 `dds.persistence.plugin`（值为 `builtin.SQLITE3`）激活该插件。下表列出该持久化插件使用的属性。

表 1：**配置 Persistence::SQLITE3 的属性**

|属性<br>名<br>（所有<br>属性|均具有|属性值|
|---|---|---|
|“dds.persistence.sqlite3.”前缀）|||
|filename||用于持久化存储的文件名。默认|
|||值：_persistence.db_|



**注意：** 当前该插件不支持两个进程访问同一个 SQLite3 文件。这可能导致不一致和失败。请确保每个进程使用不同的 SQLite3 文件。

## 13.2.2 示例
本示例说明如何配置 RTPSParticipant 以激活和配置 _PERSISTENCE:SQLITE3_ 插件。它还将 Writer 配置为在本地存储中持久化其 History，并将 Reader 配置为在本地存储中持久化最高的已通知序列号。

### RTPSParticipant 属性
eprosima::fastrtps::rtps::RTPSParticipantAttributes part_attr; 

_// Activate Persistence:SQLITE3 plugin_ part_attr.properties.properties().emplace_back("dds.persistence.plugin", "builtin. SQLITE3"); _// Configure Persistence:SQLITE3 plugin_ part_attr.properties.properties().emplace_back("dds.persistence.sqlite3.filename", "example.db"); 

### Writer 属性
eprosima::fastrtps::rtps::WriterAttributes writer_attr; _// Set durability to TRANSIENT_ writer_attr.endpoint.durabilityKind = TRANSIENT; _// Set persistence_guid_ writer_attr.endpoint.persistence_guid.guidPrefix.value[11] = 1; writer_attr.endpoint.persistence_guid.entityId = 0x12345678; 

### Reader 属性
eprosima::fastrtps::rtps::ReaderAttributes reader_attr; _// Set durability to TRANSIENT_ reader_attr.endpoint.durabilityKind = TRANSIENT; _// Set persistence_guid_ reader_attr.endpoint.persistence_guid.guidPrefix.value[11] = 1; reader_attr.endpoint.persistence_guid.entityId = 0x3456789A; 

# 第 14 章：XML 配置文件
_配置_ 一节说明如何使用 XML 配置文件配置实体属性，而本节进一步深入介绍每个字段的可用值以及如何组合完整 XML 文件。

_eProsima Fast RTPS_ 允许加载多个 XML 文件，每个文件包含若干 XML 配置。除加载用户 XML 文件的 API 函数外，_eProsima Fast RTPS_ 在初始化时还会尝试查找并加载多个默认 XML 文件。_eProsima Fast RTPS_ 提供以下使用默认 XML 文件的方式：

- 使用位于当前执行路径下、名为 _DEFAULT_FASTRTPS_PROFILES.xml_ 的 XML 文件。

- 使用位置由环境变量 _FASTRTPS_DEFAULT_PROFILES_FILE_ 定义的 XML 文件。

XML 配置由唯一名称定义（在 _传输描述符_ 情况下为 `<transport_id>` 标签），用于在创建 Fast RTPS 实体、_传输_ 或 _动态话题类型_ 时引用该 XML 配置。

# 14.1 创建 XML
一个 XML 文件可以包含多个 XML 配置。可用配置类型包括 _传输描述符_、_XML 动态类型_、_Participant 配置_、_Publisher 配置_ 和 _Subscriber 配置_。

<transport_descriptor> <transport_id> TransportProfile </transport_id> <type> UDPv4 </type> _<!-- ... -->_ </transport_descriptor> <types> <type> <struct name="struct_profile" > _<!-- ... -->_ </struct> </type> 



</types> <participant profile_name="participant_profile" > <rtps> _<!-- ... -->_ </rtps> </participant> <publisher profile_name="publisher_profile" > _<!-- ... -->_ </publisher> <subscriber profile_name="subscriber_profile" > _<!-- ... -->_ </subscriber> 

Fast-RTPS XML 格式在多种配置类型中使用一些共同结构。为提高可读性，_通用配置_ 一节汇总这些共同结构。

最后，_示例_ 一节展示一个使用全部可能配置的 XML 文件。该示例可作为查找特定属性及其用法时的快速参考。此 XSD 文件也可作为快速参考。

## 14.1.1 加载和应用配置
创建任何实体之前，必须使用 `Domain::loadXMLProfilesFile` 函数加载 XML 文件。`createParticipant`、`createPublisher` 和 `createSubscriber` 各有一个接收配置名称作为参数的版本。_eProsima Fast RTPS_ 使用该配置名称查找 XML 配置，并将其应用到实体。

eprosima::fastrtps::Domain::loadXMLProfilesFile("my_profiles.xml"); Participant *participant = Domain::createParticipant("participant_xml_profile"); Publisher *publisher = Domain::createPublisher(participant, "publisher_xml_profile"); Subscriber *subscriber = Domain::createSubscriber(participant, "subscriber_xml_profile "); 

要通过 XML 声明加载动态类型，请参见 _XML 动态类型_ 的 _用法_ 一节。

# 14.2 库设置
本节介绍不限定于特定实体（如 participant、subscriber、publisher）或功能（如传输或类型）的通用设置。这些设置都汇集在 `library_settings` 配置下。

<library_settings> <intraprocess_delivery> FULL </intraprocess_delivery> _<!-- OFF | USER_DATA_ONLY | FULL -->_ </library_settings> 

目前此处仅包含 _进程内投递_ 功能。

# 14.3 传输描述符
本节说明如何创建供 _Participant 配置_ 引用的传输描述符。定义好的传输描述符被 **Participant 配置** 引用后，每次实例化该配置时都会使用或创建相关传输。

以下 XML 代码展示完整的可配置参数列表：

<transport_descriptors> <transport_descriptor> <transport_id> TransportId1 </transport_id> _<!-- string -->_ <type> UDPv4 </type> _<!-- string -->_ <sendBufferSize> 8192 </sendBufferSize> _<!-- uint32 -->_ <receiveBufferSize> 8192 </receiveBufferSize> _<!-- uint32 -->_ <TTL> 250 </TTL> _<!-- uint8 -->_ <non_blocking_send> false </non_blocking_send> _<!-- boolean -->_ <maxMessageSize> 16384 </maxMessageSize> _<!-- uint32 -->_ <maxInitialPeersRange> 100 </maxInitialPeersRange> _<!-- uint32 -->_ <interfaceWhiteList> <address> 192.168.1.41 </address> _<!-- string -->_ <address> 127.0.0.1 </address> _<!-- string -->_ </interfaceWhiteList> <wan_addr> 80.80.55.44 </wan_addr> _<!-- string -->_ <output_port> 5101 </output_port> _<!-- uint16 -->_ <keep_alive_frequency_ms> 5000 </keep_alive_frequency_ms> _<!-- uint32 -->_ <keep_alive_timeout_ms> 25000 </keep_alive_timeout_ms> _<!-- uint32 -->_ <max_logical_port> 9000 </max_logical_port> _<!-- uint16 -->_ <logical_port_range> 100 </logical_port_range> _<!-- uint16 -->_ <logical_port_increment> 2 </logical_port_increment> _<!-- uint16 -->_ <listening_ports> <port> 5100 </port> _<!-- uint16 -->_ <port> 5200 </port> _<!-- uint16 -->_ </listening_ports> <calculate_crc> false </calculate_crc> _<!-- boolean -->_ <check_crc> false </check_crc> _<!-- boolean -->_ <enable_tcp_nodelay> false </enable_tcp_nodelay> _<!-- boolean -->_ <tls> _<!-- TLS Section -->_ </tls> </transport_descriptor> 

XML 标签 `<transport_descriptors>` 可以包含任意数量的 `<transport_descriptor>`。

|名称|说明|值|默认|
|---|---|---|---|
||||值|
|<transport_|id>|用于标识每个传输描述符的唯一名称。|string||
|<type>|传输描述符类型。|UDPv4,<br>UDPv6,<br>TCPv4,<br>TCPv6,<br>SHM|UDPv4|
|<sendBuffer|Size>|套接字发送缓冲区大小，单位为字节。如果值为零，FastRTPS 将使用套接字配置中的默认大小，且最小为 65536 字节。|uint32|0|
|<receiveBuf|ferSize>|套接字接收缓冲区大小，单位为字节。如果值为零，FastRTPS 将使用套接字配置中的默认大小，且最小为 65536 字节。|uint32|0|
|<TTL>|_Time To Live_，**仅**用于 UDP 传输。|uint8|1|
|<non_blocki|ng_send>|是否在套接字上启用非阻塞发送模式。|bool|false|
|<maxMessage|Size>|传输消息缓冲区的最大大小，单位为字节。|uint32|65500|
|<maxInitial|PeersRange>|尝试连接时最多推测的初始对等节点数量。|uint32|4|
|<interfaceW|hiteList>|允许定义 _接口白名单_。|_Whitelist_<br>_Inter-_<br>_faces_||
|<wan_addr>|使用 **TCPv4 传输**时的公网 WAN 地址。如果传输不需要定义 WAN 地址，此字段为可选。|IPv4 格式字符串<br>XXX.XXX.XXX.<br>XXX.||
|<output_por|t>|用于输出绑定的端口。如果未定义此字段，输出端口将随机选择（**仅限** UDP）。|uint16|0|
|<keep_alive|_frequency_ms>|发送 _RTCP_ keep-alive 请求的频率，单位为毫秒（**仅限** TCP）。|uint32|50000|
|<keep_alive|_timeout_ms>|自上次发送 keep-alive 请求起，超过多少毫秒后将连接视为断开（**仅限** TCP）。|uint32|10000|
|<max_logica|l_port>|在 _RTCP_ 协商期间尝试的最大逻辑端口数（**仅限** TCP）。|uint16|100|
|<logical_po|rt_range>|_RTCP_ 协商期间每次请求尝试的最大逻辑端口数（**仅限** TCP）。|uint16|20|
|<logical_po|rt_increment>|_RTCP_ 协商期间尝试的逻辑端口之间的增量（**仅限** TCP）。|uint16|2|
|<listening_|ports>|作为输入连接 TCP acceptor 的本地端口。如果未设置，传输将仅作为 TCP client 工作（**仅限** TCP）。|List<br><uint16>||
|<tls>|允许定义 TLS 相关参数和选项（**仅限** TCP）。|_TLS 配置_||
|<segment_si|i<br>ze>|共享内存段大小，单位为字节（可选，**仅限** SHM）。|uint32|262144|
|<port_queue|_capacity>|每个 Listener 可用的容量（以消息数为单位）（可选，**仅限** SHM）。|uint32|512|
|<healthy_ch|eck_timeout_ms>|检查 Listener 是否存活且正常时使用的最大超时时间，单位为毫秒（可选，**仅限** SHM）。|uint32|1000|
|<rtps_dump_|file>|用于调试的 RTPS 消息存储完整路径（包括文件名）。空字符串表示不进行跟踪（可选，**仅限** SHM）。|string|空|



RTCP 是通过 TCP/IP 连接与 RTPS 通信时使用的控制协议。

_传输_ 一节中还有更多传输描述符示例。

## 14.3.1 TLS 配置
Fast-RTPS 允许通过传输描述符的 `<tls>` 标签配置 TLS 参数。完整选项列表如下：

<transport_descriptors> <transport_descriptor> <transport_id> Test </transport_id> <type> TCPv4 </type> <tls> <password> Password </password> <private_key_file> Key_file.pem </private_key_file> <rsa_private_key_file> RSA_file.pem </rsa_private_key_file> <cert_chain_file> Chain.pem </cert_chain_file> <tmp_dh_file> DH.pem </tmp_dh_file> <verify_file> verify.pem </verify_file> <verify_mode> <verify> VERIFY_PEER </verify> </verify_mode> <options> <option> NO_TLSV1 </option> <option> NO_TLSV1_1 </option> </options> <verify_paths> <verify_path> Path1 </verify_path> <verify_path> Path2 </verify_path> <verify_path> Path3 </verify_path> </verify_paths> <verify_depth> 55 </verify_depth> <default_verify_path> true </default_verify_path> <handshake_role> SERVER </handshake_role> </tls> </transport_descriptor> </transport_descriptors> 

|名称|说明|值|默认<br>值|
|---|---|---|---|
|<passwor|d>|`private_key_file`（或 RSA）的密码（如果提供）。|string||
|<private|_key_file>|私钥证书文件路径。|string||
|<rsa_pri|vate_key_file>|RSA 私钥证书文件路径。|string||
|<cert_ch|ain_file>|公钥证书链文件路径。|string||
|<tmp_dh_|file>|Diffie-Hellman 参数文件路径。|string||
|<verify_|file>|CA（Certification Authority，证书颁发机构）文件路径。|string||
|<verify_|mode>|设置验证模式掩码。|VERIFY_NONE,<br>VERIFY_PEER,<br>VERIFY_FAIL_IF_NO_PEER_CERT,<br>VERIFY_CLIENT_ONCE||
|<options|>|设置 SSL Context 选项掩码。|DEFAULT_WORKAROUNDS,NO_COMPRESSION,<br>NO_SSLV2,<br>NO_SSLV3,<br>NO_TLSV1,<br>NO_TLSV1_1,<br>NO_TLSV1_2,<br>NO_TLSV1_3,<br>SINGLE_DH_USE||
|<verify_|paths>|系统查找验证文件的路径。|string||
|<verify_|depth>|验证中间证书时允许的最大深度。|uint32||
|<default|_verify_path>|系统查找验证文件的默认路径。|boolean|false|
|<handsha|ke_role>|传输在握手时扮演的角色。默认情况下，acceptor 作为 SERVER，connector 作为 CLIENT。|DEFAULT,SERVER,CLIENT|DEFAULT|



# 14.4 XML 动态类型
XML 动态类型允许通过 XML 直接定义并创建 _eProsima Fast RTPS 动态类型_。这使任何应用都能更改 `TopicDataType`，而无需修改源代码。

## 14.4.1 XML 结构
XML 类型定义（`<types>` 标签）在 XML 文件中的放置方式与 profiles 标签类似。它可以是独立的 XML Types 文件，也可以是 Fast-RTPS XML 根标签（`<dds>`）的子元素。`types` 标签内必须有一个或多个 `type` 标签（`<type>`）。

独立文件：

<types> <type> _<!-- Type definition -->_ </type> <type> _<!-- Type definition --> <!-- Type definition -->_ 



</type> </types> 

作为根元素子项：

<dds> <types> <type> _<!-- Type definition -->_ </type> <type> _<!-- Type definition --> <!-- Type definition -->_ </type> </types> </dds> 

最后，每个 `<type>` 标签可以包含一个或多个 _类型定义_。在同一个 `<type>` 标签中定义多个类型，或为每个类型分别使用 `<type>` 标签，结果相同。

## 14.4.2 类型定义
### 枚举（Enum）
`<enum>` 类型由名称和一组枚举项定义，每个枚举项包含名称和可选值。

示例：

XML C++ **<enum** name="MyEnum" **>** DynamicTypeBuilder_ptr enum_builder = **<enumerator** name="A" value="0" **/>** DynamicTypeBuilderFactory::get_ **<enumerator** name="B" value="1" **/>** instance()->create_enum_builder(); **<enumerator** name="C" value="2" **/>** enum_builder->set_name("MyEnum"); **</enum>** enum_builder->add_empty_member(0, "A"); enum_builder->add_empty_member(1, "B"); enum_builder->add_empty_member(2, "C"); DynamicType_ptr enum_type = DynamicTypeBuilderFactory::get instance()->create_type(enum_builder. get()); 

### 类型别名（Typedef）
`<typedef>` 类型由名称和值定义；对于复杂类型，也可以由内部元素定义。`<typedef>` 对应动态类型术语中的 Alias。

示例：

|XML|C++|
|---|---|
|**<typedef** name="MyAliasEnum" type=<br> "nonBasic" nonBasicTypeName="MyEnum"**/>**<br>**<typedef** name="MyAliasArray" type="int32<br> " arrayDimension="2,2"**/>**|DynamicTypeBuilder_ptr alias1_builder =<br> DynamicTypeBuilderFactory::get_<br> instance()->create_alias_builder(enum_<br> builder.get(), "MyAlias1");<br>DynamicType_ptr alias1_type =<br> DynamicTypeBuilderFactory::get_<br> instance()->create_type(alias1_builder.<br> get());<br>std::vector<**uint32_t**> sequence_lengths =<br> { 2, 2 };<br>DynamicTypeBuilder_ptr int_builder =<br> DynamicTypeBuilderFactory::get_<br> instance()->create_int32_builder();<br>DynamicTypeBuilder_ptr array_builder =<br> DynamicTypeBuilderFactory::get_<br> instance()->create_array_builder(int_<br> builder.get(), sequence_lengths);<br>DynamicTypeBuilder_ptr alias2_builder =<br> DynamicTypeBuilderFactory::get_<br> instance()->create_alias_builder(array_<br> builder.get(), "MyAlias2");<br>DynamicType_ptr alias2_type =<br> DynamicTypeBuilderFactory::get_<br> instance()->create_type(alias2_builder.<br> get());|



### 结构体（Struct）
`<struct>` 类型由名称和内部 _成员_ 定义。示例：

|XML|C++|
|---|---|
|**<struct** name="MyStruct"**>**<br>**<member** name="first" type="int32"**/>**<br>**<member** name="second" type="int64"**/>**<br>**</struct>**|DynamicTypeBuilder_ptr long_builder =<br> DynamicTypeBuilderFactory::get_<br> instance()->create_int32_builder();<br>DynamicTypeBuilder_ptr long_long_builder<br> = DynamicTypeBuilderFactory::get_<br> instance()->create_int64_builder();<br>DynamicTypeBuilder_ptr struct_builder =<br> DynamicTypeBuilderFactory::get_<br> instance()->create_struct_builder();<br>struct_builder->set_name("MyStruct");<br>struct_builder->add_member(0, "first",<br> long_builder.get());<br>struct_builder->add_member(1, "second",<br> long_long_builder.get());<br>DynamicType_ptr struct_type =<br> DynamicTypeBuilderFactory::get_<br> instance()->create_type(struct_builder.<br> get());|



### 结构体可以继承其他结构体：
|XML|C++|
|---|---|
|**<struct** name="ParentStruct"**>**<br>**<member** name="first" type="int32"**/>**<br>**<member** name="second" type="int64"**/>**<br>**</struct>**<br>**<struct** name="ChildStruct" baseType=<br> "ParentStruct"**>**<br>**<member** name="third" type="int32"**/>**<br>**<member** name="fourth" type="int64"**/>**<br>**</struct>**|DynamicTypeBuilder_ptr long_builder =<br> DynamicTypeBuilderFactory::get_<br> instance()->create_int32_builder();<br>DynamicTypeBuilder_ptr long_long_builder<br> = DynamicTypeBuilderFactory::get_<br> instance()->create_int64_builder();<br>DynamicTypeBuilder_ptr struct_builder =<br> DynamicTypeBuilderFactory::get_<br> instance()->create_struct_builder();|
||struct_builder->set_name("ParentStruct");<br>struct_builder->add_member(0, "first",<br> long_builder.get());<br>struct_builder->add_member(1, "second",<br> long_long_builder.get());<br>DynamicType_ptr struct_type =<br> DynamicTypeBuilderFactory::get_<br> instance()->create_type(struct_builder.<br> get());<br>DynamicTypeBuilder_ptr child_builder =<br>DynamicTypeBuilderFactory::get_<br> instance()->create_child_struct_<br> builder(struct_builder.get());<br>child_builder->set_name("ChildStruct");<br>child_builder->add_member(0, "third",<br> long_builder.get());<br>child_builder->add_member(1, "fourth",<br> long_long_builder.get());<br>DynamicType_ptr child_struct_type =<br> DynamicTypeBuilderFactory::get_<br> instance()->create_type(child_builder.<br> get());|



### 联合体（Union）
`<union>` 类型由名称、discriminator 和一组 case 定义。每个 case 包含一个或多个 `caseDiscriminator` 以及一个成员。

示例：

|XML|C++|
|---|---|
|**<union** name="MyUnion"**>**<br>**<discriminator** type="byte"**/>**<br>**<case>**<br>**<caseDiscriminator** value="0"**/>**<br>**<caseDiscriminator** value="1"**/>**<br>**<member** name="first" type="int32|DynamicTypeBuilder_ptr long_builder =<br> DynamicTypeBuilderFactory::get_<br> instance()->create_int32_builder();<br>DynamicTypeBuilder_ptr long_long_builder<br> = DynamicTypeBuilderFactory::get_<br> instance()->create_int64_builder();|
| "**/>**<br>**</case>**<br>**<case>**<br>**<caseDiscriminator** value="2"**/>**<br>**<member** name="second" type=|DynamicTypeBuilder_ptr struct_builder =<br> DynamicTypeBuilderFactory::get_<br> instance()->create_struct_builder();<br>DynamicTypeBuilder_ptr octet_builder =<br> DynamicTypeBuilderFactory::get_|
| "nonBasic" nonBasicTypeName="MyStruct"**/**<br> **>**<br>**</case>**<br>**<case>**<br>**<caseDiscriminator** value="default<br> "**/>**<br>**<member** name="third" type=| instance()->create_byte_builder();<br>DynamicTypeBuilder_ptr union_builder =<br> DynamicTypeBuilderFactory::get_<br> instance()->create_union_builder(octet_<br> builder.get());<br>union_builder->set_name("MyUnion");|
| "nonBasic" nonBasicTypeName="int64"**/>**<br>**</case>**<br>**</union>**|union_builder->add_member(0, "first",<br> long_builder.get(), "", { 0, 1 },<br> false);<br>union_builder->add_member(1, "second",<br> struct_builder.get(), "", { 2 },<br> false);<br>union_builder->add_member(2, "third",<br> long_long_builder.get(), "", { },<br> true);<br>DynamicType_ptr union_type =<br> DynamicTypeBuilderFactory::get_<br> instance()->create_type(union_builder.<br> get());|



### 位集（Bitset）
`<bitset>` 类型由名称和内部 _位字段_ 定义。示例：

|XML|C++|
|---|---|
|**<bitset** name="MyBitSet"**>**<br>**<bitfield** name="a" bit_bound="3"**/>**|DynamicTypeBuilderFactory* m_factory =<br> DynamicTypeBuilderFactory::get_|
|**<bitfield** name="b" bit_bound="1"**/>**| instance();|
|**<bitfield** bit_bound="4"**/>**<br>**<bitfield** name="c" bit_bound="10"**/>**<br>**<bitfield** name="d" bit_bound="12"<br> type="int16"**/>**<br>**</bitset>**|DynamicTypeBuilder_ptr builder_ptr = m_<br> factory->create_bitset_builder();<br>builder_ptr->add_member(0, "a", m_<br> factory->create_byte_builder()-><br> build());<br>builder_ptr->add_member(1, "b", m_<br> factory->create_bool_builder()-><br> build());<br>builder_ptr->add_member(3, "c", m_<br> factory->create_uint16_builder()-><br> build());<br>builder_ptr->add_member(4, "d", m_<br> factory->create_int16_builder()-><br> build());<br>builder_ptr->apply_annotation_to_<br> member(0, ANNOTATION_BIT_BOUND_ID,<br> "value", "3");<br>builder_ptr->apply_annotation_to_<br> member(0, ANNOTATION_POSITION_ID,<br> "value", "0");<br>builder_ptr->apply_annotation_to_<br> member(1, ANNOTATION_BIT_BOUND_ID,<br> "value", "1");<br>builder_ptr->apply_annotation_to_<br> member(1, ANNOTATION_POSITION_ID,<br> "value", "3");<br>builder_ptr->apply_annotation_to_<br> member(3, ANNOTATION_BIT_BOUND_ID,<br> "value", "10");<br>builder_ptr->apply_annotation_to_<br> member(3, ANNOTATION_POSITION_ID,<br> "value", "8"); _// 4 empty_<br>builder_ptr->apply_annotation_to_<br> member(4, ANNOTATION_BIT_BOUND_ID,<br> "value", "12");<br>builder_ptr->apply_annotation_to_<br> member(4, ANNOTATION_POSITION_ID,<br> "value", "18");<br>builder_ptr->set_name("MyBitSet");|



没有名称的位字段是一组不可访问的位。位字段可以指定其管理类型，以便修改和访问。位字段的 `bit_bound` 为必填项，且不能大于 64。

位集可以继承其他位集：

|XML|C++|
|---|---|
|**<bitset** name="ParentBitSet"**>**|DynamicTypeBuilderFactory* m_factory =|
|**<bitfield** name="a" bit_bound="3"**/>**<br>**<bitfield** name="b" bit_bound="1"**/>**| DynamicTypeBuilderFactory::get_<br> instance();|
|**</bitset>**|DynamicTypeBuilder_ptr builder_ptr = m_<br> factory->create_bitset_builder();|
|**<bitset** name="ChildBitSet" baseType=<br> "ParentBitSet"**>**<br>**<bitfield** name="c" bit_bound="30"**/>**|builder_ptr->add_member(0, "a", m_<br> factory->create_byte_builder()-><br> build());|
|**<bitfield** name="d" bit_bound="13"**/>**<br>**</bitset>**|builder_ptr->add_member(1, "b", m_<br> factory->create_bool_builder()-><br> build());<br>builder_ptr->apply_annotation_to_<br> member(0, ANNOTATION_BIT_BOUND_ID,<br> "value", "3");<br>builder_ptr->apply_annotation_to_<br> member(0, ANNOTATION_POSITION_ID,<br> "value", "0");<br>builder_ptr->apply_annotation_to_<br> member(1, ANNOTATION_BIT_BOUND_ID,<br> "value", "1");<br>builder_ptr->apply_annotation_to_<br> member(1, ANNOTATION_POSITION_ID,<br> "value", "3");<br>builder_ptr->set_name("ParentBitSet");<br>DynamicTypeBuilder_ptr child_ptr = m_<br> factory->create_child_struct_<br> builder(builder_ptr.get());<br>child_ptr->add_member(3, "c", m_factory-><br> create_uint16_builder()->build());<br>child_ptr->add_member(4, "d", m_factory-><br> create_int16_builder()->build());<br>child_ptr->apply_annotation_to_member(3,<br> ANNOTATION_BIT_BOUND_ID, "value", "10<br> ");<br>child_ptr->apply_annotation_to_member(3,<br> ANNOTATION_POSITION_ID, "value", "8");<br> // 4 empty_<br>child_ptr->apply_annotation_to_member(4,<br> ANNOTATION_BIT_BOUND_ID, "value", "12<br> ");<br>child_ptr->apply_annotation_to_member(4,<br> ANNOTATION_POSITION_ID, "value", "18");<br>child_ptr->set_name("ChildBitSet");|



### 位掩码（Bitmask）
`<bitmask>` 类型由名称和内部 _bit_values_ 定义。示例：

|XML|C++|
|---|---|
|**<bitmask** name="MyBitMask" bit_bound="8"**>**<br>**<bit_value** name="flag0" position="0"**/**<br> **>**|DynamicTypeBuilderFactory* m_factory =<br> DynamicTypeBuilderFactory::get_<br> instance();|
|**<bit_value** name="flag1"**/>**<br>**<bit_value** name="flag2" position="2"**/**<br> **>**<br>**<bit_value** name="flag5" position="5"**/**<br> **>**<br>**</bitmask>**|DynamicTypeBuilder_ptr builder_ptr = m_<br> factory->create_bitmask_builder(8);<br>builder_ptr->add_empty_member(0, "flag0<br> ");<br>builder_ptr->add_empty_member(1, "flag1<br> ");<br>builder_ptr->add_empty_member(2, "flag2<br> ");<br>builder_ptr->add_empty_member(5, "flag5<br> ");<br>builder_ptr->set_name("MyBitMask");|



位掩码可以指定其 `bit_bound`，即该类型管理的位数。内部会转换为能够存储这些位的最小类型。允许的最大 `bit_bound` 为 64。`Bit_values` 可以定义其在位掩码中的位置。

## 14.4.3 成员类型
成员类型是指可属于 `<struct>` 或 `<union>`，或可由 `<typedef>` 设置别名的任意类型。

### 基本类型
可用基本类型的标识符如下：

|boolean|int64|float128|
|---|---|---|
|byte|uint16|string|
|char|uint32|wstring|
|wchar|uint64||
|int16|float32||
|int32|float64||



所有这些类型的定义方式如下：

|XML|C++|
|---|---|
|**<member** name="my_long" type="int64"**/>**|DynamicTypeBuilder_ptr long_long_builder<br> = DynamicTypeBuilderFactory::get_<br> instance()->create_int64_builder();<br>long_long_builder->set_name("my_long");<br>DynamicType_ptr long_long_type =<br> DynamicTypeBuilderFactory::get_<br> instance()->create_type(long_long_<br> builder.get());|



### 数组
数组的定义方式与其他成员类型相同，但需添加 `arrayDimensions` 属性。该维度属性的格式为以逗号分隔的每个维度大小。

### 示例：
|XML|C++|
|---|---|
|**<member** name="long_array" type="int32"<br> arrayDimensions="2,3,4"**/>**|std::vector<**uint32_t**> lengths = { 2, 3,<br> 4 };<br>DynamicTypeBuilder_ptr long_builder =<br> DynamicTypeBuilderFactory::get_<br> instance()->create_int32_builder();<br>DynamicTypeBuilder_ptr array_builder =<br> DynamicTypeBuilderFactory::get_<br> instance()->create_array_builder(long_<br> builder.get(), lengths);<br>array_builder->set_name("long_array");<br>DynamicType_ptr array_type =<br> DynamicTypeBuilderFactory::get_<br> instance()->create_type(array_builder.<br> get());|



其 IDL 等价写法为：

**long** long_array[2][3][4]; 

### 序列
序列由名称、内容类型和 `sequenceMaxLength` 定义。内容类型应通过其 `type` 属性定义。

示例：

|XML|C++|
|---|---|
|**<typedef** name="my_sequence_inner" type=<br> "int32" sequenceMaxLength="2"**/>**<br>**<struct** name="SeqSeqStruct"**>**<br>**<member** name="my_sequence_sequence"<br> type="nonBasic" nonBasicTypeName="my_<br> sequence_inner" sequenceMaxLength="3"**/>**<br>**</struct>**|**uint32_t** child_len = 2;<br>DynamicTypeBuilder_ptr long_builder =<br> DynamicTypeBuilderFactory::get_<br> instance()->create_int32_builder();<br>DynamicTypeBuilder_ptr seq_builder =<br> DynamicTypeBuilderFactory::get_<br> instance()->create_sequence_<br> builder(long_builder.get(),<br>child_len);<br>**uint32_t** length = 3;<br>DynamicTypeBuilder_ptr seq_seq_builder =<br> DynamicTypeBuilderFactory::get_<br> instance()->create_sequence_builder(<br>seq_builder.get(), length);<br>seq_seq_builder->set_name("my_sequence_<br> sequence");<br>DynamicType_ptr seq_type =<br> DynamicTypeBuilderFactory::get_<br> instance()->create_type(seq_seq_<br> builder.get());|



该示例展示一个 `sequenceMaxLength` 为 3 的序列，其元素是 `sequenceMaxLength` 为 2、内容类型为 `<int32>` 的序列。对应 IDL 如下：

sequence<sequence< **long** ,2>,3> my_sequence_sequence; 

请注意，内部序列已事先定义。

### 映射
映射与序列相似，但需要定义两个类型。一个类型定义其 `key_type`，另一个类型定义其元素类型。同样，这两个类型既可作为属性定义，也可作为成员定义；作为成员定义时，它们应包含在另一个 XML 元素中（分别为 `<key_type>` 和 `<type>`）。

示例：

|XML|C++|
|---|---|
|**<typedef** name="my_map_inner" type="int32<br> " key_type="int32" mapMaxLength="2"**/>**<br>**<struct** name="MapMapStruct"**>**<br>**<member** name="my_map_map" type=<br> "nonBasic" nonBasicTypeName="my_map_<br> inner" key_type="int32" mapMaxLength="2<br> "**/>**<br>**</struct>**|**uint32_t** length = 2;<br>DynamicTypeBuilder_ptr long_builder =<br> DynamicTypeBuilderFactory::get_<br> instance()->create_int32_builder();<br>DynamicTypeBuilder_ptr map_builder =<br> DynamicTypeBuilderFactory::get_<br> instance()->create_map_builder(long_<br> builder.get(),<br>long_builder.get(), length);<br>DynamicTypeBuilder_ptr map_map_builder =<br> DynamicTypeBuilderFactory::get_<br> instance()->create_map_builder(long_<br> builder.get(),<br>map_builder.get(), length);<br>map_map_builder->set_name("my_map_map");<br>DynamicType_ptr map_type =<br> DynamicTypeBuilderFactory::get_<br> instance()->create_type(map_map_<br> builder.get());|



等价于以下 IDL：

map< **long** ,map< **long** , **long** ,2>,2> my_map_map; 

### 复杂类型
复杂类型定义后，可以像基本类型或数组类型一样用作成员。

示例：

<struct name="OtherStruct" > <member name="my_enum" type="nonBasic" nonBasicTypeName="MyEnum" /> <member name="my_struct" type="nonBasic" nonBasicTypeName="MyStruct" arrayDimensions="5" /> </struct> 

## 14.4.4 用法
在使用 _XML Types_ 的应用中，必须先加载定义类型的 XML 文件，然后才能尝试实例化这些类型的 _DynamicPubSubType_。需要特别说明的是，只有 `<struct>` 类型会生成可用的 _DynamicPubSubType_ 实例。

_// Load the XML File_ XMLP_ret ret = XMLProfileManager::loadXMLFile("types.xml"); _// Create the "MyStructPubSubType"_ DynamicPubSubType *pbType = XMLProfileManager::CreateDynamicPubSubType("MyStruct"); _// Create a "MyStruct" instance_ DynamicData* data = DynamicDataFactory::get_instance()->create_data(pbType-> GetDynamicType()); 

# 14.5 Participant 配置
Participant 配置允许通过 XML 文件声明 _Participant 配置_。Participant 的所有配置选项都属于 `<rtps>` 标签。属性 `profile_name` 是 Domain 加载配置时关联的名称，如 _加载和应用配置_ 所示。

<participant profile_name="part_profile_name" > <rtps> <name> Participant Name </name> _<!-- String -->_ <defaultUnicastLocatorList> _<!-- LOCATOR_LIST -->_ <locator> <udpv4/> </locator> </defaultUnicastLocatorList> 

<defaultMulticastLocatorList> _<!-- LOCATOR_LIST -->_ <locator> <udpv4/> </locator> </defaultMulticastLocatorList> <sendSocketBufferSize> 8192 </sendSocketBufferSize> _<!-- uint32 -->_ <listenSocketBufferSize> 8192 </listenSocketBufferSize> _<!-- uint32 -->_ <builtin> _<!-- BUILTIN -->_ </builtin> <port> <portBase> 7400 </portBase> _<!-- uint16 -->_ <domainIDGain> 200 </domainIDGain> _<!-- uint16 -->_ <participantIDGain> 10 </participantIDGain> _<!-- uint16 -->_ <offsetd0> 0 </offsetd0> _<!-- uint16 -->_ <offsetd1> 1 </offsetd1> _<!-- uint16 -->_ <offsetd2> 2 </offsetd2> _<!-- uint16 -->_ <offsetd3> 3 </offsetd3> _<!-- uint16 -->_ </port> <participantID> 99 </participantID> _<!-- int32 -->_ 

<throughputController> <bytesPerPeriod> 8192 </bytesPerPeriod> _<!-- uint32 -->_ <periodMillisecs> 1000 </periodMillisecs> _<!-- uint32 -->_ 



</throughputController> <userTransports> <transport_id> TransportId1 </transport_id> _<!-- string -->_ <transport_id> TransportId2 </transport_id> _<!-- string -->_ </userTransports> <useBuiltinTransports> false </useBuiltinTransports> _<!-- boolean -->_ <propertiesPolicy> _<!-- PROPERTIES_POLICY -->_ </propertiesPolicy> <allocation> _<!-- ALLOCATION -->_ </allocation> </rtps> </participant> 

### 注意：
- `LOCATOR_LIST` 表示此处需要 _LocatorListType_。

- `PROPERTIES_POLICY` 表示该标签是一个 _PropertiesPolicyType_ 块。

- `DURATION` 表示此处需要 _DurationType_。

- 有关 `BUILTIN` 的详细信息，请参见 _内置参数_。

- 有关 `ALLOCATION` 的详细信息，请参见 _Participant 分配参数_。

可能的配置参数列表如下：

|名称|说明|值|默认<br>值|
|---|---|---|---|
|<name>|Participant 的名称。它与 `profile_name` 不是同一字段。|string_25|5|
|<defaultUnica|stLocatorList>|默认输入单播定位器列表。需要 _LocatorListType_。|LocatorLi|stType|
|<defaultMulti|castLocatorList>|默认输入多播定位器列表。需要 _LocatorListType_。|LocatorLi|stType|
|<sendSocketBu|fferSize>|输出套接字缓冲区大小，单位为字节。如果值为零，FastRTPS 将使用套接字配置中的默认大小，且最小为 65536 字节。|uint32|0|
|<listenSocket|BufferSize>|输入套接字缓冲区大小，单位为字节。如果值为零，FastRTPS 将使用套接字配置中的默认大小，且最小为 65536 字节。|uint32|0|
|<builtin>|内置参数。详见 _内置参数_ 一节。|_内置<br>参数_||
|<port>|用于定义与 RTPS 协议相关的端口参数和增益。详见 _端口_ 一节。|_端口_||
|<participantI|D>|Participant 标识符。通常由 Domain 自动生成。|int32|0|
|<throughputCo|ntroller>|用于定义最大吞吐量。详见 _吞吐量_ 一节。|_吞吐量_||
|<userTranspor|ts>|participant 使用的传输描述符。|List<br><string>||
|<useBuiltinTr|ansports>|布尔字段，指示 participant 是否独立于 `<userTransports>` 使用默认内置传输。|bool|true|
|<propertiesPo|licy>|附加配置属性。需要 _PropertiesPolicyType_。|_Proper-_<br>_tiesPolicy-_<br>_Type_||
|<allocation>|与分配行为相关的配置。需要 _Participant 分配参数_。|_Participant_<br>_allocation_<br>_parameters_||



### 端口配置
|名称|说明|值|默认值|
|---|---|---|---|
|<portBase>|基础端口。|uint16|7400|
|<domainIDGain>|domainId 增益。|uint16|250|
|<participantIDGain>|participantId 增益。|uint16|2|
|<offsetd0>|多播元数据偏移量。|uint16|0|
|<offsetd1>|单播元数据偏移量。|uint16|10|
|<offsetd2>|多播用户数据偏移量。|uint16|1|
|<offsetd3>|单播用户数据偏移量。|uint16|11|



## 14.5.1 Participant 分配参数
Participant 的 `rtps` 配置中本节允许定义与 participant 分配行为相关的参数。

<allocation> <remote_locators> <max_unicast_locators> 4 </max_unicast_locators> _<!-- uint32 -->_ <max_multicast_locators> 1 </max_multicast_locators> _<!-- uint32 -->_ </remote_locators> 



<total_participants> <initial> 0 </initial> <maximum> 0 </maximum> <increment> 1 </increment> </total_participants> <total_readers> <initial> 0 </initial> <maximum> 0 </maximum> <increment> 1 </increment> </total_readers> <total_writers> <initial> 0 </initial> <maximum> 0 </maximum> <increment> 1 </increment> </total_writers> <max_partitions> 256 </max_partitions> <max_user_data> 256 </max_user_data> <max_properties> 512 </max_properties> </allocation> 

|名称|说明|值|默认<br>值|
|---|---|---|---|
|<max_unicas|t_locators>|远程实体预期的最大单播定位器数量。建议使用 participant 将连接的任何机器上找到的最大网络接口数。|UInt32|4|
|<max_multic|ast_locators>|远程实体预期的最大多播定位器数量。可设为零以禁用多播流量。|UInt32|1|
|<total_part|icipants>|与域中 participant 总数（本地和远程）相关的 Participant _分配配置_。|_Allo-_<br>_cation_<br>_Configu-_<br>_ration_||
|<total_read|ers>|与每个 participant 上 reader 总数（本地和远程）相关的 Participant _分配配置_。|_Allo-_<br>_cation_<br>_Configu-_<br>_ration_||
|<total_writ|ers>|与每个 participant 上 writer 总数（本地和远程）相关的 Participant _分配配置_。|_Allo-_<br>_cation_<br>_Configu-_<br>_ration_||
|<max_partit|ions>|partitions 子消息的最大大小。零表示不限制。参见 _子消息大小限制_。|UInt32||
|<max_user_d|ata>|用户数据子消息的最大大小。零表示不限制。参见 _子消息大小限制_。|UInt32||
|<max_proper|ties>|properties 子消息的最大大小。零表示不限制。参见 _子消息大小限制_。|UInt32||



## 14.5.2 内置参数
Participant 的 `rtps` 配置中本节允许定义内置参数。

<builtin> <discovery_config> 



<discoveryProtocol> NONE </discoveryProtocol> _<!-- DiscoveryProtocol enum -->_ <ignoreParticipantFlags> FILTER_DIFFERENT_HOST </ignoreParticipantFlags> _<!- ParticipantFlags enum -->_ <EDP> SIMPLE </EDP> _<!-- string -->_ <leaseDuration> _<!-- DURATION -->_ <sec> 20 </sec> <nanosec> 0 </nanosec> </leaseDuration> <leaseAnnouncement> _<!-- DURATION -->_ <sec> 3 </sec> <nanosec> 0 </nanosec> </leaseAnnouncement> <initialAnnouncements> _<!-- INITIAL_ANNOUNCEMENTS -->_ </initialAnnouncements> <simpleEDP> <PUBWRITER_SUBREADER> true </PUBWRITER_SUBREADER> _<!-- boolean -->_ <PUBREADER_SUBWRITER> true </PUBREADER_SUBWRITER> _<!-- boolean -->_ </simpleEDP> <staticEndpointXMLFilename> filename.xml </staticEndpointXMLFilename> _<!- string -->_ </discovery_config> <avoid_builtin_multicast> true </avoid_builtin_multicast> <use_WriterLivelinessProtocol> false </use_WriterLivelinessProtocol> _<!-- boolean - ->_ <domainId> 4 </domainId> _<!-- uint32 -->_ <metatrafficUnicastLocatorList> _<!-- LOCATOR_LIST -->_ <locator> <udpv4/> </locator> </metatrafficUnicastLocatorList> <metatrafficMulticastLocatorList> _<!-- LOCATOR_LIST -->_ <locator> <udpv4/> </locator> </metatrafficMulticastLocatorList> <initialPeersList> _<!-- LOCATOR_LIST -->_ 



<locator> <udpv4/> </locator> </initialPeersList> <readerHistoryMemoryPolicy> PREALLOCATED_WITH_REALLOC </readerHistoryMemoryPolicy> <readerPayloadSize> 512 </readerPayloadSize> <writerHistoryMemoryPolicy> PREALLOCATED_WITH_REALLOC </writerHistoryMemoryPolicy> <writerPayloadSize> 512 </writerPayloadSize> 

<mutation_tries> 55 </mutation_tries> 

</builtin> 

|名称|说明|值|默认值|
|---|---|---|---|
|<discovery_config>|用于配置发现相关设置的主要标签。|_discovery_config_||
|<avoid_builtin_multi|cast>|将元流量多播限制为仅用于 PDP。|Boolean|true|
|<use_WriterLivelines|sProtocol>|指示使用 WriterLiveliness 协议。|Boolean|true|
|<domainId>|RTPSParticipant 使用的 DomainId。|UInt32|0|
|<metatrafficUnicastL|ocatorList>|元流量单播定位器列表。|_LocatorListType_ 列表||
|<metatrafficMulticas|tLocatorList>|元流量多播定位器列表。|_LocatorListType_ 列表||
|<initialPeersList>|初始对等节点。|_LocatorListType_ 列表||
|<readerHistoryMemory|Policy>|内置 reader 的内存策略。|_historyMemoryPolicy_|PREALLOCATED_WITH_REALLOC|
|<writerHistoryMemory|Policy>|内置 writer 的内存策略。|_historyMemoryPolicy_|PREALLOCATED_WITH_REALLOC|
|<readerPayloadSize>|内置 reader 的最大负载大小。|UInt32|512|
|<writerPayloadSize>|内置 writer 的最大负载大小。|UInt32|512|
|<mutation_tries>|reader 的物理端口已被占用时尝试的不同端口数量。|UInt32|100|



**discovery_config** 

|名称|说明|值|默认值|
|---|---|---|---|
|<discoveryProtocol>|指示 participant 必须使用的 PDP 协议类型。|SIMPLE,<br>CLIENT,<br>SERVER,BACKUP|SIMPLE|
|<ignoreParticipantF|lags>|使用多种筛选条件限制元流量。|_ignoreParticipantFlags_|NO_FILTER|
|<EDP>|• 如果设为 SIMPLE，将使用 `<simpleEDP>`。<br>• 如果设为 STATIC，将使用基于 XML 文件的 StaticEDP，其内容来自 `<staticEndpointXMLFilename>`。|SIMPLE,STATIC|SIMPLE|
|<simpleEDP>|SimpleEDP 协议的属性。|_simpleEDP_||
|<leaseDuration>|指示此 RTPSParticipant 应认为远程 RTPSParticipant 存活多长时间。|_DurationType_|20 s|
|<leaseAnnouncement>|RTPSParticipant 向所有其他已发现 RTPSParticipant 以及所有多播端口发送发现消息的周期。|_DurationType_|3 s|
|<initialAnnouncemen|ts>|允许用户配置 RTPSParticipant 初始发现消息的数量和周期。|_Initial Announcements_||
|<staticEndpointXMLF|ilename>|StaticEDP XML 文件名。仅当 `<EDP>` 设为 STATIC 时需要。|string||



### ignoreParticipantFlags
|可选值|说明|
|---|---|
|NO_FILTER|处理所有发现流量。|
|FILTER_DIFFERENT_HOST|丢弃来自其他主机的发现流量。|
|FILTER_DIFFERENT_PROCESS|丢弃来自同一主机上其他进程的发现流量。|
|FILTER_SAME_PROCESS|丢弃来自 participant 自身进程的发现流量。|
|FILTER_DIFFERENT_PROCESS ||丢弃来自 participant 自身主机的发现流量。|
|FILTER_SAME_PROCESS||



### simpleEDP
|名称<br>说明|值|默认<br>值|
|---|---|---|
|<PUBWRITER_SUBREADER>|指示 participant 是否必须使用 Publication Writer 与 Subscription Reader。|Boolean|true|
|<PUBREADER_SUBWRITER>|指示 participant 是否必须使用 Publication Reader 与 Subscription Writer。|Boolean|true|



### 初始公告
|名称|说明|值|默认<br>值|
|---|---|---|---|
|<coun|t>|按 `<period>` 指定的周期发送的发现消息数量。完成这些公告后，RTPSParticipant 将继续按 `<leaseAnnouncement>` 频率发送发现消息。|Uint32|5|
|<peri|od>|RTPSParticipant 发送前 `<count>` 条发现消息的周期。|_DurationType_|100 ms|



# 14.6 Publisher 配置
Publisher 配置允许通过 XML 文件声明 _Publisher 配置_。属性 `profile_name` 是 Domain 加载配置时关联的名称，如 _加载和应用配置_ 一节所示。

<publisher profile_name="pub_profile_name" > <topic> _<!-- TOPIC_TYPE -->_ </topic> <qos> _<!-- QOS -->_ </qos> <times> _<!-- writerTimesType -->_ <initialHeartbeatDelay> _<!-- DURATION -->_ <sec> 0 </sec> <nanosec> 12 </nanosec> </initialHeartbeatDelay> <heartbeatPeriod> _<!-- DURATION -->_ <sec> 3 </sec> <nanosec> 0 </nanosec> </heartbeatPeriod> <nackResponseDelay> _<!-- DURATION -->_ <sec> 0 </sec> <nanosec> 5 </nanosec> </nackResponseDelay> <nackSupressionDuration> _<!-- DURATION -->_ <sec> 0 </sec> <nanosec> 0 </nanosec> </nackSupressionDuration> </times> <unicastLocatorList> 



_<!-- LOCATOR_LIST -->_ **<locator> <udpv4/> </locator> </unicastLocatorList> <multicastLocatorList>** _<!-- LOCATOR_LIST -->_ **<locator> <udpv4/> </locator> </multicastLocatorList> <throughputController> <bytesPerPeriod>** 8192 **</bytesPerPeriod>** _<!-- uint32 -->_ **<periodMillisecs>** 1000 **</periodMillisecs>** _<!-- uint32 -->_ **</throughputController> <historyMemoryPolicy>** DYNAMIC **</historyMemoryPolicy> <propertiesPolicy>** _<!-- PROPERTIES_POLICY -->_ **</propertiesPolicy> <userDefinedID>** 55 **</userDefinedID>** _<!-- Int16 -->_ **<entityID>** 66 **</entityID>** _<!-- Int16 -->_ **<matchedSubscribersAllocation> <initial>** 0 **</initial>** _<!-- uint32 -->_ **<maximum>** 0 **</maximum>** _<!-- uint32 -->_ **<increment>** 1 **</increment>** _<!-- uint32 -->_ **</matchedSubscribersAllocation> </publisher>** 

### 注意：
- `LOCATOR_LIST` 表示此处需要 _LocatorListType_。

- `PROPERTIES_POLICY` 表示该标签是一个 _PropertiesPolicyType_ 块。

- `DURATION` 表示此处需要 _DurationType_。

- 有关 `QOS` 的详细信息，请参见 _QOS_。

- `TOPIC_TYPE` 详见 _Topic 类型_ 一节。


|名称|说明|值|默认值|
|---|---|---|---|
|<topic>|publisher 的 _Topic 类型_ 配置。|_Topic Type_||
|<qos>|Publisher 的 _QOS_ 配置。|_QOS_||
|<times>|允许配置 publisher 的一些时间相关参数。|_Times_||
|<unicastLocatorList>|输入单播定位器列表。需要 _LocatorListType_。|_LocatorListType_ 列表||
|<multicastLocatorLis|t>|输入多播定位器列表。需要 _LocatorListType_。|_LocatorListType_ 列表||
|<throughputControlle|r>|限制 publisher 的输出带宽。|_Throughput_||
|<historyMemoryPolicy|>|publisher History 的内存分配类型。|_historyMemoryPolicy_|PREALLOCATED|
|<propertiesPolicy>|附加配置属性。|_PropertiesPolicyType_||
|<userDefinedID>|用于 StaticEndpointDiscovery。|Int16|-1|
|<entityID>|端点的 EntityId。|Int16|-1|
|<matchedSubscribersA|llocation>|与匹配 subscriber 数量相关的 Publisher _分配配置_。|_Allocation_<br>_Configuration_||



### 时间参数（Times）
|名称|说明|值|默认<br>值|
|---|---|---|---|
|<initialHeartbeatD|elay>|初始 heartbeat 延迟。|_DurationType_|~45<br>ms|
|<heartbeatPeriod>|周期性 heartbeat 周期。|_DurationType_|3 s|
|<nackResponseDelay|>|应用于 ACKNACK 消息响应的延迟。|_DurationType_|~45<br>ms|
|<nackSupressionDur|ation>|该时间允许 RTPSWriter 忽略数据发送后过早到达的 nack 消息。|_DurationType_|0 ms|



# 14.7 Subscriber 配置
Subscriber 配置允许通过 XML 文件声明 _Subscriber 配置_。属性 `profile_name` 是 Domain 加载配置时关联的名称，如 _加载和应用配置_ 所示。

<subscriber profile_name="sub_profile_name" > <topic> _<!-- TOPIC_TYPE -->_ </topic> <qos> _<!-- QOS -->_ </qos> <times> _<!-- readerTimesType -->_ <initialAcknackDelay> _<!-- DURATION -->_ <sec> 0 </sec> <nanosec> 70 </nanosec> </initialAcknackDelay> 



<heartbeatResponseDelay> _<!-- DURATION -->_ <sec> 0 </sec> <nanosec> 5 </nanosec> </heartbeatResponseDelay> </times> <unicastLocatorList> _<!-- LOCATOR_LIST -->_ <locator> <udpv4/> </locator> </unicastLocatorList> <multicastLocatorList> _<!-- LOCATOR_LIST -->_ <locator> <udpv4/> </locator> </multicastLocatorList> <expectsInlineQos> true </expectsInlineQos> _<!-- boolean -->_ <historyMemoryPolicy> DYNAMIC </historyMemoryPolicy> <propertiesPolicy> _<!-- PROPERTIES_POLICY -->_ </propertiesPolicy> <userDefinedID> 55 </userDefinedID> _<!-- Int16 -->_ <entityID> 66 </entityID> _<!-- Int16 -->_ <matchedPublishersAllocation> <initial> 0 </initial> _<!-- uint32 -->_ <maximum> 0 </maximum> _<!-- uint32 -->_ <increment> 1 </increment> _<!-- uint32 -->_ </matchedPublishersAllocation> </subscriber> 

### 注意：
- `LOCATOR_LIST` 表示此处需要 _LocatorListType_。

- `PROPERTIES_POLICY` 表示该标签是一个 _PropertiesPolicyType_ 块。

- `DURATION` 表示此处需要 _DurationType_。

- 有关 `QOS` 的详细信息，请参见 _QOS_。

- `TOPIC_TYPE` 详见 _Topic 类型_ 一节。

|名称|说明|值|默认值|
|---|---|---|---|
|<topic>|subscriber 的 _Topic 类型_ 配置。|_Topic Type_||
|<qos>|Subscriber 的 _QOS_ 配置。|_QOS_||
|<times>|允许配置 subscriber 的一些时间相关参数。|_Times_||
|<unicastLocatorList|>|输入单播定位器列表。需要 _LocatorListType_。|_LocatorListType_ 列表||
|<multicastLocatorLi|st>|输入多播定位器列表。需要 _LocatorListType_。|_LocatorListType_ 列表||
|<expectsInlineQos>|指示是否要求内联 QOS。|Boolean|false|
|<historyMemoryPolic|y>|subscriber History 的内存分配类型。|_historyMemoryPolicy_|PREALLOCATED|
|<propertiesPolicy>|附加配置属性。|_PropertiesPolicyType_||
|<userDefinedID>|用于 StaticEndpointDiscovery。|Int16|-1|
|<entityID>|端点的 EntityId。|Int16|-1|
|<matchedPublishersA|llocation>|与匹配 publisher 数量相关的 Subscriber _分配配置_。|_Allocation_<br>_Configuration_||



### 时间参数（Times）
|名称|说明|值|默认|
|---|---|---|---|
||||值|
|<initialAcknackDelay>|初始 AckNack 延迟。|_DurationType_|~45 ms|
|||_DurationType_||
|<heartbeatResponseDelay|>|收到 heartbeat 消息时应用的延迟。|_DurationType_|~4.5<br>ms|



# 14.8 通用配置
在上述配置中，有些类型会在多个不同位置使用。为避免重复介绍过多细节，其中一些位置使用 `LocatorListType` 等标签，表明该字段在本节中定义。

## 14.8.1 LocatorListType
它表示 `Locator_t` 列表。`LocatorListType` 通常作为匿名类型使用，即它没有自己的标签，而是用于其他需要定位器列表并使其具有意义的配置参数标签中，例如 `<defaultUnicastLocatorList>`。定位器类型由其自身标签定义，可取 `<udpv4>`、`<tcpv4>`、`<udpv6>` 和 `<tcpv6>`：

<defaultUnicastLocatorList> <locator> <udpv4> _<!-- Access as physical, typical UDP usage -->_ <port> 7400 </port> _<!-- uint32 -->_ <address> 192.168.1.41 </address> </udpv4> </locator> <locator> <tcpv4> 


_<!-- Both physical and logical (port), useful in TCP transports -->_ **<physical_port>** 5100 **</physical_port>** _<!-- uint16 -->_ **<port>** 7400 **</port>** _<!-- uint16 -->_ **<unique_lan_id>** 192.168.1.1.1.1.2.55 **</unique_lan_id> <wan_address>** 80.80.99.45 **</wan_address> <address>** 192.168.1.55 **</address> </tcpv4> </locator> <locator> <udpv6> <port>** 8844 **</port> <address>** ::1 **</address> </udpv6> </locator> <locator> <tcpv6>** _<!-- Both physical and logical (port), useful in TCP transports -->_ **<physical_port>** 5100 **</physical_port>** _<!-- uint16 -->_ **<port>** 7400 **</port>** _<!-- uint16 -->_ **<address>** fe80::55e3:290:165:5af8 **</address> </tcpv6> </locator> </defaultUnicastLocatorList>** 

在此示例中，`<defaultUnicastLocatorList>` 为每种定位器各包含一个实例。

下面详细说明定位器的每个可能字段：

|名称|说明|值|默认<br>值|
|---|---|---|---|
|<port>|定位器的 RTPS 端口号。在 UDP 中为 _物理端口_，在 TCP 中为 _逻辑端口_。|Uint32|0|
|<physical_po|rt>|TCP 的 _物理端口_。|Uint32|0|
|<address>|定位器的 IP 地址。|符合预期格式的<br>字符串|“”|
|<unique_lan_|id>|LAN ID 唯一标识定位器所属的 LAN（**仅限 TCPv4**）。|string（16 字节）||
|<wan_address|>|WAN IPv4 地址（**仅限 TCPv4**）。|IPv4 格式<br>字符串|0.0.<br>0.0|



## 14.8.2 PropertiesPolicyType
PropertiesPolicyType（XML 标签 `<propertiesPolicy>`）允许定义一组通用属性，适用于定义扩展或自定义配置参数。

<propertiesPolicy> <properties> <property> <name> Property1Name </name> _<!-- string -->_ <value> Property1Value </value> _<!-- string -->_ <propagate> false </propagate> _<!-- boolean -->_ </property> <property> <name> Property2Name </name> _<!-- string -->_ 



<value> Property2Value </value> _<!-- string -->_ <propagate> true </propagate> _<!-- boolean -->_ </property> </properties> </propertiesPolicy> 

|名称|说明|值|默认|
|---|---|---|---|
||||值|
|<name>|用于标识属性名称。|string||
|<value>|属性值。|string||
|<propagate>|指示该属性是否随所属对象一起序列化。|Boolean|false|



## 14.8.3 DurationType
DurationType 表示一段时间，通常作为匿名类型使用，即没有自己的标签，而是用于 `<leaseAnnouncement>` 或 `<leaseDuration>` 等使其具有意义的配置参数标签内。

<discovery_config> <leaseDuration> <sec> DURATION_INFINITY </sec> _<!-- string -->_ </leaseDuration> <leaseDuration> <sec> 500 </sec> _<!-- int32 -->_ <nanosec> 0 </nanosec> _<!-- uint32 -->_ </leaseDuration> <leaseAnnouncement> <sec> 1 </sec> _<!-- int32 -->_ <nanosec> 856000 </nanosec> _<!-- uint32 -->_ </leaseAnnouncement> </discovery_config> 

持续时间可以通过 `<sec>` 加 `<nanosec>` 标签定义（见下表）。可以使用 `DURATION_INFINITY`、`DURATION_INFINITE_SEC` 和 `DURATION_INFINITE_NSEC` 指定无限值。

|名称|说明|值|默认值|
|---|---|---|---|
|<sec>|秒数。|Int32|0|
|<nanosec>|纳秒数。|UInt32|0|



## 14.8.4 Topic 类型
Topic 名称和数据类型作为元数据，用于判断 Publisher 和 Subscriber 能否交换消息。有关 `topic` 字段的详细说明见 _Topic 信息_。

<topic> <kind> NO_KEY </kind> _<!-- string -->_ <name> TopicName </name> _<!-- string -->_ 



<dataType> TopicDataTypeName </dataType> _<!-- string -->_ <historyQos> <kind> KEEP_LAST </kind> _<!-- string -->_ <depth> 20 </depth> _<!-- uint32 -->_ </historyQos> <resourceLimitsQos> <max_samples> 5 </max_samples> _<!-- unint32 -->_ <max_instances> 2 </max_instances> _<!-- unint32 -->_ <max_samples_per_instance> 1 </max_samples_per_instance> _<!-- unint32 -->_ <allocated_samples> 20 </allocated_samples> _<!-- unint32 -->_ </resourceLimitsQos> </topic> 

|名称|说明|值|默认<br>值|
|---|---|---|---|
|<kind>|定义 Topic 类型。|NO_KEY,<br>WITH_KEY|NO_KEY|
|<name>|定义 Topic 名称。必须唯一。|string_255||
|<dataType>|引用 Topic 的数据类型。|string_255||
|<historyQos|>|控制当实例值在最终传递给某些现有 DataReader 实体之前发生变化时 _Fast RTPS_ 的行为。|_HistoryQos_||
|<resourceLi|mitsQos>|控制 _Fast RTPS_ 为满足应用和其他 QoS 设置要求可使用的资源。|_ResourceLimitsQos_||



### HistoryQoS
它控制当实例值在最终传递给某些现有 DataReader 实体之前发生变化时 _Fast RTPS_ 的行为。

|名称|说明|值|默认值|
|---|---|---|---|
|<kind>|参见下文说明。|KEEP_LAST,KEEP_ALL|KEEP_LAST|
|<depth>||UInt32|1000|



如果 `<kind>` 设置为 KEEP_LAST，_Fast RTPS_ 只会尝试保留该实例的最新值，并丢弃较旧的值。

如果 `<kind>` 设置为 KEEP_ALL，_Fast RTPS_ 将尝试保留该实例的所有值并将其投递给现有 subscriber。

`<depth>` 的设置必须与 _ResourceLimitsQos_ 的 `<max_samples_per_instance>` 一致。要使这两个 QoS 一致，必须满足 `depth <= max_samples_per_instance`。

### ResourceLimitsQos
它控制 _Fast RTPS_ 为满足应用和其他 QoS 设置要求可使用的资源。

|名称|说明|值|默认|
|---|---|---|---|
|||值|值|
|<max_samples>|必须满足 `max_samples >=`|UInt32|5000|
||`max_samples_per_instance`。|||
|<max_instances>|定义最大实例数。|UInt32|10|
|<max_samples_per_ins|tance>|必须满足 _HistoryQos_ 的 `depth <=`|UInt32|400|
||`max_samples_per_instance`。|||
|<allocated_samples>|控制可存储的最大样本数。|UInt32|100|



## 14.8.5 QOS
服务质量（QoS）处理应用于应用的约束。

<qos> _<!-- readerQosPoliciesType -->_ <durability> <kind> VOLATILE </kind> _<!-- string -->_ </durability> <liveliness> <kind> AUTOMATIC </kind> _<!-- string -->_ <lease_duration> <sec> 1 </sec> </lease_duration> <announcement_period> <sec> 1 </sec> </announcement_period> </liveliness> <reliability> <kind> BEST_EFFORT </kind> </reliability> <partition> <names> <name> part1 </name> _<!-- string -->_ <name> part2 </name> _<!-- string -->_ </names> </partition> <deadline> <period> <sec> 1 </sec> </period> </deadline> <lifespan> <duration> <sec> 1 </sec> </duration> </lifespan> <disablePositiveAcks> <enabled> true </enabled> </disablePositiveAcks> </qos> 

|名称|说明|值|默认值|
|---|---|---|---|
|<durabilit|y>|在 _设置数据持久性类型_ 一节中定义。|VOLATILE,<br>TRANSIENT_LOCAL<br>TRANSIENT|VOLATILE|
|<livelines|s>|定义 publisher 的活跃性。|_Liveliness_||
|<reliabili|ty>|在 _可靠性_ 一节中定义。|RELIABLE,<br>BEST_EFFORT|RELIABLE|
|<partition|>|允许在域产生的 _物理_ 分区内引入逻辑分区概念。||List <string>|
|<deadline>|在 _Deadline_ 一节中定义。|以 _DurationType_ 表示的<br>Deadline 周期|c_TimeInfinite|
|<lifespan>|在 _Lifespan_ 一节中定义。|以 _DurationType_ 表示的<br>Lifespan 时长|c_TimeInfinite|
|<disablePo|sitiveAcks>|在 _禁用正向确认_ 一节中定义。||默认禁用，时长设置为<br>c_TimeInfinite|



## 14.8.6 吞吐量配置
吞吐量配置允许限制输出带宽。

|名称|说明|值|默认值|
|---|---|---|---|
|<bytesPerPeri|od>|该控制器在给定时段内允许的数据包总字节数。|UInt32|4294967295|
|<periodMillis|ecs>|在该时间窗口内，允许的字节数不超过 `<bytesPerPeriod>`。|UInt32|0|



## 14.8.7 分配配置
分配配置允许控制内部集合的分配行为，这些集合的元素数量取决于系统中的实体数量。

例如，publisher 内部有集合，其元素数量取决于与其匹配的 subscriber 数量。

有关如何调优分配相关参数的详细信息，请参见 _调优内存分配_。

|名称|说明|值|默认值|
|---|---|---|---|
|<initial>|初始分配空间的元素数量。|UInt32|0|
|<maximum>|将为其分配空间的最大元素数量。|UInt32|0<br>（表示<br>不限制）|
|<increment>|需要更多空间时新分配的元素数量。|UInt32|1|



## 14.8.8 子消息大小限制
有些子消息具有固定大小（例如 SequenceNumber），另一些则根据所含数据具有可变大小。处理子消息需要一块足够大的内存来容纳子消息数据的副本。对于固定大小子消息，这很容易处理，因为大小已知且可以预先分配内存。对于可变大小子消息，可以使用两种不同策略：

- 为数据容器设置最大大小，并在 participant 设置期间预先分配。这样可避免消息通信期间动态分配。但是，任何负载超过已定义最大值的子消息都无法容纳，因此会被丢弃。

- 不为数据容器设置最大大小，而是在子消息到达时（根据子消息头声明的大小）动态分配所需内存。这允许任意大小的子消息，代价是在消息解码期间进行动态分配。

## 14.8.9 History 内存策略配置
控制变更 History 的分配行为。

- **PREALLOCATED**：History 增大时按块分配内存。每块容纳一定数量的变更，直到该块填满才继续分配。它提供最少的动态分配次数，但会增加内存占用。必须适当配置变更的最大负载大小，因为分配后 History 将无法容纳负载更大的变更。

- **PREALLOCATED_WITH_REALLOC**：与 PREALLOCATED 类似，但可以重新分配预分配内存，以容纳负载超过已定义最大值的变更。

- **DYNAMIC**：每个变更都会获得一块大小正确的新分配内存。它可最小化内存占用，但会增加动态分配次数。

- **DYNAMIC_REUSABLE**：与 DYNAMIC 类似，但当变更从 History 移除时不会释放内存，而是复用于后续变更，从而减少动态分配次数。如果新变更的负载更大，将重新分配内存以容纳新大小。

# 14.9 示例
本节给出包含所有可能配置的完整 XML 示例。它可以作为快速参考，但由于不兼容或互斥属性，它可能不是有效配置。不要将其视为可直接工作的示例。

<profiles> <transport_descriptors> <transport_descriptor> <transport_id> ExampleTransportId1 </transport_id> <type> TCPv4 </type> <sendBufferSize> 8192 </sendBufferSize> <receiveBufferSize> 8192 </receiveBufferSize> <TTL> 250 </TTL> <maxMessageSize> 16384 </maxMessageSize> <maxInitialPeersRange> 100 </maxInitialPeersRange> <interfaceWhiteList> <address> 192.168.1.41 </address> <address> 127.0.0.1 </address> </interfaceWhiteList> <wan_addr> 80.80.55.44 </wan_addr> <keep_alive_frequency_ms> 5000 </keep_alive_frequency_ms> <keep_alive_timeout_ms> 25000 </keep_alive_timeout_ms> <max_logical_port> 200 </max_logical_port> <logical_port_range> 20 </logical_port_range> <logical_port_increment> 2 </logical_port_increment> <listening_ports> <port> 5100 </port> 



<port> 5200 </port> </listening_ports> </transport_descriptor> <transport_descriptor> <transport_id> ExampleTransportId2 </transport_id> <type> UDPv6 </type> </transport_descriptor> _<!-- SHM sample transport descriptor -->_ <transport_descriptor> <transport_id> SHM_SAMPLE_DESCRIPTOR </transport_id> <type> SHM </type> _<!-- REQUIRED -->_ <maxMessageSize> 524288 </maxMessageSize> _<!-- OPTIONAL uint32 valid of all transports-->_ <segment_size> 1048576 </segment_size> _<!-- OPTIONAL uint32 SHM only-->_ <port_queue_capacity> 1024 </port_queue_capacity> _<!-- OPTIONAL uint32 SHM only-->_ <healthy_check_timeout_ms> 250 </healthy_check_timeout_ms> _<!- OPTIONAL uint32 SHM only-->_ <rtps_dump_file> test_file.dump </rtps_dump_file> _<!-- OPTIONAL string SHM only-->_ </transport_descriptor> </transport_descriptors> <types> <type> _<!-- Types can be defined in its own type of tag or sharing the same tag -->_ <enum name="MyAloneEnumType" > <enumerator name="A" value="0" /> <enumerator name="B" value="1" /> <enumerator name="C" value="2" /> </enum> </type> <type> <enum name="MyEnumType" > <enumerator name="A" value="0" /> <enumerator name="B" value="1" /> <enumerator name="C" value="2" /> </enum> <typedef name="MyAlias1" type="nonBasic" nonBasicTypeName="MyEnumType" /> <typedef name="MyAlias2" type="int32" arrayDimensions="2,2" /> <struct name="MyStruct1" > <member name="first" type="int32" /> <member name="second" type="int64" /> </struct> <union name="MyUnion1" > <discriminator type="byte" /> <case> <caseDiscriminator value="0" /> <caseDiscriminator value="1" /> <member name="first" type="int32" /> </case> <case> <caseDiscriminator value="2" />

<member name="second" type="nonBasic" nonBasicTypeName="MyStruct" / > </case> <case> <caseDiscriminator value="default" /> <member name="third" type="int64" /> </case> </union> _<!-- All possible members struct type -->_ <struct name="MyFullStruct" > _<!-- Primitives & basic -->_ <member name="my_bool" type="boolean" /> <member name="my_byte" type="byte" /> <member name="my_char" type="char8" /> <member name="my_wchar" type="char16" /> <member name="my_short" type="int16" /> <member name="my_long" type="int32" /> <member name="my_longlong" type="int64" /> <member name="my_unsignedshort" type="uint16" /> <member name="my_unsignedlong" type="uint32" /> <member name="my_unsignedlonglong" type="uint64" /> <member name="my_float" type="float32" /> <member name="my_double" type="float64" /> <member name="my_longdouble" type="float128" /> <member name="my_string" type="string" /> <member name="my_wstring" type="wstring" /> <member name="my_boundedString" type="string" stringMaxLength="41925" / > <member name="my_boundedWString" type="wstring" stringMaxLength="41925 " /> _<!-- long long_array[2][3][4]; -->_ <member name="long_array" arrayDimensions="2,3,4" type="int32" /> _<!-- map<long,map<long,long,2>,2> my_map_map; --> <!--> <typdefe name="my_map_inner" type="int32" key_type="int32" mapMaxLength="2"/> <-->_ <member name="my_map_map" type="nonBasic" nonBasicTypeName="my_map inner" key_type="int32" mapMaxLength="2" /> _<!-- Complex types -->_ <member name="my_other_struct" type="nonBasic" nonBasicTypeName= "OtherStruct" /> </struct> </type> </types> <participant profile_name="part_profile_example" > <rtps> <name> Participant Name </name> _<!-- String -->_ <defaultUnicastLocatorList> <locator> <udpv4>

_<!-- Access as physical, like UDP -->_ **<port>** 7400 **</port> <address>** 192.168.1.41 **</address> </udpv4> </locator> <locator> <tcpv4>** _<!-- Both physical and logical (port), like TCP -->_ **<physical_port>** 5100 **</physical_port> <port>** 7400 **</port> <unique_lan_id>** 192.168.1.1.1.1.2.55 **</unique_lan_id> <wan_address>** 80.80.99.45 **</wan_address> <address>** 192.168.1.55 **</address> </tcpv4> </locator> <locator> <udpv6> <port>** 8844 **</port> <address>** ::1 **</address> </udpv6> </locator> </defaultUnicastLocatorList> <defaultMulticastLocatorList> <locator> <udpv4>** _<!-- Access as physical, like UDP -->_ **<port>** 7400 **</port> <address>** 192.168.1.41 **</address> </udpv4> </locator> <locator> <tcpv4>** _<!-- Both physical and logical (port), like TCP -->_ **<physical_port>** 5100 **</physical_port> <port>** 7400 **</port> <unique_lan_id>** 192.168.1.1.1.1.2.55 **</unique_lan_id> <wan_address>** 80.80.99.45 **</wan_address> <address>** 192.168.1.55 **</address> </tcpv4> </locator> <locator> <udpv6> <port>** 8844 **</port> <address>** ::1 **</address> </udpv6> </locator> </defaultMulticastLocatorList> <sendSocketBufferSize>** 8192 **</sendSocketBufferSize> <listenSocketBufferSize>** 8192 **</listenSocketBufferSize> <builtin> <discovery_config> <discoveryProtocol>** NONE **</discoveryProtocol>** 



<EDP> SIMPLE </EDP> <leaseDuration> <sec> DURATION_INFINITY </sec> </leaseDuration> <leaseAnnouncement> <sec> 1 </sec> <nanosec> 856000 </nanosec> </leaseAnnouncement> <simpleEDP> <PUBWRITER_SUBREADER> true </PUBWRITER_SUBREADER> <PUBREADER_SUBWRITER> true </PUBREADER_SUBWRITER> </simpleEDP> <staticEndpointXMLFilename> filename.xml </ staticEndpointXMLFilename> </discovery_config> <use_WriterLivelinessProtocol> false </use_WriterLivelinessProtocol> <domainId> 4 </domainId> <metatrafficUnicastLocatorList> <locator> <udpv4> _<!-- Access as physical, like UDP -->_ <port> 7400 </port> <address> 192.168.1.41 </address> </udpv4> </locator> <locator> <tcpv4> _<!-- Both physical and logical (port), like TCP -->_ <physical_port> 5100 </physical_port> <port> 7400 </port> <unique_lan_id> 192.168.1.1.1.1.2.55 </unique_lan_id> <wan_address> 80.80.99.45 </wan_address> <address> 192.168.1.55 </address> </tcpv4> </locator> <locator> <udpv6> <port> 8844 </port> <address> ::1 </address> </udpv6> </locator> </metatrafficUnicastLocatorList> <metatrafficMulticastLocatorList> <locator> <udpv4> _<!-- Access as physical, like UDP -->_ <port> 7400 </port>

<address> 192.168.1.41 </address> </udpv4> </locator> <locator> <tcpv4> _<!-- Both physical and logical (port), like TCP -->_ <physical_port> 5100 </physical_port> <port> 7400 </port> <unique_lan_id> 192.168.1.1.1.1.2.55 </unique_lan_id> <wan_address> 80.80.99.45 </wan_address> <address> 192.168.1.55 </address> </tcpv4> </locator> <locator> <udpv6> <port> 8844 </port> <address> ::1 </address> </udpv6> </locator> </metatrafficMulticastLocatorList> <initialPeersList> <locator> <udpv4> _<!-- Access as physical, like UDP -->_ <port> 7400 </port> <address> 192.168.1.41 </address> </udpv4> </locator> <locator> <tcpv4> _<!-- Both physical and logical (port), like TCP -->_ <physical_port> 5100 </physical_port> <port> 7400 </port> <unique_lan_id> 192.168.1.1.1.1.2.55 </unique_lan_id> <wan_address> 80.80.99.45 </wan_address> <address> 192.168.1.55 </address> </tcpv4> </locator> <locator> <udpv6> <port> 8844 </port> <address> ::1 </address> </udpv6> </locator> </initialPeersList> <readerHistoryMemoryPolicy> PREALLOCATED_WITH_REALLOC </ readerHistoryMemoryPolicy> <writerHistoryMemoryPolicy> PREALLOCATED </writerHistoryMemoryPolicy> </builtin> <port> <portBase> 7400 </portBase> 

<domainIDGain> 200 </domainIDGain> <participantIDGain> 10 </participantIDGain> 



<offsetd0> 0 </offsetd0> <offsetd1> 1 </offsetd1> <offsetd2> 2 </offsetd2> <offsetd3> 3 </offsetd3> </port> <participantID> 99 </participantID> <throughputController> <bytesPerPeriod> 8192 </bytesPerPeriod> <periodMillisecs> 1000 </periodMillisecs> </throughputController> <userTransports> <transport_id> TransportId1 </transport_id> <transport_id> TransportId2 </transport_id> </userTransports> <useBuiltinTransports> false </useBuiltinTransports> <propertiesPolicy> <properties> <property> <name> Property1Name </name> <value> Property1Value </value> <propagate> false </propagate> </property> <property> <name> Property2Name </name> <value> Property2Value </value> <propagate> false </propagate> </property> </properties> </propertiesPolicy> </rtps> </participant> <publisher profile_name="pub_profile_example" > <topic> <kind> WITH_KEY </kind> <name> TopicName </name> <dataType> TopicDataTypeName </dataType> <historyQos> <kind> KEEP_LAST </kind> <depth> 20 </depth> </historyQos> <resourceLimitsQos> <max_samples> 5 </max_samples> <max_instances> 2 </max_instances> <max_samples_per_instance> 1 </max_samples_per_instance> <allocated_samples> 20 </allocated_samples> </resourceLimitsQos> </topic> <qos> _<!-- writerQosPoliciesType -->_ <durability> <kind> VOLATILE </kind> 



</durability> <liveliness> <kind> AUTOMATIC </kind> <lease_duration> <sec> 1 </sec> <nanosec> 856000 </nanosec> </lease_duration> <announcement_period> <sec> 1 </sec> <nanosec> 856000 </nanosec> </announcement_period> </liveliness> <reliability> <kind> BEST_EFFORT </kind> <max_blocking_time> <sec> 1 </sec> <nanosec> 856000 </nanosec> </max_blocking_time> </reliability> <partition> <names> <name> part1 </name> <name> part2 </name> </names> </partition> <publishMode> <kind> ASYNCHRONOUS </kind> </publishMode> <disablePositiveAcks> <enabled> true </enabled> <duration> <sec> 1 </sec> </duration> </disablePositiveAcks> </qos> <times> <initialHeartbeatDelay> <sec> 1 </sec> <nanosec> 856000 </nanosec> </initialHeartbeatDelay> <heartbeatPeriod> <sec> 1 </sec> <nanosec> 856000 </nanosec> </heartbeatPeriod> <nackResponseDelay> <sec> 1 </sec> <nanosec> 856000 </nanosec> </nackResponseDelay> <nackSupressionDuration> <sec> 1 </sec> <nanosec> 856000 </nanosec> </nackSupressionDuration> </times> <unicastLocatorList> <locator> 


<udpv4> _<!-- Access as physical, like UDP -->_ <port> 7400 </port> <address> 192.168.1.41 </address> </udpv4> </locator> <locator> <tcpv4> _<!-- Both physical and logical (port), like TCP -->_ <physical_port> 5100 </physical_port> <port> 7400 </port> <unique_lan_id> 192.168.1.1.1.1.2.55 </unique_lan_id> <wan_address> 80.80.99.45 </wan_address> <address> 192.168.1.55 </address> </tcpv4> </locator> <locator> <udpv6> <port> 8844 </port> <address> ::1 </address> </udpv6> </locator> </unicastLocatorList> <multicastLocatorList> <locator> <udpv4> _<!-- Access as physical, like UDP -->_ <port> 7400 </port> <address> 192.168.1.41 </address> </udpv4> </locator> <locator> <tcpv4> _<!-- Both physical and logical (port), like TCP -->_ <physical_port> 5100 </physical_port> <port> 7400 </port> <unique_lan_id> 192.168.1.1.1.1.2.55 </unique_lan_id> <wan_address> 80.80.99.45 </wan_address> <address> 192.168.1.55 </address> </tcpv4> </locator> <locator> <udpv6> <port> 8844 </port> <address> ::1 </address> </udpv6> </locator> </multicastLocatorList> <throughputController> <bytesPerPeriod> 8192 </bytesPerPeriod> <periodMillisecs> 1000 </periodMillisecs> </throughputController> <historyMemoryPolicy> DYNAMIC </historyMemoryPolicy> 



<propertiesPolicy> <properties> <property> <name> Property1Name </name> <value> Property1Value </value> <propagate> false </propagate> </property> <property> <name> Property2Name </name> <value> Property2Value </value> <propagate> false </propagate> </property> </properties> </propertiesPolicy> <userDefinedID> 45 </userDefinedID> <entityID> 76 </entityID> </publisher> <subscriber profile_name="sub_profile_example" > <topic> <kind> WITH_KEY </kind> <name> TopicName </name> <dataType> TopicDataTypeName </dataType> <historyQos> <kind> KEEP_LAST </kind> <depth> 20 </depth> </historyQos> <resourceLimitsQos> <max_samples> 5 </max_samples> <max_instances> 2 </max_instances> <max_samples_per_instance> 1 </max_samples_per_instance> <allocated_samples> 20 </allocated_samples> </resourceLimitsQos> </topic> <qos> <durability> <kind> PERSISTENT </kind> </durability> <liveliness> <kind> MANUAL_BY_PARTICIPANT </kind> <lease_duration> <sec> 1 </sec> <nanosec> 856000 </nanosec> </lease_duration> <announcement_period> <sec> 1 </sec> <nanosec> 856000 </nanosec> </announcement_period> </liveliness> <reliability> <kind> BEST_EFFORT </kind> <max_blocking_time> <sec> 1 </sec> <nanosec> 856000 </nanosec> 



</max_blocking_time> </reliability> <partition> <names> <name> part1 </name> <name> part2 </name> </names> </partition> </qos> <times> <initialAcknackDelay> <sec> 1 </sec> <nanosec> 856000 </nanosec> </initialAcknackDelay> <heartbeatResponseDelay> <sec> 1 </sec> <nanosec> 856000 </nanosec> </heartbeatResponseDelay> </times> <unicastLocatorList> <locator> <udpv4> _<!-- Access as physical, like UDP -->_ <port> 7400 </port> <address> 192.168.1.41 </address> </udpv4> </locator> <locator> <tcpv4> _<!-- Both physical and logical (port), like TCP -->_ <physical_port> 5100 </physical_port> <port> 7400 </port> <unique_lan_id> 192.168.1.1.1.1.2.55 </unique_lan_id> <wan_address> 80.80.99.45 </wan_address> <address> 192.168.1.55 </address> </tcpv4> </locator> <locator> <udpv6> <port> 8844 </port> <address> ::1 </address> </udpv6> </locator> </unicastLocatorList> <multicastLocatorList> <locator> <udpv4> _<!-- Access as physical, like UDP -->_ <port> 7400 </port> <address> 192.168.1.41 </address> </udpv4> </locator> <locator> <tcpv4> 


_<!-- Both physical and logical (port), like TCP -->_ **<physical_port>** 5100 **</physical_port> <port>** 7400 **</port> <unique_lan_id>** 192.168.1.1.1.1.2.55 **</unique_lan_id> <wan_address>** 80.80.99.45 **</wan_address> <address>** 192.168.1.55 **</address> </tcpv4> </locator> <locator> <udpv6> <port>** 8844 **</port> <address>** ::1 **</address> </udpv6> </locator> </multicastLocatorList> <expectsInlineQos>** true **</expectsInlineQos> <historyMemoryPolicy>** DYNAMIC **</historyMemoryPolicy> <propertiesPolicy> <properties> <property> <name>** Property1Name **</name> <value>** Property1Value **</value> <propagate>** false **</propagate> </property> <property> <name>** Property2Name **</name> <value>** Property2Value **</value> <propagate>** false **</propagate> </property> </properties> </propertiesPolicy> <userDefinedID>** 55 **</userDefinedID> <entityID>** 66 **</entityID> </subscriber>** 

# 第 15 章：使用 fastrtpsgen 生成代码
_eprosima Fast RTPS_ 附带内置代码生成工具 fastrtpsgen，可将数据类型的 IDL 规范转换为可用实现，其中包括创建该数据类型 Topic（供 publisher 和 subscriber 使用）所需的方法。该工具还可以生成使用此数据类型的示例应用，并提供在 Linux 上编译的 _Makefile_ 以及 Windows 的 Visual Studio 项目。

在 Linux 上可调用 fastrtpsgen，在 Windows 上可调用 fastrtpsgen.bat 来运行 _fastrtpsgen_。

fastrtpsgen [-d <outputdir>] [-example <platform>] [-replace] [-typeobject] <IDLfile> [<IDLfile> ...] 

如果之前已为该 IDL 生成过文件，需要使用 `-replace` 参数替换当前已有文件。

添加 `-example` 参数后，工具会生成自动化示例及用于当前调用平台构建该示例的文件。`-help` 参数提供当前支持的 Visual Studio 版本和平台列表。

使用 `-typeobject` 参数时，工具会生成用于 TypeObject 生成和管理的附加文件。有关 TypeObject 的更多信息，请参见 _动态话题类型_。

# 15.1 输出
_fastrtpsgen_ 会输出多个文件。假设 IDL 文件名为 “Mytype”，这些文件是：

- `MyType.cxx/.h`：类型定义。

- `MyTypePublisher.cxx/.h`：Publisher 及 PublisherListener 的定义。用户必须为其应用填充所需方法。

- `MyTypeSubscriber.cxx/.h`：Subscriber 及 SubscriberListener 的定义。可以通过修改这些文件中实现的方法来改变 subscriber 的行为。

- `MyTypePubSubType.cxx/.h`：该类型的序列化和反序列化代码。如果 Topic 使用 key，它还定义 `getKey` 方法。

- `MyTypePubSubMain.cxx`：如果生成示例应用，则为该应用的主文件。

- _Makefile_ 或 Visual Studio 项目文件。

如果使用了 `-typeobject`，将修改 _MyType.cxx_ 以在 TypeObjectFactory 中注册 TypeObject 表示，并生成以下文件：

- `MyTypeTypeObject.cxx/.h`：_MyType_ IDL 的 TypeObject 表示。

# 15.2 在哪里找到 _fastrtpsgen_
如果使用 _eProsima Fast RTPS_ 的二进制发行版，则已提供 _fastrtpsgen_。如果从源代码构建，则必须编译 _fastrtpsgen_。相关说明见 _从源代码安装_ 一节。

# 第 16 章：典型用例
Fast-RTPS 的用法非常多样，可根据库所应用场景提供大量配置。本节给出分布式系统中典型用例的配置示例，组织如下：

- _通过 WIFI 使用 Fast-RTPS_。介绍在多播发现具有挑战性的场景中使用 Fast-RTPS 的情况。为解决该问题，说明如何使用初始对等节点列表定义远程 participant 的地址-端口对（参见 _初始对等节点_）。此外还说明如何禁用多播发现机制（参见 _禁用多播发现_）。

- _大规模部署_。说明在部署大量通信代理的环境中推荐使用的 Fast-RTPS 配置，包括在发现阶段使用集中式服务器（参见 _服务器-客户端发现_），以及为已知网络拓扑使用 Fast-RTPS STATIC 发现机制（参见 _已知网络拓扑_）。

- _ROS 2 中的 Fast-RTPS_。由于 Fast-RTPS 是 OSRF Robot Operating System 2（ROS 2）的默认中间件实现，本教程说明如何在 ROS 2 项目中充分利用 Fast-RTPS 的广泛功能。

# 16.1 通过 WIFI 使用 Fast-RTPS
RTPS 标准将 SIMPLE 发现定义为在网络中发现 participant 的默认机制。该机制的主要特性之一是在 Participant Discovery Phase（PDP）中使用多播通信。对于非有线通信（即 WiFi 通信），这可能成为问题，因为多播在 WiFi 上不如在以太网上可靠。Fast-RTPS 对该挑战的解决方案是定义要建立单播通信的 participant，即远程对等节点的初始列表。

## 16.1.1 初始对等节点
根据 RTPS 标准（第 9.6.1.1 节），每个 participant 必须在两个不同端口上监听传入的 PDP 发现元流量，其中一个端口关联多播地址，另一个关联单播地址。Fast-RTPS 允许配置初始对等节点列表，其中包含一个或多个与

远程 participant PDP 发现监听资源对应的地址-端口对。这样，本地 participant 不仅会将 PDP 流量发送到其域指定的默认多播地址-端口，还会发送到 _初始对等节点_ 列表中指定的所有地址-端口对。

participant 的初始对等节点列表包含其将与之通信的所有其他 participant 的地址-端口对。该列表包含 participant 在单播发现机制中使用的地址，可与多播发现一起使用，也可作为其替代方案。因此，该方法也适用于无法使用多播功能的场景。

根据 RTPS 标准（第 9.6.1.1 节），participant 发现流量的单播监听端口按以下公式计算：7400 + 250 * _domainID_ + 10 + 2 * _participantID_。因此，例如 participant 在 Domain 0（默认域）中运行且 ID 为 1，其发现流量的单播监听端口为：7400 + 250 * 0 + 10 + 2 * 1 = 7412。

以下示例配置了一个初始对等节点列表，其中包含域 0 中主机 192.168.10.13 上 participant ID 为 1 的对等节点。

### C++
Locator_t initial_peers_locator; IPLocator::setIPv4(initial_peers_locator, "192.168.10.13"); initial_peers_locator.port = 7412; participant_attr.rtps.builtin.initialPeersList.push_back(initial_peers_locator); 

**XML** 

<participant profile_name="initial_peers_example_profile" is_default_profile="true" > <rtps> <builtin> <initialPeersList> <locator> <udpv4> <address> 192.168.10.13 </address> <port> 7412 </port> </udpv4> </locator> </initialPeersList> </builtin> </rtps> </participant> 

## 16.1.2 禁用多播发现
如果所有对等节点都已知，可以完全禁用多播元流量。这通过配置属性 `metatrafficUnicastLocatorList` 完成。定义自定义 `metatrafficUnicastLocatorList` 后，participant 不再使用默认的元流量多播和单播定位器，从而避免监听任何来自多播源的发现数据。本地 participant 会为 `metatrafficUnicastLocatorList` 中指定的每个地址-端口对创建元流量接收资源。

分配 `metatrafficUnicastLocatorList` 中的地址-端口对时，应避免分配不可用的端口，或与 publisher participant 的 Initial Peers 列表中列出的地址-端口不一致的端口。

### C++
Locator_t meta_unicast_locator; IPLocator::setIPv4(meta_unicast_locator, "192.168.10.13"); meta_unicast_locator.port = 7412; participant_attr.rtps.builtin.metatrafficUnicastLocatorList.push_back(meta_unicast locator); 

### XML
<participant profile_name="initial_peers_multicast_avoidance" is_default_profile= "true" > <rtps> <builtin> _<!-- Choosing a specific unicast address -->_ <metatrafficUnicastLocatorList> <locator> <udpv4> <address> 192.168.10.13 </address> <port> 7412 </port> </udpv4> </locator> </metatrafficUnicastLocatorList> </builtin> </rtps> </participant> 

# 16.2 大规模部署
通信节点数量很多的系统可能在设置时间、内存消耗和网络负载方面给基于数据分发服务（DDS）的中间件实现带来挑战。这是因为如 _发现_ 所述，Participant Discovery Phase（PDP）依赖发送到多播地址的元流量公告，使网络中的所有 participant 能够相互确认。随后是 Endpoint Discovery Phase（EDP），所有 participant 使用单播地址与其他 participant 交换其 publisher 和 subscriber 实体信息，以便使用同一 Topic 的 publisher 和 subscriber 能够匹配。随着 participant、publisher 和 subscriber 数量增加，元流量和连接数量会呈指数增长，严重影响设置时间和内存消耗。Fast-RTPS 提供扩展 DDS 标准的附加功能，以适应大规模部署场景。

|功能|用途|
|---|---|
|服务器-<br>客户端|该功能旨在用基于服务器-客户端架构的发现替代标准 SPDP 和 SEDP 协议，其中所有元流量都通过枢纽（服务器）|
|发现<br>机制|分发到网络中的各通信节点。|
|静态<br>发现|使用该功能，用户可以手动指定哪个 participant 应与哪个 participant 通信，以及通过哪个地址和端口通信。此外，用户还可以指定哪个 publisher/subscriber 与哪个 publisher/subscriber 匹配，从而消除所有 EDP 元流量。|



## 16.2.1 服务器-客户端发现
考虑部署大量通信代理（此处称为 participant）的场景，可以使用默认 RTPS 标准 SIMPLE 发现机制的替代方案。为此，FastRTPS 提供客户端-服务器发现机制，其中服务器 participant 作为通信中心，收集并处理客户端 participant 发送的元流量，并将适当信息分发给其余客户端。

下面介绍多种发现服务器用例。

### UDPv4 示例设置
要配置客户端-服务器发现场景，需要创建两种 participant：服务器 participant 和客户端 participant。此类实现中需要配置的两个参数如下：

- **Prefix**：服务器的唯一标识符。

- **地址-端口对**：指定运行服务器的机器的 IP 地址和端口。端口是一个随机数，可替换为任意其他值。分配 `metatrafficUnicastLocatorList` 中的地址-端口对时，应避免分配不可用端口。因此不建议使用 RTPS 标准端口。


![](fast-dds-docs-eprosima-com-en-v1.10.0_images/fast-dds-docs-eprosima-com-en-v1.10.0.pdf-0187-01.png)


<!-- Start of picture text -->
SERVER CLIENT<br>C++ C++<br>Locator_t server_locator; Locator_t remote_server_locator;<br>IPLocator::setIPv4(server_locator, "192. IPLocator::setIPv4(remote_server_locator,<br> 168.10.57"); "192.168.10.57");<br>server_locator.port = 56542; remote_server_locator.port = 56542;<br>participant_attr.rtps.builtin.discovery_ RemoteServerAttributes remote_server_<br> config.discoveryProtocol = attr;<br> DiscoveryProtocol_t::SERVER; remote_server_attr.ReadguidPrefix("72.61.<br>participant_attr.rtps.ReadguidPrefix("72. 73.70.66.61.72.6d.74.65.73.74");<br> 61.73.70.66.61.72.6d.74.65.73.74"); remote_server_attr.<br>participant_attr.rtps.builtin. metatrafficUnicastLocatorList.push_<br> metatrafficUnicastLocatorList.push_ back(remote_server_locator);<br> back(server_locator);<br>participant_attr.rtps.builtin.discovery_ participant_attr.rtps.builtin.discovery_<br> config.discoveryServer_client_ config.discoveryProtocol =<br> syncperiod = Duration_t(0, 250000000); DiscoveryProtocol_t::CLIENT;<br>participant_attr.rtps.builtin.discovery_<br> config.m_DiscoveryServers.push_<br> back(remote_server_attr);<br>XML XML<br><participant profile_name="UDP SERVER" <participant profile_name="UDP CLIENT"<br> is_default_profile="true" > is_default_profile="true" ><br><rtps> <rtps><br><prefix> 72.61.73.70.66.61.72.6d. <builtin><br> 74.65.73.74 </prefix> <discovery_config><br><builtin> <discoveryProtocol> CLIENT<br><discovery_config> </discoveryProtocol><br><discoveryProtocol> SERVER <discoveryServersList><br> </discoveryProtocol> <RemoteServer prefix=<br></discovery_config> "72.61.73.70.66.61.72.6d.74.65.73.74" ><br> <metatrafficUnicastLocatorList> <metatrafficUnicastLocatorList><br><locator> <locator><br><udpv4> <udpv4><br><address> 192.168.<br> 10.57 </address> <address> 192.168.10.57 </address><br><port> 56542 </<br> port> <port> 56542 </port><br></udpv4> </udpv4><br></locator> </locator><br></ </<br> metatrafficUnicastLocatorList> metatrafficUnicastLocatorList><br></builtin> </RemoteServer><br></rtps> </discoveryServersList><br></participant> </discovery_config><br></builtin><br></rtps><br></participant><br><!-- End of picture text -->

### UDPv4 冗余示例
_上述示例_ 存在 _单点故障_，即如果 _server_ 失效，则无法进行发现。为防止这种情况，可以将多个 servers 关联到 _client_。这样，只有当 _所有 servers_ 都失效时才会发生发现失败，而这种情况更不可能发生。

为确保每个服务器具有唯一的 **Prefix** 和 _单播地址_，选择了以下值：

|Prefix<br>UDPv4 address|
|---|
|75.63.2D.73.76.72.63.6C.6E.74.2D.31<br>192.168.10.57:56542|
|75.63.2D.73.76.72.63.6C.6E.74.2D.32<br>192.168.10.60:56543|




![](fast-dds-docs-eprosima-com-en-v1.10.0_images/fast-dds-docs-eprosima-com-en-v1.10.0.pdf-0188-05.png)


请注意，多个 _servers_ 可以共享同一 _IP 地址_，但端口号应不同。同样，如果多个 _servers_ 的 _IP 地址_ 不同，它们也可以共享同一端口。

### C++
```cpp
// SERVER
Locator_t server_locator_1;
Locator_t server_locator_2;
IPLocator::setIPv4(server_locator_1, "192.168.10.57");
server_locator_1.port = 56542;
IPLocator::setIPv4(server_locator_2, "192.168.10.60");
server_locator_2.port = 56543;

ParticipantAttributes participant_attr_1;
participant_attr_1.rtps.builtin.discovery_config.discoveryProtocol = DiscoveryProtocol_t::SERVER;
participant_attr_1.rtps.ReadguidPrefix("75.63.2D.73.76.72.63.6C.6E.74.2D.31");
participant_attr_1.rtps.builtin.metatrafficUnicastLocatorList.push_back(server_locator_1);
participant_attr_1.rtps.builtin.metatrafficUnicastLocatorList.push_back(server_locator_2);

ParticipantAttributes participant_attr_2;
participant_attr_2.rtps.builtin.discovery_config.discoveryProtocol = DiscoveryProtocol_t::SERVER;
participant_attr_2.rtps.ReadguidPrefix("75.63.2D.73.76.72.63.6C.6E.74.2D.32");
participant_attr_2.rtps.builtin.metatrafficUnicastLocatorList.push_back(server_locator_2);

// CLIENT
Locator_t remote_server_locator_1;
Locator_t remote_server_locator_2;
IPLocator::setIPv4(remote_server_locator_1, "192.168.10.57");
remote_server_locator_1.port = 56542;
IPLocator::setIPv4(remote_server_locator_2, "192.168.10.60");
remote_server_locator_2.port = 56543;

RemoteServerAttributes remote_server_attr_1;
remote_server_attr_1.ReadguidPrefix("75.63.2D.73.76.72.63.6C.6E.74.2D.31");
remote_server_attr_1.metatrafficUnicastLocatorList.push_back(remote_server_locator_1);

RemoteServerAttributes remote_server_attr_2;
remote_server_attr_2.ReadguidPrefix("75.63.2D.73.76.72.63.6C.6E.74.2D.32");
remote_server_attr_2.metatrafficUnicastLocatorList.push_back(remote_server_locator_2);

participant_attr.rtps.builtin.discovery_config.discoveryProtocol = DiscoveryProtocol_t::CLIENT;
participant_attr.rtps.builtin.discovery_config.m_DiscoveryServers.push_back(remote_server_attr_1);
participant_attr.rtps.builtin.discovery_config.m_DiscoveryServers.push_back(remote_server_attr_2);
```

### XML
```xml
<participant profile_name="UDP_SERVER_1">
  <rtps>
    <prefix>75.63.2D.73.76.72.63.6C.6E.74.2D.31</prefix>
    <builtin>
      <discovery_config>
        <discoveryProtocol>SERVER</discoveryProtocol>
        <metatrafficUnicastLocatorList>
          <locator>
            <udpv4>
              <address>192.168.10.57</address>
              <port>56542</port>
            </udpv4>
          </locator>
        </metatrafficUnicastLocatorList>
      </discovery_config>
    </builtin>
  </rtps>
</participant>

<participant profile_name="UDP_CLIENT">
  <rtps>
    <builtin>
      <discovery_config>
        <discoveryProtocol>CLIENT</discoveryProtocol>
        <discoveryServersList>
          <RemoteServer prefix="75.63.2D.73.76.72.63.6C.6E.74.2D.31">
            <metatrafficUnicastLocatorList>
              <locator>
                <udpv4>
                  <address>192.168.10.57</address>
                  <port>56542</port>
                </udpv4>
              </locator>
            </metatrafficUnicastLocatorList>
          </RemoteServer>
        </discoveryServersList>
      </discovery_config>
    </builtin>
  </rtps>
</participant>
```

### UDPv4 持久化示例
所有 participant 都会记录已发现的所有端点（其他 participant、subscriber 或 publisher）。不同类型 participant 使用不同流程填充该记录：

- _clients_ 从其 _servers_ 接收该信息。

- _servers_ 从其 _clients_ 接收该信息。

由于 _servers_ 通常关联许多 _clients_，该过程耗时较长。在 _server_ 失败的情况下，我们可能希望加快 _server_ 重启后的该过程。

将发现信息保存在与 _server_ 记录同步的文件中即可实现该目标。为此，只需将 _发现协议_ 指定为 **BACKUP**。

创建 _server_ 后，它会在进程工作目录中生成 _server-<GUIDPREFIX>.db_（例如 _server-73-65-72-76-65-72-636C-69-65-6E-74.db_）。

要从头开始（即不反序列化任何发现信息），必须在启动服务器前删除或重命名旧备份文件。

### 使用服务器进行 UDPv4 分区
_Server_ 关联可视为除 _域_ 和 _分区_ 之外的另一种隔离机制。不共享 _server_ 的 _clients_ 无法相互看到，并属于彼此隔离的服务器网络。要连接由服务器隔离的网络，可以：

1. 将每个 _client_ 连接到两个 _servers_。

2. 将一个 _server_ 连接到另一个 _server_。

3. 创建一个新的 _server_，并将其关联到客户端所连接的 _servers_。

选项 1 和 2 只能通过预先修改属性或 XML 配置文件实现，因此与域和分区策略类似。选项 3 可以在运行时实施，即在隔离网络已经启动并运行后。


![](fast-dds-docs-eprosima-com-en-v1.10.0_images/fast-dds-docs-eprosima-com-en-v1.10.0.pdf-0190-15.png)


### 选项 1
将每个 _client_ 连接到两个 _servers_。此情况与前面介绍的 _冗余用例_ 相同。

### 选项 2
将一个 _server_ 连接到另一个 _server_。这里考虑两个服务器，各自管理一个隔离网络：

|网络|Prefix / UDPv4 地址|
|---|---|
|A|75.63.2D.73.76.72.63.6C.6E.74.2D.31<br>192.168.10.60:56543|
|B|75.63.2D.73.76.72.63.6C.6E.74.2D.32<br>192.168.10.57:56542|



为使两个网络通信，可以将服务器 A 配置为服务器 B 的客户端，如下所示：

### C++
Locator_t server_locator, remote_server_locator; IPLocator::setIPv4(server_locator, "192.168.10.60"); server_locator.port = 56543; IPLocator::setIPv4(remote_server_locator, "192.168.10.57"); remote_server_locator.port = 56542; RemoteServerAttributes remote_server_attr; remote_server_attr.ReadguidPrefix("75.63.2D.73.76.72.63.6C.6E.74.2D.32"); remote_server_attr.metatrafficUnicastLocatorList.push_back(remote_server_locator); participant_attr.rtps.ReadguidPrefix("75.63.2D.73.76.72.63.6C.6E.74.2D.31"); participant_attr.rtps.builtin.metatrafficUnicastLocatorList.push_back(server locator); participant_attr.rtps.builtin.discovery_config.discoveryProtocol = DiscoveryProtocol_t::SERVER; participant_attr.rtps.builtin.discovery_config.m_DiscoveryServers.push_back(remote server_attr); 

### XML
<participant profile_name="UDP SERVER A" > <rtps> <prefix> 75.63.2D.73.76.72.63.6C.6E.74.2D.31 </prefix> <builtin> <discovery_config> <discoveryProtocol> SERVER </discoveryProtocol> <discoveryServersList> <RemoteServer prefix="75.63.2D.73.76.72.63.6C.6E.74.2D.32" > <metatrafficUnicastLocatorList> <locator> <udpv4> <address> 192.168.10.57 </address> <port> 56542 </port> </udpv4> </locator> </metatrafficUnicastLocatorList> </RemoteServer> </discoveryServersList> </discovery_config> <metatrafficUnicastLocatorList> <locator> <udpv4> <address> 192.168.10.60 </address> <port> 56543 </port> </udpv4> </locator> </metatrafficUnicastLocatorList> </builtin> </rtps> </participant>


### 选项 3
创建一个新的 _server_，并关联到客户端所连接的 _servers_。这里有两个可能已在运行的隔离网络 A 和 B，通过服务器 C 将它们连接起来。

|服务器|Prefix / UDPv4 地址|
|---|---|
|A|75.63.2D.73.76.72.63.6C.6E.74.2D.31<br>192.168.10.60:56543|
|B|75.63.2D.73.76.72.63.6C.6E.74.2D.32<br>192.168.10.57:56542|
|C|75.63.2D.73.76.72.63.6C.6E.74.2D.33<br>192.168.10.54:56541|



为使两个网络通信，可以将服务器 C 配置为服务器 A 和 B 的客户端，如下所示：

### C++
Locator_t server_locator, remote_server_locator_A, remote_server_locator_B; IPLocator::setIPv4(server_locator, "192.168.10.54"); server_locator.port = 56541; IPLocator::setIPv4(remote_server_locator_A, "192.168.10.60"); remote_server_locator_A.port = 56543; IPLocator::setIPv4(remote_server_locator_B, "192.168.10.57"); remote_server_locator_B.port = 56542; RemoteServerAttributes remote_server_attr_A, remote_server_attr_B; remote_server_attr_A.ReadguidPrefix("75.63.2D.73.76.72.63.6C.6E.74.2D.31"); remote_server_attr_A.metatrafficUnicastLocatorList.push_back(remote_server_locator A); remote_server_attr_B.ReadguidPrefix("75.63.2D.73.76.72.63.6C.6E.74.2D.32"); remote_server_attr_B.metatrafficUnicastLocatorList.push_back(remote_server_locator B); participant_attr.rtps.ReadguidPrefix("75.63.2D.73.76.72.63.6C.6E.74.2D.33"); participant_attr.rtps.builtin.metatrafficUnicastLocatorList.push_back(server locator); participant_attr.rtps.builtin.discovery_config.discoveryProtocol = DiscoveryProtocol_t::SERVER; participant_attr.rtps.builtin.discovery_config.m_DiscoveryServers.push_back(remote server_attr_A); participant_attr.rtps.builtin.discovery_config.m_DiscoveryServers.push_back(remote server_attr_B); 

### XML
<participant profile_name="UDP SERVER C" > <rtps> <prefix> 75.63.2D.73.76.72.63.6C.6E.74.2D.33 </prefix> <builtin> <discovery_config> <discoveryProtocol> SERVER </discoveryProtocol> <discoveryServersList> <RemoteServer prefix="75.63.2D.73.76.72.63.6C.6E.74.2D.32" > <metatrafficUnicastLocatorList> <locator> <udpv4> <address> 192.168.10.57 </address> <port> 56542 </port> </udpv4> </locator> </metatrafficUnicastLocatorList> </RemoteServer> <RemoteServer prefix="75.63.2D.73.76.72.63.6C.6E.74.2D.31" > <metatrafficUnicastLocatorList> <locator> <udpv4> <address> 192.168.10.60 </address> <port> 56543 </port> </udpv4> </locator> </metatrafficUnicastLocatorList> </RemoteServer> </discoveryServersList> </discovery_config> <metatrafficUnicastLocatorList> <locator> <udpv4> <address> 192.168.10.54 </address> 


## 16.2.2 已知网络拓扑
在生产流水线等工业部署中，通常可以预先知道整个网络拓扑（主机、IP 地址等）。此类场景非常适合 Fast-RTPS STATIC 发现机制；该机制可大幅减少中间件设置时间（直到所有实体准备好交换信息的时间），同时将连接限制为严格必要的连接。如 _发现_ 一节所述，所有 Fast-RTPS 发现机制都包括两个步骤：PDP 和 EDP。

### 对等 Participant 发现阶段
默认情况下，Fast-RTPS 在 PDP 阶段使用 SPDP 协议。这要求 participant 通过众所周知的组播地址周期发送 PDP 公告，并使用根据域计算的 IP 端口。对于大型部署，这可能产生相当多的元流量，因为每当 participant 通过多播收到 PDP 消息时，都会使用消息中指定的地址和端口回复远程 participant。在此场景中，PDP 连接数为 _N * (N - 1)_，其中 _N_ 是网络中的 participant 数量。

但通常情况下，并非所有 participant 都需要知道网络中所有其他远程 participant。为限制这些 PDP 元流量，可以将 Fast-RTPS participant 配置为只向需要连接的远程 participant 发送 PDP 公告。这通过将一组 IP 地址-端口对指定为对等节点列表并禁用 participant 多播公告来实现。_通过 WIFI 使用 Fast-RTPS_ 用例详细说明了这种配置方式。

### STATIC 端点发现阶段
如 _STATIC 端点发现设置_ 所述，通过 XML 文件指定 EDP 发现可以完全避免 EDP 元流量。这样，用户可以手动配置哪个 publisher/subscriber 与哪个 publisher/subscriber 匹配，从而立即开始共享用户数据。为此，必须向本地实体提供描述远程实体配置的 STATIC 发现 XML 文件。在本示例中，participant `HelloWorldPublisher` 中 Topic `HelloWorldTopic` 的 publisher 与 participant `HelloWorldSubscriber` 的 subscriber 匹配。实现 STATIC EDP 的完整示例是 STATIC EDP 示例。

### 创建 STATIC 发现 XML 文件

```xml
<!-- HelloWorldPublisher.xml -->
<staticdiscovery>
  <participant>
    <name>HelloWorldPublisher</name>
    <writer>
      <userId>1</userId>
      <entityId>2</entityId>
      <topicName>HelloWorldTopic</topicName>
      <topicDataType>HelloWorld</topicDataType>
    </writer>
  </participant>
</staticdiscovery>

<!-- HelloWorldSubscriber.xml -->
<staticdiscovery>
  <participant>
    <name>HelloWorldSubscriber</name>
    <reader>
      <userId>3</userId>
      <entityId>4</entityId>
      <topicName>HelloWorldTopic</topicName>
      <topicDataType>HelloWorld</topicDataType>
    </reader>
  </participant>
</staticdiscovery>
```

### 创建实体并加载 STATIC 发现 XML 文件
创建实体时，本地 publisher/subscriber 属性必须与远程实体加载的 STATIC 发现 XML 文件中定义的属性一致。

### C++
```cpp
// Publisher
ParticipantAttributes participant_attr;
participant_attr.rtps.setName("HelloWorldPublisher");
participant_attr.rtps.builtin.discovery_config.use_SIMPLE_EndpointDiscoveryProtocol = false;
participant_attr.rtps.builtin.discovery_config.use_STATIC_EndpointDiscoveryProtocol = true;
participant_attr.rtps.builtin.discovery_config.setStaticEndpointXMLFilename("HelloWorldSubscriber.xml");

PublisherAttributes publisher_attr;
publisher_attr.topic.topicName = "HelloWorldTopic";
publisher_attr.topic.topicDataType = "HelloWorld";
publisher_attr.setUserDefinedID(1);
publisher_attr.setEntityID(2);

// Subscriber
ParticipantAttributes subscriber_participant_attr;
subscriber_participant_attr.rtps.setName("HelloWorldSubscriber");
subscriber_participant_attr.rtps.builtin.discovery_config.use_SIMPLE_EndpointDiscoveryProtocol = false;
subscriber_participant_attr.rtps.builtin.discovery_config.use_STATIC_EndpointDiscoveryProtocol = true;
subscriber_participant_attr.rtps.builtin.discovery_config.setStaticEndpointXMLFilename("HelloWorldPublisher.xml");

SubscriberAttributes subscriber_attr;
subscriber_attr.topic.topicName = "HelloWorldTopic";
subscriber_attr.topic.topicDataType = "HelloWorld";
subscriber_attr.setUserDefinedID(3);
subscriber_attr.setEntityID(4);
```

### XML
```xml
<!-- HelloWorldPublisher.xml -->
<participant profile_name="participant_profile_static_pub">
  <rtps>
    <name>HelloWorldPublisher</name>
    <builtin>
      <discovery_config>
        <EDP>STATIC</EDP>
        <staticEndpointXMLFilename>HelloWorldSubscriber.xml</staticEndpointXMLFilename>
      </discovery_config>
    </builtin>
  </rtps>
</participant>

<!-- HelloWorldSubscriber.xml -->
<participant profile_name="participant_profile_static_sub">
  <rtps>
    <name>HelloWorldSubscriber</name>
    <builtin>
      <discovery_config>
        <EDP>STATIC</EDP>
        <staticEndpointXMLFilename>HelloWorldPublisher.xml</staticEndpointXMLFilename>
      </discovery_config>
    </builtin>
  </rtps>
</participant>
```

# 第 17 章：简介
eProsima FASTRTPSGEN 是一个 Java 应用程序，它使用 IDL 文件中定义的数据类型生成源代码。生成的源代码可用于在应用中发布和订阅自定义类型的 Topic。

要声明结构化数据，必须使用 IDL（Interface Definition Language，接口定义语言）格式。IDL 是由 OMG（Object Management Group）制定的规范语言，以语言无关的方式描述接口，使使用不同语言的软件组件之间能够通信。

eProsima FASTRTPSGEN 读取 IDL 文件，并解析 OMG IDL 规范的一个子集以生成序列化源代码。该子集包括 _通过 IDL 定义数据类型_ 中介绍的数据类型描述。文件中的其他内容会被忽略。

eProsima FASTRTPSGEN 生成的源代码使用 Fast CDR：一个提供序列化机制的 C++11 库。此处使用 RTPS 规范文档指定的 CDR 序列化机制。标准 CDR（Common Data Representation，公共数据表示）是一种用于代理间传输的低层传输语法，将 OMG IDL 定义的数据类型映射到字节流。

eProsima FASTRTPSGEN 的主要特性之一是让用户不必了解序列化或反序列化过程。它还使用 eProsima RTPS 库提供 publisher 和 subscriber 的初始实现。

# 17.1 编译
编译 _fastrtpsgen_ 前，首先需要安装 Gradle 和 Java JDK（请检查所用 Gradle 版本推荐的 JDK 版本）。

要编译 _fastrtpsgen_ Java 应用程序，需要从 Fast-RPTS-Gen 仓库下载源代码（使用 `--recursive` 选项），并调用 `gradle assemble` 进行编译。更多详情请参见 _编译_。

```bash
git clone --recursive https://github.com/eProsima/Fast-RTPS-Gen.git
cd Fast-RTPS-Gen
gradle assemble
```

生成的 Java 应用程序位于 `share/fastrtps`，更易用的脚本位于 `scripts` 文件夹。如果希望在任何位置使用这些脚本，可以将 `scripts` 文件夹路径添加到 `PATH` 环境变量。

# 第 18 章：执行与 IDL 定义
# 18.1 构建 publisher/subscriber 代码
本节介绍此 Java 应用程序的用法，并简要说明生成的文件。

将 `scripts` 文件夹添加到 `PATH` 后，可根据使用 Windows 还是 Linux，通过以下脚本执行该 Java 应用程序：

```bat
fastrtpsgen.bat
```

```bash
fastrtpsgen
```

如果未修改 `PATH`，可以在 `<fastrtpsgen_directory>/scripts` 文件夹中找到这些脚本。

该应用预期的参数列表为：

```text
fastrtpsgen [<options>] <IDL file> [<IDL file> ...]
```

其中选项如下：

|选项|说明|
|---|---|
|-help|显示帮助信息。|
|-version|显示 eProsima FASTRTPSGEN 的当前版本。|
|-d<br><directory>|设置生成文件的输出目录。|
|-I<br><directory>|将目录添加到预处理器包含路径。|
|-t<br><directory>|将指定目录设置为临时目录。|
|-example<br><platform>|为特定平台生成示例以及编译生成源代码的解决方案。`help` 命令显示支持的平台。|
|-replace|即使生成的源代码文件已存在，也替换它们。|
|-ppDisable|禁用预处理器。|
|-ppPath|指定预处理器路径。|
|-typeobject|为提供的 IDL 生成 _TypeObject_ 文件，并修改 MyType 构造函数，将 TypeObject 表示注册到工厂中。|



有关 TypeObject 表示的更多信息，请阅读 _动态话题类型_。

# 18.2 通过 IDL 定义数据类型
下表列出 _fastrtpsgen_ 支持的基本 IDL 类型及其到 C++11 的映射。

|IDL|C++11|
|---|---|
|char|char|
|octet|uint8_t|
|short|int16_t|
|unsigned short|uint16_t|
|long|int32_t|
|unsigned long|uint32_t|
|longlong|int64_t|
|unsigned longlong|uint64_t|
|float|float|
|double|double|
|longdouble|longdouble|
|boolean|bool|
|string|std::string|



## 18.2.1 数组
_fastrtpsgen_ 支持一维和多维数组。数组始终映射到 `std::array` 容器。下表列出支持的数组类型及其映射方式。

|IDL|C++11|
|---|---|
|char a[5]|std::array<char,5> a|
|octet a[5]|std::array<uint8_t,5> a|
|short a[5]|std::array<int16_t,5> a|
|unsigned short a[5]|std::array<uint16_t,5> a|
|longa[5]|std::array<int32_t,5> a|
|unsigned longa[5]|std::array<uint32_t,5> a|
|longlonga[5]|std::array<int64_t,5> a|
|unsigned longlonga[5]|std::array<uint64_t,5> a|
|float a[5]|std::array<float,5> a|
|double a[5]|std::array<double,5> a|



## 18.2.2 序列
_fastrtpsgen_ 支持序列，并将其映射到 STD vector 容器。下表展示 IDL 与 C++11 之间的映射方式。

|IDL|C++11|
|---|---|
|sequence<char>|std::vector<char>|
|sequence<octet>|std::vector<uint8_t>|
|sequence<short>|std::vector<int16_t>|
|sequence<unsigned short>|std::vector<uint16_t>|
|sequence<long>|std::vector<int32_t>|
|sequence<unsigned long>|std::vector<uint32_t>|
|sequence<longlong>|std::vector<int64_t>|
|sequence<unsigned longlong>|std::vector<uint64_t>|
|sequence<float>|std::vector<float>|
|sequence<double>|std::vector<double>|



## 18.2.3 映射
_fastrtpsgen_ 支持映射，其等价于 STD map 容器。类型之间的等价比照方式与 _序列_ 相同。

|IDL|C++11|
|---|---|
|map<char,unsigned longlong>|std::map<char,uint64_T>|



## 18.2.4 结构体
可以定义包含多种类型成员的 IDL 结构体。它会转换为一个 C++ 类，其中每个成员映射为属性，并附带用于 _get_ 和 _set_ 每个成员的方法。

以下 IDL 结构体：

struct Structure { octet octet_value; long long_value; 



string string_value; }; 

将转换为：

**class Structure** { public: Structure(); ~Structure(); Structure(const Structure &x); Structure(Structure &&x); Structure& operator=( const Structure &x); Structure& operator=(Structure &&x); void octet_value(uint8_t _octet_value); uint8_t octet_value() const; uint8_t& octet_value(); void long_value(int64_t _long_value); int64_t long_value() const; int64_t& long_value(); void string_value(const std::string &_string_value); void string_value(std::string &&_string_value); const std::string& string_value() const; std::string& string_value(); private: uint8_t m_octet_value; int64_t m_long_value; std::string m_string_value; }; 

结构体可以继承其他结构体，扩展其成员集合。

struct ParentStruct { octet parent_member; }; struct ChildStruct : ParentStruct { long child_member; }; 

在这种情况下，生成的 C++ 代码为：

**class ParentStruct** { ... }; **class ChildStruct** : public ParentStruct { ... }; 

## 18.2.5 Union
在 IDL 中，union 定义为一系列具有各自类型的成员以及一个指定当前使用哪个成员的 discriminant。IDL union 类型映射为 C++ 类，并提供访问 union 成员和 discriminant 的函数。

以下 IDL union：

union Union switch(long) { case 1: octet octet_value; case 2: long long_value; case 3: string string_value; }; 

将转换为：

**class Union** { public: Union(); ~Union(); Union(const Union &x); Union(Union &&x); Union& operator=(const Union &x); Union& operator=(Union &&x); void d(int32t __d); int32_t _d() const; int32_t& _d(); void octet_value(uint8_t _octet_value); uint8_t octet_value() const; uint8_t& octet_value(); void long_value(int64_t _long_value); int64_t long_value() const; int64_t& long_value(); void string_value(const std::string &_string_value); void string_value(std:: string &&_string_value); const std::string& string_value() const; std::string& string_value(); private: int32_t m__d; uint8_t m_octet_value; int64_t m_long_value; std::string m_string_value; }; 

## 18.2.6 位集
位集是一种特殊结构体，封装一组位。位集最多可表示 64 位。每个成员定义为 _位字段_，便于访问位集的一部分。

例如：

bitset MyBitset { bitfield<3> a; bitfield<10> b; bitfield<12, int> c; }; 

`MyBitset` 类型总共存储 25 位（3 + 10 + 12），并在内存中占用 32 位（能够存储该位集大小的最小基本类型）。

- 位字段 `a` 允许访问前 3 位（0..2）。

- 位字段 `b` 允许访问接下来的 10 位（3..12）。

- 位字段 `c` 允许访问接下来的 12 位（13..24）。

生成的 C++ 代码大致如下：

**class MyBitset** { public: void a(char _a); char a() const; void b(uint16_t _b); uint16_t b() const; void c(int32_t _c); int32_t c() const; private: std::bitset<25> m_bitset; }; 

内部存储为 `std::bitset`。对于每个位字段，都会生成访问方法 getter 和 setter，并使用尽可能小的基本无符号类型。对于位字段 `c`，用户指定访问类型为 **int**，因此生成的代码使用 **int32_t**，而不是自动使用 **uint16_t**。

位集可以继承其他位集，扩展其成员集合。

bitset ParentBitset { bitfield<3> parent_member; }; bitset ChildBitset : ParentBitset { bitfield<10> child_member; }; 

在这种情况下，生成的 C++ 代码为：

**class ParentBitset** { ... }; **class ChildBitset** : public ParentBitset 



{ ... }; 

请注意，在这种情况下，`ChildBitset` 将拥有两个 `std::bitset` 成员：一个属于 `ParentBitset`，另一个属于 `ChildBitset`。

## 18.2.7 枚举
IDL 格式的枚举是一组关联数值的标识符。IDL 枚举类型直接映射到相应的 C++11 枚举定义。

以下 IDL 枚举：

enum Enumeration { RED, GREEN, BLUE }; 

将转换为：

enum Enumeration : uint32_t { RED, GREEN, BLUE }; 

## 18.2.8 位掩码
位掩码是一种用于管理位掩码的特殊枚举，允许根据位的位置定义位掩码。

以下 IDL 位掩码：

**@bit_bound** (8) bitmask MyBitMask { **@position** (0) flag0, **@position** (1) flag1, **@position** (4) flag4, **@position** (6) flag6, flag7 }; 

将转换为：

enum MyBitMask : uint8_t { flag0 = 0x01 << 0, flag1 = 0x01 << 1, flag4 = 0x01 << 4, 



flag6 = 0x01 << 6, flag7 = 0x01 << 7 }; 

注解 _bit_bound_ 定义关联枚举的宽度，必须是 1 到 64 之间的正数。如果省略，则为 32 位。对于每个 _flag_，用户可以使用注解 _position_ 定义该标志的位置。如果省略，则从 0 开始，基于上一个已定义标志自动递增。

## 18.2.9 有键类型
要使用有键 Topic，用户应在结构体内部定义一些键成员。方法是在希望用作键的结构体成员之前写入 `@Key`。例如，在以下 IDL 文件中，`id` 和 `type` 字段是键：

struct MyType { **@Key** long id; **@Key** string type; long positionX; long positionY; }; 

_fastrtpsgen_ 会自动检测这些标签，并为 TopicDataType 中的键生成函数（`getKey`）正确生成序列化方法。该函数将获取 Key Members 大端序列化的 128 位 MD5 摘要。

## 18.2.10 包含其他 IDL 文件
可以在 IDL 文件中包含其他 IDL 文件，以使用其中定义的数据类型。_fastrtpsgen_ 为此使用 C/C++ 预处理器，可以使用 `#include` 指令包含 IDL 文件。

_#include "OtherFile.idl" #include <AnotherFile.idl>_ 

如果 _fastrtpsgen_ 在默认系统路径中找不到 C/C++ 预处理器，可以使用参数 `-ppPath` 指定预处理器路径。如果要禁用预处理器，可以使用参数 `-ppDisable`。

## 18.2.11 注解
该应用允许用户按 IDL 4.2 标准定义并使用自己的注解。如果使用了 `-typeobject` 参数，用户注解将传递给生成的 TypeObject 代码。

**@annotation** MyAnnotation { long value; string name; }; 

此外，以下标准注解为内置注解（可识别，并在未实现时传递给 TypeObject）。

|注解|已实现行为|
|---|---|
|@id|未实现。|
|@autoid|未实现。|
|@optional|未实现。|
|@extensibility|未实现。|
|@final|未实现。|
|@appendable|未实现。|
|@mutable|未实现。|
|@position|由 _bitmasks_ 使用。|
|@value|允许为任意元素设置常量值。|
|@key|eProsima `@Key` 注解的别名。|
|@must_understand|未实现。|
|@default_literal|允许在集合中选择一个成员作为默认值。|
|@default|允许指定被注解元素的默认值。|
|@range|未实现。|
|@min|未实现。|
|@max|未实现。|
|@unit|未实现。|
|@bit_bound|允许为 _bitmasks_ 设置大小。|
|@external|未实现。|
|@nested|未实现。|
|@verbatim|未实现。|
|@service|未实现。|
|@oneway|未实现。|
|@ami|未实现。|
|@non_serialized|被注解成员将从序列化中省略。|



大多数未实现的注解与扩展类型有关。

## 18.2.12 IDL 4.2 别名
IDL 4.2 允许为基本类型使用以下名称：


![](fast-dds-docs-eprosima-com-en-v1.10.0_images/fast-dds-docs-eprosima-com-en-v1.10.0.pdf-0211-05.png)


<!-- Start of picture text -->
int8<br>uint8<br>int16<br>uint16<br>int32<br>uint32<br>int64<br>uint64<br><!-- End of picture text -->

## 18.2.13 前向声明
该应用允许前向声明：

struct ForwardStruct; union ForwardUnion; 



![](fast-dds-docs-eprosima-com-en-v1.10.0_images/fast-dds-docs-eprosima-com-en-v1.10.0.pdf-0212-01.png)


<!-- Start of picture text -->
<br>struct ForwardStruct<br>{<br>ForwardUnion fw_union;<br>};<br>union ForwardUnion switch (long)<br>{<br>case 0:<br>ForwardStruct fw_struct;<br>default:<br>string empty;<br>};<br><!-- End of picture text -->

如示例所示，这允许声明相互依赖的结构体、union 等。

# 第 19 章：1.10.0 版
本发行版新增以下功能：

- 新增内置 _共享内存传输（SHM）_。

- 重构传输 API，以支持定位器迭代器。

- 新增 subscriber API，用于检索第一个未取走样本的信息。

- 新增参数，可完全避免动态分配。

- 内置端点的 History 可以配置。

- 升级到 FastCDR v1.0.13。

- 升级到 Fast-RTPS-Gen v1.0.4。

- 要求 CMake 3.5，但使用 3.13 的策略。

本发行版还包括以下缺陷修复和改进：

- 修复参数列表的对齐问题。

- 修复发送超过 256 个分片时的错误。

- 修复 `STRICT_REALTIME` 的处理。

- 修复最后一个 `data_frag` 的 `submessage_size` 计算。

- 解决使用相同 GUID 重新创建 publishing participant 时的问题。

- 解决 publisher 已发送大量消息后，与新 subscriber（后加入者）匹配时可能在写入上长时间阻塞的问题。

- 正确处理多个样本的 Lifespan 同时到期的情况。

- 解决无 reader 的 writer 在活跃性方面的若干问题。

- 正确从有键 Topic 的 History 中移除变更。

- 当样本无法容纳时不再复用缓存变更。

- 修复 `wait_until` 自定义方法在时间已经过去时的问题。

- 修复若干数据竞争和 ABBA 锁问题。

- 降低 CPU 和内存使用量。

- 降低活跃性测试的不稳定性。

- 支持更多性能测试用例。

发现服务器的若干缺陷修复：

- 修复本地主机通信。

- 正确裁剪服务器 History。

- 修复备份服务器操作。

- 修复时序问题。

**注意：** 如果从低于 1.7.0 的版本升级，**必须**使用 _fastrtpsgen_ 从 IDL 文件重新生成源代码。如果从低于 1.10.0 的版本升级，_建议_ 重新生成代码。

# 19.1 以前的版本
## 19.1.1 1.9.4 版
本发行版新增以下功能：

- 进程内投递机制现在默认启用。

- 同步 writer 现在允许发送分片。

- History 池新增 `DYNAMIC_RESERVE` 内存模式。

- 性能测试现在可在 Windows 和 Mac 上运行。

- 新增 requester 和 replier 的 XML 配置。

本发行版还包括以下缺陷修复和改进：

- 升级到 FastCDR v1.0.12。

- 升级到 Fast-RTPS-Gen v1.0.3。

- 修复 PDP 与 StatefulReader 之间的死锁。

- 改进定时事件管理中的 CPU 使用和分配。

- 提升 reliable writer 的性能。

- 修复启用进程内投递时的缺陷。

- 减少动态分配和内存占用。

- 改进并修复性能测试。

- 其他较小的缺陷修复和改进。

**注意：** 如果从低于 1.7.0 的版本升级，**必须**使用 _fastrtpsgen_ 从 IDL 文件重新生成源代码。

## 19.1.2 1.9.3 版
本发行版新增以下功能：

- Participant 发现筛选标志。

- 进程内投递机制改为按需启用。

本发行版还包括以下缺陷修复和改进：

- 升级到 Fast-RTPS-Gen v1.0.2。

- 恢复 `PID_TYPE_CONSISTENCY` 与 XTypes 1.1 的兼容性。

- 确保读取参数列表时正确对齐。

- 新增 `CHECK_DOCUMENTATION` _cmake_ 选项。

- `EntityId_t` 和 `GuidPrefix_t` 现在拥有各自的头文件。

- 修复潜在数据竞争和死锁。

- 改进 reader 匹配过程与其 acknack 接收之间调用 `check_acked_status` 的情况。

- `RTPSMessageGroup_t` 实例现在使用线程局部存储。

- 移除 `FragmentedChangePitStop` 管理器。

- 移除 `CacheChange_t` 中的数据分片 vector。

- 仅当第三方选项关闭时才为 TinyXML2 调用 `find_package`。

- 允许 `XMLProfileManager` 方法在未找到配置时不显示错误日志消息。

**注意：** 如果从低于 1.7.0 的版本升级，**必须**使用 _fastrtpsgen_ 从 IDL 文件重新生成源代码。

## 19.1.3 1.9.2 版
本发行版包含以下功能：

- 多次初始 PDP 公告。

- 用于避免内置多播的标志。

本发行版还新增以下缺陷修复和改进：

- 升级到 Fast-RTPS-Gen v1.0.1。

- 升级到 IDL-Parser v1.0.1。

**注意：** 如果从低于 1.7.0 的版本升级，**必须**使用 _fastrtpsgen_ 从 IDL 文件重新生成源代码。

## 19.1.4 1.9.1 版
本发行版包含以下功能：

- Fast-RTPS-Gen 现在是独立项目。

- 头文件 **eClock.h** 现已标记为弃用。

本发行版还新增以下缺陷修复和改进：

- 升级到 FastCDR v1.0.11。

- 修复从源代码安装的文档。

- 修复 WriterProxy 上的断言。

- 修复解析 Parameters 时潜在的 fall-through。

- 移除导致部分 32 位平台编译错误的弃用保护。

- `addTOCDRMessage` 方法现在从 DLL 导出，修复与 Parameters 构造函数相关的问题。

- 通过避免使用 `__Cnd_timedwait` 方法提升 Windows 性能。

- 同时通过 _localhost_ 发送多播，修复已报告的通信问题。

- 修复潜在数据竞争和死锁。

- 消除对 `acceptMsgDirectTo` 的使用。

- 改进 Discovery Server 框架的重连/重建策略。

- 移除未使用的文件夹。

- 恢复 subscriber API。

- 改进 `SequenceNumber_t`。

- 新增 `STRICT_REALTIME` _cmake_ 选项。

- 改进 `SubscriberHistory`。

- 收到远程 participant 的 RTPS 消息时声明 participant 活跃性。

- 修复在 `create_new_change_with_params` 中设置下一个 deadline 事件时的错误。

**注意：** 如果从低于 1.7.0 的版本升级，**必须**使用 _fastrtpsgen_ 从 IDL 文件重新生成源代码。

## 19.1.5 1.9.0 版
本发行版包含以下功能：

- 部分实现分配 QoS。

- 实现 Discovery Server。

- 实现非阻塞调用。

本发行版还新增以下缺陷修复和改进：

- 为 `BitmapRange` 新增滑动窗口。

- 修改未知 writer 的默认行为。

- 为 logger 新增 `Flush()` 方法，确保记录所有信息。

- 新增从 XML 加载 `Duration_t` 的测试。

- 优化移除本地 writer 时的 WLP。

- 更新部分活跃性测试，使其在 Windows 上更稳定。

- 修复 _CMakeLists.txt_ 中安装静态库的问题。

- 修复性能测试，使其可在 RT 内核上运行。

- 修复创建内置协议时的竞态条件。

- 修复在 `fixed_string` 中设置 `nullptr` 的问题。

- 修复 v1.8.1 使用 `-DBUILD_JAVA=ON` 无法构建的问题。

- 修复某些情况下不发送 GAP 消息的问题。

- 修复 Coverity 报告的问题。

- 修复若干内存问题。

- 更新 _fastrtps.repos_ 文件。

- 新增使用 Colcon 构建的文档。

- 如果设置了 `INSTALLER_PLATFORM`，则更改 CMake 配置目录。

- 将 IDL 子模块更新到当前版本。

**注意：** 如果从低于 1.7.0 的版本升级，**必须**使用 _fastrtpsgen_ 从 IDL 文件重新生成源代码。

## 19.1.6 1.8.3 版
本发行版新增以下缺陷修复和改进：

- 修复 `TypeConsistencyEnforcementQosPolicy` 的序列化。

- 升级到 Fast-RTPS-Gen v1.0.2。

- 升级到 IDL-Parser v1.0.1。

**注意：** 如果从低于 1.7.0 的版本升级，**必须**使用 _fastrtpsgen_ 从 IDL 文件重新生成源代码。

## 19.1.7 1.8.2 版
本发行版包含以下功能：

- 修改未知 writer 的默认行为。

- 多次初始 PDP 公告。

- 用于避免内置多播的标志。

- `STRICT_REALTIME` 编译标志。

本发行版还新增以下缺陷修复和改进：

- 修复在固定字符串中设置 `nullptr` 的问题。

- 修复若干情况下不发送 GAP 的问题。

- 解决 _Coverity_ 报告的问题。

- 修复 _fastrtpsgen_ 无法打开 _IDL.g4_ 文件的问题。

- 修复 _AESGCMGMAC_KeyFactory.cpp_ 中的未命名锁。

- 改进 _XMLProfiles_ 示例。

- 多播现在也会通过 _localhost_ 发送。

- _BitmapRange_ 现在实现滑动窗口。

- 改进 _SequenceNumber_t_ 结构体。

- 收到任意 RTPS 消息时现在会声明 participant 活跃性。

- 修复 `RemoteParticipantLeaseDuration` 的泄漏。

- 修改默认值，以改善 _Wi-Fi_ 场景中的行为。

- 改进 _SubscriberHistory_。

- 移除对 `acceptMsgDirectTo` 的使用。

- 改进 _WLP_。

**注意：** 如果从低于 1.7.0 的版本升级，**必须**使用 _fastrtpsgen_ 从 IDL 文件重新生成源代码。

## 19.1.8 1.8.1 版
本发行版包含以下功能：

- 实现 _Liveliness_ QoS。

本发行版还新增以下缺陷修复和改进：

- 修复 History 上的 `get_change`，该问题会在发现期间引发异常。

- 修复 participant 状态公告，该问题会重复发送 `ParticipantBuiltinData`。

- 修复关闭多播 UDP 通道的问题。

- 修复 `SubscriberHistory`、`UDPTransportInterface` 和 `StatefulReader` 中的竞态条件。

- 修复 Windows 上 `Time_t` 中的 `lroundl` 错误。

- 更新 CDR 和 IDL 子模块。

- 生成 `fastrtpsgen.jar` 时使用 Java 1.8 或更高版本。

**注意：** 如果从低于 1.7.0 的版本升级，**必须**使用 _fastrtpsgen_ 从 IDL 文件重新生成源代码。

## 19.1.9 1.8.0 版
本发行版包含以下功能：

- 实现 IDL 4.2。

- 实现 _Deadline_ QoS。

- 实现 _Lifespan_ QoS。

- 实现 _Disable positive acks_ QoS。

- TCP 传输上的安全套接字（_TLS over TCP_）。

本发行版还新增以下改进和缺陷修复：

- 实时性改进：best-effort writer 的非阻塞写入调用、固定大小字符串、固定大小位图、资源受限 vector 等。

- Duration 参数现在使用纳秒。

- 配置 participant mutation tries（参见 _Participant 配置_）。

- 当端点自定义定位器收到值 0 时自动计算端口。

- 白名单现在会过滤非本地地址。

- 优化 stateful writer 的已确认状态检查。

- 当目标为共享库时不再暴露链接库。

- 新增对 Domain ID 的限制。

- UDP 非阻塞发送现在可选，并可通过 XML 配置。

- 修复非确定性测试。

- 修复某些情况下 ReaderProxy History 被错误重新加载的问题。

- 修复 RTPS 域 hostid 可能不唯一的问题。

- 修复租约到期时间不同的 participant 无法重新连接的问题。

### 已知问题
- 使用 TPC 传输时，由于 ASIO 中的缺陷，移除 participant 时有时不会调用回调。

**注意：** 如果从低于 1.7.0 的版本升级，**必须**使用 _fastrtpsgen_ 从 IDL 文件重新生成源代码。

## 19.1.10 1.7.2 版
本发行版修复了一个重要缺陷：

- 使用 KEEP_LAST QoS 的 subscriber 分配限制取自资源限制配置，未考虑 History 深度。

本发行版还包含以下改进：

- 引入 CMake 3.14 候选版本中的 `FindThreads.cmake`，以支持 sanitizer。

- 修复 Gradle 文件格式。

还包括其他次要缺陷修复和性能改进。

**注意：** 如果从低于 1.7.0 的版本升级，**必须**使用 _fastrtpsgen_ 从 IDL 文件重新生成源代码。

## 19.1.11 1.7.1 版
本发行版包含以下功能：

- 日志系统新增 `LogFileConsumer`。

- 处理用于指定默认配置 XML 文件的 `FASTRTPS_DEFAULT_PROFILES_FILE` 环境变量。

- XML 解析器更严格，并改进了错误消息。

它还修复了一些重要缺陷：* 修复 Windows 上所选网络接口相关的发现问题。* 缩短发现时间。* 规避 QNX 系统上 ASIO 的多播问题。* 提升 TCP 传输性能。* 改进仅含 key 的数据子消息处理。

还包括其他次要缺陷修复和性能改进。

### 已知问题
- 使用 KEEP_LAST QoS 的 subscriber 分配限制取自资源限制配置，未考虑 History 深度。

**注意：** 如果从低于 1.7.0 的版本升级，**必须**使用 _fastrtpsgen_ 从 IDL 文件重新生成源代码。

## 19.1.12 1.7.0 版
本发行版包含以下功能：

- _TCP 传输_。

- _动态话题类型_。

- 符合 Security 1.1。

此外还包括缺陷修复、分配和性能改进。

**注意：** 如果从旧版本升级，**必须**使用 _fastrtpsgen_ 从 IDL 文件重新生成源代码。

## 19.1.13 1.6.0 版
本发行版包含以下功能：

- _持久化_。

- 安全访问控制插件 API 和内置 _Access:Permissions_ 插件。

此外还包括缺陷修复。

**注意：** 如果从低于 1.4.0 的版本升级，建议使用 _fastrtpsgen_ 从 IDL 文件重新生成源代码。

## 19.1.14 1.5.0 版
本发行版包含以下功能：

- 通过 XML 配置 Fast RTPS 实体。

- 新增 heartbeat piggyback 支持。

此外还包括缺陷修复。

**注意：** 如果从低于 1.4.0 的版本升级，建议使用 _fastrtpsgen_ 从 IDL 文件重新生成源代码。

## 19.1.15 1.4.0 版
本发行版包含以下内容：

- 新增安全通信。

- 移除所有 Boost 依赖。Fast RTPS 不再使用 Boost 库。

- 新增 Android 兼容性。

- 缺陷修复。

**注意：** 升级到此发行版后，建议使用 _fastrtpsgen_ 从 IDL 文件重新生成源代码。

## 19.1.16 1.3.1 版
本发行版包含以下内容：

- 新增示例，说明如何针对不同应用调整 Fast RTPS。

- 改进对嵌入式 Linux 的支持。

- 缺陷修复。

## 19.1.17 1.3.0 版
本发行版引入多项新功能：

- 无界数组支持：现在可以发送可变大小的数据数组。

- 扩展分片配置：可设置不同于标准 64Kb 限制的消息/分片最大大小。

- 改进日志系统：可获得有关通信系统状态的更多内省信息。

- 静态发现：使用 XML 映射网络，并将发现流量保持在最低水平。

- 稳定性和性能改进：新一轮内置性能测试将使基准测试更简单。

- 支持 ReadTheDocs：改进文档格式，安装手册和用户手册现已在 ReadTheDocs 在线提供。

## 19.1.18 1.2.0 版
本发行版引入两项重要的新功能：

- 流控制器：一种控制可用带宽使用并避免数据突发的机制。控制器允许指定特定时间段内发送的最大数据量，在发送需要分片的大消息时非常有用。

- 发现监听器：用户现在可以订阅发现信息，无需预先了解系统即可动态获知网络中的实体（Topic、Publisher 和 Subscriber）。这支持创建用于检查系统的通用工具。

此外还有：

- 完整 ROS2 支持：Fast RTPS 被 ROS2（Robot Operating System 的即将发布版本）使用。

- 更好的文档：更多内容和示例。

- 改进性能。

- 缺陷修复。
