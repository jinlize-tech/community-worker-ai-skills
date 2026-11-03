---
name: community-safety-inspection-041
display_name: "社区安全巡查记录整理"
display_name_en: "Community Safety Inspection Recorder"
description: "整理社区安全巡查时间、范围、客观发现、现场情况和后续跟进清单，只做记录与报告草稿。"
description_zh: "整理社区安全巡查时间、范围、客观发现、现场情况和后续跟进清单，只做记录与报告草稿。"
description_en: "Organizes community safety inspection time, scope, observed issues, site conditions, and follow-up lists without professional determinations."
examples_zh:
  - "日常消防通道巡查后整理记录"
  - "公共区域安全隐患上报前整理材料"
  - "交接班需要问题清单"
examples_en:
  - "Use Community Safety Inspection Recorder for a 社区安全与应急协作 task"
  - "Create a structured draft from supplied community materials"
  - "Check evidence, missing information, and authority boundaries before use"
version: "1.0.0"
author: "广州金励泽科技服务有限公司"
---

# 社区安全巡查记录整理

## 何时使用

当用户需要整理社区安全巡查时间、范围、客观发现、现场情况和后续跟进清单，只做记录与报告草稿。时使用。

## 输入条件

优先获取任务对象、时间范围、已核实事实、原始材料、期望输出格式和需要保留的原文。

如果信息不足，应先说明缺少的关键资料；用户要求继续时，只基于已有信息生成可用框架，所有缺失项写“待确认”或“待补充”。

## 工作步骤

1. 确认巡查日期、时段、人员、路线和记录来源
2. 逐项整理直接观察到的事实和现场状态
3. 把判断性描述改写为可核实观察，无法确认的标记待核实
4. 对问题分级仅使用内部记录标签，不冒充专业鉴定
5. 生成报告草稿、转办建议和复查清单

## 输出格式

- 巡查概况
- 对象观发现
- 现场情况
- 已采取措施
- 跟进清单
- 需专业核实事项

默认使用 Markdown。表格应可复制、可核对。不得用示意数据填补真实业务字段。

## 事实与权限边界

- 只做记录和报告，不承担专业安全检查
- 不得认定隐患已整改、违法或责任主体
- 不得替代消防、公安、住建或应急管理部门

## 隐私与安全

- 巡查涉及住户内部情况时，不记录无关个人隐私，照片和住址须按内部制度处理。
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
