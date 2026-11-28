#!/usr/bin/env python3
"""Generate all static HTML pages for The Plank of Theseus /projects/ toolkit matrix,
update sitemap.xml, and sync everything cleanly into dist/."""

from __future__ import annotations

import html
import shutil
from pathlib import Path

ROOT = Path("/Users/yunhanbao/Documents/Root/Factory/projects/plankoftheseus-site")
DIST = ROOT / "dist"
TODAY = "2026-11-26"
FEISHU_HUB_URL = "https://www.feishu.cn/wiki/Jz5PwKG2VilS2WkMJCQcg8CLnp7"

XUAN_SVG = """  <div class="xuan-texture" aria-hidden="true">
    <svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%">
      <filter id="xuan-fiber" x="0%" y="0%" width="100%" height="100%">
        <feTurbulence
          type="fractalNoise"
          baseFrequency="0.68 0.14"
          numOctaves="4"
          seed="17"
          result="rawNoise" />
        <feColorMatrix
          type="matrix"
          values="0 0 0 0 0.08
                  0 0 0 0 0.08
                  0 0 0 0 0.08
                  0 0 0 0.42 0"
          in="rawNoise"
          result="finePaper" />
      </filter>
      <rect width="100%" height="100%" filter="url(#xuan-fiber)" />
    </svg>
  </div>"""


