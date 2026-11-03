---
name: community-mediation-record-028
display_name: "调解过程记录与协议要点"
display_name_en: "Mediation Process Notes and Agreement Checklist"
description: "整理调解参与方、过程意见、自愿协商事项及已达成和未达成内容，形成记录草稿与协议要点核对表。"
description_zh: "整理调解参与方、过程意见、自愿协商事项及已达成和未达成内容，形成记录草稿与协议要点核对表。"
description_en: "Prepares mediation notes and agreement checklists covering participants, positions, voluntary consensus, and unresolved points."
examples_zh:
  - "调解结束后需要整理过程记录"
  - "双方仅部分事项达成一致"
  - "签字前需要核对协议要素"
examples_en:
  - "Use Mediation Process Notes and Agreement Checklist for a 邻里矛盾与沟通调解 task"
  - "Create a structured draft from supplied community materials"
  - "Check evidence, missing information, and authority boundaries before use"
version: "1.0.0"
author: "广州金励泽科技服务有限公司"
---

# 调解过程记录与协议要点

## 何时使用

当用户需要整理调解参与方、过程意见、自愿协商事项及已达成和未达成内容，形成记录草稿与协议要点核对表。时使用。

## 输入条件

优先获取任务对象、时间范围、已核实事实、原始材料、期望输出格式和需要保留的原文。

如果信息不足，应先说明缺少的关键资料；用户要求继续时，只基于已有信息生成可用框架，所有缺失项写“待确认”或“待补充”。

## 工作步骤

1. 确认调解时间、地点、参与方、主持人员和记录来源
2. 分方整理陈述、诉求、让步条件和仍存分歧
3. 只把双方明确同意的事项列为已达成
4. 把待确认、待审批或尚未同意的事项单列
5. 生成记录草稿、协议要点和签署前核对表
6. 提示真实性、自愿性和正式文书要求由有权人员确认

## 输出格式

- 调解基本信息
- 各方意见摘要
- 自愿协商事项
- 已达成事项
- 未达成事项
- 协议要点核对表
- 待人工确认事项

默认使用 Markdown。表格应可复制、可核对。不得用示意数据填补真实业务字段。

## 事实与权限边界

- 不得伪造签名、日期或参与方意见
- 不得将草稿冒充正式法律文书或生效协议
- 不得替任何一方作出承诺
- 不得遗漏重要分歧

## 隐私与安全

- 参与方使用姓名或代号时仍应遵循最小化原则，不记录与调解无关的身份证号、健康和家庭隐私。
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
