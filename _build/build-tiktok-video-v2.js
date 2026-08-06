/**
 * Animated TikTok / YouTube Shorts builder — v2.
 * Upgrades v1 (static slideshow, hard cuts) with:
 *  - Ken Burns zoom on every slide (real motion, not a still image)
 *  - Crossfade dissolves between slides (no hard cuts)
 *  - Floating keyword chips, reusing each post's ALREADY-WRITTEN on-screen
 *    text cues from Final/YouTubeShorts.md (no new copy invented — same
 *    approved Urdu/English text, just animated instead of static)
 *
 * Usage: node build-tiktok-video-v2.js <POST-NNN> <ur|en> [secondsPerSlide]
 */
const fs = require("fs");
const path = require("path");
const sharp = require("sharp");
const { execFileSync } = require("child_process");

const FFMPEG =
  process.env.FFMPEG_PATH ||
  "C:\\Users\\mudas\\AppData\\Local\\Microsoft\\WinGet\\Packages\\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\\ffmpeg-8.1.2-full_build\\bin\\ffmpeg.exe";
const CHROME = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";

const TEAL = { r: 10, g: 46, b: 50 };
const AMBER = "#E8B84A";
const INK = "#062E32";

const [, , post, lang, secArg] = process.argv;
if (!post || !lang) {
  console.error("Usage: node build-tiktok-video-v2.js <POST-NNN> <ur|en> [secondsPerSlide]");
  process.exit(1);
}
const SEC_PER_SLIDE = parseFloat(secArg || "4.5");
const FPS = 30;
const TRANS = 0.5; // crossfade duration

const ROOT = path.join(__dirname, "..", post);
const POSTS_ROOT = path.join(__dirname, "..", "..", "Posts");
if (!fs.existsSync(ROOT)) {
  console.error("No such post folder:", ROOT);
  process.exit(1);
}

function findPostDir() {
  const dirs = fs.readdirSync(POSTS_ROOT).filter((d) => d.startsWith(post + "-"));
  if (!dirs.length) throw new Error("No Posts/ folder matching " + post);
  return path.join(POSTS_ROOT, dirs[0]);
}

