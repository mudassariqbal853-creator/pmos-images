# POST-012 visual set - Clarity Path (teal/amber)
# Heroes + 8+8 Instagram carousel. LinkedIn/TikTok skipped unless asked.
# UR art: Urdu script only. No Latin islands. No em dashes.
# Concept: claim ("new law, effective tomorrow") vs stages (bill - committee - vote - assent)
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
  .steps {{ display: flex; flex-direction: column; gap: 10px; margin-top: 12px; }}
  .step {{
    display: flex; align-items: center; gap: 16px;
    font-size: 27px; font-weight: 700; line-height: 1.3;
    padding: 12px 18px; border-radius: 16px;
    background: rgba(10,85,92,0.06);
  }}
  .slide.dark .step {{ background: rgba(255,255,255,0.1); }}
  .step .n {{
    width: 40px; height: 40px; border-radius: 12px; flex-shrink: 0;
    background: {COLORS["amber"]}; color: {COLORS["ink"]};
    font-weight: 900; font-size: 18px;
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
    font-size: 46px; font-weight: 700; line-height: 1.3;
    margin-bottom: 10px;
    text-shadow: 0 4px 20px rgba(0,0,0,0.25);
  }}
  .sub {{ font-size: 27px; font-weight: 500; line-height: 1.4; opacity: 0.92; }}
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
    text-align: center; min-height: 380px;
    display: flex; flex-direction: column; align-items: center; justify-content: flex-start;
  }}
  .lane-bold {{
    background: linear-gradient(165deg, #C9A03A 0%, #E8B84A 55%, #F0C96A 100%);
    color: #062E32; box-shadow: 0 8px 20px rgba(200,160,50,0.28);
  }}
  .lane-read {{
    background: linear-gradient(165deg, #0A555C 0%, #0E6A72 100%);
    color: #fff; box-shadow: 0 8px 20px rgba(10,85,92,0.28);
  }}
  .lane-tag {{
    font-size: 16px; font-weight: 800;
    padding: 5px 14px; border-radius: 999px; margin-bottom: 12px;
  }}
  .lane-bold .lane-tag {{ background: rgba(6,46,50,0.12); color: #062E32; }}
  .lane-read .lane-tag {{ background: #E8B84A; color: #062E32; }}
  .lane h3 {{ font-size: 24px; font-weight: 700; line-height: 1.3; margin-bottom: 8px; }}
  .lane .desc {{ font-size: 18px; line-height: 1.3; opacity: 0.95; margin-bottom: 14px; }}
  .visual {{
    margin-top: auto; width: 100%;
    display: flex; flex-direction: column; align-items: center; gap: 10px;
  }}
  .door-sign {{
    width: 88%;
    background: rgba(255,255,255,0.55);
    border: 2px solid rgba(6,46,50,0.2);
    border-radius: 14px;
    padding: 18px 14px;
    box-shadow: inset 0 0 0 1px rgba(255,255,255,0.35);
  }}
  .door-sign .mega {{
    font-size: 23px; font-weight: 900; line-height: 1.3;
    letter-spacing: 0.02em;
  }}
  .door-sign .blank {{
    margin-top: 12px;
    height: 9px; border-radius: 6px;
    background: rgba(6,46,50,0.12);
  }}
  .door-sign .blank.short {{ width: 55%; margin-left: auto; margin-right: auto; }}
  .door-sign .blank.mid {{ width: 78%; margin-left: auto; margin-right: auto; }}
  .door-sign.ltr .mega {{ font-family: "Segoe UI", sans-serif; }}
  .checks {{
    background: rgba(255,255,255,0.14);
    border-radius: 16px;
    padding: 10px 10px;
    width: 92%;
  }}
  .checks.rtl {{ text-align: right; }}
  .checks.ltr {{ text-align: left; }}
  .checks .row {{
    font-size: 17px; font-weight: 700; line-height: 1.3;
    padding: 4px 0;
    border-bottom: 1px solid rgba(255,255,255,0.16);
    display: flex; align-items: center; gap: 10px;
  }}
  .checks .row:last-child {{ border-bottom: none; }}
  .ico {{
    width: 25px; height: 25px; border-radius: 7px; flex-shrink: 0;
    background: rgba(232,184,74,0.95); color: #062E32;
    font-size: 13px; font-weight: 900;
    display: flex; align-items: center; justify-content: center;
  }}
  .status {{
    margin-top: 12px;
    font-size: 17px; font-weight: 700;
    padding: 6px 14px; border-radius: 999px;
  }}
  .lane-bold .status {{ background: rgba(6,46,50,0.88); color: #E8B84A; }}
  .lane-read .status {{ background: rgba(232,184,74,0.95); color: #062E32; }}
  .takeaway {{
    display: block; text-align: center;
    background: #E8B84A; color: #062E32;
    font-size: 23px; font-weight: 700;
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
    door_cls = "" if is_ur else " ltr"
    badge = "شہری خواندگی · پوسٹ ۱۲" if is_ur else "Civic Literacy · Post 12"
    hook = (
        "قانون کیسے بنتا ہے؟"
        if is_ur
        else 'How does a bill become <span class="hl">law</span>?'
    )
    sub = "دعویٰ اور مرحلے میں فرق کیسے کریں" if is_ur else "How to tell a claim from a real stage"
    panel = "دعویٰ · مراحل" if is_ur else "Claim · stages"
    b_tag = "دعویٰ؟" if is_ur else "Claim?"
    b_h = "دعویٰ" if is_ur else "Claim"
    b_d = "\u201cکل سے لاگو\u201d" if is_ur else "\u201cEffective tomorrow\u201d"
    b_mega = "نیا قانون؟" if is_ur else "New law?"
    b_status = "غیر یقینی" if is_ur else "Unverified"
    r_tag = "مرحلہ؟" if is_ur else "Stage?"
    r_h = "مراحل" if is_ur else "Stages"
    r_d = "بل · کمیٹی · ووٹ · منظوری" if is_ur else "Bill · committee · vote · assent"
    checks = (
        [("۱", "بل"), ("۲", "کمیٹی"), ("۳", "ووٹ"), ("۴", "منظوری")]
        if is_ur
        else [("1", "Bill"), ("2", "Committee"), ("3", "Vote"), ("4", "Assent")]
    )
    r_status = "تصدیق شدہ عادت" if is_ur else "Verified habit"
    take = "دعویٰ خود قانون نہیں، مرحلہ چیک کرو" if is_ur else "A claim is not the law itself, check the stage"
    footer = (
        "پاکستان میڈیا او ایس · شہری خواندگی · پوسٹ ۱۲"
        if is_ur
        else "Pakistan Media OS · Civic Literacy · Post 12"
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
        <div class="lane lane-bold">
          <div class="lane-tag">{b_tag}</div>
          <h3>{b_h}</h3>
          <p class="desc">{b_d}</p>
          <div class="visual">
            <div class="door-sign{door_cls}">
              <div class="mega">{b_mega}</div>
              <div class="blank mid"></div>
              <div class="blank short"></div>
            </div>
          </div>
          <div class="status">{b_status}</div>
        </div>
        <div class="lane lane-read">
          <div class="lane-tag">{r_tag}</div>
          <h3>{r_h}</h3>
          <p class="desc">{r_d}</p>
          <div class="visual">
            <div class="checks {checks_cls}">
              {check_rows}
            </div>
          </div>
          <div class="status">{r_status}</div>
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
    series = "شہری خواندگی · پوسٹ ۱۲" if lang == "ur" else "Civic Literacy · Post 12"
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


FOOT_UR = "پاکستان میڈیا او ایس · شہری خواندگی · پوسٹ ۱۲"
FOOT_EN = "Pakistan Media OS · Civic Literacy · Post 12"

SLIDES_UR = [
    {
        "name": "POST-012-slide-ur-01.png",
        "dark": True,
        "title": "قانون کیسے بنتا ہے؟",
        "body": '<p class="sub">مرحلہ · بل یا آرڈیننس · منظوری</p><p class="sub" style="margin-top:18px">پوسٹ ۱۲</p>',
    },
    {
        "name": "POST-012-slide-ur-02.png",
        "dark": False,
        "title": "\u201cنیا قانون، کل سے لاگو\u201d",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>فارورڈ پر بحث شروع</span></li>'
            '<li><span class="dot"></span><span>اصل میں صرف بل تھا</span></li>'
            '<li><span class="dot"></span><span>ووٹ سے کوسوں دور</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-012-slide-ur-03.png",
        "dark": False,
        "title": "پوسٹ ۸ سے",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>جاری کنندہ چیک کرو</span></li>'
            '<li><span class="dot"></span><span>آج: قانون کے بھی اصل مراحل ہیں</span></li>'
            '<li><span class="dot"></span><span>عادت جاری رہتی ہے</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-012-slide-ur-04.png",
        "dark": False,
        "title": "عمومی خاکہ",
        "body": (
            '<div class="steps">'
            '<div class="step"><span class="n">۱</span><span>بل</span></div>'
            '<div class="step"><span class="n">۲</span><span>کمیٹی</span></div>'
            '<div class="step"><span class="n">۳</span><span>ایوان کا ووٹ</span></div>'
            '<div class="step"><span class="n">۴</span><span>دوسرا ایوان</span></div>'
            '<div class="step"><span class="n">۵</span><span>صدارتی منظوری</span></div>'
            "</div>"
        ),
    },
    {
        "name": "POST-012-slide-ur-05.png",
        "dark": False,
        "title": "عام غلط فہمیاں ۱ تا ۳",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>ایک شخص کا فیصلہ</span></li>'
            '<li><span class="dot"></span><span>فوری قانون</span></li>'
            '<li><span class="dot"></span><span>صرف ایوان کا ووٹ</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-012-slide-ur-06.png",
        "dark": False,
        "title": "عام غلط فہمیاں ۴ و ۵",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>ایک ایوان کی تصویر</span></li>'
            '<li><span class="dot"></span><span>آرڈیننس کو مستقل سمجھنا</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-012-slide-ur-07.png",
        "dark": False,
        "title": "پانچ سوال",
        "body": (
            '<div class="truths">'
            '<div class="truth"><span class="n">۱</span><span>کون سا مرحلہ؟</span></div>'
            '<div class="truth"><span class="n">۲</span><span>بل یا آرڈیننس؟</span></div>'
            '<div class="truth"><span class="n">۳</span><span>کون سا ایوان؟</span></div>'
            '<div class="truth"><span class="n">۴</span><span>صدارتی منظوری ملی؟</span></div>'
            '<div class="truth"><span class="n">۵</span><span>اصل متن کہاں؟</span></div>'
            "</div>"
        ),
    },
    {
        "name": "POST-012-slide-ur-08.png",
        "dark": True,
        "title": "یاد رکھیں",
        "body": (
            '<p class="sub" style="font-size:32px">دعویٰ خود قانون نہیں، مرحلہ چیک کرو۔</p>'
            '<p class="sub" style="margin-top:20px">شہری خواندگی سیریز جاری ہے</p>'
            '<div class="cta-pill">محفوظ کریں · فالو کریں · پوسٹ ۱۲</div>'
        ),
    },
]

SLIDES_EN = [
    {
        "name": "POST-012-slide-en-01.png",
        "dark": True,
        "title": 'How does a bill become <span class="hl">law</span>?',
        "body": '<p class="sub">Stage · bill or ordinance · assent</p><p class="sub" style="margin-top:18px">Post 12</p>',
    },
    {
        "name": "POST-012-slide-en-02.png",
        "dark": False,
        "title": "\u201cNew law, effective tomorrow\u201d",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>Forward sparks a debate</span></li>'
            '<li><span class="dot"></span><span>It was actually just a bill</span></li>'
            '<li><span class="dot"></span><span>Nowhere near a vote</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-012-slide-en-03.png",
        "dark": False,
        "title": "From Post 8",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>Check the issuer</span></li>'
            '<li><span class="dot"></span><span>Today: a law has real stages too</span></li>'
            '<li><span class="dot"></span><span>Same habit continues</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-012-slide-en-04.png",
        "dark": False,
        "title": "The general shape",
        "body": (
            '<div class="steps">'
            '<div class="step"><span class="n">1</span><span>Bill</span></div>'
            '<div class="step"><span class="n">2</span><span>Committee</span></div>'
            '<div class="step"><span class="n">3</span><span>House vote</span></div>'
            '<div class="step"><span class="n">4</span><span>Other house</span></div>'
            '<div class="step"><span class="n">5</span><span>Presidential assent</span></div>'
            "</div>"
        ),
    },
    {
        "name": "POST-012-slide-en-05.png",
        "dark": False,
        "title": "Common myths 1-3",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>One-person decision</span></li>'
            '<li><span class="dot"></span><span>Instant law</span></li>'
            '<li><span class="dot"></span><span>Floor-vote-only picture</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-012-slide-en-06.png",
        "dark": False,
        "title": "Common myths 4-5",
        "body": (
            '<ul class="bullets">'
            '<li><span class="dot"></span><span>One-house picture</span></li>'
            '<li><span class="dot"></span><span>Ordinance mistaken for permanent law</span></li>'
            "</ul>"
        ),
    },
    {
        "name": "POST-012-slide-en-07.png",
        "dark": False,
        "title": "Five questions",
        "body": (
            '<div class="truths">'
            '<div class="truth"><span class="n">1</span><span>Which stage?</span></div>'
            '<div class="truth"><span class="n">2</span><span>Bill or ordinance?</span></div>'
            '<div class="truth"><span class="n">3</span><span>Which house?</span></div>'
            '<div class="truth"><span class="n">4</span><span>Assent given?</span></div>'
            '<div class="truth"><span class="n">5</span><span>Where\'s the text?</span></div>'
            "</div>"
        ),
    },
    {
        "name": "POST-012-slide-en-08.png",
        "dark": True,
        "title": "Remember",
        "body": (
            '<p class="sub" style="font-size:32px">A claim is not the law itself, check the stage.</p>'
            '<p class="sub" style="margin-top:20px">Civic Literacy series continues</p>'
            '<div class="cta-pill">Save · Follow · Post 12</div>'
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
        chrome_shot(html_path, ROOT / f"POST-012-hero-{lang}-1080x1080.png")

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

    print("POST-012 visual set complete ->", ROOT)


if __name__ == "__main__":
    main()
