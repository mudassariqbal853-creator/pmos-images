# POST-007 visual set — Clarity Path (teal/amber)
# Heroes + 8+8 Instagram carousel. LinkedIn/TikTok skipped unless asked.
# UR art: Urdu script only. No Latin islands. No em dashes.
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
    font-size: 50px; font-weight: 700; line-height: 1.3;
    margin-bottom: 20px;
  }}
  .slide.dark .h1 {{ font-size: 54px; text-shadow: 0 4px 20px rgba(0,0,0,0.25); }}
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
  .truths {{ display: flex; flex-direction: column; gap: 12px; margin-top: 12px; }}
  .truth {{
    background: {COLORS["white"]};
    border: 2px solid {COLORS["mist"]};
    border-radius: 18px;
    padding: 16px 20px;
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
    font-size: 50px; font-weight: 700; line-height: 1.3;
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
  .lane-forward {{
    background: linear-gradient(165deg, #C9A03A 0%, #E8B84A 55%, #F0C96A 100%);
    color: #062E32; box-shadow: 0 8px 20px rgba(200,160,50,0.28);
  }}
  .lane-check {{
    background: linear-gradient(165deg, #0A555C 0%, #0E6A72 100%);
    color: #fff; box-shadow: 0 8px 20px rgba(10,85,92,0.28);
  }}
  .lane-tag {{
    font-size: 16px; font-weight: 800;
    padding: 5px 14px; border-radius: 999px; margin-bottom: 12px;
  }}
  .lane-forward .lane-tag {{ background: rgba(6,46,50,0.12); color: #062E32; }}
  .lane-check .lane-tag {{ background: #E8B84A; color: #062E32; }}
  .lane h3 {{ font-size: 26px; font-weight: 700; line-height: 1.35; margin-bottom: 8px; }}
  .lane .desc {{ font-size: 20px; line-height: 1.35; opacity: 0.95; margin-bottom: 14px; }}
  .visual {{
    margin-top: auto; width: 100%;
    display: flex; flex-direction: column; align-items: center; gap: 10px;
  }}
  .bubble {{
    background: rgba(6,46,50,0.12);
    border: 2px solid rgba(6,46,50,0.2);
    border-radius: 18px 18px 6px 18px;
    padding: 14px 16px;
    font-size: 18px; font-weight: 700; line-height: 1.35;
    max-width: 92%; text-align: right;
  }}
  .bubble.ltr {{ border-radius: 18px 18px 18px 6px; text-align: left; }}
  .crop-note {{
    background: rgba(6,46,50,0.1);
    border: 2px dashed rgba(6,46,50,0.35);
    border-radius: 12px;
    padding: 10px 12px;
    font-size: 16px; font-weight: 700;
    max-width: 88%;
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
  .checks .row:last-child {{ border-bottom: none; }}
  .ico {{
    width: 28px; height: 28px; border-radius: 8px; flex-shrink: 0;
    background: rgba(232,184,74,0.95); color: #062E32;
    font-size: 14px; font-weight: 900;
    display: flex; align-items: center; justify-content: center;
  }}
  .status {{
    margin-top: 12px;
    font-size: 18px; font-weight: 700;
    padding: 6px 14px; border-radius: 999px;
  }}
  .lane-forward .status {{ background: rgba(6,46,50,0.88); color: #E8B84A; }}
  .lane-check .status {{ background: rgba(232,184,74,0.95); color: #062E32; }}
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
    checks_cls = "rtl" if is_ur else "ltr"
    bubble_cls = "" if is_ur else " ltr"
    badge = "شہری خواندگی · پوسٹ ۷" if is_ur else "Civic Literacy · Post 7"
    hook = "فارورڈ آیا تو ثابت ہو گیا؟" if is_ur else 'Forwarded means <span class="hl">proven</span>?'
    sub = "عوامی دعوے کیسے پرکھیں" if is_ur else "How to check public claims"
    panel = "فارورڈ · اصل ذریعہ" if is_ur else "Forward · primary source"
    f_tag = "رفتار" if is_ur else "Speed"
    f_h = "فارورڈ / کٹی نوٹس" if is_ur else "Forward / cropped notice"
    f_d = "رفتار = ثبوت؟" if is_ur else "Speed = proof?"
    f_bubble = "«کل سے فیس بدل گئی»" if is_ur else '"Fee changes tomorrow"'
    f_crop = "کٹی «سرکاری» تصویر" if is_ur else 'Cropped "official" photo'
    f_status = "ثبوت نہیں" if is_ur else "Not proof"
    c_tag = "جانچ" if is_ur else "Check"
    c_h = "اصل ذریعہ" if is_ur else "Primary source"
    c_d = "جاری کنندہ · تاریخ · اصل" if is_ur else "Issuer · date · original"
    checks = (
        [("۱", "جاری کنندہ"), ("۲", "تاریخ"), ("۳", "اصل ذریعہ")]
        if is_ur
        else [("1", "Issuer"), ("2", "Date"), ("3", "Primary source")]
    )
    c_status = "حقیقت کی عادت" if is_ur else "Check habit"
    take = "فارورڈ ثبوت نہیں · جانچو" if is_ur else "A forward is not proof · Check"
    footer = (
        "پاکستان میڈیا او ایس · شہری خواندگی · پوسٹ ۷"
        if is_ur
        else "Pakistan Media OS · Civic Literacy · Post 7"
    )
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
        <div class="lane lane-forward">
          <div class="lane-tag">{f_tag}</div>
          <h3>{f_h}</h3>
          <p class="desc">{f_d}</p>
          <div class="visual">
            <div class="bubble{bubble_cls}">{f_bubble}</div>
            <div class="crop-note">{f_crop}</div>
          </div>
          <div class="status">{f_status}</div>
        </div>
        <div class="lane lane-check">
          <div class="lane-tag">{c_tag}</div>
          <h3>{c_h}</h3>
          <p class="desc">{c_d}</p>
          <div class="visual">
            <div class="checks {checks_cls}">
              {check_rows}
            </div>
          </div>
          <div class="status">{c_status}</div>
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
    series = "شہری خواندگی · پوسٹ ۷" if lang == "ur" else "Civic Literacy · Post 7"
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


FOOT_UR = "پاکستان میڈیا او ایس · شہری خواندگی · پوسٹ ۷"
FOOT_EN = "Pakistan Media OS · Civic Literacy · Post 7"

SLIDES_UR = [
    {
        "name": "POST-007-slide-ur-01.png",
        "dark": True,
        "title": "فارورڈ آیا تو ثابت ہو گیا؟",
        "body": '<p class="sub">عوامی دعوے کیسے پرکھیں</p><p class="sub" style="margin-top:18px">پوسٹ ۷</p>',
    },
    {
        "name": "POST-007-slide-ur-02.png",
        "dark": False,
        "title": "واٹس ایپ گروپ",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>کٹی ہوئی «سرکاری» تصویر</span></li>'
            '<li><span class="dot"></span><span>«کل سے فیس بدل گئی»</span></li>'
            '<li><span class="dot"></span><span>بحث شروع۔ ثبوت نہیں۔</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-007-slide-ur-03.png",
        "dark": False,
        "title": "اے آئی سیریز سے",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>لیبل ≠ ثبوت</span></li>'
            '<li><span class="dot"></span><span>اونچے داؤ پر جانچ</span></li>'
            '<li><span class="dot"></span><span>آج: عوامی دعوے</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-007-slide-ur-04.png",
        "dark": False,
        "title": "حقیقت",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>فارورڈ = دعوے کی کاپی</span></li>'
            '<li><span class="dot"></span><span>سرکاری لگنا ≠ جاری ہونا</span></li>'
            '<li><span class="dot"></span><span>حقیقت / رائے / پیش گوئی الگ</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-007-slide-ur-05.png",
        "dark": False,
        "title": "شکلیں ۱ تا ۳",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>کٹی ہوئی نوٹس</span></li>'
            '<li><span class="dot"></span><span>پرانی نوٹس نیا حکم</span></li>'
            '<li><span class="dot"></span><span>افواہ بطور خبر</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-007-slide-ur-06.png",
        "dark": False,
        "title": "شکلیں ۴ و ۵",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>رائے بطور فیصلہ</span></li>'
            '<li><span class="dot"></span><span>پیش گوئی بطور ہو چکا معاملہ</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-007-slide-ur-07.png",
        "dark": False,
        "title": "پانچ سوال",
        "body": (
            '<div class="truths">'
            '<div class="truth"><span class="n">۱</span><span>کس نے جاری کیا؟</span></div>'
            '<div class="truth"><span class="n">۲</span><span>اصل ذریعہ؟</span></div>'
            '<div class="truth"><span class="n">۳</span><span>تاریخ؟</span></div>'
            '<div class="truth"><span class="n">۴</span><span>حقیقت / رائے / پیش گوئی؟</span></div>'
            '<div class="truth"><span class="n">۵</span><span>غلط تو کیا نقصان؟</span></div>'
            "</div>"
        ),
    },
    {
        "name": "POST-007-slide-ur-08.png",
        "dark": True,
        "title": "یاد رکھیں",
        "body": (
            '<p class="sub" style="font-size:34px">جانچنا وفاداری کا امتحان نہیں۔</p>'
            '<p class="sub" style="margin-top:20px">اگلا: سرکاری نوٹس کیسے پڑھیں</p>'
            '<div class="cta-pill">محفوظ کریں · فالو کریں · پوسٹ ۷</div>'
        ),
    },
]

SLIDES_EN = [
    {
        "name": "POST-007-slide-en-01.png",
        "dark": True,
        "title": 'Forwarded means <span class="hl">proven</span>?',
        "body": '<p class="sub">How to check public claims</p><p class="sub" style="margin-top:18px">Post 7</p>',
    },
    {
        "name": "POST-007-slide-en-02.png",
        "dark": False,
        "title": "WhatsApp group",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>Cropped "official" photo</span></li>'
            '<li><span class="dot"></span><span>"Fee changes tomorrow"</span></li>'
            '<li><span class="dot"></span><span>Debate starts. Proof does not.</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-007-slide-en-03.png",
        "dark": False,
        "title": "From the AI series",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>Label ≠ proof</span></li>'
            '<li><span class="dot"></span><span>Check high stakes</span></li>'
            '<li><span class="dot"></span><span>Today: public claims</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-007-slide-en-04.png",
        "dark": False,
        "title": "Reality",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>Forward = copy of a claim</span></li>'
            '<li><span class="dot"></span><span>Looking official ≠ issued</span></li>'
            '<li><span class="dot"></span><span>Fact / opinion / prediction stay separate</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-007-slide-en-05.png",
        "dark": False,
        "title": "Shapes 1-3",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>Cropped notice</span></li>'
            '<li><span class="dot"></span><span>Old notice as today\'s order</span></li>'
            '<li><span class="dot"></span><span>Rumor as news</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-007-slide-en-06.png",
        "dark": False,
        "title": "Shapes 4-5",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>Opinion as decision</span></li>'
            '<li><span class="dot"></span><span>Prediction as done deal</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-007-slide-en-07.png",
        "dark": False,
        "title": "Five questions",
        "body": (
            '<div class="truths">'
            '<div class="truth"><span class="n">1</span><span>Who issued it?</span></div>'
            '<div class="truth"><span class="n">2</span><span>Primary source?</span></div>'
            '<div class="truth"><span class="n">3</span><span>Date?</span></div>'
            '<div class="truth"><span class="n">4</span><span>Fact / opinion / prediction?</span></div>'
            '<div class="truth"><span class="n">5</span><span>Harm if wrong?</span></div>'
            "</div>"
        ),
    },
    {
        "name": "POST-007-slide-en-08.png",
        "dark": True,
        "title": "Remember",
        "body": (
            '<p class="sub" style="font-size:34px">Checking is not a loyalty test.</p>'
            '<p class="sub" style="margin-top:20px">Next: how to read an official notice</p>'
            '<div class="cta-pill">Save · Follow · Post 7</div>'
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
        chrome_shot(html_path, ROOT / f"POST-007-hero-{lang}-1080x1080.png")

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

    print("POST-007 visual set complete ->", ROOT)


if __name__ == "__main__":
    main()
