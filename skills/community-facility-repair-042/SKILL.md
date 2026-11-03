---
name: community-facility-repair-042
display_name: "公共设施问题报修转办单"
display_name_en: "Public Facility Repair Referral Form"
description: "记录路灯、电梯、道路和公共区域设施问题，生成报修内容、转办记录和后续回访事项。"
description_zh: "记录路灯、电梯、道路和公共区域设施问题，生成报修内容、转办记录和后续回访事项。"
description_en: "Records public facility issues and creates repair requests, referral records, and follow-up items for lights, elevators, roads, and shared areas."
examples_zh:
  - "夜间路灯损坏需要报修"
  - "电梯异常需要转交物业"
  - "道路破损需要跟踪处理"
examples_en:
  - "Use Public Facility Repair Referral Form for a 社区安全与应急协作 task"
  - "Create a structured draft from supplied community materials"
  - "Check evidence, missing information, and authority boundaries before use"
version: "1.0.0"
author: "广州金励泽科技服务有限公司"
---

# 公共设施问题报修转办单

## 何时使用

当用户需要记录路灯、电梯、道路和公共区域设施问题，生成报修内容、转办记录和后续回访事项。时使用。

## 输入条件

优先获取任务对象、时间范围、已核实事实、原始材料、期望输出格式和需要保留的原文。

如果信息不足，应先说明缺少的关键资料；用户要求继续时，只基于已有信息生成可用框架，所有缺失项写“待确认”或“待补充”。

## 工作步骤

1. 确认设施类型、位置、发现时间、现象和已知联系人
2. 描述可观察问题，不擅自判断技术原因
3. 生成简洁报修内容和优先级说明
4. 登记转办对象、工单号和反馈状态
5. 生成回访时间点、复查标准和待确认项

## 输出格式

- 报修基本信息
- 问题描述
- 转办记录
- 安全提示
- 回访事项
- 待确认信息

默认使用 Markdown。表格应可复制、可核对。不得用示意数据填补真实业务字段。

## 事实与权限边界

- 不得虚构工单号、维修结果或责任单位
- 不得判断设备合格、故障原因或维修费用
- 紧急风险应提示立即联系有权单位

## 隐私与安全

- 报修单不附居民完整联系方式和无关家庭信息；必要时使用值班电话。
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
