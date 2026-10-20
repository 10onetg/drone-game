# はじめてのフライト（ドローンのルールを学べるRPG）

公開先：https://game.jtag-works.jp/ （Cloudflare Pages）
運営：JTAG（https://jtag-works.jp/ ）

JTAGの営業用サイト（10onetg/jtag-website、Netlify）とは別のリポジトリです。
ゲーム本体と広告のコードは、こちらにだけ置きます。

## フォルダ
- `public/` … 公開するファイル。Cloudflare Pages の「ビルドの出力ディレクトリ」はここ。
  - `index.html` 紹介ページ／`play.html` ゲーム本体／`how-to-play.html` 遊び方／`about.html` 運営者／`privacy.html` プライバシーポリシー・免責事項
  - `analytics.js` Googleアナリティクス（測定IDを入れるまでは何も送らない）
- `tools/build.py` … ゲームの試作ファイル（drone-rpg.html）から `public/play.html` を作る。
- `docs/publish-steps.md` … 公開の手順（Cloudflare・DNS・AdSense）。

## ゲームを更新するとき
1. 試作ファイル（プロジェクトの game-prototype/drone-rpg.html）を直す。
2. `python3 tools/build.py` で `public/play.html` を作り直す。
   - 公開ページ用の head（文字コード・説明文など）と、下のリンク行が付く。
   - アフィリエイト枠の「準備中」表示は自動で止める（AFF_SHOW_EMPTY=false）。
3. main に送る（push）と、Cloudflare Pages が自動で公開し直す。

## 公開前・公開後に残っていること
- [ ] Googleアナリティクスの測定IDを `public/analytics.js` に入れる（新しいプロパティかデータストリームはJunが作る）。
- [ ] AdSenseのコードを受け取ったら、各ページの `<!-- AdSense: ... -->` の所に貼る。`public/ads.txt` を置く（docs/publish-steps.md の 5）。
- [x] Amazonのリンク（室内練習機2つ）を入れ、アソシエイトの定型文をフッターとプライバシーポリシーに追加した（2026-10-20）。ほかの枠のリンクは未定。
- [ ] ゲーム内の「試作版」「絵や音楽はまだ入っていません」の表記は、正式公開のときに試作ファイル側で直す。
