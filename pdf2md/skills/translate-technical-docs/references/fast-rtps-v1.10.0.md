# Fast RTPS 1.10.0 文档专有特征

## 目录

- [适用边界](#适用边界)
- [产品名与版本](#产品名与版本)
- [双 API 层](#双-api-层)
- [实体与数据单位](#实体与数据单位)
- [QoS 语义](#qos-语义)
- [发现与匹配](#发现与匹配)
- [传输与端口](#传输与端口)
- [动态类型与 IDL](#动态类型与-idl)
- [XML 配置](#xml-配置)
- [安全、持久化与实时性](#安全持久化与实时性)
- [翻译时的版本保护](#翻译时的版本保护)

## 适用边界

仅当翻译本仓库的 _FastRTPS Documentation, Release 1.10.0_ 时读取本文件。它记录该手册独有的概念边界、命名方式和易混淆关系。

不要把它当成所有 DDS/Fast DDS 版本的通用说明。较新版本可能已经更名、重构 API 或改变默认行为；除非原文明确说明，不要用新版本知识补充旧手册。

## 产品名与版本

- 原文同时使用 `eProsima Fast RTPS`、`Fast RTPS`、`Fast-RTPS` 和 `FastRTPS`。这些形式通常都是产品名，按上下文保留原拼写。
- 本手册标题是 `FastRTPS Documentation`，版本是 `Release 1.10.0`。不要自动改写成较新的 `Fast DDS` 产品名。
- 1.10.0 仍大量使用 `Publisher`、`Subscriber`、`Participant`、`RTPSDomain` 和 `RTPSParticipant` 等名称。不要替换成新版本才有的 API 名称。
- 版本升级说明中的强制要求只适用于它声明的版本范围。例如，从 1.7.0 之前的版本升级时必须用 `fastrtpsgen` 重新生成 IDL 源文件；从 1.10.0 之前的版本升级则是建议重新生成。

## 双 API 层

该手册反复区分两个层次，翻译时不要把它们合并成同一个“发布订阅层”：

| 高层 | 低层 | 译文中的区分 |
| --- | --- | --- |
| Publisher-Subscriber Layer | Writer-Reader Layer | “发布者-订阅者层” / “写入者-读取者层” |
| Domain | RTPSDomain | 保留类型名 `Domain`、`RTPSDomain` |
| Participant | RTPSParticipant | 高层“参与者”；低层保留 `RTPSParticipant` |
| Publisher | RTPSWriter | 高层“发布者”；低层“RTPS 写入者（RTPSWriter）” |
| Subscriber | RTPSReader | 高层“订阅者”；低层“RTPS 读取者（RTPSReader）” |

高层隐藏 History 的创建与管理；低层直接暴露 `WriterHistory`、`ReaderHistory`、`WriterAttributes`、`ReaderAttributes` 和 `CacheChange_t`。凡原文讨论 history cache、change 释放或 endpoint 配置时，优先确认它说的是低层 API。

## 实体与数据单位

- `Change` 是 Topic 数据的一次更新；低层由 `CacheChange_t` 表示。译作“变更（Change）”或保留 `Change`，不要一律译成普通的“修改”。
- `Sample` 是发布或接收的一次数据值。译作“样本”，不要译成“样品”。
- `Instance` 是由 key 区分的长期数据对象，一个 instance 可以对应多个 sample。译作“实例”，不要译成“例子”。
- `History` 是保存 change/sample 的缓存或队列。按上下文译作“历史缓存（History）”或保留 `History`。
- `Payload` 是 change 中的序列化数据，译作“负载”或“数据负载”，不要译成“有效载荷”以外的泛化含义。
- `Writer` 和 `Reader` 在低层是 RTPS endpoint；`Publisher` 和 `Subscriber` 是高层的容器实体。不要交叉替换。
- `TopicDataType`、`DynamicPubSubType`、`TypeSupport` 是类型支持对象或类型名，保留原标识符。

## QoS 语义

### Reliability

- `Best-Effort`：尽力而为，不确认到达，可能丢包。
- `Reliable`：可靠，期望收到确认并支持重传。
- 本手册的兼容矩阵规定：Best-Effort publisher 不能匹配 Reliable subscriber；Reliable publisher 可以匹配两种 subscriber。翻译兼容性描述时不要反向推断。

### History 与资源

- `KEEP_LAST`：只保留最近一定数量的样本，由 `depth` 限制。
- `KEEP_ALL`：尽量保留并交付全部样本。
- `Resource Limits` 控制样本、实例和每个实例样本等资源上限。
- 不要把 `depth` 译成“历史长度”后忽略它和 `max_samples_per_instance` 的约束关系。

### Durability

- `VOLATILE`：后加入的 reader 只接收匹配后产生的新样本。
- `TRANSIENT_LOCAL`：writer 为后加入的 reader 保留并补发最近的历史样本。
- `TRANSIENT`：历史写入持久化存储，writer 或进程重启后仍可恢复。
- `Durability` 不是普通的“耐久性”，也不是 `Persistence` 的同义词。`TRANSIENT` 依赖持久化机制。

### 时间与存活

- `Deadline`：发布侧要求应用按期提供新样本，订阅侧要求按期收到新样本；报告的是期限违约。
- `Lifespan`：样本从写入开始的最长有效时间；过期后从 History 删除。
- `Liveliness`：判断实体是否仍然存活。`AUTOMATIC`、`MANUAL_BY_PARTICIPANT`、`MANUAL_BY_TOPIC` 的检测范围不同。
- `Lease Duration`：多久没有收到某 participant 的流量就认为它不再存活。不要和 `Liveliness` 的发布侧 `announcement_period` 混为一体。

### 所有权、分区与其他策略

- `Ownership` 区分 `SHARED` 和 `EXCLUSIVE`；`Ownership Strength` 只对具备相应所有权语义的 writer 有意义。
- `Partition` 是 Domain 内部、Endpoint 级别的逻辑隔离层。它不同于 Topic，也不同于 Domain。
- Partition 属于 Endpoint，不属于 Change；切换 Partition 不会改写既有 History。
- Partition 通配符遵循 POSIX `fnmatch`；`*` 不匹配默认的无名 Partition。
- `Disable Positive ACKs` 只减少正向确认流量，不等于关闭可靠传输；reader 使用它而 writer 未使用时，两者不匹配。

## 发现与匹配

发现和匹配是不同阶段：

1. `PDP`（Participant Discovery Phase）发现 participant。SIMPLE 模式下具体协议是 `SPDP`。
2. `EDP`（Endpoint Discovery Phase）交换 endpoint 的 Topic 和数据类型信息。SIMPLE 模式下具体协议是 `SEDP`。

不要误写成本手册“用 SEDP 发现 participant”。SEDP 负责 endpoint discovery；SPDP 负责 participant discovery。

本手册列出的发现机制：

- `SIMPLE`：默认机制，SPDP + SEDP。
- `STATIC`：保留 PDP，使用 XML 静态描述远程 endpoint，关闭 SEDP 元流量。
- `SERVER` / `CLIENT` / `BACKUP`：中心化发现。客户端通过 server 的 `GuidPrefix` 和 locator 连接。
- `NONE`：Manual Discovery，仅适用于 `RTPSDomain` 层；禁用 PDP，因此也没有正常的 EDP 自动发现。

关键关系：

- `metatraffic` 是发现和管理流量，`user traffic` 是业务数据流量；发现配置只直接控制前者。
- `GuidPrefix` 是 participant 的 RTPS 标识，不是普通 IP 地址。
- `BACKUP` 是带数据库的 server，备份的是客户端发现信息，不是应用数据。
- Server 与 Client 是发现角色，不限制它们同时创建 publisher/subscriber；TCP Server/Client 是传输连接角色，又是另一组概念。
- `Initial Peers` 扩展 PDP 公告的发送目标；配置后仍要检查是否同时禁用了不需要的 multicast。

## 传输与端口

- 本版本实现 UDPv4、UDPv6、TCPv4、TCPv6 和 SHM 五种传输。
- 默认同时启用 SHM 和 UDPv4；同机 participant 之间优先自动使用 SHM。
- `Locator` 描述地址和传输定位信息，不要译成 HTTP 意义上的“链接”。
- `unicast` 是单播，`multicast` 是多播，不要混用“广播”。
- 端口由 port base、domain gain、participant gain 和 offset 计算；翻译公式和常量时保持原样。
- `Metatraffic` 与 `User` 的 multicast/unicast locator 是不同集合，不能互换。
- TCP 需要先建立连接；TCP Server/Client 只描述连接建立方式，与 RTPS Publisher/Writer 角色无关。
- `Intra-process delivery` 是进程内投递，不等于 SHM；本版本默认 `FULL`，可配置为 `USER_DATA_ONLY` 或 `OFF`。
- `Flow Controller` 限制发送速率，常用于大消息、视频或避免压垮慢 subscriber。

## 动态类型与 IDL

静态类型和动态类型是两条路径，都最终为 Topic 提供可序列化的数据类型：

- 静态路径通过 IDL 定义，再由 `fastrtpsgen` 生成 C++ 类型和可选示例。
- 动态路径通过 `DynamicTypeBuilderFactory`、`DynamicType`、`DynamicData` 和 `DynamicPubSubType` 在运行时创建和操作类型。
- `TypeObject`、`TypeIdentifier` 和 `TypeLookup` 用于动态类型发现与端点类型匹配；不要将其解释为用户业务数据。
- `loan_value` 取得库管理的内部对象指针，必须用 `return_loaned_value` 归还；不要译成“贷款”。
- `bitset` 是位字段集合，`bitmask` 是位标志集合，二者不要互换。
- `union` 同一时间只有一个成员有效，由 discriminator 选择；不能译成普通结构体。
- keyed topic 必须在配置中启用 `WITH_KEY`，否则 key 定义不会自动产生有键 Topic 的效果。

## XML 配置

本手册大量使用“C++ 配置 + XML profile”双写。翻译时保留 XML 标签、属性、枚举值、profile 名和 `transport_id`：

- 常见层级为 `<dds>` → `<profiles>` → `<participant>` / `<publisher>` / `<subscriber>`。
- participant 的主体配置位于 `<rtps>` 下，发现设置位于 `<builtin>` → `<discovery_config>`。
- endpoint 的 Topic、QoS、locator、times、properties 和 allocation 各有独立层级。
- `<topic>` 中的 `<name>` 是 Topic 名；participant 的 `<name>` 是 participant 名；`profile_name` 是 profile 引用名。三者不能混译。
- `DURATION_INFINITY`、`KEEP_LAST`、`BEST_EFFORT`、`SIMPLE` 等是配置值，保留原文和大小写。
- 全量 XML 示例可能包含互斥或无效组合，原文明确说它不是可直接工作的配置；不要把它说成推荐模板。

## 安全、持久化与实时性

- 安全默认不编译；启用时使用 CMake 选项 `-DSECURITY=ON`。
- 三个安全层次分别是 authentication、access control 和 cryptographic protection。不要把 authentication 译成“授权”。
- `SIGN` 与 `ENCRYPT` 是保护类别；不要把所有保护设置都描述成“加密”。
- 持久化默认关闭。启用至少涉及 `TRANSIENT` durability、非零 `persistence_guid` 和 persistence plugin。
- 本版本内置持久化插件是 `PERSISTENCE:SQLITE3`；同一 SQLite 文件不能被两个进程同时使用。
- 实时配置需要 `-DSTRICT_REALTIME=ON`，重点是初始化后避免动态内存分配，并为阻塞调用设置最大阻塞时间。
- `PREALLOCATED`、`PREALLOCATED_WITH_REALLOC`、`DYNAMIC`、`DYNAMIC_REUSABLE` 是 History 内存策略，不要只译成“预分配”；需保留它们的内存占用与分配次数差异。

## 翻译时的版本保护

- 原文出现旧的类名、路径、方法名或配置键时，先核对 1.10.0 语境，不要“纠正”为新版命名。
- 原文明确区分 Publisher/Subscriber 与 Writer/Reader 时，译文也必须保持区分。
- 原文使用 `class`、`struct`、`enum`、`bitset`、`bitmask`、`union` 时，保留类型系统含义。
- 原文描述匹配条件、兼容矩阵、默认值、版本升级要求时，保留强制程度和适用范围。
- 遇到 `may`、`should`、`only`、`unless`，不要根据 DDS 常识改写成更强或更弱的结论。
- PDF 提取造成的断词、页眉、页脚和代码换行可以清理；API 名、XML 标签、枚举值、端口公式和证书字段保持原样。
