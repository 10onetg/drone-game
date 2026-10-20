#!/usr/bin/env python3
"""ゲームの試作ファイル（1ファイル完結）から、公開用の public/play.html を作る。

使い方:
  python3 tools/build.py [試作ファイルのパス]
  （省略時は /mnt/project-files/game-prototype/drone-rpg.html）

やること:
  - 公開ページとして必要な <!doctype html>・文字コード・viewport・説明文などを付ける
  - アフィリエイト枠の「準備中」表示を止める（AFF_SHOW_EMPTY を false に）
  - 画面の下に「トップ・遊び方・プライバシーポリシー」へのリンクを付ける
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
src = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '/mnt/project-files/game-prototype/drone-rpg.html')
body = src.read_text(encoding='utf-8')

body, n = re.subn(r'const AFF_SHOW_EMPTY = true;', 'const AFF_SHOW_EMPTY = false;', body)
if n != 1 and 'const AFF_SHOW_EMPTY = false;' not in body:
    sys.exit('AFF_SHOW_EMPTY が見つかりません。試作ファイルの形が変わっていないか確認してください。')

# 試作ファイル自身の <title> と、公開ページでは使わない meta を外す（下の head で付け直す）
body = re.sub(r'^\s*<title>.*?</title>\s*', '', body, count=1, flags=re.S)
body = re.sub(r'<meta name="claude:[^"]*"[^>]*>\s*', '', body)

head = (ROOT / 'tools' / 'play-head.html').read_text(encoding='utf-8')
foot = (ROOT / 'tools' / 'play-foot.html').read_text(encoding='utf-8')

out = head + body.strip() + '\n' + foot
(ROOT / 'public' / 'play.html').write_text(out, encoding='utf-8')
print('public/play.html を作りました（%d KB）' % (len(out.encode('utf-8')) // 1024))