TOOLS = [
    {
        "slug": "antigravity-theme",
        "title": "船板 Antigravity 美化+汉化补丁",
        "en_subtitle": "Minimalist theme & optional ZH/JA localization patch for Antigravity — featuring Morandi and Claude day/night palettes with a handy status pill.",
        "version": "v6.0.3",
        "tags": {
            "distribution": ["GitHub MIT", "全功能私人安装包"],
            "platform": "Antigravity",
            "kind": "一体化环境包",
        },
        "summary": "Antigravity 极简外观美化和汉化、日文化补丁包，可自选语言或不安装语言包独享皮肤美化。包含莫兰迪配色、Claude 风昼夜配色三种主要模式和便利性显示胶囊。",
        "lead": "Antigravity 极简外观美化和汉化、日文化补丁包，可自选语言或不安装语言包独享皮肤美化。包含莫兰迪配色、Claude 风昼夜配色三种主要模式和便利性显示胶囊。",
        "thumb": "/assets/projects/antigravity/preview-morandi-workbench.webp",
        "github_url": "https://github.com/Anarcadia/chuanban-antigravity-theme-patch",
        "github_label": "Anarcadia/chuanban-antigravity-theme-patch",
        "extra_links": [
            ("SKILL.md（Agent 部署契约）", "https://github.com/Anarcadia/chuanban-antigravity-theme-patch/blob/main/SKILL.md"),
            ("CHANGELOG.md（更新日志）", "https://github.com/Anarcadia/chuanban-antigravity-theme-patch/blob/main/CHANGELOG.md"),
        ],
        "feishu_doc_url": "https://www.feishu.cn/wiki/EQyqwJEqmi1LH3k11tzcmkMHnYd",
        "feishu_dl_url": "https://www.feishu.cn/wiki/V2lbwB8ykiLLXrkzY41cXjQ1nXc",
        "gallery": [
            ("/assets/projects/antigravity/preview-morandi-workbench.webp", "1. 默认标准主界面：莫兰迪风格（MO）与上下文信息胶囊详情卡"),
            ("/assets/projects/antigravity/preview-theme-lang-switcher.webp", "2. 外观与语言切换面板：五段式皮肤选择 + [ EN | 中文 ] 一键双切"),
            ("/assets/projects/antigravity/preview-absolutely-workbench.webp", "3. Absolutely! 主题演示：仿 Claude 书卷暖白工作台与子 Agent 汉化副栏"),
            ("/assets/projects/antigravity/preview-dark-workbench.webp", "4. 夜间界面与代码审阅视图（支持 暖纸深色 / 深海冷碳 切换）"),
        ],
        "features": [
            ("多套打磨风格与系统日夜自动跟随", "内置莫兰迪古典矿物风格（默认）、仿 Claude 书卷暖白（Absolutely!）、温润书卷夜间与深海冷碳深色模式，支持独立「跟随系统」自动日夜配对，并可一键退回官方原版风格。"),
            ("2,210 条母语级汉化与中英双切", "覆盖主界面、设置项、编排器、Swarm 蜂群工作台与子 Agent 面板的自然中文汉化，严格隔离代码块、终端与文件名避免误翻；外观面板支持 [ EN | 中文 ] 一键切换。"),
            ("字体美化与活字微润墨特效", "精选书卷衬线长文、现代无衬线界面与人文等宽代码字体组合，在浅色纸面融入细腻微润墨柔化，消除中英文混排发虚与字重断层。"),
            ("极简上下文信息胶囊与 Token 统计", "输入框底栏内嵌低干扰状态胶囊，支持主窗口、分屏、支线与子 Agent 独立显示速率、首字延迟与上下文圆环；设置面板集成多维本地只读 Token 统计。"),
            ("纯粹克制与非侵入式低风险设计", "仅通过本机回环（127.0.0.1）CDP 通道向前端渲染层注入 CSS 样式与静态汉化词条，不解包、不修改 app.asar 安装包，完整保留客户端官方数字签名与系统公证；内置的 Token 统计与指标胶囊仅离线只读解析本机已落盘的 SQLite 会话库，不读取系统钥匙串与 OAuth 凭据、不调用 Google 内部私有配额接口（如 retrieveUserQuotaSummary）、不伪造客户端身份标识（User-Agent / clientInfo），亦不涉及任何 CDP 对话流自动化操控、网络代理拦截、多账号切换或跨工具目录扫描等其他技术手段（注：纯前端运行时渲染层注入虽不涉及网络请求与鉴权凭据交互，但在客户端服务条款字面上仍属未显式授权的本地修改灰区，并非绝对零风险，支持随时一键彻底卸载并无损还原）。"),
        ],
        "table": {
            "heading": "五段式内置皮肤预设",
            "headers": ["按钮", "预设名称", "定位与氛围说明"],
            "rows": [
                ["MO", "莫兰迪 (morandi)", "默认浅色：温润耐看的古典矿物灰暖纸基调，长时间读写零疲劳。"],
                ["AB", "Absolutely! (claude)", "仿 Claude 书卷暖白：经典温暖纸面搭配陶土强调色，极简学术与长文气质。"],
                ["暖夜", "暖纸深色 (warm-dark)", "温润书卷夜间：柔和暗纸底色配暖调字色与陶土点缀，适合夜间沉浸写作。"],
                ["深色", "深海冷碳 (onyx)", "深海青黛暗底配石青点缀，冷静克制，适合代码审阅与暗光环境。"],
                ["A", "原版配色 (native)", "一键旁路补丁配色与自定义字体，回归官方原貌同时保留汉化与统计可用。"],
            ],
        },
        "install_blocks": [
            {
                "title": "新用户首次安装：复制引导词发给你的 AI Agent（推荐）",
                "desc": "环境要求 Node.js >= 22.0.0（推荐 >= 22.13.0）。必备字体支持脚本自动下载并注册；如终端网络受限，可先在「资源下载页」通过浏览器下载字体包后交给脚本安装。",
                "code_label": "AGENT PROMPT · 首次部署 v6.0.3",
                "code": """请帮我克隆 https://github.com/Anarcadia/chuanban-antigravity-theme-patch.git（或读取我已下载解压的补丁目录），先完整阅读仓库内的 SKILL.md，再按以下顺序部署并处理边缘情况：
1. 若本机有 nvm / fnm / volta，优先切换至 Node >= 22.13.0 执行命令；运行 node install.mjs doctor 检查 fonts.allRequiredInstalled 与 fonts.unregisteredWarning。
2. 若缺少字体（或 Windows 提示有未写注册表的用户字体）：
   - 若我本地已下载好字体目录或 .zip，直接执行 node install.mjs install-fonts --from "<字体目录或.zip路径>"；
   - 若本地尚未下载，直接执行 node install.mjs install-fonts --auto-download（Windows 检出旧版 SuperTTC 请追加 --retire-super-ttc）；
   - 若终端网络/代理受限，提示我通过资源下载页下载全部字体到同一目录后再运行 install-fonts --from（macOS 缺少更纱也可用 brew install --cask font-sarasa-gothic）。
3. 运行 node install.mjs install 完成安装（默认启用 "morandi" 莫兰迪风格）。
4. 若输出 cdpStatus 为 "missing_opt_in_flag" 且你当前正在 Antigravity 内部会话中，请勿强行重启自断会话，提示我空闲时运行 node ~/.gemini/antigravity/theme-patch/install.mjs relaunch（或手动重开客户端）。
5. 端口就绪后运行 node install.mjs verify，确认 "ok": true、"hasStyle": true 且 fonts.allRequiredInstalled: true 即完成验收。""",
            },
            {
                "title": "老用户无损升级至 v6.0.3",
                "desc": "升级自动备份旧版 core/ 内核并完整保留 ~/.gemini/antigravity/theme-patch/user/ 下的个人自定义字号、配色与词条覆盖。",
                "code_label": "AGENT PROMPT · 升级至 v6.0.3",
                "code": """请帮我拉取最新的 https://github.com/Anarcadia/chuanban-antigravity-theme-patch.git（或读取最新解压目录），阅读 SKILL.md 后直接运行 node install.mjs install 升级至 v6.0.3。若端口未开启且你正在 Antigravity 内部会话中，请提示我空闲时执行 relaunch，就绪后运行 node install.mjs verify 验收。""",
            },
        ],
        "callout": "<strong>开发红线与合规边界：</strong>本仓库 main 分支坚决不加入自动操控对话流、绕过配额、拦截网络请求、读取 OAuth 凭据或修改客户端二进制签名的功能。本项目为独立非官方社区视觉增强补丁，与 Google 无关，随时可运行 <code>node install.mjs uninstall</code> 彻底还原。",
        "download_intro": "集中提供 GitHub Releases 官方包、Google Drive 海外公开分流与飞书国内免代理分流页。如终端网络畅通，脚本亦支持 <code>node install.mjs install-fonts --auto-download</code> 自动拉取字体。",
        "downloads": [
            {
                "name": "主程序补丁包 · chuanban-antigravity-theme-patch-v6.0.3.zip",
                "meta": "v6.0.3 · 9.6 MB · 含 core/ 内核、install.mjs 与 SKILL.md",
                "desc": "完整预封装内核、个人改装层模板、2,210 条汉化词库与生命周期 CLI，支持 macOS / Windows / Linux。",
                "mirrors": [
                    ("GitHub Release 直下", "GITHUB", "https://github.com/Anarcadia/chuanban-antigravity-theme-patch/releases/download/v6.0.3/chuanban-antigravity-theme-patch-v6.0.3.zip", True),
                    ("Google Drive 公开分流", "DRIVE", "https://drive.google.com/file/d/1P90Y6j_2H59cGAKbjvu8B2BjofCJo6GP/view?usp=sharing", False),
                    ("GitHub 仓库源码", "REPO", "https://github.com/Anarcadia/chuanban-antigravity-theme-patch", False),
                ],
            },
            {
                "name": "更纱黑体中文拆分包 · SarasaUiSC + SarasaMonoSlabSC (v1.0.43)",
                "meta": "170.4 MB · OFL 1.1 · 按字族拆分免卡顿",
                "desc": "包含 7 个界面字重（SarasaUiSC）与 7 个等宽代码字重（SarasaMonoSlabSC），避免单文件 791MB SuperTTC 在 Windows 上的卡顿；macOS 用户亦可直接运行 brew install --cask font-sarasa-gothic。",
                "mirrors": [
                    ("GitHub 字体镜像直下", "GITHUB", "https://github.com/Anarcadia/chuanban-antigravity-theme-patch/releases/download/fonts-sarasa-v1.0.43/Windows-Sarasa-Split-SC-TTF-v1.0.43.zip", True),
                    ("Google Drive 公开分流", "DRIVE", "https://drive.google.com/file/d/1iVVvZXtwUcDiHy42tJ25X6N-JlOf3l7A/view?usp=sharing", False),
                    ("飞书国内免代理分流页", "FEISHU", "https://www.feishu.cn/wiki/V2lbwB8ykiLLXrkzY41cXjQ1nXc", False),
                ],
            },
            {
                "name": "西文衬线与等宽主力字体（3 个 Anthropic .ttf，共约 1.1 MB）",
                "meta": "AnthropicMono / AnthropicSerif Regular & Bold",
                "desc": "提供原汁原味的书卷衬线正文与人文等宽代码排版。将字体与更纱包下载至同一目录（无需手动解压），交给安装脚本一键注册即可。",
                "mirrors": [
                    ("Google Drive 公共目录直取", "DRIVE", "https://drive.google.com/drive/folders/1NX92SgVUqtSjWg6bt6sIJXy-cn7J_boC", True),
                    ("飞书国内免代理字体页（免登录）", "FEISHU", "https://www.feishu.cn/wiki/V2lbwB8ykiLLXrkzY41cXjQ1nXc", False),
                ],
            },
        ],
        "download_commands": [
            ("离线字体一键安装命令（下载至同一目录后执行）", 'node install.mjs install-fonts --from "<下载目录路径>"'),
            ("终端网络畅通时自动拉取并校验 SHA-256", "node install.mjs install-fonts --auto-download"),
        ],
    },
    {
        "slug": "obsidian-chuanban-green",
        "title": "松绿记事本 · Obsidian 主题",
        "seo_description": "仿佛绿草藤蔓记事本一样美丽的护眼 Obsidian 皮肤，推荐作为个人记事本或者小说创作默认主题使用。",
        "en_subtitle": "An eye-friendly Obsidian theme that feels like holding a vine-bound botanical notebook in your hands — my top recommendation as a default theme for personal journaling or fiction writing. Search \"chuanban-green\" in the Obsidian Community Themes store for the Lite edition; the download page provides the full theme, complete font pack, and plugin bundle.",
        "version": "v1.0.5 / 全装字体包",
        "tags": {
            "distribution": ["GitHub MIT", "全功能私人安装包"],
            "platform": "Obsidian",
            "kind": "皮肤",
        },
        "summary": "手捧绿草藤蔓记事本一般的护眼 Obsidian 皮肤，我极其推荐作为个人记事本或者小说创作默认主题使用。简装版可在 Obsidian 主题商店搜 chuanban-green 安装；下载页提供完整主题、完整字体、插件包。",
        "lead": "手捧绿草藤蔓记事本一般的护眼 Obsidian 皮肤，我极其推荐作为个人记事本或者小说创作默认主题使用。简装版可在 Obsidian 主题商店搜 chuanban-green 安装；下载页提供完整主题、完整字体、插件包。（采用植物编辑风 × 新粗野主义设计：全域 0px 直角、1px 炭黑外露网格、三阶暖色印刷纸底、松绿硬边偏移阴影与阅读/编辑双模式字体分离。）",
        "thumb": "/assets/projects/chuanban-green/screenshot.webp",
        "github_url": "https://github.com/Anarcadia/chuanban-highcontrast-green",
        "github_label": "Anarcadia/chuanban-highcontrast-green",
        "extra_links": [],
        "feishu_doc_url": "https://www.feishu.cn/wiki/OftdwaNjBidHBgk9siQcDmNlnBg",
        "feishu_dl_url": "https://www.feishu.cn/wiki/ASmww8RaaifwkjkysO6c7t9xnYc",
        "gallery": [
            ("/assets/projects/chuanban-green/screenshot.webp", "1. 主界面实机展示（满血 vivo Sans 印刷黑体 + Sarasa Mono Slab SC 等距打字机效果）"),
            ("/assets/projects/chuanban-green/screenshot-overview.webp", "2. 界面视觉与瑞士网格设计细节图解"),
        ],
        "features": [
            ("全域 0px 纯直角与 1px 炭黑外露网格", "彻底移除圆角与弧脚，所有 Tab、按钮、输入框与弹窗均为干脆利落的直角矩形；1px solid #181B18 实线贯穿切分左右侧栏、Tab、大纲与表格，重现瑞士网格秩序感。"),
            ("三阶暖色印刷纸底拉开空间景深", "中央道林浅灰纸 (#ECEAE2) → 侧栏旧报刊中暖灰 (#E2DFD5) → 右上大纲亚麻深暖灰 (#D6D2C6)，无需阴影模糊即可自然区分工作区层级。"),
            ("松绿强调色 + 3px 纯色硬边阴影", "竹青浓绿 (#78AB88) / 深松墨绿 (#26593F) 搭配零模糊纯色硬边偏移阴影 (3px 3px 0px #A3C9AE)，贯穿引用块、Callout、代码块与按钮。"),
            ("阅读态 / 编辑态双模式字体分离 + 粗体三重强化", "阅读态调用锐利现代印刷黑体（vivo Sans），编辑态切为 2:1 等距打字机体（Sarasa Mono Slab SC）；粗体叠加 750 ExtraBold、深墨松绿字色与 1.5px 细压线。"),
        ],
        "table": {
            "heading": "官方主题商店「简装版」 vs 船板「全装字体版」核心区别",
            "headers": ["对比维度", "官方商店简装版（搜 chuanban-green）", "船板全装字体版（见资源下载页）"],
            "rows": [
                ["包含内容", "仅纯 CSS 主题本体（受官方规范限制不含字体文件）", "完整 v1.0.5 主题包 + 9 字重 vivo Sans 全家桶 + 更纱等距字体拆分包"],
                ["阅读模式字体", "自动回退至系统黑体（冬青黑体 / 微软雅黑）", "满血调用 vivo Sans（400 / 750 ExtraBold / 850 Heavy），100% 复现印张效果"],
                ["编辑/源码字体", "回退至系统等宽 + 苹方 / 微软雅黑", "满血调用 Sarasa Mono Slab SC，中英文严格 2:1 等距打字机手稿台体验"],
                ["适用人群", "想 10 秒即装即用、或已有自定义字体的用户", "想零折腾一次性配齐全部推荐字体、还原展示图满血效果的用户"],
            ],
        },
        "install_blocks": [
            {
                "title": "极简安装：Obsidian 官方商店搜索 chuanban-green（简装版）",
                "desc": "字体安装到系统字库后完全退出并重启 Obsidian，主题内置 @font-face 探针会自动识别接管，无需手工填写字体名。",
                "code_label": "OBSIDIAN STORE · 安装与个性化调节",
                "code": """1. 打开 Obsidian → 设置 (Settings) → 外观 (Appearance) → 主题 (Themes) → 管理 (Manage)
2. 搜索：chuanban-green → 点击「安装并使用」
3. (可选) 安装社区插件 Style Settings → 进入 chuanban-green (松绿记事本)，自由切换激活 Tab 配色（竹青浓绿 ⇄ 深松墨绿）、三套正文字体预设与硬边阴影偏移。""",
            }
        ],
        "callout": "<strong>安装提示：</strong>若下载全装版中的 <code>vivo Sans</code>（9 字重）与 <code>Sarasa Mono Slab SC</code> 字体包，安装进系统字体册后请<strong>完全退出并重启 Obsidian</strong>，主题将自动探针接管。",
        "download_intro": "提供 Obsidian 官方商店简装版、GitHub Release (v1.0.5) 主题包，以及含 9 字重 vivo Sans 全家桶 + 更纱等距字体的全装下载入口。",
        "downloads": [
            {
                "name": "主题本体 · chuanban-green (v1.0.5)",
                "meta": "v1.0.5 · 已上架 Obsidian 官方商店",
                "desc": "支持在 Obsidian 主题商店直接搜索 chuanban-green 安装，或从 GitHub Release 下载离线 theme.css / 完整源码包。",
                "mirrors": [
                    ("GitHub Release (1.0.5)", "GITHUB", "https://github.com/Anarcadia/chuanban-highcontrast-green/releases/tag/1.0.5", True),
                    ("GitHub 源码包直下 (.zip)", "ZIP", "https://github.com/Anarcadia/chuanban-highcontrast-green/archive/refs/tags/1.0.5.zip", False),
                    ("飞书国内免代理下载页", "FEISHU", "https://www.feishu.cn/wiki/ASmww8RaaifwkjkysO6c7t9xnYc", False),
                ],
            },
            {
                "name": "全套 9 字重推荐字体 · vivo-Sans-Fonts-Full.zip + 更纱等距字体",
                "meta": "vivo Sans 9 字重 + SarasaMonoSlabSC (v1.0.43)",
                "desc": "还原展示图 100% 锐利杂志印张（正文 400 / 粗体 750 / 标题 850）与编辑态严格 2:1 打字机等距排版。vivo Sans 全家桶请在飞书免代理下载页直取，更纱包支持三源分流。",
                "mirrors": [
                    ("飞书免代理页（含 vivo Sans 全套）", "FEISHU", "https://www.feishu.cn/wiki/ASmww8RaaifwkjkysO6c7t9xnYc", True),
                    ("更纱字体 · GitHub 镜像直下", "GITHUB", "https://github.com/Anarcadia/chuanban-antigravity-theme-patch/releases/download/fonts-sarasa-v1.0.43/Windows-Sarasa-Split-SC-TTF-v1.0.43.zip", False),
                    ("更纱字体 · Google Drive 分流", "DRIVE", "https://drive.google.com/file/d/1iVVvZXtwUcDiHy42tJ25X6N-JlOf3l7A/view?usp=sharing", False),
                ],
            },
        ],
        "download_commands": [
            ("手动放入 Obsidian 主题目录路径", "<你的Vault>/.obsidian/themes/chuanban-green/"),
        ],
    },
    {
        "slug": "obsidian-notion-hc",
        "title": "仿 Notion Obsidian 高对比浅/暗主题",
        "en_subtitle": "A minimalist black-and-white ink-on-paper print-style Obsidian theme, rebuilt after Notion's High Contrast theme.",
        "version": "v0.3.2",
        "tags": {
            "distribution": ["GitHub MIT"],
            "platform": "Obsidian",
            "kind": "皮肤",
        },
        "summary": "模仿 Notion 黑白高对比主题重构的 Obsidian 极简黑白印刷风格主题，清晰明快的黑白高对比字体和圆角矩形、直线 UI 线条，给你既不会分心，又不会视觉疲劳的清爽体验。",
        "lead": "模仿 Notion 黑白高对比主题重构的 Obsidian 极简黑白印刷风格主题，清晰明快的黑白高对比字体和圆角矩形、直线 UI 线条，给你既不会分心，又不会视觉疲劳的清爽体验。（支持白天与黑夜双模式实线网格及选中/悬停双态分层，不锁死原生字体设置。）",
        "thumb": "/assets/projects/notion-obsidian/01-light-overview.webp",
        "github_url": "https://github.com/Anarcadia/chuanban-notionlikeHC",
        "github_label": "Anarcadia/chuanban-notionlikeHC",
        "extra_links": [],
        "feishu_doc_url": "https://www.feishu.cn/wiki/R0wEwAWJ0i6vaCkqyK4cRq6Qnfd",
        "feishu_dl_url": "https://www.feishu.cn/wiki/TKE6wWDO1iUuTDkrEuacVlDTn1b",
        "gallery": [
            ("/assets/projects/notion-obsidian/01-light-overview.webp", "1. 白天模式：极浅暖灰侧边栏配纯白正文，选中带清晰外框，表格与引用层次分明"),
            ("/assets/projects/notion-obsidian/02-dark-overview.webp", "2. 黑夜模式：Notion 同款深炭灰正文与亮白/银灰实线，拒绝刺眼死黑"),
            ("/assets/projects/notion-obsidian/03-light-ui-elements.webp", "3. 白天模式菜单与设计要素：描边按钮、蓝色聚焦框与带 | / 0 标识的高对比开关"),
        ],
        "features": [
            ("少用模糊阴影，靠 1px 实线分清区域", "侧边栏采用极浅暖灰（黑夜模式为抬升半档的深灰），正文保持纯白（黑夜为 Notion 同款深炭灰），以 1px 实线清晰切开，表格与 Bases 视图同步补齐横竖全网格线。"),
            ("选中与悬停双态正交分层", "当前选中的标签页、侧栏条目与设置项加一圈明确细边框；鼠标悬停则以明显底色块提示，视觉状态清晰不混淆。"),
            ("次级文字与控件轮廓整体压实", "分组标题、路径、说明文字、下拉框、按钮与开关（含开关内 | / 0 标识）全面提升对比度，输入框聚焦保留清晰 Notion 蓝外框。"),
            ("字体自由不锁死", "默认走清晰黑体（推荐更纱黑体），完全尊重 Obsidian 原生「设置 → 外观 → 字体」配置，搭配 Style Settings 还可调节边框深浅、强调色与暗色纯黑画布。"),
        ],
        "table": None,
        "install_blocks": [
            {
                "title": "手动离线安装步骤（约 30 秒完成）",
                "desc": "本主题为独立高对比皮肤，暂未上架 Obsidian 官方社区主题市场，通过下载页获取离线包放入主题目录即可。",
                "code_label": "INSTALL PATH · 放入 Vault 主题目录",
                "code": """# 1. 下载离线包并解压（或克隆 GitHub 仓库）
git clone https://github.com/Anarcadia/chuanban-notionlikeHC.git

# 2. 将包含 theme.css 与 manifest.json 的目录放入你的 Obsidian 库：
<你的Vault>/.obsidian/themes/chuanban-notionlikeHC/

# 3. 在 Obsidian 打开：设置 → 外观 → 主题 → 选择 chuanban-notionlikeHC
# 推荐：在「设置 → 界面 → 窗口边框样式」选择「隐藏标题栏」，顶部侧栏过渡更整齐。""",
            }
        ],
        "callout": "<strong>安装说明：</strong>本主题为独立皮肤，暂未推送至 Obsidian 官方社区主题商店。请直接点击下方「进入资源下载页」获取离线压缩包或通过 GitHub 仓库下载。",
        "download_intro": "提供 GitHub 仓库源码 ZIP 直链、配套更纱黑体镜像与飞书国内免代理下载页。",
        "downloads": [
            {
                "name": "主题本体 · chuanban-notionlikeHC (v0.3.2)",
                "meta": "v0.3.2 · 含 theme.css 与 manifest.json",
                "desc": "解压后将整个 chuanban-notionlikeHC/ 文件夹放入 <你的Vault>/.obsidian/themes/ 即可在设置中启用。",
                "mirrors": [
                    ("GitHub 源码包直下 (.zip)", "GITHUB", "https://github.com/Anarcadia/chuanban-notionlikeHC/archive/refs/heads/main.zip", True),
                    ("飞书国内免代理下载页", "FEISHU", "https://www.feishu.cn/wiki/TKE6wWDO1iUuTDkrEuacVlDTn1b", False),
                    ("GitHub 仓库主页", "REPO", "https://github.com/Anarcadia/chuanban-notionlikeHC", False),
                ],
            },
            {
                "name": "可选配套字体 · 更纱黑体中文拆分包 (v1.0.43)",
                "meta": "170.4 MB · SarasaUiSC + SarasaMonoSlabSC",
                "desc": "如需推荐的更纱黑体中文与代码块等宽排版，可按需下载安装至系统字库后重启 Obsidian（macOS 可用 brew install --cask font-sarasa-gothic）。",
                "mirrors": [
                    ("GitHub 字体镜像直下", "GITHUB", "https://github.com/Anarcadia/chuanban-antigravity-theme-patch/releases/download/fonts-sarasa-v1.0.43/Windows-Sarasa-Split-SC-TTF-v1.0.43.zip", True),
                    ("Google Drive 公开分流", "DRIVE", "https://drive.google.com/file/d/1iVVvZXtwUcDiHy42tJ25X6N-JlOf3l7A/view?usp=sharing", False),
                    ("飞书国内免代理页", "FEISHU", "https://www.feishu.cn/wiki/TKE6wWDO1iUuTDkrEuacVlDTn1b", False),
                ],
            },
        ],
        "download_commands": [
            ("一键克隆至本地 Obsidian 主题目录", 'git clone https://github.com/Anarcadia/chuanban-notionlikeHC.git "<你的Vault>/.obsidian/themes/chuanban-notionlikeHC"'),
        ],
    },
    {
        "slug": "dsh-writing-suite",
        "title": "DSH 写作主题综合包",
        "en_subtitle": "My DeepSeek Harness writing workbench: a muted-gold textured theme and a pure writing environment plugin that clears built-in prompts or injects pro-writer and uncensored creative prompts.",
        "version": "v0.1.2 + v0.3.0",
        "tags": {
            "distribution": ["GitHub CC BY-NC-SA 4.0"],
            "platform": "DeepSeek Harness",
            "kind": "一体化环境包",
        },
        "summary": "我的 DeepSeek Harness 写作台，包含暗金色质感皮肤和纯净写作环境插件——可把内置提示词清零或者植入专业作家、破限提示词等等。",
        "lead": "我的 DeepSeek Harness 写作台，包含暗金色质感皮肤和纯净写作环境插件——可把内置提示词清零或者植入专业作家、破限提示词等等。",
        "thumb": "/assets/projects/dsh-writing/screenshot-preview.webp",
        "github_url": "https://github.com/Anarcadia/chuanban-dsh-theme",
        "github_label": "Anarcadia/chuanban-dsh-theme",
        "extra_links": [
            ("纯净写作模式仓库 (chuanban-dsh-writingset)", "https://github.com/Anarcadia/chuanban-dsh-writingset"),
        ],
        "feishu_doc_url": "https://www.feishu.cn/wiki/SycGwfprLiEeHZkOyw0cNXEYnCg",
        "feishu_dl_url": "https://www.feishu.cn/wiki/P8OnwniD4ice1FkETAxc0j6Vneg",
        "gallery": [
            ("/assets/projects/dsh-writing/screenshot-preview.webp", "1. 暖纸阅读皮肤主界面（chuanban-dsh-theme · 三级暖纸色阶与内嵌可变字体）"),
            ("/assets/projects/dsh-writing/screenshot-session.webp", "2. 纯净写作协作模式 + 暖纸皮肤联动实机效果"),
            ("/assets/projects/dsh-writing/screenshot-settings.webp", "3. 写作模式后台设置面板（四套沉浸预设与工作区文档注入开关）"),
        ],
        "features": [
            ("暖纸皮肤：三级暖纸色阶与零轮询注入", "燕麦暖灰侧栏 (#F1EEE7) ↔ 暖白纸主阅读区 (#FBF9F5) ↔ 陶土暖光聚焦输入卡 (#FFFFFF)，通过官方 ctx.theme.overrideTokens 一次性注入 80 个设计 Token，静止与流式对话零轮询开销。"),
            ("暖纸皮肤：内嵌三款 Anthropic 可变字体", "自 v0.1.1 起通过 WOFF2 Base64 内嵌 Anthropic Sans / Serif / Mono Web（wght 300..800），macOS 与 Windows 装完即刻呈现原汁原味西文排版，免手动装西文字体。"),
            ("纯净写作模式：首轮直降 80%+ Token 消耗", "彻底砍掉 DSH 原生编程提示词与冗余工程工具（零 Shell 命令执行通道），首轮系统输入仅约 1,196 tokens，告别 AI 写小说时的“程序员肌肉记忆”。"),
            ("纯净写作模式：写作者专属工具集与 Word 双向桥", "收束为基础读写（read/write/edit）、只读检索（glob/grep）、安全可恢复文件整理（copy/move/trash/stat）与零依赖 Word 稿件双向桥（docx ↔ md），叠加三层提示词积木。"),
        ],
        "table": None,
        "install_blocks": [
            {
                "title": "方式 A：DSH Desktop 桌面端在线一键安装（推荐）",
                "desc": "打开 DSH 桌面端「设置 → 插件」，依次粘贴下方两个 GitHub Release 最新直链安装即可；关闭开关可随时热切回官方原皮。",
                "code_label": "DSH DESKTOP · 插件安装 URL",
                "code": """https://github.com/Anarcadia/chuanban-dsh-theme/releases/latest/download/chuanban-dsh-theme.tgz
https://github.com/Anarcadia/chuanban-dsh-writingset/releases/latest/download/chuanban-dsh-writingset.tgz""",
            },
            {
                "title": "方式 B：DSH Web / CLI 命令行一条命令全装",
                "desc": "使用提示：① 建议将 DSH 外观模式固定为浅色（Light）；② 若此前手动填过自定义字体名，请清空恢复默认以免覆盖内嵌三层字体栈。",
                "code_label": "DSH CLI · 一键安装双插件",
                "code": """dsh plugin --profile web add \\
  https://github.com/Anarcadia/chuanban-dsh-writingset/releases/latest/download/chuanban-dsh-writingset.tgz \\
  https://github.com/Anarcadia/chuanban-dsh-theme/releases/latest/download/chuanban-dsh-theme.tgz""",
            },
        ],
        "callout": "<strong>兼容提示：</strong>写作模式支持可选叠加工作区 <code>AGENTS.md</code> / <code>CLAUDE.md</code>，不与本地 Skill 冲突；建议不要与其他改写初始系统提示词的写作插件同时开启。",
        "download_intro": "提供 GitHub Release 最新 `.tgz` 直链（支持桌面端/CLI 直接在线安装）、离线包与飞书国内免代理分流页。",
        "downloads": [
            {
                "name": "组件一：暖纸外观皮肤 · chuanban-dsh-theme.tgz (v0.1.2)",
                "meta": "v0.1.2 · 784 KB · 内嵌 3 款 Anthropic WOFF2 可变字体",
                "desc": "仿 Claude Desktop 暖纸阅读与写作外观皮肤，开箱即用免手动安装西文字体。",
                "mirrors": [
                    ("GitHub Release 直下 (.tgz)", "GITHUB", "https://github.com/Anarcadia/chuanban-dsh-theme/releases/download/v0.1.2/chuanban-dsh-theme-0.1.2.tgz", True),
                    ("飞书国内免代理下载页", "FEISHU", "https://www.feishu.cn/wiki/P8OnwniD4ice1FkETAxc0j6Vneg", False),
                    ("GitHub 仓库源码", "REPO", "https://github.com/Anarcadia/chuanban-dsh-theme", False),
                ],
            },
            {
                "name": "组件二：纯净写作模式 · chuanban-dsh-writingset.tgz (v0.3.0)",
                "meta": "v0.3.0 · 47 KB · 文件整理 + Word 双向桥",
                "desc": "清零编程提示词噪声，收束为面向长篇写作者的本地读写、安全回收整理与 docx ↔ md 双向桥工具集。",
                "mirrors": [
                    ("GitHub Release 直下 (.tgz)", "GITHUB", "https://github.com/Anarcadia/chuanban-dsh-writingset/releases/download/v0.3.0/chuanban-dsh-writingset.tgz", True),
                    ("飞书国内免代理下载页", "FEISHU", "https://www.feishu.cn/wiki/P8OnwniD4ice1FkETAxc0j6Vneg", False),
                    ("GitHub 仓库源码", "REPO", "https://github.com/Anarcadia/chuanban-dsh-writingset", False),
                ],
            },
            {
                "name": "可选代码块字体 · 更纱黑体等宽拆分包 (v1.0.43)",
                "meta": "170.4 MB · 含 SarasaMonoSlabSC 严格 1:2 对齐",
                "desc": "如需代码块与终端实现严格 1:2 中西文等宽对齐，按需下载安装即可。",
                "mirrors": [
                    ("GitHub 字体镜像直下", "GITHUB", "https://github.com/Anarcadia/chuanban-antigravity-theme-patch/releases/download/fonts-sarasa-v1.0.43/Windows-Sarasa-Split-SC-TTF-v1.0.43.zip", True),
                    ("Google Drive 公开分流", "DRIVE", "https://drive.google.com/file/d/1iVVvZXtwUcDiHy42tJ25X6N-JlOf3l7A/view?usp=sharing", False),
                    ("飞书国内免代理页", "FEISHU", "https://www.feishu.cn/wiki/P8OnwniD4ice1FkETAxc0j6Vneg", False),
                ],
            },
        ],
        "download_commands": [
            ("本地离线包安装命令（DSH CLI）", "dsh plugin --profile web add ./chuanban-dsh-theme-0.1.2.tgz ./chuanban-dsh-writingset.tgz"),
        ],
    },
    {
        "slug": "obsidian-chuanban",
        "title": "书卷风 Obsidian 主题",
        "en_subtitle": "Warm Ivory & Oatmeal Literary Theme (Official Lite v1.0.4 & Full Suite)",
        "version": "v1.0.4 / 全装套件",
        "tags": {
            "distribution": ["GitHub CC BY-NC-SA 4.0", "全功能私人安装包"],
            "platform": "Obsidian",
            "kind": "皮肤",
        },
        "summary": "暖白象牙 × 燕麦纸感长文写作皮肤，配陶土强调色与高密度悬浮预览卡。简装版可在 Obsidian 官方商店搜 chuanban 直接安装；下载页提供含切换插件与全套字体的离线全装版。",
        "lead": "专为小说作者、专栏作家与深度长文写作者打磨的暖白象牙 × 燕麦纸感书卷风 Obsidian 主题，融合微暖纸面、陶土强调色、活字微润墨质感与固定高信息量悬浮预览卡。",
        "thumb": "/assets/projects/chuanban-obsidian/screenshot.webp",
        "github_url": "https://github.com/Anarcadia/obsidian-chuanban-theme",
        "github_label": "Anarcadia/obsidian-chuanban-theme",
        "extra_links": [
            ("Obsidian 官方商店 (chuanban)", "https://community.obsidian.md/themes/chuanban"),
            ("全功能套件仓库 (obsidian-chuanban-suite)", "https://github.com/Anarcadia/obsidian-chuanban-suite"),
        ],
        "feishu_doc_url": "https://www.feishu.cn/wiki/FY2twgUcNid5fTkhyJNc1e9gnYd",
        "feishu_dl_url": "https://www.feishu.cn/wiki/JrfuwEtziigNMskRLFIcpNYJnJg",
        "gallery": [
            ("/assets/projects/chuanban-obsidian/screenshot.webp", "书卷风 Obsidian 主题实机效果：暖白象牙纸面、燕麦侧栏与高密度悬浮预览卡"),
        ],
        "features": [
            ("暖白象牙与燕麦纸感色系", "主阅读画布 #FCFCFB 消除冷白刺眼感，燕麦暖灰侧栏 #F7F5F0 搭配 #ECE9E1 激活胶囊、陶土强调色 #D97757、鼠尾草绿划词选区与琥珀暖黄高亮。"),
            ("双排版预设一键切换", "内置「更纱打字机体（行高 1.78 + 0.25px 微润墨柔化）」与「经典书卷宋体（Songti SC 全角方块排布，行高 1.68）」，全装版附带左侧栏书本图标一键秒切插件。"),
            ("解耦式高密度悬浮预览卡", "锁定 13px / 1.52 行高与 440×360px 视口，自动隐藏 YAML 属性区；全装版附带 page-preview.json 实现左侧文件列表无修饰键悬停即见正文。"),
            ("全平台细节打磨 (v1.0.4)", "修复 Windows 裸机退化细宋体问题，全面打通 Obsidian 原生字体选择器，完整适配 Windows / Linux / macOS 隐藏标题栏窗口按钮安全区。"),
        ],
        "table": {
            "heading": "官方主题商店「简装版」 vs 船板「全装套件版」核心区别",
            "headers": ["对比维度", "官方商店简装版（搜 chuanban）", "船板全功能全装套件（见资源下载页）"],
            "rows": [
                ["包含内容", "官方市场合规纯 CSS 主题（不含插件与专有字体）", "主题本体 + 一键切换插件 + 5 款 Anthropic 字体 + 预览配置 + 自动安装脚本"],
                ["西文字体表现", "开源 / 系统字体回退（Inter / SF Pro / JetBrains Mono）", "内置 5 款 Anthropic Sans / Serif / Mono 原厂 .ttf，脚本离线注册"],
                ["双排版切换", "通过 Style Settings 或单篇 YAML 写入 cssclasses", "内置 chuanban-preset-switcher 插件，左侧栏书本图标一键秒切"],
                ["悬浮预览卡", "包含基础样式（按住 Cmd/Ctrl 悬停触发）", "附带 page-preview.json，左侧文件列表无修饰键直接悬停预览"],
                ["部署门槛", "Obsidian 内点击安装，10 秒开箱", "解压后丢给本地 AI 助手或运行 python3 install_auto.py 自动无损激活"],
            ],
        },
        "install_blocks": [
            {
                "title": "极简体验：Obsidian 官方商店 10 秒安装（简装版）",
                "desc": "如果只想先快速体验暖纸视觉，直接在 Obsidian 内搜索安装即可；需要全套插件与原厂字体请前往「资源下载页」获取全装套件。",
                "code_label": "OBSIDIAN STORE · 官方简装版安装路径",
                "code": """1. 打开 Obsidian → 设置 (Settings) → 外观 (Appearance) → 主题 (Themes) → 管理 (Manage)
2. 搜索：chuanban → 点击「安装并使用」
3. 如需在简装版切换「更纱打字机体 ⇄ 经典书卷宋体」，可安装 Style Settings 插件进入 chuanban → Typography Preset，或在笔记 Front Matter 写入：
   cssclasses: [preset-songti-serif]""",
            }
        ],
        "callout": "<strong>全装版一键无损激活：</strong>全装套件内置 <code>install_auto.py</code> 与《给 AI 助手看的零门槛一键安装引导》，安装前自动备份原有配置，不会覆盖你的个人笔记与插件设置。",
        "download_intro": "按需选择：Obsidian 官方商店简装版（纯 CSS v1.0.4），或含 5 款原厂字体 + 切换插件 + 自动脚本的完整离线套件。",
        "downloads": [
            {
                "name": "全功能离线套件版 · chuanban Full Suite (v1.0.0)",
                "meta": "含主题 + preset-switcher 插件 + 5 款 Anthropic 字体 + 自动脚本",
                "desc": "船板自用满血工作台完整打包，支持解压后运行 python3 install_auto.py 或直接交给本地 AI 助手一键无损部署。",
                "mirrors": [
                    ("Google Drive 完整套件直下", "DRIVE", "https://drive.google.com/file/d/1SS9JRWugvoW5AJdTprUjv_P2EVu0bICc/view?usp=sharing", True),
                    ("GitHub Release (v1.0.0)", "GITHUB", "https://github.com/Anarcadia/obsidian-chuanban-suite/releases/download/v1.0.0/chuanban-obsidian-full-suite-v1.0.0.zip", False),
                    ("飞书国内免代理下载页", "FEISHU", "https://www.feishu.cn/wiki/JrfuwEtziigNMskRLFIcpNYJnJg", False),
                ],
            },
            {
                "name": "官方商店简装版（纯 CSS 合规版 · v1.0.4）",
                "meta": "v1.0.4 · Obsidian 官方社区主题商店已上架",
                "desc": "100% 纯 CSS 主题，适合想 10 秒即装即用、或偏好通过 Obsidian 官方商店自动更新的用户。",
                "mirrors": [
                    ("Obsidian 官方主题商店", "STORE", "https://community.obsidian.md/themes/chuanban", True),
                    ("GitHub Release (1.0.4)", "GITHUB", "https://github.com/Anarcadia/obsidian-chuanban-theme/releases/tag/1.0.4", False),
                ],
            },
            {
                "name": "配套更纱打字机体 · SarasaMonoSlabSC (v1.0.43)",
                "meta": "170.4 MB · 中文等距打字机排版",
                "desc": "用于默认「更纱打字机体」预设的中文等距字体包（macOS 亦可直接运行 brew install --cask font-sarasa-gothic）。",
                "mirrors": [
                    ("GitHub 字体镜像直下", "GITHUB", "https://github.com/Anarcadia/chuanban-antigravity-theme-patch/releases/download/fonts-sarasa-v1.0.43/Windows-Sarasa-Split-SC-TTF-v1.0.43.zip", True),
                    ("Google Drive 公开分流", "DRIVE", "https://drive.google.com/file/d/1iVVvZXtwUcDiHy42tJ25X6N-JlOf3l7A/view?usp=sharing", False),
                    ("飞书国内免代理页", "FEISHU", "https://www.feishu.cn/wiki/JrfuwEtziigNMskRLFIcpNYJnJg", False),
                ],
            },
        ],
        "download_commands": [
            ("全装套件解压后自动无损部署", "python3 install_auto.py"),
        ],
    },
]

