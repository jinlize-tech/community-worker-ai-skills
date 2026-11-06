<p align="center"><img src="assets/brand/official-logo.png" alt="Community Worker AI Product Center" width="320"></p>

# Community Worker AI Product Center

An open-source and product catalog center for community workers, grid staff, resident committee staff, social workers, volunteer teams, and community governance practitioners.

This repository is maintained by [jinlize-tech](https://github.com/jinlize-tech). It indexes free Skills, free Agents, and public overviews of paid products for community-service scenarios. A GitHub release or public repository is not evidence that a product has passed WorkBuddy review or been published on WorkBuddy.

## Product system

The catalog currently lists **100 products**:

| Type | Count | Public scope |
|---|---:|---|
| Free Skills | 65 | Full source code |
| Paid Skills | 8 | Public overview only |
| Free Agents | 4 | Full source code |
| Paid Agents | 23 | Public overview only |
| **Total** | **100** |  |

Paid source code, system prompts, knowledge bases, submission ZIP files, and private test evidence are not published in this repository.

## Catalog and usage links

- [Chinese catalog](CATALOG.md)
- [English catalog](CATALOG_EN.md)
- [Machine-readable product index](PRODUCT_INDEX.csv)
- [Quick start (Chinese)](docs/快速开始.md)
- [WorkBuddy guide (Chinese)](docs/WorkBuddy使用指南.md)
- [Paid-product publication boundary](PAID_PRODUCTS_NOTICE.md)
- [Changelog](CHANGELOG.md)
- [Contributing](CONTRIBUTING.md)

The catalog covers administrative work, resident services, grid and grassroots governance, neighborhood communication and mediation, community events and volunteering, services for older adults and priority groups, public-space management, property coordination, charitable projects and funds, data analysis, public communication, and content operations. Catalog categories are navigation aids; WorkBuddy platform categories must be checked against the current platform options.

## Repository layout

```text
skills/       65 free Skill source packages and usage notes
agents/       4 free Agent source packages and usage notes
paid-skills/  Public overviews for 8 paid Skills
paid-agents/  Public overviews for 23 paid Agents
prompts/      Free text-workflow prompts
examples/     Synthetic input and output examples
docs/         Quick start, platform, privacy, and safety guidance
assets/       Project brand assets
```

## Installation and use

1. Free Skills: select a product from `skills/<directory>/README.md`, then follow its `USAGE.md`. Follow the current WorkBuddy import specification when importing a Skill.
2. Free Agents: start from `agents/<directory>/README.md` for the product purpose and file entry points.
3. Other compatible AI tools: use the files in `prompts/` or the general prompts included in a product directory.
4. Paid products: use `paid-skills/` or `paid-agents/` only for public product information. Availability and access are determined by WorkBuddy.

Examples:

- [Free Skill: Community Duty Log](skills/community-duty-log/README.md)
- [Free Agent: Volunteer Operations Assistant](agents/community-volunteer-operations-agent-017/README.md)
- [Full product catalog](CATALOG_EN.md)

## Status

- This repository is a product catalog and public-source repository, not a WorkBuddy review-result page.
- “Local validation passed” only means that the relevant product passed static and invocation checks in its test environment.
- Public GitHub availability does not imply WorkBuddy parsing, preview, review, or release approval.
- Current platform status must be checked in the WorkBuddy backend.

## Privacy and safety

Do not submit real resident identifiers, full addresses, phone numbers, health information, child data, family details, official case records, or other unnecessary personal information in issues, examples, or contributions.

Read the [community privacy guidance](docs/社区隐私使用建议.md) and [security policy](SECURITY.md) before use.

## License and brand

- Free Skill and free Agent source code is licensed under [Apache License 2.0](LICENSE).
- Public paid-product overviews do not grant permission to copy, extract, reverse engineer, or redistribute unpublished source code, system prompts, or knowledge bases.
- Project names, logos, and source identifiers are not granted as trademarks under Apache-2.0. See [TRADEMARKS.md](TRADEMARKS.md).

## Organization

- GitHub organization: [jinlize-tech](https://github.com/jinlize-tech)
- This repository: [community-worker-ai-skills](https://github.com/jinlize-tech/community-worker-ai-skills)
