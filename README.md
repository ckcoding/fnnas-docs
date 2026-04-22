# 飞牛开发文档镜像

这个仓库会自动从 `https://developer.fnnas.com/docs/guide/` 抓取飞牛开发文档，转换成适合 GitHub 阅读的 Markdown，并把图片资源一并本地化。

## 入口

- [阅读官方文档](docs/README.md)
- [查看单文件合集](ALL_DOCS.md)

## 仓库结构

- `scripts/sync_fnnas_docs.py`
  抓取、转换、图片下载的主脚本
- `docs/`
  生成后的 Markdown 文档目录
- `assets/`
  文档引用的本地资源
- `ALL_DOCS.md`
  合并后的单文件版本
- `.github/workflows/sync.yml`
  每日自动同步工作流

## 本地运行

```bash
pip install -r requirements.txt
python scripts/sync_fnnas_docs.py
```

## 自动同步

工作流会在每天北京时间 `09:30` 自动运行一次。

如果要让 GitHub Actions 正常自动提交，请确认：

1. 仓库已启用 Actions。
2. `Settings -> Actions -> General -> Workflow permissions` 选择了 `Read and write permissions`。
3. 默认分支允许 `GITHUB_TOKEN` 推送提交。

## 说明

- 页面来源通过站点 sitemap 自动发现，新增页面通常会被自动纳入同步。
- `docs/`、`assets/`、`ALL_DOCS.md` 都是生成产物，建议直接提交到仓库。
- 源站存在 `fnnas.com` canonical 和 `developer.fnnas.com` 实际可下载地址混用的问题，脚本内部已经做了归一化处理。
