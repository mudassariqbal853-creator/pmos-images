# POST-004 visual set — Clarity Path (teal/amber)
# Heroes + 8+8 Instagram carousel. LinkedIn/TikTok skipped unless asked.
# UR art: Urdu script only (اے آئی، اے جی آئی). No Latin islands. No em dashes.
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILD = Path(__file__).resolve().parent
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
LOGO_FILE = "file:///" + str((ROOT.parent / "Brand" / "PMOS-logo-mark.png")).replace("\\", "/")

COLORS = {
    "teal": "#0A555C",
    "ink": "#062E32",
    "mist": "#D7E8E6",
    "paper": "#F4F8F7",
    "amber": "#E8B84A",
    "charcoal": "#1A2B2E",
    "white": "#FFFFFF",
    "muted": "#3D6A6E",
}

FONT_CSS = """
  @font-face {
    font-family: "Dubai";
    src: local("Dubai"), url("file:///C:/Windows/Fonts/DUBAI-REGULAR.TTF") format("truetype");
    font-weight: 400;
  }
  @font-face {
    font-family: "Dubai";
    src: local("Dubai Medium"), url("file:///C:/Windows/Fonts/DUBAI-MEDIUM.TTF") format("truetype");
    font-weight: 500;
  }
  @font-face {
    font-family: "Dubai";
    src: local("Dubai Bold"), url("file:///C:/Windows/Fonts/DUBAI-BOLD.TTF") format("truetype");
    font-weight: 700;
  }
"""


