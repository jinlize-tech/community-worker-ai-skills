---
name: community-publicity-factcheck-035
display_name: "社区宣传材料事实核对清单"
display_name_en: "Community Publicity Fact-Check Checklist"
description: "核查宣传稿中的数字、时间、地点、机构名称和政策依据，识别夸大或绝对化表达并给出修改建议。"
description_zh: "核查宣传稿中的数字、时间、地点、机构名称和政策依据，识别夸大或绝对化表达并给出修改建议。"
description_en: "Checks numbers, dates, locations, organization names, and policy references in community publicity while flagging exaggeration."
examples_zh:
  - "发布活动通知前核对关键信息"
  - "居民群宣传稿引用数据"
  - "政策宣传材料需要二次复核"
examples_en:
  - "Use Community Publicity Fact-Check Checklist for a 宣传通知与政策解读 task"
  - "Create a structured draft from supplied community materials"
  - "Check evidence, missing information, and authority boundaries before use"
version: "1.0.0"
author: "广州金励泽科技服务有限公司"
---

# 社区宣传材料事实核对清单

## 何时使用

当用户需要核查宣传稿中的数字、时间、地点、机构名称和政策依据，识别夸大或绝对化表达并给出修改建议。时使用。

## 输入条件

优先获取任务对象、时间范围、已核实事实、原始材料、期望输出格式和需要保留的原文。

如果信息不足，应先说明缺少的关键资料；用户要求继续时，只基于已有信息生成可用框架，所有缺失项写“待确认”或“待补充”。

## 工作步骤

1. 读取待核对稿件和可用的原始依据
2. 逐项提取数字、时间、地点、机构、政策和引用
3. 对每个事实标记已核实、有冲突或待核实
4. 识别夸大、绝对化和无依据承诺
5. 给出最小修改建议并列出必须人工确认的项目

## 输出格式

- 核对范围
- 事实核对表
- 冲突与缺口
- 夸大或绝对化表达
- 修改建议
- 待确认事项

默认使用 Markdown。表格应可复制、可核对。不得用示意数据填补真实业务字段。

## 事实与权限边界

- 不得在无原始依据时给出已核实结论
- 不得为了让文稿顺畅而编造数字或引文
- 不得替代主管部门政策审核

## 隐私与安全

- 核对材料中如含真实居民信息，应采用编号或删除非必要字段。
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
