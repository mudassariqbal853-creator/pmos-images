/**
 * Generic TikTok / YouTube Shorts slideshow builder.
 * Takes an existing post's rendered hero + 8 carousel PNGs (already built by
 * Images/POST-NNN/_build/build-postNNN.js) and assembles a 1080x1920 vertical
 * MP4 slideshow, the same shape as POST-001's Images/POST-001/tiktok/*.mp4.
 *
 * Usage: node build-tiktok-video.js <POST-NNN> <ur|en> [secondsPerSlide]
 * Example: node build-tiktok-video.js POST-002 ur
 */
const fs = require("fs");
const path = require("path");
const sharp = require("sharp");
const { execFileSync } = require("child_process");

const FFMPEG =
  process.env.FFMPEG_PATH ||
  "C:\\Users\\mudas\\AppData\\Local\\Microsoft\\WinGet\\Packages\\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\\ffmpeg-8.1.2-full_build\\bin\\ffmpeg.exe";

const TEAL = { r: 10, g: 46, b: 50 }; // matches brand ink/teal background

const [, , post, lang, secArg] = process.argv;
if (!post || !lang) {
  console.error("Usage: node build-tiktok-video.js <POST-NNN> <ur|en> [secondsPerSlide]");
  process.exit(1);
}
const SEC_PER_SLIDE = parseFloat(secArg || "4");

const ROOT = path.join(__dirname, "..", post);
if (!fs.existsSync(ROOT)) {
  console.error("No such post folder:", ROOT);
  process.exit(1);
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

const workDir = path.join(ROOT, "_build", "vertical-" + lang);
fs.mkdirSync(workDir, { recursive: true });

async function main() {
  const padded = [];
  for (let i = 0; i < frames.length; i++) {
    const out = path.join(workDir, `frame-${String(i).padStart(2, "0")}.png`);
    await sharp(frames[i])
      .resize(1080, 1080)
      .extend({
        top: 420,
        bottom: 420,
        left: 0,
        right: 0,
        background: { ...TEAL, alpha: 1 },
      })
      .png()
      .toFile(out);
    padded.push(out);
    console.log("padded", path.basename(out));
  }

  const listPath = path.join(workDir, "concat.txt");
  const lines = padded.map((p) => `file '${p.replace(/\\/g, "/")}'\nduration ${SEC_PER_SLIDE}`);
  // ffmpeg concat demuxer needs the last file repeated without a duration line
  lines.push(`file '${padded[padded.length - 1].replace(/\\/g, "/")}'`);
  fs.writeFileSync(listPath, lines.join("\n"), "utf8");

  const outDir = path.join(ROOT, "tiktok");
  fs.mkdirSync(outDir, { recursive: true });
  const outPath = path.join(outDir, `${post}-tiktok-${lang}-1080x1920.mp4`);

  execFileSync(FFMPEG, [
    "-y",
    "-f", "concat",
    "-safe", "0",
    "-i", listPath,
    "-vf", "fps=30,format=yuv420p",
    "-c:v", "libx264",
    "-pix_fmt", "yuv420p",
    outPath,
  ], { stdio: "inherit" });

  console.log("\nDone:", outPath);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
