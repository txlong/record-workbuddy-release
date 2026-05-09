# Record WorkBuddy Release

这个仓库通过 GitHub Actions 每小时请求一次 WorkBuddy 更新接口，并把返回的多平台版本信息记录到仓库中。

## 最新版本

<!-- workbuddy-latest:start -->
**当前最新版本：`4.22.7.27539150`**

最新平台：macOS Apple Silicon, macOS Intel, Windows x64

| 平台 | 最新版本 | 下载 | SHA256 | 首次记录 |
| --- | --- | --- | --- | --- |
| macOS Apple Silicon | `4.22.7.27539150` **最新** | [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-arm64/WorkBuddy-darwin-arm64-4.22.7.27539150-6dc48069.zip) | `da3b155c24bf` | `2026-05-09T09:15:55Z` |
| macOS Intel | `4.22.7.27539150` **最新** | [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-x64/WorkBuddy-darwin-x64-4.22.7.27539150-6dc48069.zip) | `e7949d1b4577` | `2026-05-09T09:21:15Z` |
| Windows x64 | `4.22.7.27539150` **最新** | [下载](https://download.codebuddy.cn/workbuddy/saas/win32-x64-user/WorkBuddy-win32-x64-user-4.22.7.27539150-6dc48069.exe) | - | `2026-05-09T09:21:15Z` |
<!-- workbuddy-latest:end -->

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

- `data/releases.json`：历史版本记录。脚本会按 `platform + sha256hash` 去重；如果没有 `sha256hash`，则使用 `platform + version + productVersion + url` 去重。
- `data/latest.json`：最近一次发生写入时，各平台的接口返回内容和记录时间。

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
WORKBUDDY_RECORD_PATH="data/releases.json" \
WORKBUDDY_LATEST_PATH="data/latest.json" \
python scripts/record_workbuddy_release.py
```
