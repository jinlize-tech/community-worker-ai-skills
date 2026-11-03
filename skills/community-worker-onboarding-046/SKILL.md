---
name: community-worker-onboarding-046
display_name: "新入职社区工作者上岗清单"
display_name_en: "New Community Worker Onboarding Checklist"
description: "为新入职社区工作者生成首周上岗清单、首月学习计划、岗位职责、常用材料和带教检查表。"
description_zh: "为新入职社区工作者生成首周上岗清单、首月学习计划、岗位职责、常用材料和带教检查表。"
description_en: "Creates first-week onboarding and first-month learning plans, role duties, common materials, and mentoring checklists."
examples_zh:
  - "新员工第一天报到"
  - "社区建立带教计划"
  - "转岗人员需要快速熟悉岗位"
examples_en:
  - "Use New Community Worker Onboarding Checklist for a 社区工作者培训与能力提升 task"
  - "Create a structured draft from supplied community materials"
  - "Check evidence, missing information, and authority boundaries before use"
version: "1.0.0"
author: "广州金励泽科技服务有限公司"
---

# 新入职社区工作者上岗清单

## 何时使用

当用户需要为新入职社区工作者生成首周上岗清单、首月学习计划、岗位职责、常用材料和带教检查表。时使用。

## 输入条件

优先获取任务对象、时间范围、已核实事实、原始材料、期望输出格式和需要保留的原文。

如果信息不足，应先说明缺少的关键资料；用户要求继续时，只基于已有信息生成可用框架，所有缺失项写“待确认”或“待补充”。

## 工作步骤

1. 确认岗位方向、入职日期、工作范围和带教负责人
2. 区分通用入职事项和岗位专属事项
3. 生成首周任务、首月学习目标和材料清单
4. 设置观察点、带教反馈和完成状态
5. 标记必须由社区负责人确认的制度与权限

## 输出格式

- 岗位与对象
- 首周清单
- 首月计划
- 岗位职责
- 常用材料
- 带教检查表
- 待确认事项

默认使用 Markdown。表格应可复制、可核对。不得用示意数据填补真实业务字段。

## 事实与权限边界

- 不得虚构社区内部制度、权限或正式岗位文件
- 不得把通用建议冒充本社区制度
- 不得替代入职审批与人事决定

## 隐私与安全

- 培训清单不收集新员工家庭、健康等与岗位无关的信息。
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
