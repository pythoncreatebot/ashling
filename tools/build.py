#!/usr/bin/env python3
"""Build the Ashling home page in four languages.

    python3 tools/build.py

Writes index.html (English), zh/index.html, ja/index.html and ko/index.html.
Everything is static: one shared stylesheet, no third-party scripts, no cookies, no tracking.

On launch day put the App Store link in APP_STORE_URL below and run this again.
The "coming soon" label turns into a real download button on all four pages.
"""

from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------------------
# Paste the App Store link here on launch day, e.g. "https://apps.apple.com/app/id0000000000"
APP_STORE_URL = ""
# ---------------------------------------------------------------------------

SITE = "https://pythoncreatebot.github.io/ashling/"
LANGS = ["en", "zh", "ja", "ko"]
HTML_LANG = {"en": "en", "zh": "zh-Hans", "ja": "ja", "ko": "ko"}
DIR = {"en": "", "zh": "zh/", "ja": "ja/", "ko": "ko/"}
SHOTS_DIR = {"en": "en-US", "zh": "zh-Hans", "ja": "ja", "ko": "ko"}
LANG_NAME = {"en": "English", "zh": "简体中文", "ja": "日本語", "ko": "한국어"}
OG_LOCALE = {"en": "en_US", "zh": "zh_CN", "ja": "ja_JP", "ko": "ko_KR"}

SHOT_FILES = ["01-day", "02-near-inside", "03-dawn", "04-near-inside-door", "05-dusk", "06-night"]
SHOT_ALT = {
    "en": ["A tiny world on your windowsill", "Every walk takes it somewhere new",
           "A letter every day, nothing to chase", "Small gifts, brought home from its walks",
           "The light follows your own day", "Quiet company, day and night"],
    "zh": ["窗台上的小小世界", "你走路，它去看新地方", "每天一封信，从不催你",
           "散步带回来的小礼物", "光跟着你的一天慢慢变", "白天夜里，安静地陪着你"],
    "ja": ["窓辺の、小さな世界", "歩くたびに、新しい場所へ", "毎日一通の手紙。急かさない",
           "散歩のおみやげ", "光は、きみの一日といっしょに", "昼も夜も、そっとそばに"],
    "ko": ["창가 위의 작은 세계", "걸을 때마다 새로운 곳으로", "매일 편지 한 통, 재촉하지 않아요",
           "산책에서 가져온 작은 선물", "빛은 당신의 하루를 따라 변해요", "낮에도 밤에도, 조용히 곁에"],
}

FEATURE_ICONS = ["walk", "hourglass", "letter", "sun", "hat", "widget"]

