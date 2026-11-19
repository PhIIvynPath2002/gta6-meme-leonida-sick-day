// gta6-meme-x-01 entry (Node 22, standard library only).
//
// The entry itself is the X post: a GTA 6 meme whose first picture is
// meme.png in this repository, posted from a public X account with
// make.fun and the entrant's play code in its text. This program does
// nothing about the post except hand its address to the grader: it
// copies POST.json from the repository root to /output/POST.json, where
// the gate reads it and the house then reads the post from X itself.
//
// Run it the way the grader does:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync, readFileSync } from "node:fs";
import { join } from "node:path";

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? "/bot";
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

const post = JSON.parse(readFileSync(join(BOT_DIR, "POST.json"), "utf8"));
const url = typeof post.url === "string" ? post.url : "";
const isXPost =
  /^https:\/\/(www\.|mobile\.)?(x\.com|twitter\.com)\/\w+\/status\/\d+$/.test(url) ||
  /^https:\/\/(www\.|mobile\.)?(x\.com|twitter\.com)\/i\/web\/status\/\d+$/.test(url);
if (!isXPost) {
  console.error("POST.json does not name an X post URL");
  process.exit(1);
}

mkdirSync(OUTPUT_DIR, { recursive: true });
copyFileSync(join(BOT_DIR, "POST.json"), join(OUTPUT_DIR, "POST.json"));
