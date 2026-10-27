# Record WorkBuddy Release

这个仓库通过 GitHub Actions 每小时请求一次 WorkBuddy 更新接口，并把返回的多平台版本信息记录到仓库中。

## 最新版本

<!-- workbuddy-latest:start -->
**当前最新版本：`5.9.3.42398134`**

最新平台：macOS Apple Silicon, macOS Intel, Windows x64

| 平台 | 最新版本 | 下载 | SHA256 | 首次记录 |
| --- | --- | --- | --- | --- |
| macOS Apple Silicon | `5.9.3.42398134` **最新** | [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-arm64/WorkBuddy-darwin-arm64-5.9.3.42398134-d4692421.zip) | `55d73c63e44b` | `2026-10-27T19:59:39Z` |
| macOS Intel | `5.9.3.42398134` **最新** | [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-x64/WorkBuddy-darwin-x64-5.9.3.42398134-d4692421.zip) | `e093e214cb77` | `2026-10-27T19:59:39Z` |
| Windows x64 | `5.9.3.42398134` **最新** | [下载](https://download.codebuddy.cn/workbuddy/saas/win32-x64-user/WorkBuddy-win32-x64-user-5.9.3.42398134-d4692421.exe) | `b5edb52bd6c5` | `2026-10-27T19:59:39Z` |

更新日志：[5.9.3](https://www.codebuddy.cn/docs/workbuddy/Changelog)

- 修复从其他设备迁移数据时仅能全量导入、无法按分类选择且超大数据无法迁移的问题，导入上限调整为 100GB
- 修复 Windows 升级时因安装目录校验导致升级检查失败的问题
- 修复重启后历史会话使用的模型被误回退到其他模型的问题
- 修复打开已有长会话任务时会话区偶现崩溃、提示「出错了」的问题
- 修复 Windows 升级后 sandbox 初始化失败导致所有工具执行报错的问题
- 修复 Windows 静默升级后新进程未能继承完整环境变量、导致部分功能异常的问题
<!-- workbuddy-latest:end -->

## 历史版本

<!-- workbuddy-history:start -->
仅展示最近 10 个版本；完整逐平台历史记录见 `data/releases.json`。 另有 36 个更早版本未在 README 展开。

| 版本 | 平台下载 | 更新日志 | 接口时间戳 | 首次记录 |
| --- | --- | --- | --- | --- |
| `5.9.3.42398134` | macOS Apple Silicon: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-arm64/WorkBuddy-darwin-arm64-5.9.3.42398134-d4692421.zip)<br>macOS Intel: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-x64/WorkBuddy-darwin-x64-5.9.3.42398134-d4692421.zip)<br>Windows x64: [下载](https://download.codebuddy.cn/workbuddy/saas/win32-x64-user/WorkBuddy-win32-x64-user-5.9.3.42398134-d4692421.exe) | 修复从其他设备迁移数据时仅能全量导入、无法按分类选择且超大数据无法迁移的问题，导入上限调整为 100GB | `1793121334` | `2026-10-27T19:59:39Z` |
| `5.8.3.41334564` | macOS Apple Silicon: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-arm64/WorkBuddy-darwin-arm64-5.8.3.41334564-db0e9b51.zip)<br>macOS Intel: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-x64/WorkBuddy-darwin-x64-5.8.3.41334564-db0e9b51.zip)<br>Windows x64: [下载](https://download.codebuddy.cn/workbuddy/saas/win32-x64-user/WorkBuddy-win32-x64-user-5.8.3.41334564-db0e9b51.exe) | 修复内置运行时随版本切换时同步弹出闪屏的问题 | `1792057764` | `2026-10-16T16:30:54Z` |
| `5.8.2.41111488` | macOS Apple Silicon: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-arm64/WorkBuddy-darwin-arm64-5.8.2.41111488-b8f6c953.zip)<br>macOS Intel: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-x64/WorkBuddy-darwin-x64-5.8.2.41111488-b8f6c953.zip)<br>Windows x64: [下载](https://download.codebuddy.cn/workbuddy/saas/win32-x64-user/WorkBuddy-win32-x64-user-5.8.2.41111488-b8f6c953.exe) | 修复部分历史会话因消息异常或内容过大而无法打开的问题 | `1791834688` | `2026-10-14T06:03:03Z` |
| `5.7.7.40774747` | macOS Apple Silicon: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-arm64/WorkBuddy-darwin-arm64-5.7.7.40774747-2e8619da.zip)<br>macOS Intel: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-x64/WorkBuddy-darwin-x64-5.7.7.40774747-2e8619da.zip)<br>Windows x64: [下载](https://download.codebuddy.cn/workbuddy/saas/win32-x64-user/WorkBuddy-win32-x64-user-5.7.7.40774747-2e8619da.exe) | 优化成长计划体验问题 | `1791497947` | `2026-10-09T08:51:12Z` |
| `5.7.6.40409493` | macOS Apple Silicon: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-arm64/WorkBuddy-darwin-arm64-5.7.6.40409493-306add2a.zip)<br>macOS Intel: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-x64/WorkBuddy-darwin-x64-5.7.6.40409493-306add2a.zip)<br>Windows x64: [下载](https://download.codebuddy.cn/workbuddy/saas/win32-x64-user/WorkBuddy-win32-x64-user-5.7.6.40409493-306add2a.exe) | 海外版新增 Gmail 连接器，完成授权后可直接读取和发送邮件 | `1791132693` | `2026-10-06T10:04:53Z` |
| `5.6.2.39298511` | macOS Apple Silicon: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-arm64/WorkBuddy-darwin-arm64-5.6.2.39298511-37a65c0b.zip)<br>macOS Intel: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-x64/WorkBuddy-darwin-x64-5.6.2.39298511-37a65c0b.zip)<br>Windows x64: [下载](https://download.codebuddy.cn/workbuddy/saas/win32-x64-user/WorkBuddy-win32-x64-user-5.6.2.39298511-37a65c0b.exe) | 优化文档预览窗口的打开、保存、主题与关闭，未登录也可预览 PPT | `1790021711` | `2026-09-23T11:22:40Z` |
| `5.5.6.38337834` | macOS Apple Silicon: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-arm64/WorkBuddy-darwin-arm64-5.5.6.38337834-5f969292.zip)<br>macOS Intel: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-x64/WorkBuddy-darwin-x64-5.5.6.38337834-5f969292.zip)<br>Windows x64: [下载](https://download.codebuddy.cn/workbuddy/saas/win32-x64-user/WorkBuddy-win32-x64-user-5.5.6.38337834-5f969292.exe) | 优化自动化任务重试，失败后可在当前会话中继续，避免创建重复的任务会话 | `1789061034` | `2026-09-11T04:24:03Z` |
| `5.5.4.38151288` | macOS Apple Silicon: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-arm64/WorkBuddy-darwin-arm64-5.5.4.38151288-1ca4889a.zip)<br>macOS Intel: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-x64/WorkBuddy-darwin-x64-5.5.4.38151288-1ca4889a.zip)<br>Windows x64: [下载](https://download.codebuddy.cn/workbuddy/saas/win32-x64-user/WorkBuddy-win32-x64-user-5.5.4.38151288-1ca4889a.exe) | 「允许锁屏运行」新增关闭、熄屏后继续运行、保持屏幕常亮三种模式 | `1788874488` | `2026-09-09T09:34:26Z` |
| `5.5.3.37748631` | macOS Apple Silicon: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-arm64/WorkBuddy-darwin-arm64-5.5.3.37748631-104760a2.zip)<br>macOS Intel: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-x64/WorkBuddy-darwin-x64-5.5.3.37748631-104760a2.zip)<br>Windows x64: [下载](https://download.codebuddy.cn/workbuddy/saas/win32-x64-user/WorkBuddy-win32-x64-user-5.5.3.37748631-104760a2.exe) | 本地 Office 文件预览支持更大文件，Word 和表格最高 100MB，演示文稿最高 500MB | `1788471831` | `2026-09-04T09:29:28Z` |
| `5.5.2.37672479` | macOS Apple Silicon: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-arm64/WorkBuddy-darwin-arm64-5.5.2.37672479-2b0177c3.zip)<br>macOS Intel: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-x64/WorkBuddy-darwin-x64-5.5.2.37672479-2b0177c3.zip)<br>Windows x64: [下载](https://download.codebuddy.cn/workbuddy/saas/win32-x64-user/WorkBuddy-win32-x64-user-5.5.2.37672479-2b0177c3.exe) | 优化积分到期提醒和积分明细，按有效期分类展示，并保留尚未过期的积分包记录 | `1788395679` | `2026-09-03T09:37:05Z` |
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