SKILLS = [
    {
        "title": "网文拆书分析 Skills",
        "repo_name": "Anarcadia/chuanban-chaishu-skills",
        "url": "https://github.com/Anarcadia/chuanban-chaishu-skills",
        "tags": {
            "distribution": ["GitHub CC BY-NC-SA 4.0"],
            "platform": "通用 Agent",
            "kind": "工作流 Skill",
        },
        "paragraphs": [
            "小说拆书 Skill 基座，为 Claude Code 适配。",
            "本意为建立长篇小说真实、可信、无幻觉的全景图（以细颗粒度的章节概要组成），而非执行花里胡哨的小说创作维度的分析（诸如节奏、爽点分层、情绪等）。个人对这些高层次分析并不信任，所以并没去花力气开发，只建立了基于最简单判定规则的 ABC 三类爽点判断。",
            "拿到 Skill 之后，如果对分析功能不满意，可以自己 DIY 加上想要的分析组件，命令 AI 必须建立调研计划，回到原文去查阅后再制作分析报告。",
        ],
    },
    {
        "title": "仿 Perplexity 杂志风本地深度研究",
        "repo_name": "Anarcadia/local-deep-research-perplexity-magazine-style",
        "url": "https://github.com/Anarcadia/local-deep-research-perplexity-magazine-style",
        "tags": {
            "distribution": ["GitHub CC BY-NC-SA 4.0"],
            "platform": "通用 Agent",
            "kind": "工作流 Skill",
        },
        "paragraphs": [
            "手搓的模仿 Perplexity 的深度研究文章创作流程。主要使用 Codex 逆向分析 Perplexity 网页 Deep Research Agent 的调研流程行为模式得出调研部分机制，而撰写部分则由自己选定符合口味的模型和提示词确定风格。",
            "这个 Skill 的目的不是去做严谨、学术化、以最高可验证性和准确率为目标的学术型 Deep Research（所以不适合给学术用户或专业研报使用），而是为了写出一般人易读、爱读的知识性文章，让读者获得优质的学习与阅读体验，避免受到严重的 AI 写作风味干扰。",
            "现阶段调研流程已经足够好用，写作思路和风格控制仍在持续迭代优化中。",
        ],
    },
    {
        "title": "日语长篇小说精翻工作流",
        "repo_name": "Anarcadia/chuanban-jp-novel-translator",
        "url": "https://github.com/Anarcadia/chuanban-jp-novel-translator",
        "tags": {
            "distribution": ["GitHub CC BY-NC-SA 4.0"],
            "platform": "通用 Agent",
            "kind": "工作流 Skill",
        },
        "paragraphs": [
            "日语小说精翻流程。长期作为个人译者自 DIY、自维护使用，实际已完成翻译超过 10 本小说、累计 200 万字，主要使用 Claude Opus 4.6 与 DeepSeek V4 Pro 执行翻译，成稿效果令人满意。",
            "目前正在制作适配 Proma 的新版本，重点优化子进程模型调用以及术语表一致性规则。",
        ],
    },
]


