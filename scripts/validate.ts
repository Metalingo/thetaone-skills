import { readdirSync, readFileSync, existsSync } from "node:fs";
import { resolve } from "node:path";

const root = resolve(import.meta.dir, "..");
const dirs = readdirSync(resolve(root, "skills"), { withFileTypes: true }).filter(d => d.isDirectory());
const names = new Set<string>();
let errors = 0;
for (const dir of dirs) {
  const path = resolve(root, "skills", dir.name, "SKILL.md");
  try {
    const source = readFileSync(path, "utf8");
    const match = source.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n([\s\S]+)$/);
    if (!match) throw new Error("Missing frontmatter or body");
    const meta = Bun.YAML.parse(match[1]) as Record<string, unknown>;
    if (meta.name !== dir.name || !/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(dir.name) || dir.name.length > 64) throw new Error("Invalid skill name");
    if (names.has(dir.name)) throw new Error("Duplicate skill name");
    names.add(dir.name);
    if (typeof meta.description !== "string" || !meta.description.trim() || meta.description.length > 1024) throw new Error("Invalid description");
    for (const link of match[2].matchAll(/\]\(([^)]+)\)/g)) {
      if (!/^(?:[a-z]+:|#)/i.test(link[1]) && !existsSync(resolve(root, "skills", dir.name, link[1].split("#")[0]))) throw new Error(`Broken local link: ${link[1]}`);
    }
    console.log(`PASS ${dir.name} (${match[2].trim().split(/\s+/).length} words)`);
  } catch (error) {
    errors++;
    console.error(`FAIL ${dir.name}: ${error instanceof Error ? error.message : error}`);
  }
}
if (!dirs.length) { console.error("No skills found"); errors++; }
console.log(`${dirs.length} skills checked; ${errors} errors`);
process.exitCode = errors ? 1 : 0;