T = {
    "en": {
        "title": "Ashling · a tiny cozy world in a glass jar",
        "meta": "Ashling is a cozy virtual pet for iPhone. A little friend lives in a glass jar on your windowsill: it walks when you walk, writes you letters, and the light follows your day. No ads, no account, no subscription.",
        "h1": "A tiny cozy world in a glass jar.",
        "lead": "A little friend lives on your windowsill. It walks when you walk, rests when you rest, and leaves small gifts by the jar.",
        "soon": "Coming to the App Store",
        "live": "Download on the App Store",
        "when": "Spring 2027 · iPhone",
        "facts": ["Free download", "No ads", "No account", "No subscription"],
        "hero_cap": "The light in the jar follows your real day.",
        "meet_h": "Open the jar, take a breath, set it back.",
        "meet_p": "Ashling lives only on your iPhone. There is no feed to scroll and nothing to keep up with. Open it when you want a quiet moment, then go on with your day.",
        "trailer": "19-second trailer",
        "feat_h": "What lives in the jar",
        "feats": [
            ("Your walks become its walks", "With your permission, Ashling reads your steps from Apple Health. The snow-globe path grows a little further each day, and new plants and places appear."),
            ("Focus without pressure", "On day three an hourglass appears. Each session walks a tiny caravan across the desert, and it brings back a bag of colored sand. No streaks to lose."),
            ("A letter every day", "The little friend writes short letters and leaves instant photos by the jar. Keep them in a small photo book."),
            ("The light follows your day", "Dawn, noon, dusk and night inside the jar match the real clock. At night the windows glow and the island sleeps."),
            ("Hats and instant photos", "Pick a hat for your friend, take your own instant photo of the jar, and share it in one tap."),
            ("Always nearby", "A Home Screen widget, a focus Live Activity on the Lock Screen, and a StandBy night light by your bed."),
        ],
        "shots_h": "A look inside",
        "shots_hint": "Swipe to see more",
        "price_h": "Bought once, kept for good",
        "price_p": "Ashling is free to download. Two optional extras are one-time purchases, never a subscription.",
        "prices": [
            ("The jar, the island and the little friend", "Free"),
            ("Hourglass focus", "One-time purchase. Appears on day 3, and the first session is free."),
            ("Moss jar lid", "One-time purchase."),
        ],
        "priv_h": "Private by design",
        "priv_p": "No account, no server, no ads, no analytics. Your steps are read on your iPhone and never leave it. This website has no trackers or cookies either.",
        "priv_link": "Read the privacy policy",
        "faq_h": "Questions",
        "faq": [
            ("Is it a subscription?", "No. Ashling is free to download. The hourglass and the moss lid are one-time purchases, and Restore Purchases brings them back on a new phone."),
            ("Do I need an account?", "No. There is no sign-in and no server. Everything stays on your iPhone."),
            ("What does it do with my steps?", "With your permission it reads your daily step count from Apple Health to decide how far the little friend walks. It never writes to Health, and the numbers never leave your device. If you say no, the app still works."),
            ("What if I forget to open it for a week?", "Nothing bad happens. The friend doesn't get sick or sad, and nothing is lost. The island simply waits for you."),
            ("Is there an iPad or Android version?", "Ashling is iPhone only at launch."),
            ("When can I get it?", "Ashling is planned for the App Store in spring 2027, for iPhone with iOS 17 or later. On launch day this page will link straight to it."),
        ],
        "privacy": "Privacy policy",
        "support": "Support",
        "anchor": "#en",
        "made": "Made by one independent developer.",
        "lang_label": "Language",
        "home": "Ashling home",
    },
    "zh": {
        "title": "Ashling 掌中玻璃罐 · 窗台上的小小世界",
        "meta": "Ashling（掌中玻璃罐）是一款 iPhone 治愈系电子宠物。窗台上的玻璃罐里住着一只小家伙：你走路，它就去新的地方；它会给你写信，罐子里的光跟着你的一天变化。没有广告，不用注册，没有订阅。",
        "h1": "窗台上的玻璃罐里，有一个小小的世界。",
        "lead": "里面住着一只小家伙。你走路，它也走路；你休息，它也休息，还会把小礼物留在罐子旁边。",
        "soon": "即将上架 App Store",
        "live": "在 App Store 下载",
        "when": "2027 年春季 · iPhone",
        "facts": ["免费下载", "没有广告", "不用注册", "没有订阅"],
        "hero_cap": "罐子里的光，跟着你真实的一天变化。",
        "meet_h": "打开罐子，喘口气，再放回窗台。",
        "meet_p": "Ashling 只住在你的 iPhone 上。没有信息流要刷，也没有什么要追赶。想安静一会儿就打开它，然后继续过你的日子。",
        "trailer": "19 秒预告片（英文字幕）",
        "feat_h": "罐子里有什么",
        "feats": [
            ("你走路，它就去新的地方", "经你允许后，Ashling 会读取 Apple 健康里的步数。雪花球里的小路每天往前长一点，新的植物和小地方也会慢慢出现。"),
            ("不催促的专注", "第 3 天，沙漏会出现。每专注一段，小商队就穿过沙漠走一程，带回一小袋彩色的沙。没有要保住的连胜。"),
            ("每天一封小信", "小家伙会写短短的信，还会在罐边留下拍立得。把它们收进小相册里。"),
            ("光跟着你的一天走", "罐子里的清晨、正午、黄昏和夜晚，和真实时间一致。到了晚上，窗户亮起灯，小岛也睡着了。"),
            ("帽子和拍立得", "给小家伙挑一顶帽子，自己也给罐子拍一张拍立得，一键分享。"),
            ("总在身边", "主屏幕小组件、锁屏上的专注实时活动，还有放在床边的 StandBy 夜灯。"),
        ],
        "shots_h": "看看罐子里",
        "shots_hint": "左右滑动看更多",
        "price_h": "买一次，一直是你的",
        "price_p": "Ashling 免费下载。两样可选的东西都是一次性购买，永远不是订阅。",
        "prices": [
            ("玻璃罐、小岛和小家伙", "免费"),
            ("沙漏专注", "一次性购买。第 3 天出现，第一次免费。"),
            ("苔藓罐盖", "一次性购买。"),
        ],
        "priv_h": "不收集你的任何数据",
        "priv_p": "没有账号、没有服务器、没有广告、没有统计分析。步数只在你的 iPhone 上读取，不会离开设备。这个网站也没有追踪代码和 Cookie。",
        "priv_link": "查看隐私政策",
        "faq_h": "常见问题",
        "faq": [
            ("是订阅吗？", "不是。Ashling 免费下载；沙漏和苔藓罐盖是一次性购买，换新手机时用“恢复购买”就能找回。"),
            ("需要注册吗？", "不需要。没有登录，也没有服务器，所有东西都留在你的 iPhone 上。"),
            ("它怎么用我的步数？", "经你允许后，它只读取 Apple 健康里每天的步数，用来决定小家伙走多远。它不会写入健康数据，步数也不会离开设备。不允许也能正常使用。"),
            ("一个星期没打开会怎样？", "什么都不会坏。小家伙不会生病、不会难过，也不会丢东西。小岛只是在那里等你。"),
            ("有 iPad 或安卓版吗？", "上架时只有 iPhone 版。"),
            ("什么时候能下载？", "计划 2027 年春季在 App Store 上架，支持 iOS 17 及以上的 iPhone。上架那天，这里会换成下载链接。"),
        ],
        "privacy": "隐私政策",
        "support": "客服支持",
        "anchor": "#zh",
        "made": "由一位独立开发者制作。",
        "lang_label": "语言",
        "home": "Ashling 首页",
    },
    "ja": {
        "title": "Ashling｜ガラスびんの中の小さな世界",
        "meta": "Ashling は iPhone の癒しペットアプリ。窓辺のガラスびんに小さな友だちが住んでいます。歩けばいっしょに歩き、手紙を書いてくれて、びんの中の光はきみの一日に合わせて移り変わります。広告なし、アカウント不要、サブスクなし。",
        "h1": "窓辺のガラスびんの中に、小さくてあたたかい世界。",
        "lead": "小さな友だちが住んでいます。きみが歩けばいっしょに歩き、休めばいっしょに休み、びんのそばに小さな贈りものを置いていきます。",
        "soon": "App Store で近日公開",
        "live": "App Store でダウンロード",
        "when": "2027年春 · iPhone",
        "facts": ["ダウンロード無料", "広告なし", "アカウント不要", "サブスクなし"],
        "hero_cap": "びんの中の光は、きみの一日に合わせて移り変わります。",
        "meet_h": "びんを開けて、ひと息ついて、また窓辺へ。",
        "meet_p": "Ashling はきみの iPhone の中だけで暮らします。スクロールするフィードも、追いかけるものもありません。静かな時間がほしいときに開いて、また一日を続けましょう。",
        "trailer": "19秒の予告編（英語字幕）",
        "feat_h": "びんの中にあるもの",
        "feats": [
            ("きみの散歩が、あの子の散歩に", "許可してもらえれば、「ヘルスケア」から歩数を読み取ります。スノードームの小道が毎日少しずつのびて、新しい草花や場所があらわれます。"),
            ("急かさない集中", "3日目に砂時計があらわれます。集中するたびに小さなキャラバンが砂漠を進み、色とりどりの砂を持ち帰ります。連続記録はありません。"),
            ("毎日一通の手紙", "あの子は短い手紙を書き、びんのそばにインスタント写真を置いていきます。小さなアルバムにしまっておけます。"),
            ("光はきみの一日といっしょに", "びんの中の朝、昼、夕方、夜は本当の時刻と同じ。夜になると窓に灯りがともり、島も眠りにつきます。"),
            ("帽子とインスタント写真", "あの子に帽子を選んであげたり、びんのインスタント写真を撮ってワンタップで共有したり。"),
            ("いつもそばに", "ホーム画面のウィジェット、ロック画面の集中ライブアクティビティ、ベッドのそばの StandBy ナイトライト。"),
        ],
        "shots_h": "びんの中をのぞいてみる",
        "shots_hint": "スワイプしてもっと見る",
        "price_h": "一度買えば、ずっと使える",
        "price_p": "Ashling はダウンロード無料。2つの追加アイテムは買い切りで、サブスクリプションではありません。",
        "prices": [
            ("ガラスびん、島、小さな友だち", "無料"),
            ("砂時計での集中", "買い切り。3日目にあらわれ、最初の一回は無料です。"),
            ("苔のびんのふた", "買い切り。"),
        ],
        "priv_h": "データは集めません",
        "priv_p": "アカウントも、サーバーも、広告も、分析ツールもありません。歩数は iPhone の中で読み取られ、外に出ることはありません。このサイトにもトラッカーや Cookie はありません。",
        "priv_link": "プライバシーポリシー（英語）を読む",
        "faq_h": "よくある質問",
        "faq": [
            ("サブスクですか？", "いいえ。ダウンロード無料で、砂時計と苔のふたは買い切りです。新しい iPhone では「購入を復元」で戻せます。"),
            ("アカウントは必要ですか？", "いりません。サインインもサーバーもなく、すべて iPhone の中に残ります。"),
            ("歩数はどう使われますか？", "許可してもらえれば、「ヘルスケア」から一日の歩数だけを読み取り、あの子が歩く距離を決めます。ヘルスケアに書き込むことはなく、歩数が端末の外に出ることもありません。許可しなくても使えます。"),
            ("一週間開かなかったら？", "何も悪いことは起きません。あの子が病気になったり悲しんだりすることも、何かを失うこともありません。島はただ待っています。"),
            ("iPad や Android 版はありますか？", "公開時は iPhone のみです。"),
            ("いつ使えますか？", "2027年春に App Store で公開予定です（iOS 17 以降の iPhone）。公開日には、このページからダウンロードできるようになります。"),
        ],
        "privacy": "プライバシーポリシー（英語）",
        "support": "サポート（英語）",
        "anchor": "#en",
        "made": "ひとりの個人開発者がつくっています。",
        "lang_label": "言語",
        "home": "Ashling ホーム",
    },
    "ko": {
        "title": "Ashling · 유리병 속 작고 아늑한 세계",
        "meta": "Ashling은 iPhone용 힐링 펫 앱이에요. 창가 유리병 속에 작은 친구가 살아요. 걸으면 함께 걷고, 편지를 써 주고, 유리병 속 빛은 당신의 하루를 따라 바뀌어요. 광고도, 계정도, 구독도 없어요.",
        "h1": "창가 유리병 속, 작고 아늑한 세계.",
        "lead": "작은 친구가 살고 있어요. 당신이 걸으면 함께 걷고, 쉬면 함께 쉬고, 유리병 옆에 작은 선물을 놓아 두어요.",
        "soon": "App Store 출시 예정",
        "live": "App Store에서 다운로드",
        "when": "2027년 봄 · iPhone",
        "facts": ["무료 다운로드", "광고 없음", "계정 없음", "구독 없음"],
        "hero_cap": "유리병 속 빛은 당신의 진짜 하루를 따라 바뀌어요.",
        "meet_h": "유리병을 열고, 숨 한 번 고르고, 다시 창가에.",
        "meet_p": "Ashling은 당신의 iPhone 안에서만 살아요. 넘겨야 할 피드도, 따라잡아야 할 것도 없어요. 조용한 순간이 필요할 때 열고, 다시 하루를 이어 가세요.",
        "trailer": "19초 예고편(영어 자막)",
        "feat_h": "유리병 속에 있는 것",
        "feats": [
            ("당신의 산책이 꼬마의 산책이 돼요", "허락해 주시면 건강 앱에서 걸음 수를 읽어요. 스노볼 속 오솔길이 매일 조금씩 길어지고, 새로운 풀꽃과 장소가 나타나요."),
            ("재촉하지 않는 집중", "3일째에 모래시계가 나타나요. 집중할 때마다 작은 카라반이 사막을 건너 알록달록한 모래를 가져와요. 연속 기록은 없어요."),
            ("매일 편지 한 통", "꼬마는 짧은 편지를 쓰고, 유리병 옆에 즉석 사진을 남겨요. 작은 앨범에 모아 둘 수 있어요."),
            ("빛은 당신의 하루를 따라가요", "유리병 속 새벽, 한낮, 해 질 녘, 밤은 실제 시간과 같아요. 밤이 되면 창문에 불이 켜지고 섬도 잠들어요."),
            ("모자와 즉석 사진", "꼬마에게 모자를 골라 주고, 유리병을 즉석 사진으로 찍어 한 번에 공유해요."),
            ("언제나 곁에", "홈 화면 위젯, 잠금 화면의 집중 실시간 현황, 침대 곁의 StandBy 수면등."),
        ],
        "shots_h": "유리병 속을 들여다보기",
        "shots_hint": "옆으로 넘겨 더 보기",
        "price_h": "한 번 사면 계속 내 것",
        "price_p": "Ashling은 무료로 다운로드할 수 있어요. 선택 항목 두 가지는 한 번만 사는 것이고, 구독이 아니에요.",
        "prices": [
            ("유리병, 섬, 작은 친구", "무료"),
            ("모래시계 집중", "한 번 구입. 3일째에 나타나고, 첫 번째는 무료예요."),
            ("이끼 유리병 뚜껑", "한 번 구입."),
        ],
        "priv_h": "데이터를 모으지 않아요",
        "priv_p": "계정도, 서버도, 광고도, 분석 도구도 없어요. 걸음 수는 iPhone 안에서만 읽고, 밖으로 나가지 않아요. 이 웹사이트에도 추적 코드나 쿠키가 없어요.",
        "priv_link": "개인정보 처리방침(영어) 보기",
        "faq_h": "자주 묻는 질문",
        "faq": [
            ("구독인가요?", "아니요. 무료로 다운로드하고, 모래시계와 이끼 뚜껑은 한 번만 사면 돼요. 새 iPhone에서는 '구입 복원'으로 되찾을 수 있어요."),
            ("계정이 필요한가요?", "필요 없어요. 로그인도 서버도 없고, 모든 것이 iPhone 안에 남아요."),
            ("걸음 수는 어떻게 쓰이나요?", "허락해 주시면 건강 앱에서 하루 걸음 수만 읽어 꼬마가 얼마나 걸을지 정해요. 건강 앱에 기록하지 않고, 걸음 수가 기기 밖으로 나가지 않아요. 허락하지 않아도 그대로 쓸 수 있어요."),
            ("일주일 동안 안 열면요?", "나쁜 일은 없어요. 꼬마가 아프거나 슬퍼하지 않고, 잃어버리는 것도 없어요. 섬은 그냥 기다려요."),
            ("iPad나 Android 버전이 있나요?", "출시 때는 iPhone만 지원해요."),
            ("언제 받을 수 있나요?", "2027년 봄 App Store 출시 예정이에요(iOS 17 이상 iPhone). 출시일에는 이 페이지에서 바로 다운로드할 수 있어요."),
        ],
        "privacy": "개인정보 처리방침(영어)",
        "support": "지원(영어)",
        "anchor": "#en",
        "made": "한 명의 독립 개발자가 만들어요.",
        "lang_label": "언어",
        "home": "Ashling 홈",
    },
}