function parseCues() {
  const postDir = findPostDir();
  const file =
    lang === "ur"
      ? path.join(postDir, "Final", "YouTubeShorts.md")
      : path.join(postDir, "Final", "en", "YouTubeShorts.md");
  if (!fs.existsSync(file)) return [];
  const text = fs.readFileSync(file, "utf8");
  const section = text.split(/## On-screen text cues/)[1];
  if (!section) return [];
  const rows = section
    .split("\n")
    .filter((l) => l.trim().startsWith("|") && !l.includes("---") && !l.includes("Time"));
  const cues = [];
  for (const row of rows) {
    const cells = row.split("|").map((c) => c.trim()).filter(Boolean);
    if (cells.length < 2) continue;
    const m = cells[0].match(/(\d+)[–-](\d+)s/);
    if (!m) continue;
    cues.push({ start: parseFloat(m[1]), end: parseFloat(m[2]), text: cells[1] });
  }
  return cues;
}

const frames = [
  path.join(ROOT, `${post}-hero-${lang}-1080x1080.png`),
  ...Array.from({ length: 8 }, (_, i) =>
    path.join(ROOT, `${post}-slide-${lang}-${String(i + 1).padStart(2, "0")}.png`)
  ),
].filter((f) => fs.existsSync(f));

if (frames.length === 0) {
  console.error("No source PNGs found for", post, lang);
  process.exit(1);
}

const workDir = path.join(ROOT, "_build", "v2-" + lang);
fs.mkdirSync(workDir, { recursive: true });

function run(args) {
  execFileSync(FFMPEG, args, { stdio: "inherit" });
}

async function padFrame(src, out) {
  await sharp(src)
    .resize(1080, 1080)
    .extend({ top: 420, bottom: 420, left: 0, right: 0, background: { ...TEAL, alpha: 1 } })
    .png()
    .toFile(out);
}

function kenBurnsClip(paddedPng, outMp4, durSec, zoomOut) {
  const totalFrames = Math.round(durSec * FPS);
  const zExpr = zoomOut ? "if(eq(on,0),1.06,max(zoom-0.0009,1.0))" : "min(zoom+0.0007,1.06)";
  const centerX = "iw/2-(iw/zoom/2)";
  const centerY = "ih/2-(ih/zoom/2)";
  const vf = `zoompan=z='${zExpr}':x='${centerX}':y='${centerY}':d=${totalFrames}:s=1080x1920:fps=${FPS},format=yuv420p`;
  run(["-y", "-loop", "1", "-i", paddedPng, "-vf", vf, "-t", String(durSec), "-c:v", "libx264", "-pix_fmt", "yuv420p", outMp4]);
}

function crossfadeConcat(clips, durations, outMp4) {
  const inputs = [];
  clips.forEach((c) => inputs.push("-i", c));
  let filter = "";
  let last = "0:v";
  let cum = durations[0];
  for (let i = 1; i < clips.length; i++) {
    const nextLabel = `xf${i}`;
    const offset = Math.max(cum - TRANS, 0);
    filter += `[${last}][${i}:v]xfade=transition=fade:duration=${TRANS}:offset=${offset.toFixed(2)}[${nextLabel}];`;
    last = nextLabel;
    cum = cum + durations[i] - TRANS;
  }
  filter = filter.slice(0, -1);
  run(["-y", ...inputs, "-filter_complex", filter, "-map", `[${last}]`, "-c:v", "libx264", "-pix_fmt", "yuv420p", outMp4]);
  return cum;
}

async function chipPng(text, outPng) {
  const dir = lang === "ur" ? "rtl" : "ltr";
  const html = `<!DOCTYPE html><html lang="${lang}" dir="${dir}"><head><meta charset="utf-8" /><style>
    @font-face { font-family: "Dubai"; src: local("Dubai"), url("file:///C:/Windows/Fonts/DUBAI-BOLD.TTF") format("truetype"); font-weight: 700; }
    html,body{margin:0;padding:0;background:transparent;width:1000px;height:200px;display:flex;align-items:center;justify-content:center;}
    .pill{background:${AMBER};color:${INK};font-family:"Dubai","Segoe UI",sans-serif;font-weight:800;font-size:44px;
      padding:20px 44px;border-radius:999px;box-shadow:0 10px 30px rgba(0,0,0,0.35);white-space:nowrap;direction:${dir};}
  </style></head><body><div class="pill">${text}</div></body></html>`;
  const htmlPath = outPng.replace(".png", ".html");
  fs.writeFileSync(htmlPath, html, "utf8");
  execFileSync(CHROME, [
    "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
    "--window-size=1000,200", "--default-background-color=00000000",
    `--screenshot=${outPng}`, "file:///" + htmlPath.replace(/\\/g, "/"),
  ], { stdio: "ignore" });
}

function overlayChips(baseVideo, cues, chipFiles, outMp4, totalDur) {
  if (!cues.length) {
    fs.copyFileSync(baseVideo, outMp4);
    return;
  }
  const inputs = ["-i", baseVideo];
  cues.forEach((c, i) => inputs.push("-loop", "1", "-t", String(totalDur), "-i", chipFiles[i]));
  let filter = "";
  let last = "0:v";
  cues.forEach((c, i) => {
    const idx = i + 1;
    const label = `ov${i}`;
    const y = `(H*0.135)+14*sin(2*PI*(t-${c.start})/1.4)`;
    filter += `[${idx}:v]scale=760:-1[chip${i}];[${last}][chip${i}]overlay=x=(W-w)/2:y='${y}':enable='between(t,${c.start},${Math.min(c.end, totalDur)})'[${label}];`;
    last = label;
  });
  filter = filter.slice(0, -1);
  run(["-y", ...inputs, "-filter_complex", filter, "-map", `[${last}]`, "-t", String(totalDur), "-shortest", "-c:v", "libx264", "-pix_fmt", "yuv420p", outMp4]);
}

function particlePngs(workDir) {
  // A handful of soft glowing dot/ring "node" particles (AI-network motif),
  // brand amber + teal, transparent background, various sizes.
  const specs = [
    { name: "p-dot-amber.png", size: 40, color: AMBER, ring: false },
    { name: "p-dot-teal.png", size: 34, color: "#3FBFB0", ring: false },
    { name: "p-ring-amber.png", size: 60, color: AMBER, ring: true },
    { name: "p-ring-teal.png", size: 54, color: "#3FBFB0", ring: true },
  ];
  const out = [];
  for (const s of specs) {
    const p = path.join(workDir, s.name);
    const svg = s.ring
      ? `<svg xmlns="http://www.w3.org/2000/svg" width="${s.size}" height="${s.size}"><circle cx="${s.size / 2}" cy="${s.size / 2}" r="${s.size / 2 - 4}" fill="none" stroke="${s.color}" stroke-width="4" opacity="0.55"/></svg>`
      : `<svg xmlns="http://www.w3.org/2000/svg" width="${s.size}" height="${s.size}"><circle cx="${s.size / 2}" cy="${s.size / 2}" r="${s.size / 2 - 2}" fill="${s.color}" opacity="0.5"/></svg>`;
    out.push({ file: p, svg });
  }
  return out;
}

async function renderParticles(workDir) {
  const specs = particlePngs(workDir);
  for (const s of specs) {
    await sharp(Buffer.from(s.svg)).png().toFile(s.file);
  }
  return specs.map((s) => s.file);
}

function overlayParticles(baseVideo, particleFiles, outMp4, totalDur) {
  // 7 particles drifting slowly with individual paths, low opacity, behind chip layer timing-wise
  // (applied to base BEFORE chip overlay so keyword chips stay crisply on top).
  const n = 7;
  const inputs = ["-i", baseVideo];
  const picks = [];
  for (let i = 0; i < n; i++) {
    const file = particleFiles[i % particleFiles.length];
    inputs.push("-loop", "1", "-t", String(totalDur), "-i", file);
    picks.push(file);
  }
  let filter = "";
  let last = "0:v";
  for (let i = 0; i < n; i++) {
    const idx = i + 1;
    const label = `pp${i}`;
    // Spread starting positions across the canvas; slow diagonal drift + gentle bob.
    const x0 = 80 + ((i * 137) % 900);
    const y0 = 200 + ((i * 271) % 1500);
    const dir = i % 2 === 0 ? 1 : -1;
    const speed = 6 + (i % 3) * 3;
    const x = `${x0}+${dir}*${speed}*t`;
    const y = `${y0}+40*sin(2*PI*(t+${i})/6)`;
    filter += `[${last}][${idx}:v]overlay=x='mod(${x},1080)':y='mod(${y},1920)'[${label}];`;
    last = label;
  }
  filter = filter.slice(0, -1);
  run(["-y", ...inputs, "-filter_complex", filter, "-map", `[${last}]`, "-t", String(totalDur), "-c:v", "libx264", "-pix_fmt", "yuv420p", outMp4]);
}

const AUDIO_BED = path.join(__dirname, "..", "Brand", "audio", "brand-bed-60s.mp3");

function muxAudio(videoIn, audioIn, outMp4, totalDur) {
  if (!fs.existsSync(audioIn)) {
    fs.copyFileSync(videoIn, outMp4);
    return;
  }
  run([
    "-y", "-i", videoIn, "-i", audioIn,
    "-filter_complex", `[1:a]afade=t=out:st=${Math.max(totalDur - 2, 0)}:d=2[a]`,
    "-map", "0:v", "-map", "[a]",
    "-c:v", "copy", "-c:a", "aac", "-b:a", "128k",
    "-t", String(totalDur), "-shortest", outMp4,
  ]);
}

async function main() {
  const cues = parseCues();
  console.log("cues:", cues.length);

  const baseOut = path.join(workDir, "base-crossfade.mp4");
  let totalDur = SEC_PER_SLIDE * frames.length - TRANS * (frames.length - 1);

  if (fs.existsSync(baseOut) && process.env.REUSE_BASE === "1") {
    console.log("reusing existing crossfade base:", baseOut);
  } else {
    const paddedFiles = [];
    for (let i = 0; i < frames.length; i++) {
      const out = path.join(workDir, `pad-${String(i).padStart(2, "0")}.png`);
      await padFrame(frames[i], out);
      paddedFiles.push(out);
    }

    const clipFiles = [];
    const durations = [];
    for (let i = 0; i < paddedFiles.length; i++) {
      const out = path.join(workDir, `kb-${String(i).padStart(2, "0")}.mp4`);
      kenBurnsClip(paddedFiles[i], out, SEC_PER_SLIDE, i % 3 === 2);
      clipFiles.push(out);
      durations.push(SEC_PER_SLIDE);
      console.log("ken-burns clip", i + 1, "/", paddedFiles.length);
    }

    totalDur = crossfadeConcat(clipFiles, durations, baseOut);
    console.log("crossfade base built, ~duration", totalDur.toFixed(1), "s");
  }

  const particleFiles = await renderParticles(workDir);
  const particlesOut = path.join(workDir, "with-particles.mp4");
  overlayParticles(baseOut, particleFiles, particlesOut, totalDur);
  console.log("particles composited");

  const chipFiles = [];
  for (let i = 0; i < cues.length; i++) {
    const out = path.join(workDir, `chip-${i}.png`);
    await chipPng(cues[i].text, out);
    chipFiles.push(out);
  }

  const withChipsOut = path.join(workDir, "with-chips.mp4");
  overlayChips(particlesOut, cues, chipFiles, withChipsOut, totalDur);
  console.log("chips composited");

  const outDir = path.join(ROOT, "tiktok");
  fs.mkdirSync(outDir, { recursive: true });
  const finalOut = path.join(outDir, `${post}-tiktok-${lang}-1080x1920-v2.mp4`);
  muxAudio(withChipsOut, AUDIO_BED, finalOut, totalDur);

  console.log("\nDone:", finalOut);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
