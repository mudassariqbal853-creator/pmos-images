/**
 * Generates the fixed PMOS brand audio bed: a synthesized (royalty-free,
 * no samples) beat — kick + hi-hat + bass pulse — layered under the
 * existing ambient pad, looped to 60s with fade in/out.
 * Output: Images/Brand/audio/brand-bed-60s.mp3
 */
const fs = require("fs");
const path = require("path");
const { execFileSync } = require("child_process");

const FFMPEG =
  process.env.FFMPEG_PATH ||
  "C:\\Users\\mudas\\AppData\\Local\\Microsoft\\WinGet\\Packages\\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\\ffmpeg-8.1.2-full_build\\bin\\ffmpeg.exe";

const OUT_DIR = path.join(__dirname, "..", "Brand", "audio");
fs.mkdirSync(OUT_DIR, { recursive: true });
const BAR = path.join(OUT_DIR, "_bar.wav");
const PAD = path.join(OUT_DIR, "_pad.wav");
const FINAL = path.join(OUT_DIR, "brand-bed-60s.mp3");

function run(args) {
  execFileSync(FFMPEG, args, { stdio: "inherit" });
}

// 120 BPM -> 0.5s per beat, 2s bar = 4 beats, 8 eighth-notes.
const BPM = 120;
const BEAT = 60 / BPM; // 0.5s
const BAR_LEN = BEAT * 4; // 2s

function buildBar() {
  const filter = [
    // Kick: low sine thump on beats 1 and 3, fast decay, low-passed for punch.
    `sine=frequency=62:duration=0.22[k0]`,
    `sine=frequency=62:duration=0.22[k1]`,
    `[k0]afade=t=out:st=0:d=0.22,lowpass=f=180,volume=1.6[kick0]`,
    `[k1]afade=t=out:st=0:d=0.22,lowpass=f=180,volume=1.6,adelay=${Math.round(BEAT * 2 * 1000)}|${Math.round(BEAT * 2 * 1000)}[kick1]`,
    // Hi-hat: short filtered noise on every eighth note.
    ...Array.from({ length: 8 }, (_, i) => `anoisesrc=color=white:duration=0.045[hn${i}]`),
    ...Array.from({ length: 8 }, (_, i) =>
      `[hn${i}]highpass=f=7000,afade=t=out:st=0:d=0.045,volume=${i % 2 === 0 ? 0.5 : 0.32},adelay=${Math.round(i * BEAT * 0.5 * 1000)}|${Math.round(i * BEAT * 0.5 * 1000)}[hat${i}]`
    ),
    // Bass pulse: sine on every beat, slightly longer decay than kick, an octave up from kick fundamental feel.
    ...Array.from({ length: 4 }, (_, i) => `sine=frequency=110:duration=0.3[bn${i}]`),
    ...Array.from({ length: 4 }, (_, i) =>
      `[bn${i}]afade=t=out:st=0:d=0.3,lowpass=f=400,volume=0.55,adelay=${Math.round(i * BEAT * 1000)}|${Math.round(i * BEAT * 1000)}[bass${i}]`
    ),
  ].join(";");

  const mixInputs = ["kick0", "kick1", ...Array.from({ length: 8 }, (_, i) => `hat${i}`), ...Array.from({ length: 4 }, (_, i) => `bass${i}`)];
  const fullFilter = `${filter};${mixInputs.map((m) => `[${m}]`).join("")}amix=inputs=${mixInputs.length}:duration=longest:normalize=0[mixed];[mixed]apad=whole_dur=${BAR_LEN},atrim=0:${BAR_LEN},alimiter=limit=0.95[out]`;

  run(["-y", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=mono", "-filter_complex", fullFilter, "-map", "[out]", "-t", String(BAR_LEN), BAR]);
}

function buildPad() {
  run([
    "-y",
    "-f", "lavfi", "-i", "sine=frequency=110:duration=60",
    "-f", "lavfi", "-i", "sine=frequency=164.81:duration=60",
    "-f", "lavfi", "-i", "sine=frequency=220:duration=60",
    "-filter_complex",
    "[0:a]volume=0.5[a0];[1:a]volume=0.4[a1];[2:a]volume=0.32[a2];[a0][a1][a2]amix=inputs=3:duration=longest:normalize=0[mix];[mix]tremolo=f=0.12:d=0.2,aecho=0.6:0.5:60:0.25[out]",
    "-map", "[out]", "-t", "60", PAD,
  ]);
}

function combine() {
  const loops = Math.ceil(60 / BAR_LEN) - 1; // -stream_loop N means N extra repeats
  run([
    "-y",
    "-stream_loop", String(loops), "-i", BAR,
    "-i", PAD,
    "-filter_complex",
    `[0:a]atrim=0:60,volume=1.0[beat];[1:a]volume=0.8[pad];[beat][pad]amix=inputs=2:duration=first:normalize=0[mix];[mix]alimiter=limit=0.92,afade=t=in:st=0:d=1.5,afade=t=out:st=56:d=4[out]`,
    "-map", "[out]", "-t", "60",
    "-c:a", "libmp3lame", "-q:a", "3",
    FINAL,
  ]);
}

buildBar();
console.log("bar built");
buildPad();
console.log("pad built");
combine();
console.log("Done:", FINAL);