ICONS = {
    "walk": '<path d="M8.2 3.8c1.9 0 2.9 2 2.7 4.5-.2 2.2-1.3 3.6-2.9 3.6s-2.7-1.4-2.6-3.6c.1-2.6 1-4.5 2.8-4.5Z"/><path d="M6.4 14.4c.6-.5 3.2-.5 3.6.1.4.7.2 3-.4 3.8-.7.9-2.2.9-2.9 0-.6-.8-.8-3.4-.3-3.9Z"/><path d="M15.8 6.8c1.8 0 2.8 1.9 2.6 4.3-.2 2.1-1.2 3.4-2.8 3.4s-2.6-1.3-2.5-3.4c.1-2.5 1-4.3 2.7-4.3Z"/><path d="M14 17.2c.6-.5 3.1-.5 3.5.1.4.7.2 2.8-.4 3.6-.7.9-2.1.9-2.8 0-.6-.8-.8-3.2-.3-3.7Z"/>',
    "hourglass": '<path d="M6.5 3.5h11M6.5 20.5h11"/><path d="M7.5 3.5c0 4.5 4.5 5.8 4.5 8.5s-4.5 4-4.5 8.5M16.5 3.5c0 4.5-4.5 5.8-4.5 8.5s4.5 4 4.5 8.5"/><path d="M9.5 18.5c.8-1.3 1.6-2 2.5-2s1.7.7 2.5 2"/>',
    "letter": '<rect x="3.5" y="6" width="17" height="12.5" rx="2"/><path d="m4 7 8 6.2L20 7"/>',
    "sun": '<circle cx="12" cy="12" r="3.8"/><path d="M12 2.8v2.4M12 18.8v2.4M2.8 12h2.4M18.8 12h2.4M5.5 5.5l1.7 1.7M16.8 16.8l1.7 1.7M5.5 18.5l1.7-1.7M16.8 7.2l1.7-1.7"/>',
    "hat": '<path d="M3.5 17.5c2.2 1.4 5.1 2 8.5 2s6.3-.6 8.5-2"/><path d="M6.5 16.6c.2-4.6 2.4-8.6 5.5-8.6s5.3 4 5.5 8.6"/><path d="M12 8V5.5"/><circle cx="12" cy="4.6" r="1.1"/>',
    "widget": '<rect x="6" y="2.8" width="12" height="18.4" rx="2.6"/><rect x="8.6" y="6" width="6.8" height="5.4" rx="1.2"/><path d="M8.8 14.6h6.4M8.8 17.2h4"/>',
}