def chrome_shot(html_path: Path, out_path: Path, w: int = 1080, h: int = 1080) -> None:
    uri = "file:///" + str(html_path).replace("\\", "/")
    subprocess.run(
        [
            CHROME,
            "--headless=new",
            "--disable-gpu",
            "--hide-scrollbars",
            "--force-device-scale-factor=1",
            f"--window-size={w},{h}",
            f"--screenshot={out_path}",
            uri,
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    print("ok", out_path.name)


BASE_CSS = f"""
  {FONT_CSS}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  html, body {{ width: 1080px; height: 1080px; overflow: hidden; }}
  body {{
    font-family: "Dubai", "Segoe UI", sans-serif;
    color: {COLORS["charcoal"]};
  }}
  .slide {{
    width: 1080px; height: 1080px;
    position: relative; overflow: hidden;
    padding: 56px 64px 48px;
    display: flex; flex-direction: column;
  }}
  .slide.dark {{
    background:
      radial-gradient(ellipse 80% 50% at 15% 10%, rgba(232,184,74,0.22) 0%, transparent 55%),
      linear-gradient(155deg, {COLORS["ink"]} 0%, {COLORS["teal"]} 55%, #0E6A72 100%);
    color: {COLORS["white"]};
  }}
  .slide.light {{
    background:
      radial-gradient(ellipse 70% 40% at 90% 0%, rgba(10,85,92,0.08) 0%, transparent 60%),
      {COLORS["paper"]};
  }}
  .slide.light::before {{
    content: "";
    position: absolute; left: 0; top: 0; bottom: 0; width: 14px;
    background: {COLORS["teal"]};
  }}
  .topbar {{
    display: flex; align-items: center; justify-content: space-between;
    margin-bottom: 28px; direction: ltr;
  }}
  .badge {{
    display: inline-flex; align-items: center; gap: 8px;
    background: {COLORS["amber"]};
    color: {COLORS["ink"]};
    font-weight: 800; font-size: 20px;
    padding: 8px 18px; border-radius: 999px;
  }}
  .badge.en {{ font-family: "Segoe UI", sans-serif; font-size: 18px; }}
  .badge i {{ width: 8px; height: 8px; border-radius: 50%; background: #E85D04; display: inline-block; }}
  .logo {{ width: 64px; height: 64px; }}
  .content {{ flex: 1; display: flex; flex-direction: column; justify-content: center; }}
  .footer {{
    margin-top: auto;
    padding-top: 20px;
    border-top: 1.5px solid rgba(10,85,92,0.18);
    font-size: 18px; font-weight: 600;
    color: {COLORS["muted"]};
  }}
  .footer.en {{ font-family: "Segoe UI", sans-serif; direction: ltr; }}
  .slide.dark .footer {{
    border-top-color: rgba(255,255,255,0.2);
    color: rgba(255,255,255,0.75);
  }}
  .h1 {{
    font-size: 52px; font-weight: 700; line-height: 1.3;
    margin-bottom: 20px;
  }}
  .slide.dark .h1 {{ font-size: 56px; text-shadow: 0 4px 20px rgba(0,0,0,0.25); }}
  .h1 .hl {{ color: {COLORS["amber"]}; font-weight: 800; }}
  .slide.light .h1 .hl {{ color: {COLORS["teal"]}; }}
  .sub {{ font-size: 30px; font-weight: 500; line-height: 1.4; opacity: 0.92; }}
  .body {{ font-size: 32px; font-weight: 400; line-height: 1.45; }}
  .bullets {{ list-style: none; margin-top: 12px; }}
  .bullets li {{
    font-size: 30px; line-height: 1.35;
    padding: 14px 0;
    border-bottom: 1px solid rgba(10,85,92,0.12);
    display: flex; gap: 14px; align-items: flex-start;
  }}
  .slide.dark .bullets li {{ border-bottom-color: rgba(255,255,255,0.15); }}
  .dot {{
    flex-shrink: 0; width: 14px; height: 14px; margin-top: 12px;
    border-radius: 50%; background: {COLORS["amber"]};
  }}
  .cta-pill {{
    display: inline-block; margin-top: 24px;
    background: {COLORS["amber"]}; color: {COLORS["ink"]};
    font-size: 28px; font-weight: 700;
    padding: 14px 28px; border-radius: 999px;
  }}
  .truths {{ display: flex; flex-direction: column; gap: 16px; margin-top: 12px; }}
  .truth {{
    background: {COLORS["white"]};
    border: 2px solid {COLORS["mist"]};
    border-radius: 18px;
    padding: 20px 22px;
    display: flex; gap: 18px; align-items: center;
    font-size: 28px; font-weight: 600; line-height: 1.3;
    box-shadow: 0 6px 16px rgba(10,85,92,0.06);
  }}
  .truth .n {{
    width: 48px; height: 48px; border-radius: 14px; flex-shrink: 0;
    background: {COLORS["teal"]}; color: #fff;
    font-weight: 900; font-size: 22px;
    display: flex; align-items: center; justify-content: center;
  }}
  .compare-slide {{
    display: flex; gap: 16px; align-items: stretch; margin-top: 8px;
  }}
  .compare-slide.rtl {{ direction: rtl; }}
  .compare-slide.ltr {{ direction: ltr; }}
  .lane {{
    flex: 1; border-radius: 22px; padding: 28px 18px;
    text-align: center; min-height: 280px;
    display: flex; flex-direction: column; align-items: center; justify-content: center;
  }}
  .lane-hype {{
    background: linear-gradient(165deg, #C9A03A 0%, #E8B84A 55%, #F0C96A 100%);
    color: #062E32;
  }}
  .lane-reality {{
    background: linear-gradient(165deg, #0A555C 0%, #0E6A72 100%);
    color: #fff;
  }}
  .lane h3 {{ font-size: 28px; font-weight: 700; margin-bottom: 12px; line-height: 1.3; }}
  .lane p {{ font-size: 22px; line-height: 1.35; opacity: 0.95; }}
  .lane-tag {{
    font-size: 15px; font-weight: 800;
    padding: 6px 14px; border-radius: 999px;
    margin-bottom: 14px;
  }}
  .lane-hype .lane-tag {{ background: rgba(6,46,50,0.12); color: #062E32; }}
  .lane-reality .lane-tag {{ background: #E8B84A; color: #062E32; }}
"""

HERO_CSS = f"""
  {FONT_CSS}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  html, body {{ width: 1080px; height: 1080px; overflow: hidden; }}
  body {{ font-family: "Dubai", "Segoe UI", sans-serif; color: #1A2B2E; }}
  .badge {{
    display: inline-flex; align-items: center; gap: 8px;
    background: #E8B84A; color: #062E32;
    font-weight: 800; font-size: 20px;
    padding: 8px 18px; border-radius: 999px;
  }}
  .badge.en {{ font-family: "Segoe UI", sans-serif; font-size: 18px; }}
  .badge i {{ width: 8px; height: 8px; border-radius: 50%; background: #E85D04; display: inline-block; }}
  .logo-lg {{ width: 88px; height: 88px; }}
  .hl {{ color: #E8B84A; font-weight: 800; }}
  .hero {{
    width: 1080px; height: 1080px; position: relative; overflow: hidden;
    background:
      radial-gradient(ellipse 80% 50% at 15% 10%, rgba(232,184,74,0.25) 0%, transparent 55%),
      linear-gradient(155deg, #062E32 0%, #0A555C 50%, #0E6A72 100%);
    color: #fff;
    padding: 48px 52px 40px;
    display: flex; flex-direction: column; justify-content: space-between;
  }}
  .hero-top {{ text-align: center; }}
  .hero .h1 {{
    font-size: 56px; font-weight: 700; line-height: 1.3;
    margin-bottom: 10px;
    text-shadow: 0 4px 20px rgba(0,0,0,0.25);
  }}
  .sub {{ font-size: 28px; font-weight: 500; line-height: 1.4; opacity: 0.92; }}
  .panel {{
    background: rgba(255,255,255,0.97);
    border-radius: 28px;
    padding: 22px 20px 18px;
    color: #1A2B2E;
    box-shadow: 0 18px 40px rgba(0,0,0,0.28);
  }}
  .panel-title {{
    text-align: center; font-size: 24px; font-weight: 700;
    color: #0A555C; margin-bottom: 16px;
  }}
  .compare {{ display: flex; gap: 14px; align-items: stretch; }}
  .compare.rtl {{ direction: rtl; }}
  .compare.ltr {{ direction: ltr; }}
  .lane {{
    flex: 1; border-radius: 22px; padding: 20px 14px 18px;
    text-align: center; min-height: 360px;
    display: flex; flex-direction: column; align-items: center; justify-content: flex-start;
  }}
  .lane-hype {{
    background: linear-gradient(165deg, #C9A03A 0%, #E8B84A 55%, #F0C96A 100%);
    color: #062E32; box-shadow: 0 8px 20px rgba(200,160,50,0.28);
  }}
  .lane-reality {{
    background: linear-gradient(165deg, #0A555C 0%, #0E6A72 100%);
    color: #fff; box-shadow: 0 8px 20px rgba(10,85,92,0.28);
  }}
  .lane-tag {{
    font-size: 16px; font-weight: 800;
    padding: 5px 14px; border-radius: 999px; margin-bottom: 12px;
  }}
  .lane-hype .lane-tag {{ background: rgba(6,46,50,0.12); color: #062E32; }}
  .lane-reality .lane-tag {{ background: #E8B84A; color: #062E32; }}
  .lane h3 {{ font-size: 28px; font-weight: 700; line-height: 1.35; margin-bottom: 8px; }}
  .lane .desc {{ font-size: 22px; line-height: 1.35; opacity: 0.95; margin-bottom: 16px; }}
  .visual {{
    margin-top: auto; width: 100%;
    display: flex; flex-direction: column; align-items: center; gap: 10px;
  }}
  .shop-sign {{
    background: rgba(6,46,50,0.14);
    border: 2px solid rgba(6,46,50,0.22);
    border-radius: 16px;
    padding: 16px 14px;
    font-size: 22px; font-weight: 800; line-height: 1.35;
    max-width: 92%;
  }}
  .proof-box {{
    background: rgba(255,255,255,0.14);
    border-radius: 16px;
    padding: 14px 12px;
    width: 92%;
  }}
  .proof-box.rtl {{ text-align: right; }}
  .proof-box.ltr {{ text-align: left; }}
  .proof-box .q {{
    font-size: 22px; font-weight: 700; line-height: 1.45;
    padding: 6px 0;
    border-bottom: 1px solid rgba(255,255,255,0.18);
  }}
  .proof-box .q:last-child {{ border-bottom: none; }}
  .status {{
    margin-top: 12px;
    font-size: 18px; font-weight: 700;
    padding: 6px 14px; border-radius: 999px;
  }}
  .lane-hype .status {{ background: rgba(6,46,50,0.88); color: #E8B84A; }}
  .lane-reality .status {{ background: rgba(232,184,74,0.95); color: #062E32; }}
  .takeaway {{
    display: block; text-align: center;
    background: #E8B84A; color: #062E32;
    font-size: 26px; font-weight: 700;
    padding: 12px 18px; border-radius: 999px;
    margin: 16px auto 10px; max-width: 96%; line-height: 1.4;
  }}
  .brand-line {{
    text-align: center;
    font-size: 18px; font-weight: 600; color: #3D6A6E;
  }}
  .brand-line.en {{ font-family: "Segoe UI", sans-serif; direction: ltr; }}
"""


def hero_html(lang: str) -> str:
    is_ur = lang == "ur"
    direction = "rtl" if is_ur else "ltr"
    compare_dir = "rtl" if is_ur else "ltr"
    badge_cls = "" if is_ur else " en"
    brand_cls = "" if is_ur else " en"
    proof_cls = "rtl" if is_ur else "ltr"
    badge = "اردو اے آئی لٹریسی · پوسٹ ۴" if is_ur else "AI Literacy · Post 4"
    hook = "اے آئی نے سب بدل دیا؟" if is_ur else 'Did <span class="hl">AI</span> change everything?'
    sub = "لیبل دیکھو یا ثبوت؟" if is_ur else "Label or proof?"
    panel = "ہائپ دیکھیں · حقیقت پوچھیں" if is_ur else "See the hype · Ask for reality"
    hype_tag = "ہائپ" if is_ur else "Hype"
    hype_h = "اے آئی نے سب بدل دیا" if is_ur else "AI changed everything"
    hype_d = "چمکتا لیبل · بلند دعویٰ" if is_ur else "Shiny label · loud claim"
    hype_sign = "«سب بدل گیا · اے جی آئی»" if is_ur else '"Everything changed · AGI"'
    hype_status = "صرف لیبل" if is_ur else "Only a label"
    real_tag = "حقیقت" if is_ur else "Reality"
    real_h = "کام؟ ثبوت؟" if is_ur else "Job? Evidence?"
    real_d = "مخصوص کام · کھلا ثبوت" if is_ur else "Specific job · open proof"
    q1 = "کام کیا ہے؟" if is_ur else "What job?"
    q2 = "ثبوت کیا ہے؟" if is_ur else "What evidence?"
    q3 = "نقصان کس کا؟" if is_ur else "Who pays if it fails?"
    real_status = "کھلا خانہ" if is_ur else "Open box"
    take = (
        "لیبل ثبوت نہیں · کام اور ثبوت پوچھو"
        if is_ur
        else "A label is not proof · Ask job and evidence"
    )
    footer = (
        "پاکستان میڈیا او ایس · اردو اے آئی لٹریسی · پوسٹ ۴"
        if is_ur
        else "Pakistan Media OS · AI Literacy · Post 4"
    )
    # LTR: hype left, reality right. RTL: hype first in DOM = right.
    return f"""<!DOCTYPE html>
<html lang="{lang}" dir="{direction}">
<head><meta charset="utf-8" /><style>{HERO_CSS}</style></head>
<body>
  <div class="hero" dir="{direction}">
    <div class="hero-top">
      <div style="display:flex;justify-content:space-between;align-items:center;direction:ltr;margin-bottom:18px">
        <div class="badge{badge_cls}" dir="{direction}"><i></i>{badge}</div>
        <img class="logo-lg" src="{LOGO_FILE}" alt="" />
      </div>
      <h1 class="h1">{hook}</h1>
      <p class="sub">{sub}</p>
    </div>
    <div class="panel">
      <div class="panel-title">{panel}</div>
      <div class="compare {compare_dir}">
        <div class="lane lane-hype">
          <div class="lane-tag">{hype_tag}</div>
          <h3>{hype_h}</h3>
          <p class="desc">{hype_d}</p>
          <div class="visual">
            <div class="shop-sign">{hype_sign}</div>
          </div>
          <div class="status">{hype_status}</div>
        </div>
        <div class="lane lane-reality">
          <div class="lane-tag">{real_tag}</div>
          <h3>{real_h}</h3>
          <p class="desc">{real_d}</p>
          <div class="visual">
            <div class="proof-box {proof_cls}">
              <div class="q">{q1}</div>
              <div class="q">{q2}</div>
              <div class="q">{q3}</div>
            </div>
          </div>
          <div class="status">{real_status}</div>
        </div>
      </div>
      <div class="takeaway">{take}</div>
      <div class="brand-line{brand_cls}">{footer}</div>
    </div>
  </div>
</body>
</html>"""


def shell(lang: str, dark: bool, title: str, body_html: str, footer: str) -> str:
    direction = "rtl" if lang == "ur" else "ltr"
    theme = "dark" if dark else "light"
    badge_cls = "" if lang == "ur" else " en"
    footer_cls = "" if lang == "ur" else " en"
    series = "اردو اے آئی لٹریسی · پوسٹ ۴" if lang == "ur" else "AI Literacy · Post 4"
    title_block = f'<h1 class="h1">{title}</h1>' if title else ""
    return f"""<!DOCTYPE html>
<html lang="{lang}" dir="{direction}">
<head><meta charset="utf-8" /><style>{BASE_CSS}</style></head>
<body>
  <div class="slide {theme}" dir="{direction}">
    <div class="topbar">
      <div class="badge{badge_cls}" dir="{direction}"><i></i>{series}</div>
      <img class="logo" src="{LOGO_FILE}" alt="" />
    </div>
    <div class="content">
      {title_block}
      {body_html}
    </div>
    <div class="footer{footer_cls}">{footer}</div>
  </div>
</body>
</html>"""


FOOT_UR = "پاکستان میڈیا او ایس · اردو اے آئی لٹریسی · پوسٹ ۴"
FOOT_EN = "Pakistan Media OS · AI Literacy · Post 4"

SLIDES_UR = [
    {
        "name": "POST-004-slide-ur-01.png",
        "dark": True,
        "title": "اے آئی نے سب بدل دیا؟",
        "body": '<p class="sub">لیبل دیکھو یا ثبوت؟</p><p class="sub" style="margin-top:18px">پوسٹ ۴</p>',
    },
    {
        "name": "POST-004-slide-ur-02.png",
        "dark": False,
        "title": "عام غلط فہمی",
        "body": (
            '<p class="body">«اے آئی لکھا ہے، تو سچ اور طاقتور ہے۔»</p>'
            '<p class="body" style="margin-top:22px">لیبل ≠ ثبوت</p>'
        ),
    },
    {
        "name": "POST-004-slide-ur-03.png",
        "dark": False,
        "title": "پوسٹ ۱ تا ۳",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>حقیقی ٹولز موجود</span></li>'
            '<li><span class="dot"></span><span>محدود اے آئی</span></li>'
            '<li><span class="dot"></span><span>روانی ≠ سچ</span></li>'
            "</ul>"
            '<p class="body" style="margin-top:22px;color:#0A555C;font-weight:700">آج: ہائپ کی شکلیں</p>'
        ),
    },
    {
        "name": "POST-004-slide-ur-04.png",
        "dark": False,
        "title": "ہائپ ۱ اور ۲",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>لیبل کھینچنا</span></li>'
            '<li><span class="dot"></span><span>«سب بدل گیا / اے جی آئی»</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-004-slide-ur-05.png",
        "dark": False,
        "title": "ہائپ ۳، ۴، ۵",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>گارنٹی پیسہ یا نوکری</span></li>'
            '<li><span class="dot"></span><span>معجزہ ایک ٹول</span></li>'
            '<li><span class="dot"></span><span>ڈیمو = محفوظ نتیجہ؟</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-004-slide-ur-06.png",
        "dark": False,
        "title": "حقیقت",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>مخصوص کام</span></li>'
            '<li><span class="dot"></span><span>حدیں موجود</span></li>'
            '<li><span class="dot"></span><span>جانچ کے بغیر بھروسہ خطرناک</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-004-slide-ur-07.png",
        "dark": False,
        "title": "تین سوال",
        "body": (
            '<div class="truths">'
            '<div class="truth"><span class="n">۱</span><span>کام کیا ہے؟</span></div>'
            '<div class="truth"><span class="n">۲</span><span>ثبوت کیا ہے؟</span></div>'
            '<div class="truth"><span class="n">۳</span><span>نقصان کس کا؟</span></div>'
            "</div>"
        ),
    },
    {
        "name": "POST-004-slide-ur-08.png",
        "dark": True,
        "title": "یاد رکھیں",
        "body": (
            '<p class="sub" style="font-size:34px">اوزار رکھو۔ بے بنیاد وعدے چھوڑو۔</p>'
            '<p class="sub" style="margin-top:20px">اگلا: ڈیپ فیک</p>'
            '<div class="cta-pill">محفوظ کریں · فالو کریں · پوسٹ ۴</div>'
        ),
    },
]

SLIDES_EN = [
    {
        "name": "POST-004-slide-en-01.png",
        "dark": True,
        "title": 'Did <span class="hl">AI</span> change everything?',
        "body": '<p class="sub">Label or proof?</p><p class="sub" style="margin-top:18px">Post 4</p>',
    },
    {
        "name": "POST-004-slide-en-02.png",
        "dark": False,
        "title": "Common myth",
        "body": (
            '<p class="body">“It says AI, so it must be true and powerful.”</p>'
            '<p class="body" style="margin-top:22px">Label ≠ proof</p>'
        ),
    },
    {
        "name": "POST-004-slide-en-03.png",
        "dark": False,
        "title": "From Posts 1-3",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>Real tools exist</span></li>'
            '<li><span class="dot"></span><span>Narrow AI</span></li>'
            '<li><span class="dot"></span><span>Fluency ≠ truth</span></li>'
            "</ul>"
            '<p class="body" style="margin-top:22px;color:#0A555C;font-weight:700">Today: hype shapes</p>'
        ),
    },
    {
        "name": "POST-004-slide-en-04.png",
        "dark": False,
        "title": "Hype 1 and 2",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>Label stretch</span></li>'
            '<li><span class="dot"></span><span>“Everything changed / AGI”</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-004-slide-en-05.png",
        "dark": False,
        "title": "Hype 3, 4, 5",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>Guaranteed money or jobs</span></li>'
            '<li><span class="dot"></span><span>Miracle one-tool</span></li>'
            '<li><span class="dot"></span><span>Demo = safe results?</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-004-slide-en-06.png",
        "dark": False,
        "title": "Reality",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>Specific job</span></li>'
            '<li><span class="dot"></span><span>Real limits</span></li>'
            '<li><span class="dot"></span><span>Trust needs checking</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-004-slide-en-07.png",
        "dark": False,
        "title": "Three questions",
        "body": (
            '<div class="truths">'
            '<div class="truth"><span class="n">1</span><span>What job?</span></div>'
            '<div class="truth"><span class="n">2</span><span>What evidence?</span></div>'
            '<div class="truth"><span class="n">3</span><span>Who pays if it fails?</span></div>'
            "</div>"
        ),
    },
    {
        "name": "POST-004-slide-en-08.png",
        "dark": True,
        "title": "Keep this",
        "body": (
            '<p class="sub" style="font-size:34px">Keep tools. Drop unproven promises.</p>'
            '<p class="sub" style="margin-top:20px">Next: deepfakes</p>'
            '<div class="cta-pill">Save · Follow · Post 4</div>'
        ),
    },
]


