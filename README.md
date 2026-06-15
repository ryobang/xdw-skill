# DocuWorks (.xdw) スキル

ClaudeCodeに**DocuWorks** ファイル（`.xdw` / `.xbd`）を読ませるための
[エージェントスキル](https://skills.sh)です。

DocuWorks ファイルは直接読めないため、このスキルがまず PDF に変換し（`xdwlib` 使用）、あとは通常の PDF ツールで処理します。

## インストール

```bash
npx skills add ryobang/xdw-skill
```


## できること

- `.xdw` / `.xbd` ファイルや DocuWorks 文書への言及で自動的に発動
- ファイルを PDF へ変換（既定の圧縮は `MRC_NORMAL`）
- 変換後の PDF をエージェントが読み取り・処理

## 必要環境

- **Windows 専用** — DocuWorks（FUJIFILM Business Innovation）がインストール済みであること
- **Python 3.10 以上**（`str | None` 型注記を使用）
- `xdwlib` — 未インストールなら `xdw_to_pdf.py` が初回実行時に自動で `pip install` します（手動なら `pip install xdwlib`）

## 構成

```
skills/
  xdw/
    SKILL.md        # スキル定義（フロントマター + 手順）
    xdw_to_pdf.py   # 変換用スクリプト
```

## ライセンス

[MIT](./LICENSE)
