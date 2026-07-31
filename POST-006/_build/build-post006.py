# POST-006 visual set — Clarity Path (teal/amber)
# Heroes + 8+8 Instagram carousel. LinkedIn/TikTok skipped unless asked.
# UR art: Urdu script only (اے آئی). No Latin islands. No em dashes.
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
  .truths {{ display: flex; flex-direction: column; gap: 14px; margin-top: 12px; }}
  .truth {{
    background: {COLORS["white"]};
    border: 2px solid {COLORS["mist"]};
    border-radius: 18px;
    padding: 18px 20px;
    display: flex; gap: 16px; align-items: center;
    font-size: 26px; font-weight: 600; line-height: 1.3;
    box-shadow: 0 6px 16px rgba(10,85,92,0.06);
  }}
  .truth .n {{
    width: 44px; height: 44px; border-radius: 14px; flex-shrink: 0;
    background: {COLORS["teal"]}; color: #fff;
    font-weight: 900; font-size: 20px;
    display: flex; align-items: center; justify-content: center;
  }}
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
    font-size: 52px; font-weight: 700; line-height: 1.3;
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
  .lane-promise {{
    background: linear-gradient(165deg, #C9A03A 0%, #E8B84A 55%, #F0C96A 100%);
    color: #062E32; box-shadow: 0 8px 20px rgba(200,160,50,0.28);
  }}
  .lane-tool {{
    background: linear-gradient(165deg, #0A555C 0%, #0E6A72 100%);
    color: #fff; box-shadow: 0 8px 20px rgba(10,85,92,0.28);
  }}
  .lane-tag {{
    font-size: 16px; font-weight: 800;
    padding: 5px 14px; border-radius: 999px; margin-bottom: 12px;
  }}
  .lane-promise .lane-tag {{ background: rgba(6,46,50,0.12); color: #062E32; }}
  .lane-tool .lane-tag {{ background: #E8B84A; color: #062E32; }}
  .lane h3 {{ font-size: 26px; font-weight: 700; line-height: 1.35; margin-bottom: 8px; }}
  .lane .desc {{ font-size: 20px; line-height: 1.35; opacity: 0.95; margin-bottom: 14px; }}
  .visual {{
    margin-top: auto; width: 100%;
    display: flex; flex-direction: column; align-items: center; gap: 12px;
  }}
  .claim-badge {{
    background: rgba(6,46,50,0.14);
    border: 2px solid rgba(6,46,50,0.22);
    border-radius: 16px;
    padding: 16px 14px;
    font-size: 22px; font-weight: 800; line-height: 1.35;
    max-width: 92%;
  }}
  .icon-box {{
    width: 110px; height: 110px;
    border-radius: 22px;
    display: flex; align-items: center; justify-content: center;
  }}
  .lane-promise .icon-box {{ background: rgba(6,46,50,0.12); }}
  .lane-tool .icon-box {{ background: rgba(255,255,255,0.14); }}
  .status {{
    margin-top: 12px;
    font-size: 18px; font-weight: 700;
    padding: 6px 14px; border-radius: 999px;
  }}
  .lane-promise .status {{ background: rgba(6,46,50,0.88); color: #E8B84A; }}
  .lane-tool .status {{ background: rgba(232,184,74,0.95); color: #062E32; }}
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

ICON_ATM = """
<svg width="72" height="72" viewBox="0 0 72 72" fill="none" aria-hidden="true">
  <rect x="14" y="10" width="44" height="52" rx="6" stroke="#062E32" stroke-width="3"/>
  <rect x="22" y="18" width="28" height="16" rx="3" fill="#062E32" opacity="0.25"/>
  <rect x="24" y="42" width="24" height="6" rx="2" fill="#062E32" opacity="0.55"/>
  <circle cx="36" cy="56" r="2.5" fill="#062E32"/>
</svg>
"""

ICON_DRILL = """
<svg width="72" height="72" viewBox="0 0 72 72" fill="none" aria-hidden="true">
  <rect x="10" y="28" width="34" height="18" rx="5" stroke="#FFFFFF" stroke-width="3"/>
  <path d="M44 32h14l4 5-4 5H44" stroke="#E8B84A" stroke-width="3" stroke-linejoin="round"/>
  <circle cx="22" cy="37" r="4" fill="#E8B84A"/>
  <path d="M18 46v8M26 46v8" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>
</svg>
"""


def hero_html(lang: str) -> str:
    is_ur = lang == "ur"
    direction = "rtl" if is_ur else "ltr"
    compare_dir = "rtl" if is_ur else "ltr"
    badge_cls = "" if is_ur else " en"
    brand_cls = "" if is_ur else " en"
    badge = "اردو اے آئی لٹریسی · پوسٹ ۶" if is_ur else "AI Literacy · Post 6"
    hook = "اے آئی سے گارنٹی آمدنی؟" if is_ur else 'Guaranteed income with <span class="hl">AI</span>?'
    sub = "اوزار ہے یا جال؟" if is_ur else "Tool or trap?"
    panel = "وعدہ دیکھیں · حقیقت سمجھیں" if is_ur else "Promise vs tool reality"
    p_tag = "جال کا لیبل" if is_ur else "Trap label"
    p_h = "گارنٹی آمدنی / نوکری" if is_ur else "Guaranteed income / job"
    p_d = "چمکتا دعویٰ · بغیر ثبوت" if is_ur else "Shiny claim · no proof"
    p_claim = "«گارنٹی آمدنی»" if is_ur else '"Guaranteed income"'
    p_status = "وعدہ خریدو؟" if is_ur else "Buy the promise?"
    t_tag = "حقیقت" if is_ur else "Reality"
    t_h = "اوزار: مخصوص کام" if is_ur else "Tool: specific job"
    t_d = "کام میں مدد · تنخواہ نہیں" if is_ur else "Helps work · not a paycheck"
    t_status = "وعدہ نہیں" if is_ur else "Not a promise"
    take = "اوزار رکھو · وعدے مت خریدو" if is_ur else "Keep tools · Don't buy promises"
    footer = (
        "پاکستان میڈیا او ایس · اردو اے آئی لٹریسی · پوسٹ ۶"
        if is_ur
        else "Pakistan Media OS · AI Literacy · Post 6"
    )
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
        <div class="lane lane-promise">
          <div class="lane-tag">{p_tag}</div>
          <h3>{p_h}</h3>
          <p class="desc">{p_d}</p>
          <div class="visual">
            <div class="icon-box">{ICON_ATM}</div>
            <div class="claim-badge">{p_claim}</div>
          </div>
          <div class="status">{p_status}</div>
        </div>
        <div class="lane lane-tool">
          <div class="lane-tag">{t_tag}</div>
          <h3>{t_h}</h3>
          <p class="desc">{t_d}</p>
          <div class="visual">
            <div class="icon-box">{ICON_DRILL}</div>
          </div>
          <div class="status">{t_status}</div>
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
    series = "اردو اے آئی لٹریسی · پوسٹ ۶" if lang == "ur" else "AI Literacy · Post 6"
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


FOOT_UR = "پاکستان میڈیا او ایس · اردو اے آئی لٹریسی · پوسٹ ۶"
FOOT_EN = "Pakistan Media OS · AI Literacy · Post 6"

SLIDES_UR = [
    {
        "name": "POST-006-slide-ur-01.png",
        "dark": True,
        "title": "اے آئی سے گارنٹی آمدنی؟",
        "body": '<p class="sub">اوزار ہے یا جال؟</p><p class="sub" style="margin-top:18px">پوسٹ ۶</p>',
    },
    {
        "name": "POST-006-slide-ur-02.png",
        "dark": False,
        "title": "عام غلط فہمی",
        "body": (
            '<p class="body">«اے آئی لکھا ہے، تو پیسہ پکا ہے۔»</p>'
            '<p class="body" style="margin-top:22px">لیبل ≠ تنخواہ</p>'
        ),
    },
    {
        "name": "POST-006-slide-ur-03.png",
        "dark": False,
        "title": "پوسٹ ۴ و ۵",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>ثبوت مانگو</span></li>'
            '<li><span class="dot"></span><span>اونچے داؤ پر جانچ</span></li>'
            '<li><span class="dot"></span><span>آج: پیسہ / نوکری کے دعوے</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-006-slide-ur-04.png",
        "dark": False,
        "title": "حقیقت",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>اے آئی مخصوص کام</span></li>'
            '<li><span class="dot"></span><span>گارنٹی منافع صلاحیت نہیں</span></li>'
            '<li><span class="dot"></span><span>مہارت ≠ وعدہ خریدنا</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-006-slide-ur-05.png",
        "dark": False,
        "title": "شکلیں ۱ تا ۳",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>گارنٹی آمدنی بوٹ</span></li>'
            '<li><span class="dot"></span><span>نوکری گارنٹی فیس</span></li>'
            '<li><span class="dot"></span><span>خفیہ پرامپٹ پیک</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-006-slide-ur-06.png",
        "dark": False,
        "title": "شکلیں ۴ و ۵",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>دباؤ / رازداری</span></li>'
            '<li><span class="dot"></span><span>جعلی آواز سے پیسے کا مطالبہ</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-006-slide-ur-07.png",
        "dark": False,
        "title": "پانچ سوال",
        "body": (
            '<div class="truths">'
            '<div class="truth"><span class="n">۱</span><span>گارنٹی؟</span></div>'
            '<div class="truth"><span class="n">۲</span><span>پیسہ کسے؟</span></div>'
            '<div class="truth"><span class="n">۳</span><span>واپسی؟</span></div>'
            '<div class="truth"><span class="n">۴</span><span>دباؤ؟</span></div>'
            '<div class="truth"><span class="n">۵</span><span>مہارت یا جادو؟</span></div>'
            "</div>"
        ),
    },
    {
        "name": "POST-006-slide-ur-08.png",
        "dark": True,
        "title": "یاد رکھیں",
        "body": (
            '<p class="sub" style="font-size:34px">اوزار رکھو۔ وعدے مت خریدو۔</p>'
            '<p class="sub" style="margin-top:20px">اگلا: شہری خواندگی</p>'
            '<div class="cta-pill">محفوظ کریں · فالو کریں · پوسٹ ۶</div>'
        ),
    },
]

SLIDES_EN = [
    {
        "name": "POST-006-slide-en-01.png",
        "dark": True,
        "title": 'Guaranteed income with <span class="hl">AI</span>?',
        "body": '<p class="sub">Tool or trap?</p><p class="sub" style="margin-top:18px">Post 6</p>',
    },
    {
        "name": "POST-006-slide-en-02.png",
        "dark": False,
        "title": "Common myth",
        "body": (
            '<p class="body">"It says AI, so the money is locked."</p>'
            '<p class="body" style="margin-top:22px">Label ≠ paycheck</p>'
        ),
    },
    {
        "name": "POST-006-slide-en-03.png",
        "dark": False,
        "title": "From Posts 4-5",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>Ask for proof</span></li>'
            '<li><span class="dot"></span><span>Check high stakes</span></li>'
            '<li><span class="dot"></span><span>Today: money / job pitches</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-006-slide-en-04.png",
        "dark": False,
        "title": "Reality",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>AI does specific jobs</span></li>'
            '<li><span class="dot"></span><span>Guaranteed profit is not a capability</span></li>'
            '<li><span class="dot"></span><span>Skills ≠ buying promises</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-006-slide-en-05.png",
        "dark": False,
        "title": "Shapes 1-3",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>Guaranteed income bot</span></li>'
            '<li><span class="dot"></span><span>Job-guarantee fee</span></li>'
            '<li><span class="dot"></span><span>Secret prompt pack</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-006-slide-en-06.png",
        "dark": False,
        "title": "Shapes 4-5",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>Pressure / secrecy</span></li>'
            '<li><span class="dot"></span><span>Fake voice asking for money</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-006-slide-en-07.png",
        "dark": False,
        "title": "Five questions",
        "body": (
            '<div class="truths">'
            '<div class="truth"><span class="n">1</span><span>Guarantee?</span></div>'
            '<div class="truth"><span class="n">2</span><span>Who gets paid?</span></div>'
            '<div class="truth"><span class="n">3</span><span>Refund path?</span></div>'
            '<div class="truth"><span class="n">4</span><span>Pressure?</span></div>'
            '<div class="truth"><span class="n">5</span><span>Skill or magic?</span></div>'
            "</div>"
        ),
    },
    {
        "name": "POST-006-slide-en-08.png",
        "dark": True,
        "title": "Keep this",
        "body": (
            '<p class="sub" style="font-size:34px">Keep tools. Don\'t buy promises.</p>'
            '<p class="sub" style="margin-top:20px">Next: civic literacy</p>'
            '<div class="cta-pill">Save · Follow · Post 6</div>'
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
    BUILD.mkdir(parents=True, exist_ok=True)

    for lang in ("ur", "en"):
        html = hero_html(lang)
        assert_no_emdash(html, f"hero-{lang}")
        if lang == "ur":
            assert_ur_no_latin(html, "hero-ur")
        html_path = BUILD / f"hero-{lang}.html"
        html_path.write_text(html, encoding="utf-8")
        chrome_shot(html_path, ROOT / f"POST-006-hero-{lang}-1080x1080.png")

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

    print("POST-006 visual set complete ->", ROOT)


if __name__ == "__main__":
    main()
