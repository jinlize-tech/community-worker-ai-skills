---
name: community-proposal-response-038
display_name: "居民提案分类与回应草稿"
display_name_en: "Resident Proposal Triage and Response Draft"
description: "对居民提案分类、提取核心诉求、标记跨部门协调事项并生成稳妥回应与跟进清单。"
description_zh: "对居民提案分类、提取核心诉求、标记跨部门协调事项并生成稳妥回应与跟进清单。"
description_en: "Classifies resident proposals, extracts requests, flags cross-department coordination, and drafts neutral responses and follow-up lists."
examples_zh:
  - "集中整理居民议事会提案"
  - "需要给居民发送阶段性回应"
  - "识别需要物业或街道协调的提案"
examples_en:
  - "Use Resident Proposal Triage and Response Draft for a 居民议事与社区自治 task"
  - "Create a structured draft from supplied community materials"
  - "Check evidence, missing information, and authority boundaries before use"
version: "1.0.0"
author: "广州金励泽科技服务有限公司"
---

# 居民提案分类与回应草稿

## 何时使用

当用户需要对居民提案分类、提取核心诉求、标记跨部门协调事项并生成稳妥回应与跟进清单。时使用。

## 输入条件

优先获取任务对象、时间范围、已核实事实、原始材料、期望输出格式和需要保留的原文。

如果信息不足，应先说明缺少的关键资料；用户要求继续时，只基于已有信息生成可用框架，所有缺失项写“待确认”或“待补充”。

## 工作步骤

1. 读取提案原文和已确认的处理信息
2. 按设施、环境、服务、活动、治理等主题分类
3. 提取诉求、理由、影响范围和可执行建议
4. 标记社区可处理、需协调和需进一步核实的事项
5. 生成不承诺结果的回应草稿
6. 输出负责人、时限和后续反馈清单

## 输出格式

- 提案分类表
- 核心诉求
- 协调事项
- 回应草稿
- 后续跟进清单
- 待确认事项

默认使用 Markdown。表格应可复制、可核对。不得用示意数据填补真实业务字段。

## 事实与权限边界

- 不得虚构审批结果、工程预算或办理承诺
- 不得用统一模板替代逐项回应
- 不得擅自确定跨部门责任

## 隐私与安全

- 提案人和附议人使用编号，不展示联系方式或家庭情况。
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