# 检验标签白名单与扩展说明：
# 1. distribution（多选）："GitHub <开源协议>"（如 "GitHub MIT" / "GitHub CC BY-NC-SA 4.0"）/ "全功能私人安装包"
# 2. platform（单选）："Antigravity" / "Obsidian" / "DeepSeek Harness" / "通用 Agent"（支持未来随时扩展新平台）
# 3. kind（单选）："皮肤" / "工作流 Skill" / "一体化环境包"
VALID_KINDS = {"皮肤", "工作流 Skill", "一体化环境包"}

# 真实品牌图标（本地静态资源）与通用表意矢量图标（Inline SVG）
PLATFORM_IMG_ICONS = {
    "Antigravity": "/assets/projects/icons/antigravity.png",
    "Obsidian": "/assets/projects/icons/obsidian.png",
    "DeepSeek Harness": "/assets/projects/icons/dsh.png",
}

SVG_GENERIC_AGENT = (
    '<span class="badge-icon" aria-hidden="true">'
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">'
    '<path d="M9.937 15.5A2 2 0 0 0 8.5 14.063l-6.135-1.582a.5.5 0 0 1 0-.962L8.5 9.936A2 2 0 0 0 9.937 8.5l1.582-6.135a.5.5 0 0 1 .963 0L14.063 8.5A2 2 0 0 0 15.5 9.937l6.135 1.581a.5.5 0 0 1 0 .964L15.5 14.063a2 2 0 0 0-1.437 1.437l-1.582 6.135a.5.5 0 0 1-.963 0z"/>'
    '<path d="M20 3v4"/><path d="M22 5h-4"/>'
    '</svg></span>'
)

