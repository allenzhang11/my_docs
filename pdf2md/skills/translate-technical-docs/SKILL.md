---
name: translate-technical-docs
description: Translate English technical documentation, programming manuals, API references, READMEs, specifications, and PDF-derived Markdown into accurate, beginner-friendly Simplified Chinese while preserving meaning, structure, code, identifiers, links, warnings, and normative language. Use when the user asks for faithful Chinese translation, bilingual alignment, jargon explanation, study notes, or translation of professional English material for junior programmers.
---

# 技术文档通俗翻译

## 目标

把英文技术文档翻译成初级程序员容易理解的中文，同时完整保留原文的技术含义。

优先级固定为：

1. **忠实**：不增加、删除、弱化或强化原文信息。
2. **完整**：不漏段落、列表、条件、限制、警告、代码和交叉引用。
3. **通俗**：把长句拆成中文逻辑，首次出现的术语给中文解释。
4. **简洁**：不堆砌译注，不重复解释简单内容。

不得为了“读起来顺”而省略限定条件、改变责任主体、混淆因果或把可能说成必然。

## 默认交付

除用户另有要求，采用“忠实中文正文 + 必要辅助信息”：

1. 保留原文档的标题层级、章节顺序、表格、列表、图片、链接、公式和代码块。
2. 正文完整翻译为简体中文，不把翻译改成摘要。
3. 代码、命令、路径、URL、文件名、API 名、配置键、类名、函数名、版本号和字面字符串保持不变。
4. 技术术语首次出现时写成“中文（English）”，后续保持同一译法；代码中直接使用的标识符保留英文。
5. 对较长的复杂章节，可在正文前添加一行 `> **本节速览（非原文）**：...`。
6. 对真正容易误解的术语、歧义或隐含背景，使用 `> **译注**：...`；译注不得混入正文冒充原文。
7. 在文档末尾增加“术语对照”表，仅收录本文反复出现或容易误解的术语。

用户要求“双语对照”时，按原文段落与译文段落交替排列；要求“学习版”时，在忠实译文之外增加速览、术语和少量理解提示；不得因此删减正文。

## 工作流

### 1. 识别输入与范围

- 确认文件格式、章节范围、目标读者和是否有术语表。
- 对 PDF，先取得可靠文本或 Markdown。检查页数、目录、代码块和图片是否完整；文本层缺失时先说明，不要凭空补写。
- 对超长文档，按章节或 800-1500 个英文单词分段；不要一次处理整本手册。
- 明确本轮翻译范围，未翻译部分要明确标出，不能假装已完成。

### 2. 建立上下文

- 先读目录、前言、术语表、警告和 2-3 个代表段落后再开始翻译。
- 先浏览下一节标题和首段，避免把跨段句子、代词或列表拆错。
- 建立临时术语表，记录固定译法、缩写、产品名和代码标识符。
- 处理 DDS、RTPS、Fast DDS/Fast RTPS 文档时，读取
  [references/dds-terminology.md](references/dds-terminology.md)。
- 处理本仓库的 _FastRTPS Documentation, Release 1.10.0_ 时，另读
  [references/fast-rtps-v1.10.0.md](references/fast-rtps-v1.10.0.md)。

### 3. 忠实翻译

- 以段落或列表项为最小单位，逐句确认主语、动作、对象、条件、范围和时态。
- 先保证技术关系正确，再调整中文语序。
- 保留 `must / should / may / can / must not` 等情态动词的强度差异。
- 保留 `only / unless / except / at least / at most / not necessarily` 等限定词。
- 把英文长句拆成多个中文句子时，显式保留因果、转折、条件和指代关系。
- 不擅自把被动改主动；只有动作执行者明确时才改写。
- 表格逐格翻译；代码、枚举值、配置项和单位保持原样。

### 4. 通俗化改写

- 第一次出现的关键术语给简短中文解释，不展开成百科。
- 把名词堆叠拆成“谁对谁做什么”；必要时补充“也就是说”。
- 用具体动作替代空泛表达，但不得改变技术范围。
- 类比只能帮助理解，且必须与原文一致；不确定时不用类比。
- 不把原文的“可能”改成“会”，不把“通常”改成“总是”，不把“应”改成“必须”。

### 5. 回查与交付

每一段完成后回查：

- 数字、版本、单位、否定词和情态动词是否一致。
- 列表项、条件分支、警告和交叉引用是否齐全。
- 术语是否前后一致，代词指代是否清楚。
- 代码、命令、链接和图片路径是否原样保留。
- 译注是否与正文清楚分开。

处理 Markdown 文件时，运行：

```bash
python scripts/check_markdown_translation.py source.md translated.md
```

该脚本只能检查结构不变量，不能替代语义审校。存在警告时逐项人工确认；使用 `--strict` 可把警告视为失败。

交付时说明：翻译了哪些范围、采用的术语、尚未确认之处，以及输出文件路径。

## 关键判断

- **歧义**：选择与上下文最一致的解释；无法排除另一种解释时，正文按最可能含义翻译，并加译注列出风险。
- **原文错误**：保留原意并加译注说明疑似错误，不擅自修正事实。
- **过时内容**：照实翻译，可加 `> **译注**：该行为在较新版本中可能已变化。`，不得编造新版本细节。
- **产品名与缩写**：首次给出全称和中文解释，之后保留常用英文名，例如 DDS、RTPS、QoS、IDL。
- **代码注释**：默认保持代码块原样；需要解释时，在代码块外用中文说明，不改写代码内容。
- **表格与目录**：优先保持可用结构；PDF 提取造成的断行、连字符和重复页眉可以清理，但要保留信息。
- **图片**：保留原链接和相对路径；可翻译 alt 文本，但不替换图片文件。
- **不确定内容**：标记为待确认，不用流畅措辞掩盖不确定性。

## 输出格式

推荐结构：

```markdown
> **本节速览（非原文）**：用一两句话说明本节解决什么问题。

## 原文章节标题（中文翻译）

忠实翻译的正文。

> **译注**：只解释容易误解之处。
```

不要每段都加快览或译注。简单命令、普通 API 参数和直白说明直接翻译即可。

## 质量红线

- 不摘要代替翻译，除非用户明确要求摘要。
- 不省略“必须、不得、仅、除非、至少、默认、已弃用”等限制。
- 不翻译代码标识符、命令参数或配置键。
- 不把多个列表项合并成一段。
- 不凭常识补充原文没有的版本、行为或结论。
- 不把译注写成正文的一部分。

## 资源

- 详细规则、情态动词映射和难句处理：阅读
  [references/translation-rules.md](references/translation-rules.md)。
- DDS/RTPS/Fast DDS 术语：阅读
  [references/dds-terminology.md](references/dds-terminology.md)。
- Fast RTPS 1.10.0 文档专有概念和版本边界：阅读
  [references/fast-rtps-v1.10.0.md](references/fast-rtps-v1.10.0.md)。
- Markdown 结构与代码保真检查：运行
  `scripts/check_markdown_translation.py`。
