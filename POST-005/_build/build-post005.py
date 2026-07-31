# POST-005 visual set — Clarity Path (teal/amber)
# Heroes + 8+8 Instagram carousel. LinkedIn/TikTok skipped unless asked.
# UR art: Urdu script only (ڈیپ فیک، اے آئی). No Latin islands. No em dashes.
# Abstract silhouettes only. No real faces, horror, political symbols, detector badges.
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
  .lane-looks {{
    background: linear-gradient(165deg, #C9A03A 0%, #E8B84A 55%, #F0C96A 100%);
    color: #062E32; box-shadow: 0 8px 20px rgba(200,160,50,0.28);
  }}
  .lane-verify {{
    background: linear-gradient(165deg, #0A555C 0%, #0E6A72 100%);
    color: #fff; box-shadow: 0 8px 20px rgba(10,85,92,0.28);
  }}
  .lane-tag {{
    font-size: 16px; font-weight: 800;
    padding: 5px 14px; border-radius: 999px; margin-bottom: 12px;
  }}
  .lane-looks .lane-tag {{ background: rgba(6,46,50,0.12); color: #062E32; }}
  .lane-verify .lane-tag {{ background: #E8B84A; color: #062E32; }}
  .lane h3 {{ font-size: 26px; font-weight: 700; line-height: 1.35; margin-bottom: 8px; }}
  .lane .desc {{ font-size: 20px; line-height: 1.35; opacity: 0.95; margin-bottom: 14px; }}
  .visual {{
    margin-top: auto; width: 100%;
    display: flex; flex-direction: column; align-items: center; gap: 10px;
  }}
  .sil-wrap {{
    width: 120px; height: 120px;
    position: relative;
    display: flex; align-items: center; justify-content: center;
  }}
  .sil {{
    width: 72px; height: 72px;
    border-radius: 50% 50% 46% 46%;
    background: rgba(6,46,50,0.22);
    position: relative;
  }}
  .sil::after {{
    content: "";
    position: absolute;
    bottom: -28px; left: 50%; transform: translateX(-50%);
    width: 88px; height: 44px;
    border-radius: 44px 44px 12px 12px;
    background: rgba(6,46,50,0.18);
  }}
  .mask-ring {{
    position: absolute;
    inset: 8px;
    border: 3px dashed rgba(6,46,50,0.45);
    border-radius: 50%;
  }}
  .qmark {{
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%, -58%);
    font-size: 42px; font-weight: 900;
    color: #062E32;
    line-height: 1;
  }}
  .checks {{
    background: rgba(255,255,255,0.14);
    border-radius: 16px;
    padding: 12px 10px;
    width: 92%;
  }}
  .checks.rtl {{ text-align: right; }}
  .checks.ltr {{ text-align: left; }}
  .checks .row {{
    font-size: 20px; font-weight: 700; line-height: 1.4;
    padding: 5px 0;
    border-bottom: 1px solid rgba(255,255,255,0.16);
    display: flex; align-items: center; gap: 10px;
  }}
  .checks.rtl .row {{ justify-content: flex-start; }}
  .checks.ltr .row {{ justify-content: flex-start; }}
  .checks .row:last-child {{ border-bottom: none; }}
  .ico {{
    width: 28px; height: 28px; border-radius: 8px; flex-shrink: 0;
    background: rgba(232,184,74,0.95); color: #062E32;
    font-size: 14px; font-weight: 900;
    display: flex; align-items: center; justify-content: center;
    font-family: "Segoe UI", "Dubai", sans-serif;
  }}
  .status {{
    margin-top: 12px;
    font-size: 18px; font-weight: 700;
    padding: 6px 14px; border-radius: 999px;
  }}
  .lane-looks .status {{ background: rgba(6,46,50,0.88); color: #E8B84A; }}
  .lane-verify .status {{ background: rgba(232,184,74,0.95); color: #062E32; }}
  .takeaway {{
    display: block; text-align: center;
    background: #E8B84A; color: #062E32;
    font-size: 24px; font-weight: 700;
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
    checks_cls = "rtl" if is_ur else "ltr"
    badge = "اردو اے آئی لٹریسی · پوسٹ ۵" if is_ur else "AI Literacy · Post 5"
    hook = "ویڈیو اصلی لگتی ہے؟" if is_ur else 'If it looks <span class="hl">real</span>…'
    sub = "کیا ثابت ہو گئی؟" if is_ur else "Is it proof?"
    panel = "دکھائی دینا · جانچ ضروری" if is_ur else "Looks real · Needs a check"
    looks_tag = "دکھائی دینا" if is_ur else "Looks real"
    looks_h = "ویڈیو اصلی لگتی ہے" if is_ur else "The video looks real"
    looks_d = "پُراعتماد «ثابت» نظر" if is_ur else 'Confident "proven" look'
    looks_status = "ثبوت نہیں" if is_ur else "Not proof"
    verify_tag = "جانچ" if is_ur else "Verify"
    verify_h = "چار چیک" if is_ur else "Four checks"
    verify_d = (
        "ذریعہ · داؤ · سیاق · نظر"
        if is_ur
        else "Source · stakes · context · look"
    )
    checks = (
        [
            ("۱", "ذریعہ"),
            ("۲", "داؤ"),
            ("۳", "سیاق"),
            ("۴", "نظر"),
        ]
        if is_ur
        else [
            ("1", "Source"),
            ("2", "Stakes"),
            ("3", "Context"),
            ("4", "Second look"),
        ]
    )
    verify_status = "ثبوت چاہیے" if is_ur else "Evidence needed"
    take = (
        "دکھائی دینا ثبوت نہیں · خوف حکمت نہیں"
        if is_ur
        else "Looking real is not proof · Panic is not wisdom"
    )
    footer = (
        "پاکستان میڈیا او ایس · اردو اے آئی لٹریسی · پوسٹ ۵"
        if is_ur
        else "Pakistan Media OS · AI Literacy · Post 5"
    )
    qmark = "؟" if is_ur else "?"
    check_rows = "".join(
        f'<div class="row"><span class="ico">{n}</span><span>{label}</span></div>'
        for n, label in checks
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
        <div class="lane lane-looks">
          <div class="lane-tag">{looks_tag}</div>
          <h3>{looks_h}</h3>
          <p class="desc">{looks_d}</p>
          <div class="visual">
            <div class="sil-wrap" aria-hidden="true">
              <div class="sil"></div>
              <div class="mask-ring"></div>
              <div class="qmark">{qmark}</div>
            </div>
          </div>
          <div class="status">{looks_status}</div>
        </div>
        <div class="lane lane-verify">
          <div class="lane-tag">{verify_tag}</div>
          <h3>{verify_h}</h3>
          <p class="desc">{verify_d}</p>
          <div class="visual">
            <div class="checks {checks_cls}">
              {check_rows}
            </div>
          </div>
          <div class="status">{verify_status}</div>
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
    series = "اردو اے آئی لٹریسی · پوسٹ ۵" if lang == "ur" else "AI Literacy · Post 5"
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


FOOT_UR = "پاکستان میڈیا او ایس · اردو اے آئی لٹریسی · پوسٹ ۵"
FOOT_EN = "Pakistan Media OS · AI Literacy · Post 5"

SLIDES_UR = [
    {
        "name": "POST-005-slide-ur-01.png",
        "dark": True,
        "title": "ویڈیو اصلی لگتی ہے؟",
        "body": '<p class="sub">کیا ثابت ہو گئی؟</p><p class="sub" style="margin-top:18px">پوسٹ ۵</p>',
    },
    {
        "name": "POST-005-slide-ur-02.png",
        "dark": False,
        "title": "عام غلط فہمی",
        "body": (
            '<p class="body">«دکھائی دیا، سچ ہے۔»</p>'
            '<p class="body" style="margin-top:22px">دکھائی دینا ≠ ثبوت</p>'
        ),
    },
    {
        "name": "POST-005-slide-ur-03.png",
        "dark": False,
        "title": "پوسٹ ۴ سے",
        "body": (
            '<p class="body">لیبل ثبوت نہیں</p>'
            '<p class="body" style="margin-top:22px;color:#0A555C;font-weight:700">آج: میڈیا جو حقیقی لگے</p>'
        ),
    },
    {
        "name": "POST-005-slide-ur-04.png",
        "dark": False,
        "title": "ڈیپ فیک کیا ہے؟",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>چہرہ / آواز / ویڈیو</span></li>'
            '<li><span class="dot"></span><span>اصلی جیسی لگے</span></li>'
            '<li><span class="dot"></span><span>اے آئی سے بدلا ہوا میڈیا بھی اسی عادت کا حصہ</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-005-slide-ur-05.png",
        "dark": False,
        "title": "دو غلط راستے",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>سب مان لو</span></li>'
            '<li><span class="dot"></span><span>یا سب جعلی کہہ دو</span></li>'
            "</ul>"
            '<p class="body" style="margin-top:22px;color:#0A555C;font-weight:700">درمیان: اونچے داؤ پر جانچ</p>'
        ),
    },
    {
        "name": "POST-005-slide-ur-06.png",
        "dark": False,
        "title": "نقصان کہاں؟",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>شناخت کا سوء استعمال</span></li>'
            '<li><span class="dot"></span><span>پیسہ / جعلی آواز</span></li>'
            '<li><span class="dot"></span><span>عزت والا فارورڈ</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-005-slide-ur-07.png",
        "dark": False,
        "title": "چار چیک",
        "body": (
            '<div class="truths">'
            '<div class="truth"><span class="n">۱</span><span>ذریعہ</span></div>'
            '<div class="truth"><span class="n">۲</span><span>داؤ</span></div>'
            '<div class="truth"><span class="n">۳</span><span>سیاق</span></div>'
            '<div class="truth"><span class="n">۴</span><span>دوسری نظر / مت بھیجو</span></div>'
            "</div>"
        ),
    },
    {
        "name": "POST-005-slide-ur-08.png",
        "dark": True,
        "title": "یاد رکھیں",
        "body": (
            '<p class="sub" style="font-size:34px">نظر ثبوت نہیں۔ خوف حکمت نہیں۔</p>'
            '<p class="sub" style="margin-top:20px">اگلا: اے آئی اسکیمز</p>'
            '<div class="cta-pill">محفوظ کریں · فالو کریں · پوسٹ ۵</div>'
        ),
    },
]

SLIDES_EN = [
    {
        "name": "POST-005-slide-en-01.png",
        "dark": True,
        "title": 'If it looks <span class="hl">real</span>…',
        "body": '<p class="sub">Is it proof?</p><p class="sub" style="margin-top:18px">Post 5</p>',
    },
    {
        "name": "POST-005-slide-en-02.png",
        "dark": False,
        "title": "Common myth",
        "body": (
            '<p class="body">"I saw it, so it\'s true."</p>'
            '<p class="body" style="margin-top:22px">Looking real ≠ proof</p>'
        ),
    },
    {
        "name": "POST-005-slide-en-03.png",
        "dark": False,
        "title": "From Post 4",
        "body": (
            '<p class="body">A label is not proof</p>'
            '<p class="body" style="margin-top:22px;color:#0A555C;font-weight:700">Today: media that looks real</p>'
        ),
    },
    {
        "name": "POST-005-slide-en-04.png",
        "dark": False,
        "title": "What is a deepfake?",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>Face / voice / video</span></li>'
            '<li><span class="dot"></span><span>Made to look authentic</span></li>'
            '<li><span class="dot"></span><span>Other AI-altered media needs the same habit</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-005-slide-en-05.png",
        "dark": False,
        "title": "Two wrong paths",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>Believe everything</span></li>'
            '<li><span class="dot"></span><span>Or call everything fake</span></li>'
            "</ul>"
            '<p class="body" style="margin-top:22px;color:#0A555C;font-weight:700">Middle: check high stakes</p>'
        ),
    },
    {
        "name": "POST-005-slide-en-06.png",
        "dark": False,
        "title": "Where harm hits",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>Identity misuse</span></li>'
            '<li><span class="dot"></span><span>Money / fake voice</span></li>'
            '<li><span class="dot"></span><span>Reputation forwards</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-005-slide-en-07.png",
        "dark": False,
        "title": "Four checks",
        "body": (
            '<div class="truths">'
            '<div class="truth"><span class="n">1</span><span>Source</span></div>'
            '<div class="truth"><span class="n">2</span><span>Stakes</span></div>'
            '<div class="truth"><span class="n">3</span><span>Context</span></div>'
            '<div class="truth"><span class="n">4</span><span>Second look / don\'t send</span></div>'
            "</div>"
        ),
    },
    {
        "name": "POST-005-slide-en-08.png",
        "dark": True,
        "title": "Keep this",
        "body": (
            '<p class="sub" style="font-size:34px">Appearance isn\'t proof. Panic isn\'t wisdom.</p>'
            '<p class="sub" style="margin-top:20px">Next: AI scams</p>'
            '<div class="cta-pill">Save · Follow · Post 5</div>'
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
        chrome_shot(html_path, ROOT / f"POST-005-hero-{lang}-1080x1080.png")

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

    print("POST-005 visual set complete ->", ROOT)


if __name__ == "__main__":
    main()
