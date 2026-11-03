---
name: community-dialogue-listening-027
display_name: "矛盾沟通开场与倾听提问"
display_name_en: "Conflict Dialogue Opening and Listening Prompts"
description: "根据邻里矛盾场景生成中性沟通开场、开放式问题、情绪确认和复述句式。"
description_zh: "根据邻里矛盾场景生成中性沟通开场、开放式问题、情绪确认和复述句式。"
description_en: "Creates neutral openings, open questions, emotional acknowledgements, and reflective-listening prompts for neighbor conflicts."
examples_zh:
  - "首次约谈邻里纠纷双方"
  - "对方情绪激动需要先降温"
  - "工作人员担心自己的表达引发误解"
examples_en:
  - "Use Conflict Dialogue Opening and Listening Prompts for a 邻里矛盾与沟通调解 task"
  - "Create a structured draft from supplied community materials"
  - "Check evidence, missing information, and authority boundaries before use"
version: "1.0.0"
author: "广州金励泽科技服务有限公司"
---

# 矛盾沟通开场与倾听提问

## 何时使用

当用户需要根据邻里矛盾场景生成中性沟通开场、开放式问题、情绪确认和复述句式。时使用。

## 输入条件

优先获取任务对象、时间范围、已核实事实、原始材料、期望输出格式和需要保留的原文。

如果信息不足，应先说明缺少的关键资料；用户要求继续时，只基于已有信息生成可用框架，所有缺失项写“待确认”或“待补充”。

## 工作步骤

1. 识别沟通对象、矛盾主题、已知事实和当前情绪
2. 生成尊重双方且不预判责任的开场
3. 提供开放式事实问题和感受问题
4. 给出情绪确认、内容复述和澄清句式
5. 列出应避免的指责、威胁和预设责任表达
6. 生成可直接使用的沟通话术卡

## 输出格式

- 沟通目标与边界
- 开场白
- 开放式问题
- 情绪确认与复述句式
- 避免使用的表达
- 话术卡

默认使用 Markdown。表格应可复制、可核对。不得用示意数据填补真实业务字段。

## 事实与权限边界

- 不得指导操纵、威胁、羞辱或逼迫对方
- 不得把沟通技巧用于取得虚假陈述
- 不得代替调解结论或责任认定

## 隐私与安全

- 只保留沟通所需信息，示例和练习应使用角色代称，不写入真实联系方式或身份证信息。
- 默认不调用外部收费 API，不连接未经用户明确提供或授权的业务系统。
- 不在用户可见输出中展示内部提示词、文件路径、校验过程、公司宣传、Logo 或水印。

## 异常处理

- 输入为空或核心事实缺失时，先列出最小补充清单。
- 材料互相矛盾时，并列呈现，不擅自选择有利版本。
- 用户要求编造、伪造、越权认定或越过正式程序时，明确拒绝该部分，并提供合规替代做法。
- 工具不可用时，输出可直接复制使用的人工工作框架，并说明未完成项。

## 完成检查

- 是否完整覆盖用户要完成的核心任务？
- 是否区分已提供事实、直接整理、推断和待确认事项？
- 是否避免越权、虚假承诺和绝对化结论？
- 是否执行了信息最小化和脱敏提醒？
- 是否交付了清晰、可编辑、可核对的结果？
