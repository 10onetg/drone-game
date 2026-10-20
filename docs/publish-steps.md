# 公開の手順（Junさん向け）

アカウントの作成・ログイン・規約への同意・支払い情報の入力は、すべてJunさん自身が行います。
Claudeは、ファイルの用意と、手順の案内だけをします。

画面の文言は、サービス側の変更で少し違うことがあります。迷ったら、その画面をClaudeに伝えてください。

---

## 1. ゲーム用リポジトリ（GitHub）
- 名前：`drone-game`（10onetg/drone-game）
- 中身はClaudeが用意して送ります（push）。

## 2. Cloudflare Pages で公開する

1. https://dash.cloudflare.com/sign-up で無料アカウントを作る（Junさん）。
2. 左のメニューから **Workers & Pages**（「コンピューティング」の中にある場合あり）を開く。
3. **作成（Create application）** を押し、**Pages** のタブを選ぶ。
   - Workers の画面が先に出たら、下のほうの「Pages を使いたい場合はこちら（Looking to deploy Pages?）」から Pages に進む。
4. **Git に接続（Connect to Git / Import an existing Git repository）** を押す。
5. GitHub の画面が開くので、Cloudflare に `drone-game` だけを読ませる設定にして許可する（Junさん）。
   - 「Only select repositories」→ `10onetg/drone-game` を選ぶのがおすすめ。
6. リポジトリ `drone-game` を選び、**セットアップの開始（Begin setup）**。
7. 設定はこのとおり：
   | 項目 | 入れる内容 |
   |---|---|
   | プロジェクト名 | `drone-game`（これが仮の住所 `drone-game.pages.dev` になる） |
   | 本番ブランチ | `main` |
   | フレームワーク プリセット | `None`（なし） |
   | ビルドコマンド | 空欄のまま |
   | ビルド出力ディレクトリ | `public` |
8. **保存してデプロイ（Save and Deploy）** を押す。1分ほどで完了。
9. `https://drone-game.pages.dev/`（プロジェクト名が違えばその名前）を開いて、ゲームが動くか確認する。
   - 仮の住所は、プロジェクトの画面の上のほうに表示されます。メモしておいてください（4で使います）。

## 3. 住所 game.jtag-works.jp を Cloudflare 側に登録する（DNSより先に）

**順番が大事です。** 先に Cloudflare 側で登録しないで DNS を足すと、エラー（522）になります。

1. Cloudflare の `drone-game` プロジェクトを開き、**カスタムドメイン（Custom domains）** タブ。
2. **カスタムドメインを設定（Set up a custom domain / Set up a domain）** を押す。
3. `game.jtag-works.jp` と入力して **続行（Continue）**。
4. 「DNS は Cloudflare ではありません。CNAME レコードを追加してください」という内容の画面が出る。
   ここに書かれた **ターゲット（例：`drone-game.pages.dev`）** を確認する。
   - ネームサーバーを Cloudflare に移す案内が出ても、**移さないでください**（サイトとメールに影響します）。CNAME の方法を選びます。

## 4. Netlify の DNS に game の CNAME を1行「追加」する（Junさんの確認のもとで）

**追加だけ。今ある行（サイト・メール）は消さない・書き換えない。**

1. https://app.netlify.com にログイン（Junさん）。
2. 左のメニュー（またはチームの画面）の **Domains** → `jtag-works.jp` を開く。
3. 作業の前に、今の DNS の一覧をスクリーンショットで残しておく（念のため）。
4. **Add new record**（新しいレコードを追加）を押し、次のとおり入れる：
   | 項目 | 入れる内容 |
   |---|---|
   | Record type | `CNAME` |
   | Name | `game`（画面によっては `game.jtag-works.jp` と表示される） |
   | Value | 3で確認したターゲット（例：`drone-game.pages.dev`） |
   | TTL | そのまま（初期値） |
5. **Save** を押す。
6. 一覧に `game` の行が1行増え、ほかの行がそのままか確かめる。
7. Cloudflare のカスタムドメインの画面に戻り、`game.jtag-works.jp` が **有効（Active）** になるのを待つ（数分〜最大1日ほど）。鍵マーク（https）も自動で付きます。
8. https://game.jtag-works.jp/ を開いて確認。

## 5. 広告（AdSense）の審査に申し込む

### 申し込む前に（Claudeが用意済み）
- 紹介ページ（トップ）、遊び方、運営者・お問い合わせ、プライバシーポリシー・免責事項。
- 審査では「独自の説明ページ」があるかを見られます。

### 注意：サイトは「jtag-works.jp」で登録することになりそうです
- 2026年時点の AdSense の説明では、ふつうのサブドメイン（game.jtag-works.jp）は、サイトとして単独で追加できません。追加できるのは親のドメイン（jtag-works.jp）です。親が承認されると、サブドメインでも広告を出せます。
- 広告が表示されるのは、広告のコードを貼ったページだけです。JTAGのサイトにコードを貼らなければ、JTAGのサイトに広告は出ません。
- ただし「サイトの所有の確認」で、jtag-works.jp 側に何か1つ置く必要があります（下の 4）。
- 実際の画面で、サブドメインのまま申し込めるようなら、そちらを選んでください。

### 手順
1. https://adsense.google.com でアカウントを作る（Junさん。住所・支払い情報もJunさんが入力）。
2. **サイト** → **新しいサイトを追加** → 画面の指示に合わせて `jtag-works.jp`（サブドメインが入れられれば `game.jtag-works.jp`）を入れる。
3. 「サイトを AdSense にリンク」の画面で、確認の方法を選ぶ。表示されたコードや番号（`pub-` で始まる番号）を Claude に伝えてください。
4. 確認の方法は、次のどれか：
   - **ads.txt スニペット**（おすすめ）：`jtag-works.jp/ads.txt` に1行のファイルを置く。JTAGのサイトに広告のコードを入れずに済む。jtag-website への変更になるので、ほかの変更と**まとめて1回で**送ります。
   - **メタタグ**：jtag-works.jp のトップの head に1行。
   - **AdSense コード スニペット**：JTAGのサイトに広告のコードが入るので、使わない。
   - ゲーム側（game.jtag-works.jp）には、Claude が AdSense のコードと `ads.txt` を置きます。
5. **審査をリクエスト** を押す。結果はメールで届きます（数日〜数週間）。
6. 承認されたら、ゲーム側で広告を出す場所を決めます（ゲーム画面のじゃまにならない場所）。

## 6. アフィリエイト
- ASP（Amazonアソシエイト、もしもアフィリエイトなど）の登録・規約への同意はJunさん。
- リンクを受け取ったら、Claude がゲームの「実際に買うなら」の枠に入れます。枠には「広告」と表示されます。