SVG_GENERIC_PLATFORM = (
    '<span class="badge-icon" aria-hidden="true">'
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">'
    '<rect x="3" y="4" width="18" height="14" rx="2"/><path d="M8 20h8"/><path d="M12 18v2"/>'
    '</svg></span>'
)

KIND_SVG_ICONS = {
    "皮肤": (
        '<span class="badge-icon" aria-hidden="true">'
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">'
        '<circle cx="13.5" cy="6.5" r=".6" fill="currentColor"/><circle cx="17.5" cy="10.5" r=".6" fill="currentColor"/>'
        '<circle cx="8.5" cy="7.5" r=".6" fill="currentColor"/><circle cx="6.5" cy="12.5" r=".6" fill="currentColor"/>'
        '<path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10c.926 0 1.648-.746 1.648-1.688 0-.437-.18-.835-.437-1.125-.29-.289-.438-.652-.438-1.125a1.64 1.64 0 0 1 1.668-1.668h1.996c3.051 0 5.555-2.503 5.555-5.554C21.965 6.012 17.461 2 12 2z"/>'
        '</svg></span>'
    ),
    "工作流 Skill": (
        '<span class="badge-icon" aria-hidden="true">'
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">'
        '<rect x="3" y="3" width="6" height="6" rx="1"/><rect x="15" y="15" width="6" height="6" rx="1"/>'
        '<rect x="15" y="3" width="6" height="6" rx="1"/><path d="M9 6h6"/><path d="M6 9v6a3 3 0 0 0 3 3h6"/>'
        '</svg></span>'
    ),
    "一体化环境包": (
        '<span class="badge-icon" aria-hidden="true">'
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">'
        '<path d="m12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.91a2 2 0 0 0 1.66 0l8.58-3.9a1 1 0 0 0 0-1.83Z"/>'
        '<path d="m22 12.65-9.17 4.16a2 2 0 0 1-1.66 0L2 12.65"/>'
        '<path d="m22 17.65-9.17 4.16a2 2 0 0 1-1.66 0L2 17.65"/>'
        '</svg></span>'
    ),
}

