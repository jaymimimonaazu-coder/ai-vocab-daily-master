# AI用語デイリーマスター

AI・ITの基礎用語を毎日3単語ずつ学び、週末に一問一答でおさらいする、スマホ向け学習アプリ（PWA対応予定）。

公開URL: https://jaymimimonaazu-coder.github.io/ai-vocab-daily-master/

## 構成

| パス | 内容 |
|---|---|
| `index.html` | アプリ本体（Tailwind CSS CDN + vanilla JS） |
| `data/terms.json` | 用語データ（用語／読み／解説／例） |
| `manifest.json`, `sw.js`, `icons/` | PWA（インストール・オフライン対応） |
| `.github/workflows/deploy-pages.yml` | `main` へのpushでGitHub Pagesへ自動デプロイ |

## 実装済み

- 今日の3単語を日付から決定（同じ日なら何度開いても同じ3語、翌日には次の3語）
- 「覚えた！」の状態を localStorage に保存（リロード後も復元）
- 用語集タブに全用語と習得状況を一覧表示
- 平日／週末でダッシュボードを切り替え（確認用の手動切替ボタンつき）
- PWA: ホーム画面に追加、オフラインでも起動（Tailwindのみ CDN 依存）

## 未実装

- 週末テストの出題ロジック（その週に学んだ単語からの出題・「もう一度」の再出題）
- 用語集の検索
- 設定タブの各項目

## 動かし方

`fetch` を使うためHTTP経由で開く必要があります。

```bash
python3 -m http.server 8000
# http://localhost:8000/ を開く
```
