---
name: community-resident-meeting-036
display_name: "居民议事会议程与材料"
display_name_en: "Resident Deliberation Agenda and Materials"
description: "围绕居民议事主题生成会议背景、讨论问题、议程、记录框架和准备清单。"
description_zh: "围绕居民议事主题生成会议背景、讨论问题、议程、记录框架和准备清单。"
description_en: "Creates meeting background, discussion questions, agenda, minutes framework, and preparation checklist for resident deliberation."
examples_zh:
  - "组织召开楼栋公共空间改造议事会"
  - "需要让居民围绕明确问题讨论"
  - "会前准备材料和记录模板"
examples_en:
  - "Use Resident Deliberation Agenda and Materials for a 居民议事与社区自治 task"
  - "Create a structured draft from supplied community materials"
  - "Check evidence, missing information, and authority boundaries before use"
version: "1.0.0"
author: "广州金励泽科技服务有限公司"
---

# 居民议事会议程与材料

## 何时使用

当用户需要围绕居民议事主题生成会议背景、讨论问题、议程、记录框架和准备清单。时使用。

## 输入条件

优先获取任务对象、时间范围、已核实事实、原始材料、期望输出格式和需要保留的原文。

如果信息不足，应先说明缺少的关键资料；用户要求继续时，只基于已有信息生成可用框架，所有缺失项写“待确认”或“待补充”。

## 工作步骤

1. 确认议事主题、召集主体、参会对象、时间和目标
2. 整理已核实背景、待决事项和不可越过的规则
3. 把议题拆成可讨论的问题并标注决策权归属
4. 设计议程、时间分配和记录框架
5. 生成会前材料清单、会后跟进栏和人工核对项

## 输出格式

- 会议基本信息
- 背景材料
- 讨论问题
- 议程表
- 会议记录框架
- 会前准备清单
- 决策边界

默认使用 Markdown。表格应可复制、可核对。不得用示意数据填补真实业务字段。

## 事实与权限边界

- 不得预设表决结果或宣称会议已经通过
- 不得替居民议事组织作最终决定
- 不得虚构参会人员、预算或政策依据

## 隐私与安全

- 参会名单如需提供，应使用岗位、楼栋或编号，不公开与议题无关的个人信息。
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
