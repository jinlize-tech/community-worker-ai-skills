<p align="center"><img src="assets/brand/official-logo.png" alt="金励泽科技" width="360"></p>

# 社区工作者 AI Skill 开源工具集

面向社区工作者、网格员、居民委员会工作人员、社区社工和志愿服务组织者的免费 AI 文本工作流集合。

本仓库包含 15 款标准 Skill、可复制的通用提示词、模板、示例和使用指南。它们帮助整理记录、起草材料、规划活动和做隐私最小化检查，不连接政府业务系统，也不代替正式审批、执法、医疗诊断或救助资格认定。

## 15 款免费 Skill

| 产品 | 分类 | 标准 Skill | 其他 AI 工具提示词 |
|---|---|---|---|
| 社区值班日志整理 | 办公效率 / 文档处理 | [进入](skills/community-duty-log/README.md) | [通用提示词](prompts/community-duty-log.md) |
| 社区周报月报与数据摘要 | 办公效率 / 文档处理 | [进入](skills/community-work-summary/README.md) | [通用提示词](prompts/community-work-summary.md) |
| 社区通知公告生成 | 办公效率 / 文档处理 | [进入](skills/community-notice/README.md) | [通用提示词](prompts/community-notice.md) |
| 居民诉求接待记录整理 | 居民服务 / 诉求接待与回访 | [进入](skills/resident-request-record/README.md) | [通用提示词](prompts/resident-request-record.md) |
| 居民诉求分类与转办建议 | 居民服务 / 诉求接待与回访 | [进入](skills/resident-request-routing/README.md) | [通用提示词](prompts/resident-request-routing.md) |
| 居民回访记录与满意度摘要 | 居民服务 / 诉求接待与回访 | [进入](skills/resident-followup-summary/README.md) | [通用提示词](prompts/resident-followup-summary.md) |
| 网格走访记录整理 | 基层工作管理 / 网格走访与事项跟踪 | [进入](skills/grid-visit-record/README.md) | [通用提示词](prompts/grid-visit-record.md) |
| 网格巡查问题上报单 | 基层工作管理 / 网格走访与事项跟踪 | [进入](skills/grid-issue-report/README.md) | [通用提示词](prompts/grid-issue-report.md) |
| 楼栋/网格事项交接清单 | 基层工作管理 / 网格走访与事项跟踪 | [进入](skills/grid-handover/README.md) | [通用提示词](prompts/grid-handover.md) |
| 社区活动方案生成 | 活动策划 / 志愿服务与现场执行 | [进入](skills/community-event-plan/README.md) | [通用提示词](prompts/community-event-plan.md) |
| 活动流程单与主持串词 | 活动策划 / 志愿服务与现场执行 | [进入](skills/event-hosting-script/README.md) | [通用提示词](prompts/event-hosting-script.md) |
| 志愿者排班与岗位分工 | 活动策划 / 志愿服务与现场执行 | [进入](skills/volunteer-scheduling/README.md) | [通用提示词](prompts/volunteer-scheduling.md) |
| 老年人上门关怀清单 | 生活服务 / 老年关怀与数字助老 | [进入](skills/elderly-visit-checklist/README.md) | [通用提示词](prompts/elderly-visit-checklist.md) |
| 老年人探访记录脱敏整理 | 生活服务 / 老年关怀与数字助老 | [进入](skills/elderly-visit-privacy/README.md) | [通用提示词](prompts/elderly-visit-privacy.md) |
| 老年人智能手机教学步骤 | 生活服务 / 老年关怀与数字助老 | [进入](skills/elderly-smartphone-guide/README.md) | [通用提示词](prompts/elderly-smartphone-guide.md) |

## 直接使用

1. **支持 Skill 的客户端**：进入对应 `skills/<产品名>/`，按 `USAGE.md` 导入或使用 `SKILL.md`。
2. **WorkBuddy**：打开 [WorkBuddy 使用指南](docs/WorkBuddy使用指南.md)，按平台界面导入或安装。
3. **其他 AI 工具**：打开 `prompts/<产品名>.md` 或 Skill 目录中的 `通用提示词.md`，复制到 ChatGPT、DeepSeek、豆包、通义千问等文本对话工具，再粘贴材料。

不同平台对原生 Skill 文件、文件上传和自定义指令的支持不同，以各平台当前规则为准。

## 隐私优先

不要向公开仓库、Issue、讨论区或外部 AI 工具提交真实居民身份证号、完整住址、电话、健康病史、家庭情况或其他非必要个人信息。使用前请阅读 [社区隐私使用建议](docs/社区隐私使用建议.md)。

## 开源与品牌

- 免费 Skill、提示词、模板和文档采用 [Apache License 2.0](LICENSE)。
- 金励泽科技名称、Logo 和项目来源标识不随 Apache-2.0 授予商标或商业使用授权，详见 [TRADEMARKS.md](TRADEMARKS.md)。
- 商标和品牌文件适用范围见 [assets/brand/README.md](assets/brand/README.md)。

## 贡献

欢迎提交脱敏、合成的社区工作示例和文档改进。请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 和 [SECURITY.md](SECURITY.md)，不要提交真实居民资料、凭据或未授权内容。
