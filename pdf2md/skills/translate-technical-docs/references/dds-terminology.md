# DDS、RTPS 与 Fast DDS 术语

## 目录

- [使用原则](#使用原则)
- [核心实体](#核心实体)
- [数据模型](#数据模型)
- [通信与发现](#通信与发现)
- [QoS 术语](#qos-术语)
- [可靠性状态与样本状态](#可靠性状态与样本状态)
- [类型、序列化与互操作](#类型序列化与互操作)
- [常见误译](#常见误译)

## 使用原则

DDS 文档中的类型名、实体名和 API 名通常保留英文。第一次出现时给出中文解释，之后优先沿用英文标识符，避免中文译名与代码对象混淆。

默认写法示例：

- `DataWriter`：首次写“数据写入者（DataWriter）”，后文写 `DataWriter`。
- `Best Effort`：首次写“尽力而为（Best Effort）”，后文可保留 `Best Effort`。
- `QoS`：首次写“服务质量（Quality of Service，QoS）”，后文写 QoS。
- `Reliable`：作为 QoS 策略值时保留英文；作为普通形容词可译“可靠的”。

不要把 `publisher` 与 `Publisher`、`participant` 与 `DomainParticipant` 混为一谈。普通名词可以翻译，正式 DDS 实体名应保留英文。

## 核心实体

| 英文 | 建议译法 | 说明 |
| --- | --- | --- |
| DDS | 数据分发服务（DDS） | Data Distribution Service，以数据为中心的发布/订阅中间件规范 |
| RTPS | 实时发布订阅协议（RTPS） | Real-Time Publish-Subscribe Protocol，DDS 的互操作线协议 |
| Fast DDS | Fast DDS | 产品名，不翻译 |
| Fast RTPS | Fast RTPS | 旧产品名或历史语境，不翻译 |
| DomainParticipant | 域参与者（DomainParticipant） | 加入 DDS 域的实体，管理 Publisher、Subscriber 和 Topic |
| Publisher | 发布者（Publisher） | 管理 DataWriter 的发布侧容器实体 |
| Subscriber | 订阅者（Subscriber） | 管理 DataReader 的订阅侧容器实体 |
| DataWriter | 数据写入者（DataWriter） | 向某个 Topic 发布数据的实体 |
| DataReader | 数据读取者（DataReader） | 从某个 Topic 接收数据的实体 |
| Topic | 话题（Topic） | 绑定名称和数据类型的数据流抽象 |
| Entity | 实体（Entity） | DDS 对象总称，如 participant、writer、reader |
| Endpoint | 端点（Endpoint） | DataWriter 或 DataReader 的统称 |
| Listener | 监听器（Listener） | 接收实体状态或数据事件回调的对象 |
| Condition | 条件（Condition） | 用于等待和触发处理逻辑的状态对象 |
| WaitSet | 等待集（WaitSet） | 等待一个或多个 Condition 的机制 |

实体关系可以简写为：

```text
DomainParticipant
├── Publisher -> DataWriter
└── Subscriber -> DataReader
```

## 数据模型

| 英文 | 建议译法 | 说明 |
| --- | --- | --- |
| Domain | 域（Domain） | 使用 domain ID 隔离的逻辑通信范围 |
| Domain ID | 域 ID | 通常保留数字，不翻译为“域编号 ID” |
| Type | 类型 | 结合上下文可指应用数据类型或 DDS 类型 |
| Data Type | 数据类型 | Topic 上传输的数据结构 |
| Instance | 实例 | 由 key 区分的具体数据对象 |
| Sample | 样本 | 某个实例在某一时刻发布的数据值 |
| Key | 键 | 标识实例的字段或字段组合 |
| Keyed Topic | 有键话题 | 支持多个实例的话题 |
| Unkeyed Topic | 无键话题 | 整个话题只有一个实例 |
| Type Support | 类型支持 | 负责类型注册、序列化和相关操作的支持对象 |
| Dynamic Type | 动态类型 | 运行时定义或操作的类型 |
| Member | 成员 | 类型定义中的字段；不要一律译成“会员” |

区分三个容易混淆的词：

- **Topic** 是数据流的概念。
- **Sample** 是一次发布或接收的数据值。
- **Instance** 是被 key 标识的长期数据对象，可对应多个 sample。

## 通信与发现

| 英文 | 建议译法 | 说明 |
| --- | --- | --- |
| Publish / Subscribe | 发布 / 订阅 | 通信模型 |
| Discovery | 发现 | 自动寻找 participant、endpoint 和类型信息的过程 |
| Simple Discovery | 简单发现 | Fast DDS 的默认发现机制 |
| Discovery Server | 发现服务器 | 集中式发现部署方式 |
| Initial Peers | 初始对等节点 | 用于启动发现的已知地址 |
| Built-in Endpoint | 内置端点 | DDS 自动创建的管理端点 |
| SPDP | 参与者发现协议（SPDP） | Simple Participant Discovery Protocol |
| SEDP | 端点发现协议（SEDP） | Simple Endpoint Discovery Protocol |
| Locator | 定位器（Locator） | 描述网络地址和传输定位信息 |
| Transport | 传输 | UDP、TCP、共享内存等通信机制 |
| Shared Memory | 共享内存 | 传输方式，缩写 SHM 首次出现应展开 |
| Multicast | 多播 | 不要与“广播”混用 |
| Unicast | 单播 | 点对点传输 |
| GUID | 全局唯一标识符（GUID） | DDS 实体或端点的全局标识 |
| Participant GUID | 参与者 GUID | 保留 GUID |
| Endpoint GUID | 端点 GUID | 保留 GUID |

## QoS 术语

QoS 策略名是 API 概念，通常保留英文：

| 英文 | 建议解释 |
| --- | --- |
| Quality of Service (QoS) | 服务质量，控制可靠性、持久性、时限等通信行为 |
| Reliability | 可靠性策略 |
| Best Effort | 尽力而为，不保证重传 |
| Reliable | 可靠，提供重传与确认机制 |
| Durability | 持久性策略，决定后加入的 reader 能否收到旧数据 |
| Volatile | 易失的，默认通常只接收加入后发布的数据 |
| Transient Local | 本地瞬态，为后加入的 reader 保留一定历史数据 |
| Transient | 瞬态 |
| Persistent | 持久 |
| History | 历史策略，控制保留最新样本还是全部样本 |
| Keep Last | 仅保留最近的指定数量 |
| Keep All | 保留全部可用样本 |
| Depth | 深度，历史队列中保留的样本数量 |
| Resource Limits | 资源限制 |
| Deadline | 截止时间 |
| Lifespan | 生存期 |
| Liveliness | 活跃性 |
| Ownership | 所有权 |
| Ownership Strength | 所有权强度 |
| Partition | 分区 |
| Presentation | 呈现策略 |
| Destination Order | 目标顺序 |
| Time Based Filter | 基于时间的过滤 |
| Content Filtered Topic | 内容过滤话题 |

不要把 `Durability` 一律译成“耐久性”，也不要把 `Lifespan` 译成“生命周期”。DDS 中它们表达特定 QoS 语义。

## 可靠性状态与样本状态

| 英文 | 建议译法 | 说明 |
| --- | --- | --- |
| Acknowledged | 已确认 | reader 已确认收到 |
| Unacknowledged | 未确认 | 不要译成“未被发现” |
| Sample Rejected | 样本被拒绝 | 通常由资源限制导致 |
| Sample Lost | 样本丢失 | reader 侧观察到样本未到达 |
| Instance State | 实例状态 | Alive、Not Alive、Disposed |
| Alive | 存活 | 实例仍有效 |
| Not Alive | 非存活 | 实例暂无有效数据 |
| Disposed | 已处置 | 数据实例被显式处置 |
| View State | 视图状态 | New、Not New |
| New | 新 | reader 首次看到该实例 |
| Not New | 非新 | 已见过该实例 |
| Sample State | 样本状态 | Read、Not Read |
| Read | 已读 | 应用已访问该样本 |
| Not Read | 未读 | 应用尚未访问该样本 |

状态值出现在 API 或枚举中时保留英文，在解释性正文中可写成“`ALIVE`（存活）”。

## 类型、序列化与互操作

| 英文 | 建议译法 | 说明 |
| --- | --- | --- |
| IDL | 接口定义语言（IDL） | Interface Definition Language |
| IDL Type | IDL 类型 | 保留 IDL |
| XTypes | 扩展类型系统（XTypes） | DDS-XTypes 规范 |
| Type Object | 类型对象 | 描述类型的运行期表示 |
| Type Identifier | 类型标识符 | 用于类型匹配 |
| Serialization | 序列化 | 不要译成“串联” |
| Deserialization | 反序列化 | 从字节流恢复对象 |
| CDR | 公共数据表示（CDR） | Common Data Representation |
| Wire Protocol | 线协议 | 网络传输协议 |
| Interoperability | 互操作性 | 不同实现之间协同工作的能力 |
| Compatibility | 兼容性 | 数据交换是否可行 |
| Request / Reply | 请求 / 应答 | 不要固定译成“请求 / 回复” |
| RPC | 远程过程调用（RPC） | Remote Procedure Call |

## 常见误译

| 原文 | 避免译法 | 更合适的处理 |
| --- | --- | --- |
| `may` | 永远译成“必须” | 根据语境译“可能”或“可以” |
| `should` | 永远译成“必须” | 通常译“应”或“应当” |
| `subscriber`（普通概念） | 订阅服务器 | 通常是“订阅者” |
| `subscriber`（DDS 实体） | 订阅器 | 保留 `Subscriber`，首次解释为“订阅者” |
| `participant` | 参加者 | DDS 语境用“参与者”或保留 `DomainParticipant` |
| `endpoint` | 终端 | DDS 语境用“端点” |
| `sample` | 样品 | DDS 语境用“样本” |
| `instance` | 例子 | DDS 语境用“实例” |
| `key` | 关键词 | 数据模型语境用“键” |
| `liveliness` | 活泼度 | 用“活跃性” |
| `lifespan` | 生命线 | 用“生存期” |
| `dispose` | 丢弃 | 数据实例语境用“处置” |
| `lost` | 遗漏 | 样本状态语境用“丢失” |