def e(s: str) -> str:
    return escape(s, quote=True)


def store_button(t: dict) -> str:
    if APP_STORE_URL:
        return (f'<a class="store-btn" href="{e(APP_STORE_URL)}">'
                f'<span class="store-main">{e(t["live"])}</span></a>')
    return (f'<span class="store-btn is-soon">'
            f'<span class="store-main">{e(t["soon"])}</span>'
            f'<span class="store-sub">{e(t["when"])}</span></span>')


def page(lang: str) -> str:
    t = T[lang]
    up = "../" if DIR[lang] else ""
    a = f"{up}assets/"
    url = SITE + DIR[lang]

    alternates = "\n".join(
        f'  <link rel="alternate" hreflang="{HTML_LANG[l]}" href="{SITE}{DIR[l]}">' for l in LANGS
    ) + f'\n  <link rel="alternate" hreflang="x-default" href="{SITE}">'

    lang_links = "\n".join(
        f'        <li><a href="{(up + DIR[l]) or './'}" hreflang="{HTML_LANG[l]}" lang="{HTML_LANG[l]}"'
        + (' aria-current="page"' if l == lang else "")
        + f'>{LANG_NAME[l]}</a></li>'
        for l in LANGS
    )

    facts = "".join(f"<li>{e(f)}</li>" for f in t["facts"])

    feats = "\n".join(
        f'''        <article class="feat">
          <svg class="feat-icon" viewBox="0 0 24 24" aria-hidden="true">{ICONS[icon]}</svg>
          <h3>{e(h)}</h3>
          <p>{e(p)}</p>
        </article>'''
        for icon, (h, p) in zip(FEATURE_ICONS, t["feats"])
    )

    shots = "\n".join(
        f'''        <li><img src="{a}shots/{SHOTS_DIR[lang]}/{f}.webp" width="480" height="1043" loading="lazy" decoding="async" alt="{e(alt)}"></li>'''
        for f, alt in zip(SHOT_FILES, SHOT_ALT[lang])
    )

    prices = "\n".join(
        f'''          <li><span class="price-name">{e(n)}</span><span class="price-note">{e(d)}</span></li>'''
        for n, d in t["prices"]
    )

    faq = "\n".join(
        f'''        <details>
          <summary>{e(q)}</summary>
          <p>{e(ans)}</p>
        </details>'''
        for q, ans in t["faq"]
    )

    # The root page sends a first-time visitor whose browser asks for Chinese, Japanese or
    # Korean to that page. It only runs when they arrive from another site, so picking a
    # language on this site always sticks. Nothing is stored.
    redirect = ""
    if lang == "en":
        redirect = """  <script>
    (function () {
      try {
        if (document.referrer && new URL(document.referrer).host === location.host) return;
        if (location.search.indexOf("lang=en") !== -1) return;
        var l = (navigator.languages && navigator.languages[0] || navigator.language || "").toLowerCase();
        var to = l.indexOf("zh") === 0 ? "zh/" : l.indexOf("ja") === 0 ? "ja/" : l.indexOf("ko") === 0 ? "ko/" : "";
        if (to) location.replace(to + location.hash);
      } catch (err) {}
    })();
  </script>
"""

    return f'''<!doctype html>
<html lang="{HTML_LANG[lang]}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{e(t["title"])}</title>
  <meta name="description" content="{e(t["meta"])}">
  <meta name="theme-color" content="#f7efe3" media="(prefers-color-scheme: light)">
  <meta name="theme-color" content="#1b1511" media="(prefers-color-scheme: dark)">
  <link rel="canonical" href="{url}">
{alternates}
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Ashling">
  <meta property="og:title" content="{e(t["title"])}">
  <meta property="og:description" content="{e(t["meta"])}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{SITE}assets/og.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:locale" content="{OG_LOCALE[lang]}">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" type="image/png" href="{a}icon/favicon-64.png">
  <link rel="apple-touch-icon" href="{a}icon/apple-touch-icon.png">
  <link rel="stylesheet" href="{a}site.css">
{redirect}</head>
<body>
  <header class="top">
    <a class="brand" href="./" aria-label="{e(t["home"])}">
      <img src="{a}icon/icon-256.png" width="36" height="36" alt="">
      <span>Ashling</span>
    </a>
    <nav aria-label="{e(t["lang_label"])}">
      <ul class="langs">
{lang_links}
      </ul>
    </nav>
  </header>

  <main>
    <section class="hero">
      <div class="hero-text">
        <img class="hero-icon" src="{a}icon/icon-256.png" width="96" height="96" alt="Ashling">
        <h1>{e(t["h1"])}</h1>
        <p class="lead">{e(t["lead"])}</p>
        <div class="cta">
          {store_button(t)}
        </div>
        <ul class="facts">{facts}</ul>
      </div>
      <figure class="hero-media">
        <div class="jar-frame">
          <video class="jar-video" src="{a}media/jar-day.mp4" poster="{a}media/jar-day-poster.webp" width="640" height="800" autoplay muted loop playsinline preload="metadata" aria-hidden="true"></video>
        </div>
        <figcaption>{e(t["hero_cap"])}</figcaption>
      </figure>
    </section>

    <section class="meet">
      <div class="meet-text">
        <h2>{e(t["meet_h"])}</h2>
        <p>{e(t["meet_p"])}</p>
      </div>
      <figure class="trailer">
        <video src="{a}media/trailer.mp4" poster="{a}media/trailer-poster.webp" width="540" height="960" controls playsinline preload="none" aria-label="{e(t["trailer"])}"></video>
        <figcaption>{e(t["trailer"])}</figcaption>
      </figure>
    </section>

    <section class="features" aria-labelledby="feat-h">
      <h2 id="feat-h">{e(t["feat_h"])}</h2>
      <div class="feat-grid">
{feats}
      </div>
    </section>

    <section class="shots" aria-labelledby="shots-h">
      <h2 id="shots-h">{e(t["shots_h"])}</h2>
      <p class="hint">{e(t["shots_hint"])}</p>
      <ul class="shot-row" tabindex="0">
{shots}
      </ul>
    </section>

    <section class="pair">
      <div class="card price">
        <h2>{e(t["price_h"])}</h2>
        <p>{e(t["price_p"])}</p>
        <ul class="price-list">
{prices}
        </ul>
      </div>
      <div class="card privacy">
        <h2>{e(t["priv_h"])}</h2>
        <p>{e(t["priv_p"])}</p>
        <p><a href="{up}privacy/{t["anchor"]}">{e(t["priv_link"])}</a></p>
      </div>
    </section>

    <section class="faq" aria-labelledby="faq-h">
      <h2 id="faq-h">{e(t["faq_h"])}</h2>
{faq}
    </section>

    <section class="end">
      <img src="{a}icon/icon-256.png" width="72" height="72" alt="">
      <p class="end-name">Ashling</p>
      {store_button(t)}
    </section>
  </main>

  <footer class="foot">
    <p class="foot-links">
      <a href="{up}privacy/{t["anchor"]}">{e(t["privacy"])}</a>
      <a href="{up}support/{t["anchor"]}">{e(t["support"])}</a>
    </p>
    <p>{e(t["made"])} © 2026 Ashling</p>
  </footer>

  <script>
    (function () {{
      var v = document.querySelector(".jar-video");
      if (!v || !window.matchMedia) return;
      var m = window.matchMedia("(prefers-reduced-motion: reduce)");
      function apply() {{ if (m.matches) {{ v.pause(); v.removeAttribute("autoplay"); }} }}
      apply();
      if (m.addEventListener) m.addEventListener("change", apply);
    }})();
  </script>
</body>
</html>
'''


def main() -> None:
    for lang in LANGS:
        out = ROOT / DIR[lang] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page(lang), encoding="utf-8")
        print("wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
