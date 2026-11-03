---
name: community-emergency-supplies-045
display_name: "应急物资清单与检查表"
display_name_en: "Emergency Supplies Inventory Checklist"
description: "整理应急物资名称、实际库存、存放位置、检查日期和缺口，生成可核对的检查表。"
description_zh: "整理应急物资名称、实际库存、存放位置、检查日期和缺口，生成可核对的检查表。"
description_en: "Creates checklists for emergency supply names, actual stock, storage locations, inspection dates, and shortages."
examples_zh:
  - "季度应急物资盘点"
  - "汛前检查社区储备"
  - "交接时需要库存清单"
examples_en:
  - "Use Emergency Supplies Inventory Checklist for a 社区安全与应急协作 task"
  - "Create a structured draft from supplied community materials"
  - "Check evidence, missing information, and authority boundaries before use"
version: "1.0.0"
author: "广州金励泽科技服务有限公司"
---

# 应急物资清单与检查表

## 何时使用

当用户需要整理应急物资名称、实际库存、存放位置、检查日期和缺口，生成可核对的检查表。时使用。

## 输入条件

优先获取任务对象、时间范围、已核实事实、原始材料、期望输出格式和需要保留的原文。

如果信息不足，应先说明缺少的关键资料；用户要求继续时，只基于已有信息生成可用框架，所有缺失项写“待确认”或“待补充”。

## 工作步骤

1. 确认盘点日期、范围、盘点和复核人员
2. 按物资名称记录实盘数量、单位、存放位置和状态记录
3. 用计划数或配置数对照形成缺口，不把缺测当零
4. 标记过期、损坏或待专业检查的物资
5. 生成检查表、补充建议和复核任务

## 输出格式

- 盘点范围
- 物资库存表
- 缺口清单
- 存放位置
- 检查发现
- 补充与复核任务

默认使用 Markdown。表格应可复制、可核对。不得用示意数据填补真实业务字段。

## 事实与权限边界

- 不得虚构库存和专业合格结论
- 不得把数量记录等同于质量检测
- 不得覆盖原始盘点记录

## 隐私与安全

- 库存信息只保留物资管理所需字段，不录入无关人员信息。
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