SVG_GITHUB = (
    '<span class="badge-icon" aria-hidden="true">'
    '<svg viewBox="0 0 24 24" fill="currentColor">'
    '<path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/>'
    '</svg></span>'
)

SVG_PRIVATE_PKG = (
    '<span class="badge-icon" aria-hidden="true">'
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">'
    '<path d="M16.5 9.4 7.55 4.24"/>'
    '<path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/>'
    '<polyline points="3.29 7 12 12 20.71 7"/><line x1="12" y1="22" x2="12" y2="12"/>'
    '</svg></span>'
)


def e(text: str) -> str:
    return html.escape(text, quote=True)


def render_tags(tags: dict) -> str:
    platform = str(tags.get("platform") or "").strip()
    kind = str(tags.get("kind") or "").strip()
    dists = list(tags.get("distribution") or [])
    if not platform:
        raise ValueError("Project tag missing required single-select 'platform'")
    if kind not in VALID_KINDS:
        raise ValueError(f"Invalid project kind: {kind!r}; expected one of {VALID_KINDS}")
    if not dists or any(
        d != "全功能私人安装包" and not d.startswith("GitHub ")
        for d in dists
    ):
        raise ValueError(f"Invalid project distribution: {dists!r}; expected 'GitHub <LICENSE>' or '全功能私人安装包'")

    if platform in PLATFORM_IMG_ICONS:
        p_icon = f'<img class="badge-icon-img" src="{PLATFORM_IMG_ICONS[platform]}" alt="" width="15" height="15" decoding="async" />'
    elif platform == "通用 Agent":
        p_icon = SVG_GENERIC_AGENT
    else:
        p_icon = SVG_GENERIC_PLATFORM

    k_icon = KIND_SVG_ICONS[kind]

    items = [
        f'<span class="badge badge--platform" title="面向平台：{e(platform)}">{p_icon}<span>{e(platform)}</span></span>',
        f'<span class="badge badge--kind" title="工具属性：{e(kind)}">{k_icon}<span>{e(kind)}</span></span>',
    ]
    for d in dists:
        if d == "全功能私人安装包":
            items.append(
                f'<span class="badge badge--cinnabar" title="分发形态：GitHub 之外额外提供全功能私人安装包">{SVG_PRIVATE_PKG}<span>含全功能私人安装包</span></span>'
            )
        else:
            items.append(
                f'<span class="badge badge--open" title="分发形态：{e(d)}">{SVG_GITHUB}<span>{e(d)}</span></span>'
            )
    return "".join(items)


def render_shell(
    *,
    title: str,
    description: str,
    canonical: str,
    back_href: str | None,
    back_label: str,
    body_html: str,
) -> str:
    top_back_html = (
        f'\n        <a href="{e(back_href)}" class="nav-back"><span class="arrow-glyph">←</span> {e(back_label)}</a>'
        if back_href and back_label
        else ""
    )
    return f"""<!DOCTYPE html>
<html lang="zh-Hans">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{e(title)}</title>
  <meta name="description" content="{e(description)}" />
  <link rel="canonical" href="{e(canonical)}" />

  <meta property="og:type" content="website" />
  <meta property="og:url" content="{e(canonical)}" />
  <meta property="og:title" content="{e(title)}" />
  <meta property="og:description" content="{e(description)}" />

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=Noto+Serif+SC:wght@300;400;500&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="/assets/projects/projects.css?v=20261126c" />
</head>
<body>
{XUAN_SVG}

  <div class="page-frame">
    <header class="utility-bar">
      <a href="/" class="seal-mark" aria-label="The Plank of Theseus">
        <span class="cinnabar-seal" title="船板">船</span>
        <span class="seal-caption">THE PLANK OF THESEUS</span>
      </a>
      <div class="utility-actions">{top_back_html}
        <button class="theme-btn" id="themeBtn" type="button" aria-label="Toggle Ink Mode">夜砚 · Ink</button>
      </div>
    </header>

    <main>
{body_html}
    </main>

    <footer class="foot">
      <span>© Chuanban · 忒修斯的船板</span>
      <span>Monochrome Ink &amp; Raw Xuan</span>
    </footer>
  </div>

  <script src="/assets/projects/projects.js"></script>
</body>
</html>
"""


