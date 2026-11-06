<p align="center"><img src="assets/brand/official-logo.png" alt="社区工作者 AI 产品中心" width="320"></p>

# 社区工作者 AI 产品中心

面向社区工作者、网格员、居民委员会工作人员、社会工作者、志愿服务团队和社区治理相关人员的开源与产品目录中心。

本仓库由 [jinlize-tech](https://github.com/jinlize-tech) 管理，统一记录社区工作场景中的免费 Skill、免费专家（Agent）以及付费产品公开介绍。仓库提供产品目录、使用入口、示例和安全说明；GitHub 发布状态不代表 WorkBuddy 平台审核或上架状态。

## 产品体系

当前目录共记录 **100 款产品**：

| 类型 | 数量 | 公开方式 |
|---|---:|---|
| 免费 Skill | 65 | 公开完整源码 |
| 付费 Skill | 8 | 仅公开产品介绍 |
| 免费专家（Agent） | 4 | 公开完整源码 |
| 付费专家（Agent） | 23 | 仅公开产品介绍 |
| **合计** | **100** |  |

付费源码、系统提示词、知识库、正式上传 ZIP 和内部测试证据不在本仓库公开。

## 产品导航

- [100 款产品目录](CATALOG.md)
- [English catalog](CATALOG_EN.md)
- [机器可读产品索引](PRODUCT_INDEX.csv)
- [快速开始](docs/快速开始.md)
- [WorkBuddy 使用指南](docs/WorkBuddy使用指南.md)
- [付费产品公开边界](PAID_PRODUCTS_NOTICE.md)
- [更新记录](CHANGELOG.md)
- [贡献指南](CONTRIBUTING.md)

产品覆盖办公与行政事务、居民服务、网格与基层治理、邻里沟通与调解、社区活动与志愿服务、老年人与重点群体服务、环境卫生与公共空间、物业协作、公益项目与资金管理、数据分析、宣传沟通和内容运营等场景。目录中的分类为项目内导航分类，平台实际类目以 WorkBuddy 当前选项为准。

## 仓库结构

```text
skills/       65 款免费 Skill 源码与使用说明
agents/       4 款免费专家源码与使用说明
paid-skills/  8 款付费 Skill 的公开介绍
paid-agents/  23 款付费专家的公开介绍
prompts/      免费文字工作流提示词
examples/     合成输入与输出示例
docs/         快速开始、平台使用、隐私与安全说明
assets/       项目品牌素材
```

## 安装与使用

1. 免费 Skill：从 `skills/<目录名>/README.md` 选择产品，按同目录的 `USAGE.md` 使用；需要导入 WorkBuddy 时以其当前导入规范为准。
2. 免费专家（Agent）：从 `agents/<目录名>/README.md` 查看用途和文件入口。
3. 其他兼容 AI 工具：可使用 `prompts/` 或产品目录内的通用提示词。
4. 付费产品：仅从 `paid-skills/` 或 `paid-agents/` 查看公开信息；正式获取和使用情况以 WorkBuddy 平台为准。

示例入口：

- [免费 Skill：社区值班日志整理](skills/community-duty-log/README.md)
- [免费专家：志愿服务运营协作助手](agents/community-volunteer-operations-agent-017/README.md)
- [产品目录：付费 Skill](CATALOG.md)

## 状态说明

- 本仓库是产品目录与公开源码仓库，不是 WorkBuddy 审核结果页。
- “本地验证通过”只表示产品在对应测试环境中完成静态检查和调用验证。
- GitHub 开源不等于 WorkBuddy 平台解析、预览、审核或正式上架。
- 平台状态应以 WorkBuddy 后台的当前记录为准。

## 隐私与安全

提交 Issue、示例或贡献内容时，请勿提供真实居民身份证号、完整住址、电话号码、健康信息、儿童信息、家庭情况、正式案件记录或其他非必要个人信息。

使用前请阅读 [社区隐私使用建议](docs/社区隐私使用建议.md) 和 [安全说明](SECURITY.md)。

## 许可与品牌

- 免费 Skill、免费专家及其使用所需源码采用 [Apache License 2.0](LICENSE)。
- 付费产品的公开介绍不构成对其未公开源码、系统提示词或知识库的复制、提取、逆向或再分发授权。
- 项目名称、Logo 和来源标识不随 Apache-2.0 授予商标权，详见 [TRADEMARKS.md](TRADEMARKS.md)。

## 组织

- GitHub 组织：[jinlize-tech](https://github.com/jinlize-tech)
- 本仓库：[community-worker-ai-skills](https://github.com/jinlize-tech/community-worker-ai-skills)
