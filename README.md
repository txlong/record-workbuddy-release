# Record WorkBuddy Release

这个仓库通过 GitHub Actions 每小时请求一次 WorkBuddy 更新接口，并把返回的多平台版本信息记录到仓库中。

## 最新版本

<!-- workbuddy-latest:start -->
**当前最新版本：`5.0.2.29916712`**

最新平台：macOS Apple Silicon, macOS Intel, Windows x64

| 平台 | 最新版本 | 下载 | SHA256 | 首次记录 |
| --- | --- | --- | --- | --- |
| macOS Apple Silicon | `5.0.2.29916712` **最新** | [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-arm64/WorkBuddy-darwin-arm64-5.0.2.29916712-0ce39ce2.zip) | `b2c8a2650c31` | `2026-06-05T08:49:52Z` |
| macOS Intel | `5.0.2.29916712` **最新** | [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-x64/WorkBuddy-darwin-x64-5.0.2.29916712-0ce39ce2.zip) | `a80db8d3645e` | `2026-06-05T08:49:52Z` |
| Windows x64 | `5.0.2.29916712` **最新** | [下载](https://download.codebuddy.cn/workbuddy/saas/win32-x64-user/WorkBuddy-win32-x64-user-5.0.2.29916712-0ce39ce2.exe) | - | `2026-06-05T08:49:52Z` |
<!-- workbuddy-latest:end -->

## 历史版本

<!-- workbuddy-history:start -->
仅展示最近 10 个版本；完整逐平台历史记录见 `data/releases.json`。 另有 4 个更早版本未在 README 展开。

| 版本 | 平台下载 | 更新日志 | 接口时间戳 | 首次记录 |
| --- | --- | --- | --- | --- |
| `5.0.2.29916712` | macOS Apple Silicon: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-arm64/WorkBuddy-darwin-arm64-5.0.2.29916712-0ce39ce2.zip)<br>macOS Intel: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-x64/WorkBuddy-darwin-x64-5.0.2.29916712-0ce39ce2.zip)<br>Windows x64: [下载](https://download.codebuddy.cn/workbuddy/saas/win32-x64-user/WorkBuddy-win32-x64-user-5.0.2.29916712-0ce39ce2.exe) | - | `1780639912` | `2026-06-05T08:49:52Z` |
| `4.24.8.29724905` | macOS Apple Silicon: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-arm64/WorkBuddy-darwin-arm64-4.24.8.29724905-8d20aed6.zip)<br>macOS Intel: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-x64/WorkBuddy-darwin-x64-4.24.8.29724905-8d20aed6.zip)<br>Windows x64: [下载](https://download.codebuddy.cn/workbuddy/saas/win32-x64-user/WorkBuddy-win32-x64-user-4.24.8.29724905-8d20aed6.exe) | 修复上下文压缩相关异常：偶现自动取消、压缩失败后加载动画一直转、回放出现重复分隔线、压缩后历史漂移或丢失 | `1780448105` | `2026-06-03T05:04:32Z` |
| `4.24.7.29589271` | macOS Apple Silicon: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-arm64/WorkBuddy-darwin-arm64-4.24.7.29589271-f87d79a5.zip)<br>macOS Intel: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-x64/WorkBuddy-darwin-x64-4.24.7.29589271-f87d79a5.zip)<br>Windows x64: [下载](https://download.codebuddy.cn/workbuddy/saas/win32-x64-user/WorkBuddy-win32-x64-user-4.24.7.29589271-f87d79a5.exe) | 修复部分自动化定时任务跑过一次后卡在"即将开始"、无法再次触发的问题 | `1780312471` | `2026-06-01T11:52:22Z` |
| `4.24.5.29470881` | Windows x64: [下载](https://download.codebuddy.cn/workbuddy/saas/win32-x64-user/WorkBuddy-win32-x64-user-4.24.5.29470881-8666543c.exe) | - | `1780194081` | `2026-06-01T18:13:17Z` |
| `4.24.3.29355504` | macOS Apple Silicon: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-arm64/WorkBuddy-darwin-arm64-4.24.3.29355504-8711449a.zip)<br>macOS Intel: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-x64/WorkBuddy-darwin-x64-4.24.3.29355504-8711449a.zip)<br>Windows x64: [下载](https://download.codebuddy.cn/workbuddy/saas/win32-x64-user/WorkBuddy-win32-x64-user-4.24.3.29355504-8711449a.exe) | 优化会话列表，隐藏专家团子成员与展开箭头，列表更聚焦 | `1780078704` | `2026-05-30T10:09:07Z` |
| `4.24.2.29266680` | macOS Apple Silicon: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-arm64/WorkBuddy-darwin-arm64-4.24.2.29266680-b451b1ea.zip)<br>macOS Intel: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-x64/WorkBuddy-darwin-x64-4.24.2.29266680-b451b1ea.zip)<br>Windows x64: [下载](https://download.codebuddy.cn/workbuddy/saas/win32-x64-user/WorkBuddy-win32-x64-user-4.24.2.29266680-b451b1ea.exe) | 新增微信分享、项目邀请页与 OAuth 应用管理 | `1779989880` | `2026-05-29T12:24:32Z` |
| `4.24.1.29012054` | macOS Apple Silicon: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-arm64/WorkBuddy-darwin-arm64-4.24.1.29012054-dd5bfae4.zip)<br>macOS Intel: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-x64/WorkBuddy-darwin-x64-4.24.1.29012054-dd5bfae4.zip)<br>Windows x64: [下载](https://download.codebuddy.cn/workbuddy/saas/win32-x64-user/WorkBuddy-win32-x64-user-4.24.1.29012054-dd5bfae4.exe) | 优化「我分享的任务」列表，移除分享次数列并修正入口文案 | `1779735254` | `2026-05-26T16:50:09Z` |
| `4.22.16.28604695` | macOS Apple Silicon: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-arm64/WorkBuddy-darwin-arm64-4.22.16.28604695-d6e0fd20.zip)<br>macOS Intel: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-x64/WorkBuddy-darwin-x64-4.22.16.28604695-d6e0fd20.zip)<br>Windows x64: [下载](https://download.codebuddy.cn/workbuddy/saas/win32-x64-user/WorkBuddy-win32-x64-user-4.22.16.28604695-d6e0fd20.exe) | 修复部分场景下自定义模型可能请求失败的问题 | `1779327895` | `2026-05-21T05:14:56Z` |
| `4.22.15.28494097` | macOS Apple Silicon: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-arm64/WorkBuddy-darwin-arm64-4.22.15.28494097-a145005c.zip)<br>macOS Intel: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-x64/WorkBuddy-darwin-x64-4.22.15.28494097-a145005c.zip)<br>Windows x64: [下载](https://download.codebuddy.cn/workbuddy/saas/win32-x64-user/WorkBuddy-win32-x64-user-4.22.15.28494097-a145005c.exe) | 新增专家 / 专家团可见性配置，支持按内外网环境控制展示范围 | `1779217297` | `2026-05-20T08:33:17Z` |
| `4.22.14.28167846` | macOS Apple Silicon: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-arm64/WorkBuddy-darwin-arm64-4.22.14.28167846-33b73f3d.zip)<br>macOS Intel: [下载](https://download.codebuddy.cn/workbuddy/saas/darwin-x64/WorkBuddy-darwin-x64-4.22.14.28167846-33b73f3d.zip)<br>Windows x64: [下载](https://download.codebuddy.cn/workbuddy/saas/win32-x64-user/WorkBuddy-win32-x64-user-4.22.14.28167846-33b73f3d.exe) | 新增产物分享至微信能力，可在产物预览面板生成二维码，使用微信扫码即可查看分享内容 | `1778891046` | `2026-05-16T11:59:14Z` |
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
