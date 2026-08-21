# Record WorkBuddy Release

这个仓库通过 GitHub Actions 每小时请求一次 WorkBuddy 更新接口，并把返回的多平台版本信息记录到仓库中。

## 最新版本

<!-- workbuddy-latest:start -->
**当前最新版本：`5.3.14.36279234`**

最新平台：macOS Apple Silicon, macOS Intel, Windows x64

| 平台 | 最新版本 | 下载 | SHA256 | 首次记录 |
| --- | --- | --- | --- | --- |
| macOS Apple Silicon | `5.3.14.36279234` **最新** | [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-arm64/WorkBuddy-darwin-arm64-5.3.14.36279234-825709d4.zip) | `a7c18fecd293` | `2026-08-18T06:56:20Z` |
| macOS Intel | `5.3.14.36279234` **最新** | [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-x64/WorkBuddy-darwin-x64-5.3.14.36279234-825709d4.zip) | `25fe856763ff` | `2026-08-18T06:56:20Z` |
| Windows x64 | `5.3.14.36279234` **最新** | [下载](https://download.codebuddy.cn/workbuddy/saas/win32-x64-user/WorkBuddy-win32-x64-user-5.3.14.36279234-825709d4.exe) | - | `2026-08-18T06:56:20Z` |

更新日志：[5.3.14](https://www.codebuddy.cn/docs/workbuddy/Changelog)

- 新增 Markdown AI 编辑快捷键提示，支持 Enter 直接发送、Cmd+Enter 换行
- 优化长期记忆加载与本地助理变量恢复，新建和恢复对话更稳定
- 优化自动化任务高峰期调度，减少集中触发和误判错过执行
- 优化灵感案例访问和做同款流程，提升资源打开、分享口令和覆盖确认体验
- 优化并行灵感任务页面性能，减少任务切换卡顿和历史任务白屏
- 修复多个任务同时提问时回复内容串话的问题
<!-- workbuddy-latest:end -->

## 历史版本

<!-- workbuddy-history:start -->
仅展示最近 10 个版本；完整逐平台历史记录见 `data/releases.json`。 另有 23 个更早版本未在 README 展开。

| 版本 | 平台下载 | 更新日志 | 接口时间戳 | 首次记录 |
| --- | --- | --- | --- | --- |
| `5.3.14.36279234` | macOS Apple Silicon: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-arm64/WorkBuddy-darwin-arm64-5.3.14.36279234-825709d4.zip)<br>macOS Intel: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-x64/WorkBuddy-darwin-x64-5.3.14.36279234-825709d4.zip)<br>Windows x64: [下载](https://download.codebuddy.cn/workbuddy/saas/win32-x64-user/WorkBuddy-win32-x64-user-5.3.14.36279234-825709d4.exe) | 新增 Markdown AI 编辑快捷键提示，支持 Enter 直接发送、Cmd+Enter 换行 | `1787002434` | `2026-08-18T06:56:20Z` |
| `5.3.13.35923969` | macOS Apple Silicon: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-arm64/WorkBuddy-darwin-arm64-5.3.13.35923969-20fd9da5.zip)<br>macOS Intel: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-x64/WorkBuddy-darwin-x64-5.3.13.35923969-20fd9da5.zip)<br>Windows x64: [下载](https://download.codebuddy.cn/workbuddy/saas/win32-x64-user/WorkBuddy-win32-x64-user-5.3.13.35923969-20fd9da5.exe) | 新增灵感「一键做同款」，支持快速套版复刻网页 | `1786647169` | `2026-08-14T11:51:33Z` |
| `5.3.12.35805101` | macOS Apple Silicon: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-arm64/WorkBuddy-darwin-arm64-5.3.12.35805101-a981f41f.zip)<br>macOS Intel: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-x64/WorkBuddy-darwin-x64-5.3.12.35805101-a981f41f.zip)<br>Windows x64: [下载](https://download.codebuddy.cn/workbuddy/saas/win32-x64-user/WorkBuddy-win32-x64-user-5.3.12.35805101-a981f41f.exe) | 新增灵感分享口令，可复制口令给他人并直达对应灵感详情 | `1786528301` | `2026-08-12T10:14:49Z` |
| `5.3.11.35348084` | macOS Apple Silicon: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-arm64/WorkBuddy-darwin-arm64-5.3.11.35348084-45487630.zip)<br>macOS Intel: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-x64/WorkBuddy-darwin-x64-5.3.11.35348084-45487630.zip)<br>Windows x64: [下载](https://download.codebuddy.cn/workbuddy/saas/win32-x64-user/WorkBuddy-win32-x64-user-5.3.11.35348084-45487630.exe) | 新增对话出错时「检查网络」快捷入口，网络异常可一键跳转诊断 | `1786071284` | `2026-08-10T04:46:24Z` |
| `5.3.8.34705286` | macOS Apple Silicon: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-arm64/WorkBuddy-darwin-arm64-5.3.8.34705286-e9991e2b.zip)<br>macOS Intel: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-x64/WorkBuddy-darwin-x64-5.3.8.34705286-e9991e2b.zip)<br>Windows x64: [下载](https://download.codebuddy.cn/workbuddy/saas/win32-x64-user/WorkBuddy-win32-x64-user-5.3.8.34705286-e9991e2b.exe) | 优化 macOS 文件系统，修复长期间使用下的性能问题 | `1785428486` | `2026-08-01T09:11:30Z` |
| `5.3.5.34189228` | macOS Apple Silicon: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-arm64/WorkBuddy-darwin-arm64-5.3.5.34189228-8044e898.zip)<br>macOS Intel: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-x64/WorkBuddy-darwin-x64-5.3.5.34189228-8044e898.zip)<br>Windows x64: [下载](https://download.codebuddy.cn/workbuddy/saas/win32-x64-user/WorkBuddy-win32-x64-user-5.3.5.34189228-8044e898.exe) | Buddy AI 国内升配（订阅计费） | `1784912428` | `2026-07-25T07:24:18Z` |
| `5.3.3.33961208` | macOS Apple Silicon: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-arm64/WorkBuddy-darwin-arm64-5.3.3.33961208-5801cce5.zip)<br>macOS Intel: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-x64/WorkBuddy-darwin-x64-5.3.3.33961208-5801cce5.zip)<br>Windows x64: [下载](https://download.codebuddy.cn/workbuddy/saas/win32-x64-user/WorkBuddy-win32-x64-user-5.3.3.33961208-5801cce5.exe) | 新增项目计划板块重构升级，支持待办富文本编辑、评论图片粘贴上传与动态留言 | `1784684408` | `2026-07-23T07:39:57Z` |
| `5.2.6.33159827` | macOS Apple Silicon: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-arm64/WorkBuddy-darwin-arm64-5.2.6.33159827-8ee6bc11.zip)<br>macOS Intel: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-x64/WorkBuddy-darwin-x64-5.2.6.33159827-8ee6bc11.zip)<br>Windows x64: [下载](https://download.codebuddy.cn/workbuddy/saas/win32-x64-user/WorkBuddy-win32-x64-user-5.2.6.33159827-8ee6bc11.exe) | 新增助理配额上限六档套餐文案与端内升级弹窗，权益变更更透明 | `1783883027` | `2026-07-14T09:11:05Z` |
| `5.2.5.32793105` | macOS Apple Silicon: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-arm64/WorkBuddy-darwin-arm64-5.2.5.32793105-1067a2de.zip)<br>macOS Intel: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-x64/WorkBuddy-darwin-x64-5.2.5.32793105-1067a2de.zip)<br>Windows x64: [下载](https://download.codebuddy.cn/workbuddy/saas/win32-x64-user/WorkBuddy-win32-x64-user-5.2.5.32793105-1067a2de.exe) | 稳定性增加 | `1783516305` | `2026-07-08T14:33:31Z` |
| `5.2.3.32357678` | macOS Apple Silicon: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-arm64/WorkBuddy-darwin-arm64-5.2.3.32357678-3865830d.zip)<br>macOS Intel: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-x64/WorkBuddy-darwin-x64-5.2.3.32357678-3865830d.zip)<br>Windows x64: [下载](https://download.codebuddy.cn/workbuddy/saas/win32-x64-user/WorkBuddy-win32-x64-user-5.2.3.32357678-3865830d.exe) | 新增模型夜间折扣展示，费用信息更透明 | `1783080878` | `2026-07-07T05:00:30Z` |
<!-- workbuddy-history:end -->

默认接口模板：

```text
https://www.codebuddy.cn/v2/update?platform={platform}
```

默认平台来自 WorkBuddy 官网下载页当前使用的参数：

```text
workbuddy-darwin-arm64
workbuddy-darwin-x64
workbuddy-win32-x64-user
```

## 记录文件

- `README.md`：顶部自动展示“最新版本”和精简后的“历史版本”摘要，方便直接在 GitHub 项目首页查看。
- `data/releases.json`：历史版本记录。脚本会按 `platform + sha256hash` 去重；如果没有 `sha256hash`，则使用 `platform + version + productVersion + url` 去重。
- `data/latest.json`：最近一次发生写入时，各平台的接口返回内容和记录时间。
- `data/changelog.json`：从官方 WorkBuddy 更新日志解析出的版本说明缓存，只保留已记录版本对应的条目。

每条历史记录包含：

- `releaseKey`：去重键。
- `platform`：接口请求使用的平台参数。
- `firstSeenAt`：第一次记录到该版本的 UTC 时间。
- `lastSeenAt`：当前与 `firstSeenAt` 相同，保留这个字段方便以后扩展为持续观测。
- `release`：接口原始返回内容。
- `source`：本次记录对应的接口 URL。

## GitHub Actions

工作流文件位于 `.github/workflows/record-workbuddy-release.yml`。

- 每小时自动运行一次。
- 支持在 GitHub Actions 页面手动运行。
- 只有发现新版本时才会写入文件并自动提交，避免每小时重复提交相同内容。

## 本地运行

```bash
python scripts/record_workbuddy_release.py
```

可以临时指定平台：

```bash
python scripts/record_workbuddy_release.py \
  --platform workbuddy-darwin-arm64 \
  --platform workbuddy-darwin-x64 \
  --platform workbuddy-win32-x64-user
```

也可以通过环境变量覆盖配置，多个平台用英文逗号分隔：

```bash
WORKBUDDY_PLATFORMS="workbuddy-darwin-arm64,workbuddy-darwin-x64,workbuddy-win32-x64-user" \
WORKBUDDY_UPDATE_URL_TEMPLATE="https://www.codebuddy.cn/v2/update?platform={platform}" \
WORKBUDDY_CHANGELOG_URL="https://www.codebuddy.cn/docs/workbuddy/Changelog" \
WORKBUDDY_RECORD_PATH="data/releases.json" \
WORKBUDDY_LATEST_PATH="data/latest.json" \
WORKBUDDY_CHANGELOG_PATH="data/changelog.json" \
WORKBUDDY_README_HISTORY_LIMIT="10" \
python scripts/record_workbuddy_release.py
```
