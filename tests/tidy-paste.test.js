// Runs the real <script> out of tidy-paste/index.html against a minimal fake DOM,
// so the parsing logic is tested as shipped rather than as a copy.
//
//   node tests/tidy-paste.test.js
//
// No test framework on purpose — same reason build.py has no dependencies: this
// has to run in a bare sandbox where `npm install` is a coin flip. Read the
// output and check it; the cases are chosen so wrong answers are obvious.
const fs = require("fs");
const path = require("path");

const file = process.argv[2] ||
  path.join(__dirname, "..", "tools", "tidy-paste", "index.html");
const html = fs.readFileSync(file, "utf8");
const m = html.match(/<script>([\s\S]*?)<\/script>/);
if (!m) throw new Error("no script block found");
const src = m[1];

function makeEl(tag) {
  const el = {
    tagName: tag,
    value: "",
    checked: false,
    disabled: false,
    className: "",
    textContent: "",
    title: "",
    href: "",
    download: "",
    style: {},
    children: [],
    _listeners: {},
    appendChild(c) { this.children.push(c); return c; },
    removeChild(c) { this.children = this.children.filter(x => x !== c); },
    setAttribute() {},
    addEventListener(evt, fn) { (this._listeners[evt] ||= []).push(fn); },
    fire(evt) { (this._listeners[evt] || []).forEach(fn => fn()); },
    select() {}, focus() {}, click() {},
  };
  // Setting innerHTML must actually drop children, or reads go stale.
  let _html = "";
  Object.defineProperty(el, "innerHTML", {
    get: () => _html,
    set(v) { _html = v; if (v === "") el.children = []; },
  });
  return el;
}

const els = {};
["in", "mode", "out", "status", "trim", "blanks", "dedupe", "hdr", "copy", "csv", "clear"]
  .forEach(id => { els[id] = makeEl(id); });

els.trim.checked = true;
els.blanks.checked = true;
els.mode.value = "auto";

global.document = {
  getElementById: id => els[id],
  createElement: makeEl,
  body: makeEl("body"),
  execCommand: () => true,
};
function setNavigator(v) {
  // Node >=21 defines `navigator` as a read-only accessor, so plain assignment
  // silently does nothing.
  Object.defineProperty(global, "navigator", { value: v, configurable: true, writable: true });
}
setNavigator({});
global.window = global;

eval(src);

// ---- Read the rendered table back out of the fake DOM ----
function readTable() {
  const table = els.out.children.find(c => c.tagName === "table");
  if (!table) return null;
  const [thead, tbody] = table.children;
  const headers = thead.children[0].children
    .slice(1)
    .map(th => th.children.find(c => c.tagName === "input").value);
  const rows = tbody.children.map(tr => tr.children.slice(1).map(td => td.textContent));
  return { headers, rows };
}

function run(name, text, opts = {}) {
  els.mode.value = opts.mode || "auto";
  els.trim.checked = opts.trim !== false;
  els.blanks.checked = opts.blanks !== false;
  els.dedupe.checked = !!opts.dedupe;
  els.hdr.checked = !!opts.hdr;
  els.in.value = text;
  els.in.fire("input");
  const t = readTable();
  console.log("\n=== " + name + " ===");
  console.log("status:", els.status.textContent);
  if (!t) { console.log("(no table)"); return; }
  console.log("headers:", JSON.stringify(t.headers));
  t.rows.forEach(r => console.log("  ", JSON.stringify(r)));
}

run("tabs", "Name\tEmail\nDana\tdana@example.com\nMarcus\tmarcus@example.org", { hdr: true });

run("csv with quoted comma", 'Name,City\n"Whitfield, Dana",Leeds\n"Ellery, Marcus",Bristol', { hdr: true });

run("runs of spaces", [
  "Dana Whitfield    dana@example.com    (555) 201-8834",
  "Marcus Ellery     marcus@example.org  555.884.1120",
].join("\n"));

run("em-dash separated", [
  "Dana Whitfield — dana@example.com — (555) 201-8834",
  "Marcus Ellery — marcus.ellery@example.org — 555.884.1120",
].join("\n"));

run("extract emails from prose", [
  "Hi all, please copy dana@example.com and also",
  "marcus.ellery@example.org (and dana@example.com again).",
  "Priya is priya@example.net.",
].join("\n"), { mode: "emails" });

run("extract phones", "call (555) 201-8834 or +1 555 660 2287, not 42 or 1999", { mode: "phones" });

run("extract links", "see https://example.com/a, and www.example.org/b too.", { mode: "links" });

run("ragged rows padded", "a,b,c\nd,e\nf", {});

run("dedupe", "a,1\na,1\nb,2", { dedupe: true });

run("blank lines dropped", "a,1\n\n\nb,2");

run("no separator at all", "just one sentence here\nand another line");

run("prose with commas must NOT split", [
  "We met on Tuesday, which was already late, and agreed to postpone.",
  "Dana said, quite reasonably, that the deadline had moved again.",
  "Nobody objected, so the plan stands, at least for now.",
].join("\n"));

run("phones keep their brackets", "(555) 201-8834 and (020) 7946 0018", { mode: "phones" });

// ---- Exercise the export paths, which the fake DOM doesn't cover ----
console.log("\n=== exports ===");
els.mode.value = "auto";
els.hdr.checked = true;
els.in.value = 'Name,Note\n"Whitfield, Dana",said "hi"\nMarcus,plain';
els.in.fire("input");
let csvOut = null;
global.Blob = function (parts) { this.parts = parts; csvOut = parts.join(""); };
global.URL = { createObjectURL: () => "blob:x", revokeObjectURL: () => {} };
let captured = null;
setNavigator({ clipboard: { writeText: t => { captured = t; return Promise.resolve(); } } });
els.copy.fire("click");
setTimeout(() => {
  console.log("TSV copied:\n" + JSON.stringify(captured));
  els.csv.fire("click");
  console.log("CSV downloaded (BOM shown as \\ufeff):\n" + JSON.stringify(csvOut));
}, 10);