def build_index() -> str:
    tool_rows = []
    for t in TOOLS:
        badges_html = render_tags(t["tags"])
        data_platform = e(t["tags"]["platform"])
        data_kind = e(t["tags"]["kind"])
        data_dist = e(",".join(t["tags"]["distribution"]))
        detail_url = f"/projects/{t['slug']}/"
        dl_url = f"/projects/{t['slug']}/download/"
        tool_rows.append(
            f"""          <article class="tool-row" data-platform="{data_platform}" data-kind="{data_kind}" data-dist="{data_dist}">
            <a class="tool-thumb-link" href="{detail_url}" aria-label="查看 {e(t['title'])} 介绍">
              <div class="tool-thumb-mat">
                <img src="{t['thumb']}" alt="{e(t['title'])} 实机截图" loading="lazy" decoding="async" />
              </div>
            </a>
            <div class="tool-row-body">
              <div class="tool-badges">{badges_html}</div>
              <h3 class="tool-row-title"><a href="{detail_url}">{e(t['title'])}</a></h3>
              <p class="tool-row-en">{e(t['en_subtitle'])}</p>
              <p class="tool-row-desc">{e(t['summary'])}</p>
              <div class="tool-row-actions">
                <a class="btn btn--primary" href="{detail_url}">查看详细介绍 <span class="arrow-glyph">→</span></a>
                <a class="btn btn--cinnabar" href="{dl_url}">多源资源下载 <span class="arrow-glyph">↓</span></a>
                <a class="btn" href="{e(t['github_url'])}" target="_blank" rel="noopener">GitHub <span class="arrow-glyph">↗</span></a>
              </div>
            </div>
          </article>"""
        )

    skill_rows = []
    for s in SKILLS:
        badges_html = render_tags(s["tags"])
        data_platform = e(s["tags"]["platform"])
        data_kind = e(s["tags"]["kind"])
        data_dist = e(",".join(s["tags"]["distribution"]))
        paras_html = "\n".join(f"              <p>{e(p)}</p>" for p in s["paragraphs"])
        skill_rows.append(
            f"""          <article class="skill-item" data-platform="{data_platform}" data-kind="{data_kind}" data-dist="{data_dist}">
            <div class="skill-meta">
              <div class="tool-badges">{badges_html}</div>
              <h3 class="skill-name">{e(s['title'])}</h3>
              <p class="skill-slug">{e(s['repo_name'])}</p>
            </div>
            <div class="skill-prose">
{paras_html}
              <a class="btn" href="{e(s['url'])}" target="_blank" rel="noopener">访问 GitHub 仓库 <span class="arrow-glyph">↗</span></a>
            </div>
          </article>"""
        )

    body = f"""      <section class="page-masthead" aria-label="Projects Title Banner">
        <a href="/" class="page-back-btn" aria-label="Back to The Plank of Theseus 主页">
          <span class="page-back-arrow" aria-hidden="true">←</span>
          <span>Back</span>
        </a>
        <div class="page-side">
          <h1 class="page-zh">船板写作工具集</h1>
          <p class="page-meta">PLANKOFTHESEUS.COM / PROJECTS</p>
        </div>
      </section>

      <section class="intro-band" aria-label="Collection Overview">
        <div class="intro-inner">
          <p class="intro-en">
            Writing workflows, Skills, themes, and handy utilities — built and used daily by Chuanban.
          </p>
          <p class="intro-zh">
            船板亲自使用、开发的写作工作流、Skill、皮肤和便利化小工具。
          </p>
        </div>
      </section>

      <section class="section-block" aria-label="Client Themes and Writing Suites">
        <div class="section-header">
          <h2 class="section-title">客户端美化与写作主题</h2>
          <span class="section-sub">05 TOOLS · LANDING + MULTI-MIRROR DOWNLOADS</span>
        </div>
        <div class="tool-waterfall">
{chr(10).join(tool_rows)}
        </div>
      </section>

      <section class="section-block" aria-label="AI Writing and Research Skills">
        <div class="section-header">
          <h2 class="section-title">AI 写作与研究工作流 Skills</h2>
          <span class="section-sub">03 OPEN-SOURCE WORKFLOWS · GITHUB</span>
        </div>
        <div class="skill-list">
{chr(10).join(skill_rows)}
        </div>
      </section>

      <div class="ref-strip">
        <a href="/" class="ref-link"><span class="arrow-glyph">←</span> Back to The Plank of Theseus · 返回船板主页</a>
        <a href="{FEISHU_HUB_URL}" target="_blank" rel="noopener" class="ref-link">飞书公开知识库国内镜像（免代理） <span class="arrow-glyph">↗</span></a>
        <a href="https://github.com/Anarcadia" target="_blank" rel="noopener" class="ref-link">GitHub · @Anarcadia <span class="arrow-glyph">↗</span></a>
      </div>"""

    return render_shell(
        title="My Project · 船板写作工具集 — The Plank of Theseus",
        description="船板亲自使用、开发的写作工作流、Skill、皮肤和便利化小工具。 (Writing workflows, Skills, themes, and handy utilities — built and used daily by Chuanban.)",
        canonical="https://plankoftheseus.com/projects/",
        back_href=None,
        back_label="",
        body_html=body,
    )


def build_detail(idx: int, t: dict) -> str:
    dl_url = f"/projects/{t['slug']}/download/"
    badges_html = render_tags(t["tags"])
    extra_btns = "".join(
        f'<a class="btn" href="{e(url)}" target="_blank" rel="noopener">{e(label)} <span class="arrow-glyph">↗</span></a>'
        for label, url in t["extra_links"]
    )

    gallery_cls = "gallery-grid gallery-grid--single" if len(t["gallery"]) == 1 else "gallery-grid"
    gallery_items = []
    for src, caption in t["gallery"]:
        gallery_items.append(
            f"""          <figure class="gallery-figure">
            <div class="gallery-mat" data-full="{src}" data-caption="{e(caption)}" title="点击放大查看高清实机图">
              <img src="{src}" alt="{e(caption)}" loading="lazy" decoding="async" />
            </div>
            <figcaption class="gallery-caption">{e(caption)}</figcaption>
          </figure>"""
        )

    feat_cards = "\n".join(
        f"""          <li class="feature-card">
            <h3>{e(ft)}</h3>
            <p>{e(fd)}</p>
          </li>"""
        for ft, fd in t["features"]
    )

    table_section = ""
    if t["table"]:
        tb = t["table"]
        ths = "".join(f"<th>{e(h)}</th>" for h in tb["headers"])
        trs = "\n".join(
            "              <tr>" + "".join(f"<td>{e(cell)}</td>" for cell in row) + "</tr>"
            for row in tb["rows"]
        )
        table_section = f"""
      <section class="content-section">
        <h2>{e(tb['heading'])}</h2>
        <div class="table-wrap">
          <table class="ink-table">
            <thead><tr>{ths}</tr></thead>
            <tbody>
{trs}
            </tbody>
          </table>
        </div>
      </section>"""

    install_parts = []
    for bi, blk in enumerate(t["install_blocks"]):
        cid = f"code-{t['slug']}-{bi}"
        install_parts.append(
            f"""        <h3>{e(blk['title'])}</h3>
        <p>{e(blk['desc'])}</p>
        <div class="code-box">
          <div class="code-box-head">
            <span>{e(blk['code_label'])}</span>
            <button class="copy-btn" type="button" data-copy-target="{cid}">复制内容</button>
          </div>
          <pre id="{cid}"><code>{e(blk['code'])}</code></pre>
        </div>"""
        )

    prev_link = ""
    if idx > 0:
        pt = TOOLS[idx - 1]
        prev_link = f'<a href="/projects/{pt["slug"]}/" class="ref-link"><span class="arrow-glyph">←</span> 上一款：{e(pt["title"])}</a>'
    else:
        prev_link = '<a href="/projects/" class="ref-link"><span class="arrow-glyph">←</span> 返回全部写作工具</a>'

    next_link = ""
    if idx < len(TOOLS) - 1:
        nt = TOOLS[idx + 1]
        next_link = f'<a href="/projects/{nt["slug"]}/" class="ref-link">下一款：{e(nt["title"])} <span class="arrow-glyph">→</span></a>'
    else:
        next_link = '<a href="/projects/" class="ref-link">查看全部工具与 Skills <span class="arrow-glyph">→</span></a>'

    body = f"""      <nav class="breadcrumb" aria-label="Breadcrumb">
        <a href="/">The Plank of Theseus</a>
        <span class="breadcrumb-sep">/</span>
        <a href="/projects/">My Project · 船板写作工具集</a>
        <span class="breadcrumb-sep">/</span>
        <span>{e(t['title'])}</span>
      </nav>

      <section class="detail-hero">
        <div class="detail-kicker">{badges_html}</div>
        <h1 class="detail-title">{e(t['title'])}</h1>
        <p class="tool-row-en" style="margin-bottom: 16px;">{e(t['en_subtitle'])}</p>
        <p class="detail-lead">{e(t['lead'])}</p>
        <div class="detail-cta-row">
          <a class="btn btn--primary" href="{dl_url}">进入专属资源下载页 <span class="arrow-glyph">→</span></a>
          <a class="btn" href="{e(t['github_url'])}" target="_blank" rel="noopener">GitHub · {e(t['github_label'])} <span class="arrow-glyph">↗</span></a>
          {extra_btns}
          <a class="btn" href="{e(t['feishu_doc_url'])}" target="_blank" rel="noopener">飞书文档版 <span class="arrow-glyph">↗</span></a>
        </div>
      </section>

      <section class="content-section">
        <h2>实机效果预览（点击图片可放大）</h2>
        <div class="{gallery_cls}">
{chr(10).join(gallery_items)}
        </div>
      </section>

      <section class="content-section">
        <h2>核心特性与设计细节</h2>
        <ul class="feature-list">
{feat_cards}
        </ul>
      </section>{table_section}

      <section class="content-section">
        <h2>安装与快速上手</h2>
{chr(10).join(install_parts)}
        <div class="callout">{t['callout']}</div>
      </section>

      <section class="content-section">
        <h2>获取安装包与配套字体</h2>
        <p>所有安装包、字体拆分包及多源高速分流（GitHub Releases / Google Drive / 飞书国内免代理）均集中整理在专属下载页。</p>
        <div class="detail-cta-row">
          <a class="btn btn--cinnabar" href="{dl_url}">打开 {e(t['title'])} 资源下载页 <span class="arrow-glyph">→</span></a>
          <a class="btn" href="{e(t['feishu_dl_url'])}" target="_blank" rel="noopener">飞书国内免代理分流页 <span class="arrow-glyph">↗</span></a>
        </div>
      </section>

      <div class="ref-strip">
        {prev_link}
        {next_link}
      </div>"""

    return render_shell(
        title=f"{t['title']} ({t['version']}) — My Project · The Plank of Theseus",
        description=t.get("seo_description") or t["summary"],
        canonical=f"https://plankoftheseus.com/projects/{t['slug']}/",
        back_href="/projects/",
        back_label="返回工具集",
        body_html=body,
    )