def write_slide(spec: dict, lang: str, footer: str) -> Path:
    html = shell(lang, spec["dark"], spec["title"], spec["body"], footer)
    html_path = BUILD / spec["name"].replace(".png", ".html")
    html_path.write_text(html, encoding="utf-8")
    return html_path


def assert_no_emdash(text: str, label: str) -> None:
    if "—" in text or "\u2014" in text:
        raise SystemExit(f"em dash found in {label}")


def assert_ur_no_latin(html: str, label: str) -> None:
    body = re.search(r"(?s)<body>(.*)</body>", html)
    if not body:
        return
    text = re.sub(r"(?s)<[^>]+>", " ", body.group(1))
    latin = re.findall(r"[A-Za-z]{2,}", text)
    if latin:
        raise SystemExit(f"Latin in UR art {label}: {sorted(set(latin))}")


def main() -> None:
    ROOT.mkdir(parents=True, exist_ok=True)

    for lang in ("ur", "en"):
        html = hero_html(lang)
        assert_no_emdash(html, f"hero-{lang}")
        if lang == "ur":
            assert_ur_no_latin(html, "hero-ur")
        html_path = BUILD / f"hero-{lang}.html"
        html_path.write_text(html, encoding="utf-8")
        chrome_shot(html_path, ROOT / f"POST-004-hero-{lang}-1080x1080.png")

    for s in SLIDES_UR:
        html_path = write_slide(s, "ur", FOOT_UR)
        html = html_path.read_text(encoding="utf-8")
        assert_no_emdash(html, s["name"])
        assert_ur_no_latin(html, s["name"])
        chrome_shot(html_path, ROOT / s["name"])

    for s in SLIDES_EN:
        html_path = write_slide(s, "en", FOOT_EN)
        html = html_path.read_text(encoding="utf-8")
        assert_no_emdash(html, s["name"])
        chrome_shot(html_path, ROOT / s["name"])

    print("POST-004 visual set complete ->", ROOT)


if __name__ == "__main__":
    main()
