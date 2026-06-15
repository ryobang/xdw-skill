---
name: xdw
description: DocuWorks ファイル（.xdw / .xbd）を読む・閲覧する・処理したいときに使うスキル。まず PDF に変換してから PDF として読み取り・処理する。.xdw ファイルや DocuWorks 文書への言及で必ず発動する。Use this skill whenever the user wants to read, view, or process a DocuWorks file (.xdw or .xbd).
---

# DocuWorks (.xdw) ファイルの取り扱い

## 概要

DocuWorks ファイル（`.xdw` / `.xbd`）は、エージェントや一般的なツールから直接は
読めません。必ず先に `xdwlib` で PDF に変換し、変換後の PDF を通常の PDF ツールで
処理してください。

## 前提条件

- **Windows 専用。** DocuWorks（富士ゼロックス / FUJIFILM Business Innovation の
  ソフトウェア）は Windows で動作し、`xdwlib` はインストール済みの DocuWorks エンジンを
  呼び出します。
- DocuWorks がマシンにインストールされていること。
- **Python 3.10 以上**（`str | None` 型注記を使用）。
- `xdwlib` … 未インストールでも `xdw_to_pdf.py` が初回実行時に自動で `pip install` を
  試みます。手動で入れる場合は `pip install xdwlib`。
  なお `xdwlib` は DocuWorks エンジンのラッパーなので、DocuWorks 本体が未インストールだと
  `pip` できても変換は失敗します。

## セットアップ

`xdw_to_pdf.py` はこのスキルフォルダに同梱されています。スキルディレクトリから
そのまま使うか、作業ファイルの隣にコピーして使ってください。

## 変換して読む手順

### 手順1: .xdw を PDF に変換

```python
import sys
sys.path.insert(0, r"<xdw_to_pdf.py を置いたフォルダのパス>")
from xdw_to_pdf import convert_xdw_to_pdf

pdf_path = convert_xdw_to_pdf(r"path/to/file.xdw")
# 出力 PDF のパスを返す（同じ場所・拡張子 .pdf）
```

またはコマンドラインから直接実行:

```bash
python "<xdw_to_pdf.py のパス>" "path/to/file.xdw"
# 第2引数で出力先を明示することも可能
python "<xdw_to_pdf.py のパス>" "path/to/file.xdw" "path/to/out.pdf"
```

### 手順2: PDF を読む

変換後、生成された `.pdf` を通常の PDF リーダーや PDF スキルで読み取ってください。

## 補足

- 出力 PDF は、出力先を明示しない限り、元の `.xdw` と同じ場所に `.pdf` 拡張子で
  保存されます。
- 既定の圧縮方式: `MRC_NORMAL`（品質とファイルサイズのバランスが良い）。

## 圧縮オプション

| オプション         | 用途                       |
| ----------------- | ------------------------- |
| `MRC_NORMAL`      | 既定。バランス型           |
| `MRC_HIGHQUALITY` | 品質を優先したいとき        |
| `MRC_HIGHCOMPRESS`| ファイルサイズを優先したいとき |
| `NORMAL`          | MRC なしの単純ラスター      |