def build_download(t: dict) -> str:
    detail_url = f"/projects/{t['slug']}/"
    dl_cards = []
    for item in t["downloads"]:
        mirrors_html = []
        for label, tag, url, is_primary in item["mirrors"]:
            cls = "mirror-pill mirror-pill--primary" if is_primary else "mirror-pill"
            mirrors_html.append(
                f'<a class="{cls}" href="{e(url)}" target="_blank" rel="noopener"><span class="mirror-tag">{e(tag)}</span> {e(label)} <span class="arrow-glyph">↗</span></a>'
            )
        dl_cards.append(
            f"""          <article class="dl-card">
            <div class="dl-card-head">
              <h3 class="dl-card-title">{e(item['name'])}</h3>
              <span class="dl-card-meta">{e(item['meta'])}</span>
            </div>
            <p class="dl-card-desc">{e(item['desc'])}</p>
            <div class="dl-mirrors">
              {"".join(mirrors_html)}
            </div>
          </article>"""
        )

    cmd_blocks = []
    for ci, (label, cmd) in enumerate(t["download_commands"]):
        cid = f"dlcmd-{t['slug']}-{ci}"
        cmd_blocks.append(
            f"""        <div class="code-box">
          <div class="code-box-head">
            <span>{e(label)}</span>
            <button class="copy-btn" type="button" data-copy-target="{cid}">复制命令</button>
          </div>
          <pre id="{cid}"><code>{e(cmd)}</code></pre>
        </div>"""
        )

    body = f"""      <nav class="breadcrumb" aria-label="Breadcrumb">
        <a href="/">The Plank of Theseus</a>
        <span class="breadcrumb-sep">/</span>
        <a href="/projects/">My Project</a>
        <span class="breadcrumb-sep">/</span>
        <a href="{detail_url}">{e(t['title'])}</a>
        <span class="breadcrumb-sep">/</span>
        <span>资源下载页</span>
      </nav>

      <section class="detail-hero">
        <div class="detail-kicker">
          <span class="badge badge--cinnabar">MULTI-MIRROR DOWNLOAD</span>
          <span class="badge">{e(t['version'])}</span>
        </div>
        <h1 class="detail-title">{e(t['title'])} · 资源下载</h1>
        <p class="detail-lead">{t['download_intro']}</p>
        <div class="detail-cta-row">
          <a class="btn" href="{detail_url}"><span class="arrow-glyph">←</span> 返回产品介绍页</a>
          <a class="btn btn--cinnabar" href="{e(t['feishu_dl_url'])}" target="_blank" rel="noopener">飞书国内免代理分流页（免登录） <span class="arrow-glyph">↗</span></a>
          <a class="btn" href="{e(t['github_url'])}" target="_blank" rel="noopener">GitHub 源码仓库 <span class="arrow-glyph">↗</span></a>
        </div>
      </section>

      <section class="content-section">
        <h2>多源下载清单</h2>
        <div class="download-grid">
{chr(10).join(dl_cards)}
        </div>
        <div class="callout">
          <strong>分流选择建议：</strong>海外或代理通畅环境首选 <strong>GitHub Release</strong> 或 <strong>Google Drive</strong> 直下；国内无代理环境直接点击卡片内的 <strong>飞书国内免代理分流页</strong>，无需登录飞书账号即可浏览器直下全部离线包与配套字体。
        </div>
      </section>

      <section class="content-section">
        <h2>下载后快速安装指令</h2>
{chr(10).join(cmd_blocks)}
      </section>

      <div class="ref-strip">
        <a href="{detail_url}" class="ref-link"><span class="arrow-glyph">←</span> 返回 {e(t['title'])} 介绍页</a>
        <a href="/projects/" class="ref-link">浏览全部写作工具 <span class="arrow-glyph">→</span></a>
      </div>"""

    return render_shell(
        title=f"{t['title']} 资源下载 — My Project · The Plank of Theseus",
        description=f"{t['title']} ({t['version']}) 多源资源下载页：GitHub Releases、Google Drive 与飞书国内免代理分流。",
        canonical=f"https://plankoftheseus.com/projects/{t['slug']}/download/",
        back_href=detail_url,
        back_label="返回产品页",
        body_html=body,
    )


def build_sitemap() -> str:
    urls = [
        ("https://plankoftheseus.com/", "1.0", True),
        ("https://plankoftheseus.com/projects/", "0.9", False),
    ]
    for t in TOOLS:
        urls.append((f"https://plankoftheseus.com/projects/{t['slug']}/", "0.8", False))
        urls.append((f"https://plankoftheseus.com/projects/{t['slug']}/download/", "0.7", False))

    entries = []
    for loc, prio, is_home in urls:
        alts = ""
        if is_home:
            alts = """
    <xhtml:link rel="alternate" hreflang="en" href="https://plankoftheseus.com/" />
    <xhtml:link rel="alternate" hreflang="zh-Hans" href="https://chuanban.cc/" />
    <xhtml:link rel="alternate" hreflang="x-default" href="https://plankoftheseus.com/" />"""
        entries.append(
            f"""  <url>
    <loc>{loc}</loc>{alts}
    <lastmod>{TODAY}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{prio}</priority>
  </url>"""
        )

    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
        '        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + "\n".join(entries)
        + "\n</urlset>\n"
    )


def sync_to_dist() -> None:
    for fname in ("index.html", "sitemap.xml", "llms.txt", "robots.txt"):
        shutil.copy2(ROOT / fname, DIST / fname)
    for dname in ("assets", "projects"):
        src = ROOT / dname
        dst = DIST / dname
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)


def main() -> None:
    # 1. Projects index
    (ROOT / "projects").mkdir(parents=True, exist_ok=True)
    (ROOT / "projects" / "index.html").write_text(build_index(), encoding="utf-8")

    # 2. Detail + Download pages for all 5 tools
    for idx, t in enumerate(TOOLS):
        pdir = ROOT / "projects" / t["slug"]
        ddir = pdir / "download"
        ddir.mkdir(parents=True, exist_ok=True)
        (pdir / "index.html").write_text(build_detail(idx, t), encoding="utf-8")
        (ddir / "index.html").write_text(build_download(t), encoding="utf-8")

    # 3. Update sitemap.xml
    (ROOT / "sitemap.xml").write_text(build_sitemap(), encoding="utf-8")

    # 4. Sync all site assets and pages into dist/
    sync_to_dist()
    print(f"GENERATED_OK: 1 index + {len(TOOLS)} detail + {len(TOOLS)} download pages synced to dist/")


if __name__ == "__main__":
    main()
